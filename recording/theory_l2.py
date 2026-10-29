#!/usr/bin/env python3
"""Pictures for the lesson 2 page: paragraph.png, styles.png, result.png.

Built from real Writer screenshots kept in recording/raw (L2-marks.png,
L2-navigator.png) and the sample PDF in src/lesson-2-writer/files.
"""
import os
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.join(HERE, "..", "src", "lesson-2-writer")
OUT = os.path.join(L2, "media")
RAW = os.path.join(HERE, "raw")
BOLD = os.path.join(HERE, "fonts", "FixelDisplay-Bold.otf")
TEXT = os.path.join(HERE, "fonts", "FixelText-Regular.otf")
SEMI = os.path.join(HERE, "fonts", "FixelText-SemiBold.otf")
RED = (230, 40, 40)
INK = (30, 30, 30)


def font(path, size):
    return ImageFont.truetype(path, size)


def paragraph():
    """CV text with formatting marks on: ¶ ends every paragraph."""
    src = Image.open(os.path.join(RAW, "L2-marks.png")).convert("RGB")
    crop = src.crop((180, 250, 1040, 600))           # 860 x 350
    W, H = crop.width, crop.height + 110
    img = Image.new("RGB", (W, H), (255, 255, 255))
    img.paste(crop, (0, 0))
    d = ImageDraw.Draw(img)
    # the long paragraph: 3 lines on screen, one ¶ at the end
    d.line([(22, 266), (22, 334)], fill=RED, width=4)
    d.line([(22, 266), (32, 266)], fill=RED, width=4)
    d.line([(22, 334), (32, 334)], fill=RED, width=4)
    d.ellipse([348, 310, 374, 336], outline=RED, width=3)
    d.ellipse([534, 158, 560, 184], outline=RED, width=3)
    f = font(SEMI, 20)
    d.text((24, crop.height + 22), "¶ — кінець абзацу: тут натиснули Enter", font=f, fill=INK)
    d.text((24, crop.height + 54), "Довгий абзац сам переноситься на нові рядки — Enter натискають лише в кінці абзацу",
           font=font(TEXT, 18), fill=(80, 80, 80))
    img.save(os.path.join(OUT, "paragraph.png"), optimize=True)
    print("wrote paragraph.png")


def styles():
    """Headings in the document and the same headings as a plan in the Navigator."""
    src = Image.open(os.path.join(RAW, "L2-navigator.png")).convert("RGB")
    crop = src.crop((100, 255, 1230, 745))
    img = Image.new("RGB", (crop.width, crop.height), (255, 255, 255))
    img.paste(crop, (0, 0))
    d = ImageDraw.Draw(img)
    ox, oy = 100, 255
    for x, y, w, h in [(372, 262, 256, 38), (108, 343, 128, 34), (108, 472, 128, 34), (108, 598, 118, 34)]:
        d.rounded_rectangle([x - ox, y - oy, x - ox + w, y - oy + h], radius=6, outline=RED, width=3)
    d.rounded_rectangle([952 - ox, 298 - oy, 1221 - ox, 447 - oy], radius=8, outline=RED, width=4)
    img = img.resize((960, int(crop.height * 960 / crop.width)), Image.LANCZOS)
    img.save(os.path.join(OUT, "styles.png"), optimize=True)
    print("wrote styles.png")


def result():
    """First page of the finished sample CV (PDF)."""
    tmp = tempfile.mkdtemp()
    subprocess.run(["pdftoppm", "-png", "-r", "80", "-f", "1", "-l", "1",
                    os.path.join(L2, "files", "zrazok-rezyume.pdf"), os.path.join(tmp, "p")], check=True)
    page = Image.open(os.path.join(tmp, os.listdir(tmp)[0])).convert("RGB")
    page = page.crop((0, 0, page.width, int(page.height * 0.62)))
    img = Image.new("RGB", (page.width + 24, page.height + 24), (225, 225, 225))
    img.paste(page, (12, 12))
    img.save(os.path.join(OUT, "result.png"), optimize=True)
    print("wrote result.png", img.size)


if __name__ == "__main__":
    paragraph()
    styles()
    result()
