#!/usr/bin/env python3
"""Pictures and charts for lesson 3, page «Детальніше» (src/lesson-3-internet/more.md).

- dns.png: how a name becomes an address (real IP of diia.gov.ua at build time)
- http-https.png: what others on the same Wi-Fi can read
- password-chart.png: time to try every combination (computed, assumption stated)
- totp.png: three real one-time codes from a demo key (RFC 6238 algorithm)
- adblock.png: the same page without / with uBlock, plus uBlock's own counters
  (screenshots recorded in recording/raw: page-off.png, page-on.png, ubo-off.png, ubo-on.png)

    python3 recording/more_l3.py
"""
import base64
import hashlib
import hmac
import json
import math
import os
import socket
import struct

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "src", "lesson-3-internet", "media", "more")
RAW = os.path.join(HERE, "raw")
F_BOLD = os.path.join(HERE, "fonts", "FixelDisplay-Bold.otf")
F_SEMI = os.path.join(HERE, "fonts", "FixelText-SemiBold.otf")
F_TEXT = os.path.join(HERE, "fonts", "FixelText-Regular.otf")
MONO = "/usr/share/fonts/TTF/JetBrainsMono-Regular.ttf"
MONO_B = "/usr/share/fonts/TTF/JetBrainsMono-Bold.ttf"
INK = (30, 30, 30)
MUTED = (100, 100, 100)
RED = (230, 40, 40)
GREEN = (20, 140, 70)
BLUE_RGB = (42, 120, 214)
BLUE = "#2a78d6"      # validated categorical slot 1 (single series)
SURFACE = "#ffffff"
GUESSES_PER_SECOND = 1e10   # assumption shown on the chart and on the page

for f in (F_TEXT, F_SEMI, F_BOLD):
    font_manager.fontManager.addfont(f)
plt.rcParams.update({
    "font.family": "Fixel Text", "font.size": 13,
    "axes.edgecolor": "#b5b4ad", "axes.labelcolor": "#52514e",
    "xtick.color": "#52514e", "ytick.color": "#52514e",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#e6e5e0", "grid.linewidth": 1,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
})
numbers = {}


def font(p, s):
    return ImageFont.truetype(p, s)


def save(img, name):
    img.save(os.path.join(OUT, name), optimize=True)
    print("wrote", name)


def box(d, xy, title, sub, fill):
    d.rounded_rectangle(xy, radius=14, fill=fill, outline=(170, 170, 170), width=2)
    x0, y0, x1, y1 = xy
    d.text(((x0 + x1) / 2, y0 + 34), title, font=font(F_BOLD, 21), fill=INK, anchor="mm")
    if sub:
        d.text(((x0 + x1) / 2, y0 + 68), sub, font=font(F_TEXT, 17), fill=MUTED, anchor="mm")


def arrow(d, a, b, label=None, below=False, col=(80, 80, 80)):
    d.line([a, b], fill=col, width=3)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    p1 = (b[0] - 14 * math.cos(ang - 0.4), b[1] - 14 * math.sin(ang - 0.4))
    p2 = (b[0] - 14 * math.cos(ang + 0.4), b[1] - 14 * math.sin(ang + 0.4))
    d.polygon([b, p1, p2], fill=col)
    if label:
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        d.text((mx, my + (18 if below else -18)), label, font=font(F_TEXT, 17), fill=INK, anchor="mm")


# --- 1. DNS --------------------------------------------------------------------------

def dns():
    try:
        ip = socket.gethostbyname("diia.gov.ua")
    except OSError:
        ip = "172.66.3.137"
    numbers["diia_ip"] = ip
    W, H = 960, 400
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    box(d, (30, 10, 250, 110), "DNS-сервер", "«телефонна книга»", (253, 244, 228))
    box(d, (30, 200, 250, 310), "Ваш браузер", "ви ввели diia.gov.ua", (234, 242, 252))
    box(d, (710, 200, 930, 310), "Сервер сайту", ip, (232, 246, 236))
    arrow(d, (110, 200), (110, 112))
    arrow(d, (170, 112), (170, 198))
    d.text((270, 138), "1. Яка IP-адреса в diia.gov.ua?", font=font(F_TEXT, 17), fill=INK, anchor="lm")
    d.text((270, 172), f"2. Ось вона: {ip}", font=font(F_TEXT, 17), fill=INK, anchor="lm")
    arrow(d, (250, 240), (710, 240), "3. Браузер з’єднується з цією адресою")
    arrow(d, (710, 280), (250, 280), "4. Сервер надсилає сторінку", below=True)
    d.text((W / 2, 370), "Домен — зручна для людей назва; комп’ютери з’єднуються за числовою IP-адресою.",
           font=font(F_TEXT, 17), fill=MUTED, anchor="mm")
    save(img, "dns.png")


# --- 2. HTTP vs HTTPS -----------------------------------------------------------------

