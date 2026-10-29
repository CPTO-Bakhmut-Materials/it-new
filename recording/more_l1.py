#!/usr/bin/env python3
"""Pictures and charts for lesson 1, page «Детальніше» (src/lesson-1-graphics/more.md).

Every number on the page comes from here: run it and copy the printed values
(file sizes, measurements) into the page's tables.

    python3 recording/more_l1.py
"""
import io
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageChops, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.join(HERE, "..", "src", "lesson-1-graphics")
OUT = os.path.join(L1, "media", "more")
FONTS = os.path.join(HERE, "fonts")
F_BOLD = os.path.join(FONTS, "FixelDisplay-Bold.otf")
F_SEMI = os.path.join(FONTS, "FixelText-SemiBold.otf")
F_TEXT = os.path.join(FONTS, "FixelText-Regular.otf")
INK = (30, 30, 30)
MUTED = (90, 90, 90)
RED = (230, 40, 40)
BG = (255, 255, 255)
# chart colours: validated categorical slots 1-2 (blue, orange) on a light surface
BLUE, ORANGE = "#2a78d6", "#eb6834"
SURFACE = "#ffffff"

for f in (F_TEXT, F_SEMI, F_BOLD):
    font_manager.fontManager.addfont(f)
plt.rcParams.update({
    "font.family": "Fixel Text",
    "font.size": 13,
    "axes.edgecolor": "#b5b4ad",
    "axes.labelcolor": "#52514e",
    "xtick.color": "#52514e",
    "ytick.color": "#52514e",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": "#e6e5e0",
    "grid.linewidth": 1,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
})

numbers = {}


def font(path, size):
    return ImageFont.truetype(path, size)


def save(img, name):
    img.save(os.path.join(OUT, name), optimize=True)
    print("wrote", name)


def jpg_bytes(im, q):
    b = io.BytesIO()
    im.save(b, "JPEG", quality=q)
    return b.getvalue()


def photo():
    return Image.open(os.path.join(L1, "files", "photo.jpg")).convert("RGB")


# --- 1. What a pixel stores -------------------------------------------------

def pixel_rgb():
    """A 6x4 patch of real photo pixels, enlarged, with their R,G,B numbers."""
    from PIL import ImageStat
    small = photo().resize((480, 318), Image.LANCZOS)
    cols, rows, cell = 6, 4, 140
    # the most varied 6x4 patch (a treetop against fog), so the numbers differ
    x0, y0 = max(((x, y) for x in range(100, 470, 2) for y in range(150, 300, 2)),
                 key=lambda p: ImageStat.Stat(small.crop((p[0], p[1], p[0] + cols, p[1] + rows))
                                              .convert("L")).stddev[0])
    W, H = cols * cell + 60, rows * cell + 110
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((W / 2, 34), "Кожен піксель — три числа: червоний, зелений, синій (від 0 до 255)",
           font=font(F_SEMI, 22), fill=INK, anchor="mm")
    f = font(F_TEXT, 19)
    for r in range(rows):
        for c in range(cols):
            rgb = small.getpixel((x0 + c, y0 + r))
            X, Y = 30 + c * cell, 70 + r * cell
            d.rectangle([X, Y, X + cell - 3, Y + cell - 3], fill=rgb)
            lum = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
            ink = (0, 0, 0) if lum > 140 else (255, 255, 255)
            for i, (name, v) in enumerate(zip("RGB", rgb)):
                d.text((X + cell / 2, Y + 40 + i * 28), f"{name} {v}", font=f, fill=ink, anchor="mm")
    save(img, "pixel-rgb.png")


def color_codes():
    """Swatches with their RGB numbers and HEX codes."""
    small = photo().resize((480, 318), Image.LANCZOS)
    # the bluest pixel of the distant mountains (rows 110-200)
    sky = max((small.getpixel((x, y)) for x in range(0, 480, 3) for y in range(110, 200, 3)),
              key=lambda c: (c[2] - c[0]) - abs(sum(c) / 3 - 120) / 4)
    items = [("Червоний", (255, 0, 0)), ("Зелений", (0, 255, 0)), ("Синій", (0, 0, 255)),
             ("Жовтий", (255, 255, 0)), ("Білий", (255, 255, 255)), ("Чорний", (0, 0, 0)),
             ("Гори з фото", sky)]
    sw, W = 128, 7 * 128 + 60
    img = Image.new("RGB", (W, 260), BG)
    d = ImageDraw.Draw(img)
    for i, (name, rgb) in enumerate(items):
        X = 30 + i * sw
        d.rounded_rectangle([X + 8, 20, X + sw - 8, 130], radius=10, fill=rgb, outline=(190, 190, 190), width=2)
        d.text((X + sw / 2, 155), name, font=font(F_SEMI, 18), fill=INK, anchor="mm")
        d.text((X + sw / 2, 185), "{}, {}, {}".format(*rgb), font=font(F_TEXT, 16), fill=MUTED, anchor="mm")
        d.text((X + sw / 2, 212), "#{:02X}{:02X}{:02X}".format(*rgb), font=font(F_SEMI, 17), fill=INK, anchor="mm")
    numbers["sky_rgb"] = sky
    save(img, "color-codes.png")


