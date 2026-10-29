#!/usr/bin/env python3
"""Pictures and charts for lesson 2, page «Детальніше» (src/lesson-2-writer/more.md).

Uses the real files made while recording the lesson (the sample CV in .odt,
.docx and .pdf) and real Writer screenshots kept in recording/raw. Prints the
measured numbers to copy into the page's tables.

    python3 recording/more_l2.py
"""
import json
import os
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.join(HERE, "..", "src", "lesson-2-writer")
FILES = os.path.join(L2, "files")
OUT = os.path.join(L2, "media", "more")
RAW = os.path.join(HERE, "raw")
FONTS = os.path.join(HERE, "fonts")
F_BOLD = os.path.join(FONTS, "FixelDisplay-Bold.otf")
F_SEMI = os.path.join(FONTS, "FixelText-SemiBold.otf")
F_TEXT = os.path.join(FONTS, "FixelText-Regular.otf")
LIB = "/usr/share/fonts/liberation"
MONO = "/usr/share/fonts/TTF/JetBrainsMono-Regular.ttf"
INK = (30, 30, 30)
MUTED = (90, 90, 90)
RED = (230, 40, 40)
BG = (255, 255, 255)
BLUE = "#2a78d6"   # validated categorical slot 1, single series
SURFACE = "#ffffff"

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


def font(path, size):
    return ImageFont.truetype(path, size)


def save(img, name):
    img.save(os.path.join(OUT, name), optimize=True)
    print("wrote", name)


# --- 1. Plain text vs a formatted document --------------------------------------

def plain_vs_formatted():
    text = open(os.path.join(FILES, "text.txt"), encoding="utf-8").read().splitlines()
    W, H = 960, 470
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # left: the .txt as a text editor shows it
    d.rectangle([20, 50, 455, 450], fill=(250, 250, 250), outline=(170, 170, 170), width=2)
    d.rectangle([20, 50, 455, 76], fill=(225, 225, 225))
    d.text((30, 63), "text.txt — текстовий редактор", font=font(F_SEMI, 15), fill=INK, anchor="lm")
    f = font(MONO, 13)
    for i, line in enumerate(text[:16]):
        d.text((32, 88 + i * 21), line[:52] + ("…" if len(line) > 52 else ""), font=f, fill=INK)
    # right: the finished CV in Writer (real screenshot)
    cv = Image.open(os.path.join(RAW, "w-top.png")).convert("RGB").crop((130, 156, 1078, 768))
    cv = cv.resize((470, int(cv.height * 470 / cv.width)), Image.LANCZOS)
    img.paste(cv, (W - 20 - cv.width, 50))
    d.rectangle([W - 20 - cv.width, 50, W - 20, 50 + cv.height], outline=(170, 170, 170), width=2)
    d.text((237, 24), "Простий текст (.txt)", font=font(F_BOLD, 21), fill=INK, anchor="mm")
    d.text((W - 20 - cv.width / 2, 24), "Документ (.odt / .docx)", font=font(F_BOLD, 21), fill=INK, anchor="mm")
    save(img, "plain-vs-formatted.png")


# --- 2. File sizes and what is inside -----------------------------------------------

def sizes_chart():
    items = [("Простий текст .txt", os.path.join(FILES, "text.txt")),
             ("Word .docx", os.path.join(RAW, "L2-rezyume.docx")),
             ("LibreOffice .odt", os.path.join(FILES, "zrazok-rezyume.odt")),
             ("PDF .pdf", os.path.join(FILES, "zrazok-rezyume.pdf"))]
    vals = [os.path.getsize(p) / 1024 for _, p in items]
    numbers["sizes_kb"] = {n: round(v, 1) for (n, _), v in zip(items, vals)}
    fig, ax = plt.subplots(figsize=(9.6, 3.6), dpi=100)
    ys = range(len(items))
    ax.barh(list(ys), vals, color=BLUE, height=0.55, zorder=3)
    for y, v in zip(ys, vals):
        ax.annotate(f"{v:.1f} КБ".replace(".", ","), (v, y), textcoords="offset points", xytext=(6, 0),
                    va="center", fontsize=13, color="#0b0b0b")
    ax.set_yticks(list(ys), [n for n, _ in items])
    ax.invert_yaxis()
    ax.set_xlabel("Розмір файлу, КБ")
    ax.grid(axis="y", visible=False)
    ax.set_xlim(0, max(vals) * 1.18)
    ax.set_title("Те саме резюме в різних форматах",
                 loc="left", fontsize=15, fontweight="semibold", color="#0b0b0b", pad=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "sizes-chart.png"))
    plt.close(fig)
    print("wrote sizes-chart.png")