def http_https():
    W, H = 960, 330
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    rows = [("http://  — без шифрування", "login=oksana  password=Kvitka2026", RED,
             "Хтось у тій самій мережі Wi-Fi може прочитати"),
            ("https:// — з шифруванням", "x9#Lq2!vR0.. 7Fz@pW3k$e1..", GREEN,
             "Видно лише «шум»: прочитати дані неможливо")]
    for i, (title, data, col, note) in enumerate(rows):
        y = 30 + i * 150
        d.text((30, y), title, font=font(F_BOLD, 21), fill=col)
        box(d, (30, y + 40, 200, y + 120), "Ви", "", (234, 242, 252))
        box(d, (760, y + 40, 930, y + 120), "Сайт", "", (232, 246, 236))
        d.line([(200, y + 80), (760, y + 80)], fill=(150, 150, 150), width=3)
        d.rounded_rectangle([280, y + 58, 680, y + 102], radius=8, fill=(250, 250, 250), outline=col, width=2)
        d.text((480, y + 80), data, font=font(MONO, 17), fill=col, anchor="mm")
        d.text((480, y + 128), note, font=font(F_TEXT, 16), fill=MUTED, anchor="mm")
    save(img, "http-https.png")


# --- 3. Password guessing time --------------------------------------------------------

def human_time(sec):
    units = [(3.156e13, "млн р."), (3.156e7, "р."), (86400, "дн."), (3600, "год"), (60, "хв"), (1, "с")]
    if sec < 1:
        return "миттєво"
    for size, name in units:
        if sec >= size:
            v = sec / size
            return (f"{v:,.0f}".replace(",", " ") if v >= 10 else f"{v:.1f}".replace(".", ",")) + " " + name
    return "миттєво"


def password_chart():
    items = [
        ("8 малих літер\nnfhpxkqz", 26 ** 8),
        ("8 символів: літери, цифри, знаки\nTk7#q!Lp", 95 ** 8),
        ("12 символів: літери, цифри, знаки\nTk7#q!Lp2@vX", 95 ** 12),
        ("4 випадкові слова\nкіт-ракета-сир-хмара", 7776 ** 4),
        ("5 випадкових слів\nкіт-ракета-сир-хмара-ліс", 7776 ** 5),
        ("6 випадкових слів\nкіт-ракета-сир-хмара-ліс-міст", 7776 ** 6),
    ]
    secs = [n / GUESSES_PER_SECOND for _, n in items]
    numbers["password_seconds"] = {lbl.split(chr(10))[0]: human_time(s) for (lbl, _), s in zip(items, secs)}
    fig, ax = plt.subplots(figsize=(9.6, 5.0), dpi=100)
    ys = list(range(len(items)))
    ax.barh(ys, secs, color=BLUE, height=0.55, zorder=3)
    ax.set_xscale("log")
    for y, s in zip(ys, secs):
        ax.annotate(human_time(s), (s, y), textcoords="offset points", xytext=(6, 0), va="center",
                    fontsize=13, color="#0b0b0b")
    ax.set_yticks(ys, [lbl for lbl, _ in items], fontsize=12)
    ax.invert_yaxis()
    ticks = [1, 3600, 86400 * 365, 3.156e7 * 1e3, 3.156e7 * 1e6, 3.156e7 * 1e9]
    ax.set_xticks(ticks, ["1 с", "1 год", "1 рік", "1000 років", "1 млн років", "1 млрд років"])
    ax.minorticks_off()
    ax.set_xlim(1, max(secs) * 400)
    ax.grid(axis="y", visible=False)
    ax.set_title("Час, щоб перебрати всі варіанти (умовно 10 млрд спроб/с)",
                 loc="left", fontsize=15, fontweight="semibold", color="#0b0b0b", pad=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "password-chart.png"))
    plt.close(fig)
    print("wrote password-chart.png")


# --- 4. TOTP ------------------------------------------------------------------------------