def gradient_levels():
    """The same gradient with 8, 32 and 256 levels: more levels, smoother."""
    W, bar = 900, 70
    img = Image.new("RGB", (W + 60, 3 * (bar + 50) + 20), BG)
    d = ImageDraw.Draw(img)
    for i, levels in enumerate((8, 32, 256)):
        Y = 20 + i * (bar + 50)
        d.text((30, Y + 12), f"{levels} відтінків", font=font(F_SEMI, 19), fill=INK, anchor="lm")
        for x in range(W):
            v = int(x / W * levels) * 255 // (levels - 1)
            d.line([(30 + x, Y + 30), (30 + x, Y + 30 + bar)], fill=(v // 3, v // 2 + 40, v))
    save(img, "gradient-levels.png")


# --- 2. Screen and printer ---------------------------------------------------

def rgb_cmy():
    """Light adds up (RGB on black); inks absorb (CMY on white)."""
    S = 420
    def panel(bg, colours, op):
        base = Image.new("RGB", (S, S), bg)
        centres = [(S / 2, S / 2 - 62), (S / 2 - 70, S / 2 + 52), (S / 2 + 70, S / 2 + 52)]
        for (cx, cy), col in zip(centres, colours):
            layer = Image.new("RGB", (S, S), (0, 0, 0) if op == "add" else (255, 255, 255))
            ImageDraw.Draw(layer).ellipse([cx - 105, cy - 105, cx + 105, cy + 105], fill=col)
            base = ImageChops.add(base, layer) if op == "add" else ImageChops.multiply(base, layer)
        return base
    left = panel((0, 0, 0), [(255, 0, 0), (0, 255, 0), (0, 0, 255)], "add")
    right = panel((255, 255, 255), [(0, 255, 255), (255, 0, 255), (255, 255, 0)], "mul")
    W = 2 * S + 90
    img = Image.new("RGB", (W, S + 110), BG)
    img.paste(left, (30, 70))
    img.paste(right, (60 + S, 70))
    d = ImageDraw.Draw(img)
    d.text((30 + S / 2, 24), "Екран: світло додається (RGB)", font=font(F_SEMI, 21), fill=INK, anchor="mm")
    d.text((60 + S + S / 2, 24), "Принтер: фарби поглинають (CMY + K)", font=font(F_SEMI, 21), fill=INK, anchor="mm")
    d.text((30 + S / 2, 52), "разом дають білий", font=font(F_TEXT, 17), fill=MUTED, anchor="mm")
    d.text((60 + S + S / 2, 52), "разом дають майже чорний", font=font(F_TEXT, 17), fill=MUTED, anchor="mm")
    save(img, "rgb-cmyk.png")


# --- 3. Resolution and print ------------------------------------------------

def dpi_print():
    """One 1200x800 px picture printed at 300, 150 and 72 dpi, drawn to scale."""
    px_w, px_h = 1200, 800
    thumb = photo().resize((px_w, px_h), Image.LANCZOS)
    scale = 10  # drawing pixels per centimetre
    rows = []
    for dpi in (300, 150, 72):
        w_cm, h_cm = px_w / dpi * 2.54, px_h / dpi * 2.54
        rows.append((dpi, w_cm, h_cm))
    W = 30 + sum(int(r[1] * scale) for r in rows) + 2 * 40 + 30
    H = int(rows[-1][2] * scale) + 180
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((W / 2, 22), f"Те саме зображення {px_w} × {px_h} пікселів,",
           font=font(F_SEMI, 21), fill=INK, anchor="mm")
    d.text((W / 2, 50), "надруковане з різною роздільністю (у масштабі)",
           font=font(F_TEXT, 19), fill=MUTED, anchor="mm")
    X, top = 30, 80
    for dpi, w_cm, h_cm in rows:
        w, h = int(w_cm * scale), int(h_cm * scale)
        img.paste(thumb.resize((w, h), Image.LANCZOS), (X, top))
        d.rectangle([X, top, X + w, top + h], outline=(120, 120, 120), width=2)
        d.text((X + w / 2, top + h + 24), f"{dpi} dpi", font=font(F_BOLD, 22), fill=INK, anchor="mm")
        d.text((X + w / 2, top + h + 52), f"{w_cm:.1f} × {h_cm:.1f} см".replace(".", ","),
               font=font(F_TEXT, 18), fill=MUTED, anchor="mm")
        X += w + 40
    numbers["dpi"] = [(dpi, round(w, 1), round(h, 1)) for dpi, w, h in rows]
    save(img, "dpi-print.png")


# --- 4. File size and compression -------------------------------------------

def jpeg_quality():
    """A detail of the photo after saving as JPG at quality 90, 50 and 10."""
    from PIL import ImageStat
    full = photo()
    # the most detailed 120x80 area (tree tops against fog)
    grey = full.convert("L")
    bx, by = max(((x, y) for x in range(0, 2256 - 120, 24) for y in range(600, 1496 - 80, 24)),
                 key=lambda p: ImageStat.Stat(grey.crop((p[0], p[1], p[0] + 120, p[1] + 80))).stddev[0])
    box = (bx, by, bx + 120, by + 80)
    crops, labels = [], []
    for q in (90, 50, 10):
        data = jpg_bytes(full, q)
        im = Image.open(io.BytesIO(data)).convert("RGB")
        crops.append(im.crop(box).resize((360, 240), Image.NEAREST))
        labels.append((q, len(data)))
    W = 3 * 360 + 4 * 30
    img = Image.new("RGB", (W, 360), BG)
    d = ImageDraw.Draw(img)
    for i, (c, (q, size)) in enumerate(zip(crops, labels)):
        X = 30 + i * 390
        img.paste(c, (X, 70))
        d.text((X + 180, 26), f"Якість {q}", font=font(F_BOLD, 22), fill=INK, anchor="mm")
        d.text((X + 180, 338), f"файл: {size / 1024:.0f} КБ".replace(".", ","), font=font(F_TEXT, 19),
               fill=MUTED, anchor="mm")
    save(img, "jpeg-quality.png")


def jpeg_size_chart():
    """File size of the lesson photo at JPG quality 10 … 100 (measured)."""
    full = photo()
    qs = list(range(10, 101, 10))
    sizes = [len(jpg_bytes(full, q)) / 1024 for q in qs]
    numbers["jpeg_sizes_kb"] = dict(zip(qs, [round(s) for s in sizes]))
    fig, ax = plt.subplots(figsize=(9.6, 4.6), dpi=100)
    ax.plot(qs, sizes, color=BLUE, linewidth=2, marker="o", markersize=8,
            markeredgecolor=SURFACE, markeredgewidth=2, zorder=3)
    for q in (80, 100):
        s = sizes[qs.index(q)]
        ax.annotate(f"{s:.0f} КБ", (q, s), textcoords="offset points", xytext=(-12, 10),
                    ha="right", fontsize=13, color="#0b0b0b")
    ax.set_xlabel("Якість JPG")
    ax.set_ylabel("Розмір файлу, КБ")
    ax.set_xticks(qs)
    ax.set_ylim(0, max(sizes) * 1.15)
    ax.set_title("Фото уроку (2256 × 1496): що вища якість, то важчий файл",
                 loc="left", fontsize=15, fontweight="semibold", color="#0b0b0b", pad=14)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "jpeg-size-chart.png"))
    plt.close(fig)
    print("wrote jpeg-size-chart.png")