def odt_inside():
    """An .odt is a ZIP archive: boxes for its real parts, sized by bytes."""
    z = zipfile.ZipFile(os.path.join(FILES, "zrazok-rezyume.odt"))
    parts = {i.filename: i.file_size for i in z.infolist()}
    numbers["odt_parts"] = parts
    label = {
        "content.xml": "content.xml\nтекст і таблиця",
        "styles.xml": "styles.xml\nстилі: заголовки, шрифти",
        "settings.xml": "settings.xml\nмасштаб, положення курсора",
        "meta.xml": "meta.xml\nавтор, дата, кількість слів",
    }
    pic = next(n for n in parts if n.startswith("Pictures/"))
    rows = [("content.xml", parts["content.xml"]), ("styles.xml", parts["styles.xml"]),
            ("settings.xml", parts["settings.xml"]), ("meta.xml", parts["meta.xml"]),
            (pic, parts[pic]), ("Thumbnails/thumbnail.png", parts["Thumbnails/thumbnail.png"])]
    names = {pic: "Pictures/…jpg\nвставлене фото",
             "Thumbnails/thumbnail.png": "Thumbnails/thumbnail.png\nмініатюра для провідника"}
    W, H = 960, 420
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([20, 20, W - 20, H - 20], radius=16, outline=(120, 120, 120), width=3)
    d.text((40, 48), "zrazok-rezyume.odt — насправді це ZIP-архів з такими файлами:",
           font=font(F_SEMI, 20), fill=INK, anchor="lm")
    cols, cw, ch = 3, 283, 140
    for i, (n, size) in enumerate(rows):
        x = 40 + (i % cols) * (cw + 15)
        y = 85 + (i // cols) * (ch + 15)
        is_xml = n.endswith(".xml")
        fill = (234, 242, 252) if is_xml else (253, 240, 232)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=10, fill=fill, outline=(170, 170, 170), width=2)
        title, sub = (label.get(n) or names[n]).split("\n")
        d.text((x + 16, y + 30), title, font=font(MONO, 16), fill=INK, anchor="lm")
        d.text((x + 16, y + 64), sub, font=font(F_TEXT, 17), fill=MUTED, anchor="lm")
        d.text((x + 16, y + 106), f"{size / 1024:.1f} КБ".replace(".", ","), font=font(F_BOLD, 22), fill=INK, anchor="lm")
    save(img, "odt-inside.png")


# --- 3. Enter vs Shift+Enter ---------------------------------------------------------

def enter_shift():
    src = Image.open(os.path.join(RAW, "L2-enter.png")).convert("RGB").crop((205, 240, 560, 315))
    z = src.resize((src.width * 2, src.height * 2), Image.LANCZOS)
    W, H = 960, z.height + 120
    img = Image.new("RGB", (W, H), BG)
    img.paste(z, (20, 10))
    d = ImageDraw.Draw(img)
    # ↵ after the first line, ¶ after the second (positions in the 2x crop)
    for (x, y, txt) in [((360 - 205) * 2 + 20, (256 - 240) * 2 + 10, "Shift+Enter: новий рядок у тому самому абзаці (знак ↵)"),
                        ((340 - 205) * 2 + 20, (278 - 240) * 2 + 10, "Enter: новий абзац (знак ¶)")]:
        d.ellipse([x - 16, y - 16, x + 16, y + 16], outline=RED, width=3)
    sym = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 20)   # Fixel has no ↵
    for k, (mark, text) in enumerate((("↵", "Shift+Enter — новий рядок, але той самий абзац (зручно для адреси, віршів)"),
                                      ("¶", "Enter — новий абзац (з власним відступом, вирівнюванням, стилем)"))):
        yy = z.height + 30 + k * 36
        d.text((40, yy + 2), mark, font=sym, fill=(40, 120, 220))
        d.text((72, yy), text, font=font(F_TEXT, 19), fill=INK)
    save(img, "enter-shift.png")


# --- 4. Fonts -----------------------------------------------------------------------------