def totp(secret_b32, t, step=30, digits=6):
    """RFC 6238 time-based one-time password."""
    key = base64.b32decode(secret_b32)
    msg = struct.pack(">Q", int(t // step))
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[-1] & 0x0F
    code = (struct.unpack(">I", h[o:o + 4])[0] & 0x7FFFFFFF) % (10 ** digits)
    return f"{code:0{digits}d}"


def totp_picture():
    secret = "JBSWY3DPEHPK3PXP"   # a well-known demo key, not a real account
    t0 = 1793289600              # 29.10.2026 12:00:00 (Kyiv, UTC+2)
    times = [t0, t0 + 30, t0 + 60]
    codes = [totp(secret, t) for t in times]
    numbers["totp_codes"] = codes
    W, H = 960, 380
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for i, (t, code) in enumerate(zip(times, codes)):
        x = 60 + i * 300
        d.rounded_rectangle([x, 30, x + 240, 330], radius=30, fill=(30, 34, 44))
        d.rounded_rectangle([x + 12, 52, x + 228, 308], radius=18, fill=(245, 247, 250))
        d.text((x + 120, 84), "Застосунок 2FA", font=font(F_SEMI, 17), fill=MUTED, anchor="mm")
        d.text((x + 120, 116), "ТвійБанк", font=font(F_BOLD, 21), fill=INK, anchor="mm")
        d.text((x + 120, 178), code[:3] + " " + code[3:], font=font(MONO_B, 40), fill=BLUE_RGB, anchor="mm")
        hh, mm, ss = 12, (t - t0) // 60, (t - t0) % 60
        d.text((x + 120, 240), f"{hh}:{mm:02d}:{ss:02d}", font=font(F_TEXT, 19), fill=MUTED, anchor="mm")
        d.text((x + 120, 272), "новий код що 30 с", font=font(F_TEXT, 16), fill=MUTED, anchor="mm")
        if i < 2:
            arrow(d, (x + 248, 180), (x + 292, 180))
    d.text((W / 2, 358), "Код рахується з секретного ключа і поточного часу — його не можна вгадати наперед.",
           font=font(F_TEXT, 17), fill=MUTED, anchor="mm")
    save(img, "totp.png")


# --- 5. Ad blocking: measured on sinoptik.ua -------------------------------------------

def adblock():
    off = Image.open(os.path.join(RAW, "page-off.png")).convert("RGB")
    on = Image.open(os.path.join(RAW, "page-on.png")).convert("RGB")
    W = 960
    pw = (W - 3 * 20) // 2
    ph = int(800 * pw / 1280)
    img = Image.new("RGB", (W, ph + 210), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for i, (shot, title, col) in enumerate(((off, "Без uBlock", RED), (on, "З uBlock", GREEN))):
        x = 20 + i * (pw + 20)
        img.paste(shot.resize((pw, ph), Image.LANCZOS), (x, 50))
        d.rectangle([x, 50, x + pw, 50 + ph], outline=(170, 170, 170), width=2)
        d.text((x + pw / 2, 26), title, font=font(F_BOLD, 22), fill=col, anchor="mm")
    stats = [("Сайтів (доменів), з якими з’єднався браузер", "36", "1 (ще 4 заблоковано)")]
    y = 50 + ph + 30
    d.text((20, y), stats[0][0] + ":", font=font(F_SEMI, 19), fill=INK)
    d.text((20 + pw / 2, y + 60), stats[0][1], font=font(F_BOLD, 40), fill=RED, anchor="mm")
    d.text((40 + pw + pw / 2, y + 60), stats[0][2], font=font(F_BOLD, 32), fill=GREEN, anchor="mm")
    d.text((W / 2, y + 120), "sinoptik.ua, головна сторінка; лічильники самого uBlock Origin, жовтень 2026",
           font=font(F_TEXT, 15), fill=MUTED, anchor="mm")
    save(img, "adblock.png")


def adblock_diagram():
    W, H = 960, 400
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    box(d, (10, 150, 220, 250), "Сторінка", "просить завантажити", (234, 242, 252))
    box(d, (300, 140, 520, 260), "uBlock Origin", "звіряє зі списками", (253, 244, 228))
    reqs = [("текст і фото сайту", GREEN, "✓ завантажити"),
            ("ads.example-adnet.com", RED, "✗ заблокувати"),
            ("tracker.example-stat.net", RED, "✗ заблокувати"),
            ("шрифти й стилі сайту", GREEN, "✓ завантажити")]
    for i, (name, col, verdict) in enumerate(reqs):
        y = 40 + i * 90
        arrow(d, (520, 200), (610, y + 30), col=(150, 150, 150))
        d.rounded_rectangle([615, y, 940, y + 60], radius=10, fill=(250, 250, 250), outline=col, width=2)
        d.text((630, y + 18), name, font=font(MONO, 16), fill=INK, anchor="lm")
        d.text((630, y + 44), verdict, font=font(F_SEMI, 16), fill=col, anchor="lm")
    arrow(d, (220, 200), (300, 200))
    d.rounded_rectangle([300, 300, 520, 380], radius=10, fill=(245, 245, 245), outline=(170, 170, 170), width=2)
    d.text((410, 325), "Списки фільтрів", font=font(F_SEMI, 17), fill=INK, anchor="mm")
    d.text((410, 352), "оновлюють волонтери", font=font(F_TEXT, 15), fill=MUTED, anchor="mm")
    arrow(d, (410, 300), (410, 262))
    # ✓/✗ glyphs are not in Fixel: redraw verdict marks with DejaVu
    sym = font("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 16)
    for i, (_, col, verdict) in enumerate(reqs):
        y = 40 + i * 90
        d.rectangle([628, y + 34, 646, y + 54], fill=(250, 250, 250))
        d.text((630, y + 44), verdict[0], font=sym, fill=col, anchor="lm")
    save(img, "adblock-diagram.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    dns()
    http_https()
    password_chart()
    totp_picture()
    adblock()
    adblock_diagram()
    print(json.dumps(numbers, ensure_ascii=False, indent=1))