def flat_drawing():
    """A simple flat drawing (shapes + text), 1200x800, like the postcard."""
    img = Image.new("RGB", (1200, 800), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 520, 1200, 800], fill=(120, 190, 90))
    d.ellipse([880, 80, 1080, 280], fill=(250, 200, 30))
    d.rectangle([180, 330, 520, 560], fill=(230, 80, 50))
    d.polygon([(150, 340), (350, 180), (550, 340)], fill=(120, 60, 40))
    d.rectangle([310, 430, 390, 560], fill=(250, 230, 180))
    d.text((640, 420), "Вітаю!", font=font(F_BOLD, 120), fill=(30, 60, 160))
    return img


def formats_chart():
    """Size of a photo and a flat drawing in PNG, JPG and WebP (measured)."""
    pic = photo().resize((1200, 796), Image.LANCZOS)
    draw = flat_drawing()
    fmts = [("PNG", dict(format="PNG", optimize=True)),
            ("JPG (якість 85)", dict(format="JPEG", quality=85)),
            ("WebP (якість 85)", dict(format="WEBP", quality=85))]
    res = {"photo": [], "drawing": []}
    for key, im in (("photo", pic), ("drawing", draw)):
        for name, kw in fmts:
            b = io.BytesIO()
            im.save(b, **kw)
            res[key].append(b.tell() / 1024)
    numbers["formats_kb"] = {k: [round(v) for v in vals] for k, vals in res.items()}
    numbers["raw_1200x800_kb"] = round(1200 * 800 * 3 / 1024)

    fig, ax = plt.subplots(figsize=(9.6, 4.8), dpi=100)
    xs = range(len(fmts))
    w = 0.36
    b1 = ax.bar([x - w / 2 - 0.01 for x in xs], res["photo"], w, color=BLUE, label="Фото",
                zorder=3)
    b2 = ax.bar([x + w / 2 + 0.01 for x in xs], res["drawing"], w, color=ORANGE,
                label="Простий малюнок", zorder=3)
    for bars in (b1, b2):
        for r in bars:
            ax.annotate(f"{r.get_height():.0f}", (r.get_x() + r.get_width() / 2, r.get_height()),
                        textcoords="offset points", xytext=(0, 4), ha="center", fontsize=12,
                        color="#0b0b0b")
    ax.set_xticks(list(xs), [n for n, _ in fmts])
    ax.set_ylabel("Розмір файлу, КБ")
    ax.grid(axis="x", visible=False)
    ax.legend(frameon=False, loc="upper right")
    ax.set_title("Те саме зображення 1200 × 800 у різних форматах",
                 loc="left", fontsize=15, fontweight="semibold", color="#0b0b0b", pad=14)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "formats-chart.png"))
    plt.close(fig)
    print("wrote formats-chart.png")
    save(draw.resize((600, 400), Image.LANCZOS), "flat-drawing.png")
    pic.resize((600, 398), Image.LANCZOS).save(os.path.join(OUT, "photo-small.jpg"), quality=85)