def serif_sans():
    W, H = 960, 330
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    serif = font(os.path.join(LIB, "LiberationSerif-Regular.ttf"), 64)
    sans = font(os.path.join(LIB, "LiberationSans-Regular.ttf"), 64)
    d.text((40, 30), "З зарубками (serif)", font=font(F_SEMI, 20), fill=MUTED)
    d.text((40, 60), "Шрифт Нп", font=serif, fill=INK)
    d.text((500, 30), "Без зарубок (sans-serif)", font=font(F_SEMI, 20), fill=MUTED)
    d.text((500, 60), "Шрифт Нп", font=sans, fill=INK)
    # zoom one letter of each to show the serifs
    for i, (fnt, x0) in enumerate(((serif, 40), (sans, 500))):
        big = Image.new("RGB", (120, 120), BG)
        ImageDraw.Draw(big).text((14, -8), "Н", font=ImageFont.truetype(fnt.path, 120), fill=INK)
        img.paste(big.resize((150, 150), Image.LANCZOS), (x0 + 20, 160))
        if i == 0:
            for cx, cy in ((x0 + 36, 300), (x0 + 152, 300), (x0 + 36, 182), (x0 + 152, 182)):
                d.ellipse([cx - 18, cy - 14, cx + 18, cy + 14], outline=RED, width=3)
        d.text((x0 + 200, 236), "Liberation Serif" if i == 0 else "Liberation Sans", font=font(F_TEXT, 19), fill=MUTED)
    save(img, "serif-sans.png")


def font_sizes():
    sizes = [(8, "дрібні примітки"), (10, "виноски"), (12, "звичайний текст"), (14, "Заголовок 2"),
             (18, "Заголовок 1"), (24, "титульна сторінка")]
    W = 960
    rows = [(s, int(s * 96 / 72 * 1.25)) for s, _ in sizes]   # Writer at 125 %, 96 dpi screen
    H = 30 + sum(px + 22 for _, px in rows)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    y = 20
    for (pt, use), (_, px) in zip(sizes, rows):
        d.text((40, y + px / 2), f"{pt} pt", font=font(F_BOLD, 20), fill=INK, anchor="lm")
        d.text((140, y), "Абзац тексту", font=ImageFont.truetype(os.path.join(LIB, "LiberationSans-Regular.ttf"), px), fill=INK)
        d.text((W - 40, y + px / 2), use, font=font(F_TEXT, 18), fill=MUTED, anchor="rm")
        y += px + 22
    save(img, "font-sizes.png")


# --- 5. Page: orientation and margins --------------------------------------------------

def page_orientation():
    s = 9  # px per cm
    W, H = 960, 360
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for i, (pw, ph, name) in enumerate(((21, 29.7, "Книжкова (вертикальна)"), (29.7, 21, "Альбомна (горизонтальна)"))):
        x0 = 120 + i * 420
        y0 = 40
        d.rectangle([x0, y0, x0 + pw * s, y0 + ph * s], fill=(250, 250, 250), outline=(90, 90, 90), width=2)
        m = 2 * s
        for x in range(int(x0 + m), int(x0 + pw * s - m), 10):
            d.line([(x, y0 + m), (x + 5, y0 + m)], fill=RED, width=2)
            d.line([(x, y0 + ph * s - m), (x + 5, y0 + ph * s - m)], fill=RED, width=2)
        for y in range(int(y0 + m), int(y0 + ph * s - m), 10):
            d.line([(x0 + m, y), (x0 + m, y + 5)], fill=RED, width=2)
            d.line([(x0 + pw * s - m, y), (x0 + pw * s - m, y + 5)], fill=RED, width=2)
        for k in range(6):
            yy = y0 + m + 14 + k * 16
            if yy < y0 + ph * s - m - 10:
                d.line([(x0 + m + 10, yy), (x0 + pw * s - m - 10, yy)], fill=(190, 190, 190), width=4)
        d.text((x0 + pw * s / 2, y0 + ph * s + 22), name, font=font(F_SEMI, 19), fill=INK, anchor="mm")
        d.text((x0 + pw * s / 2, y0 + ph * s + 46), f"{pw:g} × {ph:g} см".replace(".", ","),
               font=font(F_TEXT, 17), fill=MUTED, anchor="mm")
    d.text((W - 20, 20), "пунктир — поля 2 см", font=font(F_TEXT, 16), fill=RED, anchor="ra")
    save(img, "page-orientation.png")


def page_dialog():
    src = Image.open(os.path.join(RAW, "L2-page.png")).convert("RGB").crop((208, 140, 880, 590))
    img = src.copy()
    d = ImageDraw.Draw(img)
    for x, y, w, h in [(150, 30, 270, 34), (150, 140, 150, 50), (148, 270, 166, 186)]:
        d.rounded_rectangle([x, y, x + w, y + h], radius=6, outline=RED, width=3)
    save(img, "page-dialog.png")


# --- 6. Automatic table of contents ------------------------------------------------------

def toc():
    src = Image.open(os.path.join(RAW, "L2-toc.png")).convert("RGB").crop((200, 245, 1010, 530))
    save(src, "toc.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    plain_vs_formatted()
    sizes_chart()
    odt_inside()
    enter_shift()
    serif_sans()
    font_sizes()
    page_orientation()
    page_dialog()
    toc()
    print(json.dumps(numbers, ensure_ascii=False, indent=1))