def jpg_text_artifacts():
    """Letters from the flat drawing: PNG is clean, JPG leaves 'dirt' around edges."""
    draw = flat_drawing()
    box = (646, 470, 686, 497)  # the left edge of «В» on white
    png = draw.crop(box)
    jpg = Image.open(io.BytesIO(jpg_bytes(draw, 50))).convert("RGB").crop(box)
    W = 2 * 400 + 90
    img = Image.new("RGB", (W, 360), BG)
    d = ImageDraw.Draw(img)
    for i, (im, name) in enumerate(((png, "PNG: краї чисті"), (jpg, "JPG: «бруд» навколо літер"))):
        X = 30 + i * 430
        img.paste(im.resize((400, 270), Image.NEAREST), (X, 60))
        d.text((X + 200, 28), name, font=font(F_SEMI, 21), fill=INK, anchor="mm")
    d.text((W / 2, 345), "Край літери «В», збільшено в 10 разів; JPG з якістю 50", font=font(F_TEXT, 17),
           fill=MUTED, anchor="mm")
    save(img, "jpg-text-artifacts.png")


# --- 5. Vector ---------------------------------------------------------------

SUN_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <rect width="200" height="200" fill="#bfe3ff"/>
  <circle cx="100" cy="100" r="45" fill="#f5c400"/>
  <g stroke="#f5c400" stroke-width="8" stroke-linecap="round">
    <line x1="100" y1="15" x2="100" y2="40"/>
    <line x1="100" y1="160" x2="100" y2="185"/>
    <line x1="15" y1="100" x2="40" y2="100"/>
    <line x1="160" y1="100" x2="185" y2="100"/>
  </g>
</svg>
"""


def sun_svg():
    with open(os.path.join(OUT, "sun.svg"), "w") as f:
        f.write(SUN_SVG)
    numbers["sun_svg_bytes"] = len(SUN_SVG.encode())
    print("wrote sun.svg")


# --- 6. Tablet ---------------------------------------------------------------

def pressure():
    """Mouse: one width. Tablet pen: width follows pressure."""
    W, H = 900, 330
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    import math
    for row, (name, width_fn) in enumerate((
            ("Миша: товщина однакова", lambda t: 7),
            ("Перо планшета: сильніше натиск — товща лінія", lambda t: 2 + 16 * math.sin(math.pi * t) ** 2))):
        Y = 100 + row * 150
        d.text((30, Y - 82), name, font=font(F_SEMI, 20), fill=INK)
        for i in range(400):
            t = i / 399
            x = 40 + t * 820
            y = Y + 22 * math.sin(t * 2 * math.pi)
            r = width_fn(t) / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill=(40, 60, 140))
    save(img, "pressure.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    pixel_rgb()
    color_codes()
    gradient_levels()
    rgb_cmy()
    dpi_print()
    jpeg_quality()
    jpeg_size_chart()
    formats_chart()
    jpg_text_artifacts()
    sun_svg()
    pressure()
    print(json.dumps(numbers, ensure_ascii=False, indent=1))
