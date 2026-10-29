#!/usr/bin/env python3
"""Theory pictures for lesson 1: pixels.png and raster-vector.png."""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.join(HERE, "..", "src", "lesson-1-graphics")
OUT = os.path.join(L1, "media")
BOLD = os.path.join(HERE, "fonts", "FixelDisplay-Bold.otf")
RED = (230, 40, 40)
BG = (255, 255, 255)
INK = (30, 30, 30)


def label(d, xy, text, size=26, anchor="mm"):
    d.text(xy, text, font=ImageFont.truetype(BOLD, size), fill=INK, anchor=anchor)


def pixels():
    """Photo, a marked square, and that square enlarged until pixels show."""
    photo = Image.open(os.path.join(L1, "files", "photo.jpg")).convert("RGB")
    small = photo.resize((480, 318), Image.LANCZOS)
    # the most contrasty 16x16 square (a tree tip against fog): pixels show best
    from PIL import ImageStat
    s = 16
    cx, cy = max(((x, y) for x in range(100, 460, 4) for y in range(150, 280, 4)),
                 key=lambda p: ImageStat.Stat(small.crop((p[0], p[1], p[0] + s, p[1] + s))
                                              .convert("L")).stddev[0])
    zoom = small.crop((cx, cy, cx + s, cy + s)).resize((320, 320), Image.NEAREST)
    W, H = 960, 420
    img = Image.new("RGB", (W, H), BG)
    img.paste(small, (30, 60))
    img.paste(zoom, (W - 30 - 320, 60))
    d = ImageDraw.Draw(img)
    d.rectangle([30 + cx, 60 + cy, 30 + cx + s, 60 + cy + s], outline=RED, width=3)
    d.line([30 + cx + s, 60 + cy, W - 350, 60], fill=RED, width=2)
    d.line([30 + cx + s, 60 + cy + s, W - 350, 380], fill=RED, width=2)
    d.rectangle([W - 350, 60, W - 30, 380], outline=RED, width=3)
    label(d, (270, 30), "Фото")
    label(d, (W - 190, 30), "Збільшено в 20 разів")
    label(d, (W / 2, 402), "Кожен квадратик — це піксель (одна точка одного кольору)", 20)
    img.save(os.path.join(OUT, "pixels.png"), optimize=True)


def shape(draw, k, ox, oy):
    """A circle with a letter, drawn at scale k (for the raster/vector pair)."""
    draw.ellipse([ox + 4 * k, oy + 4 * k, ox + 36 * k, oy + 36 * k], fill=(40, 90, 220))
    draw.text((ox + 20 * k, oy + 21 * k), "А", font=ImageFont.truetype(BOLD, 22 * k),
              fill=(255, 220, 0), anchor="mm")


def raster_vector():
    """Same small picture enlarged 8x: raster gets blocky, vector stays sharp."""
    k = 8
    tiny = Image.new("RGB", (40, 40), BG)
    shape(ImageDraw.Draw(tiny), 1, 0, 0)
    raster = tiny.resize((40 * k, 40 * k), Image.NEAREST)
    W, H = 960, 470
    img = Image.new("RGB", (W, H), BG)
    img.paste(raster, (80, 70))
    d = ImageDraw.Draw(img)
    shape(d, k, W - 80 - 40 * k, 70)  # drawn directly at the big size = vector
    label(d, (80 + 20 * k, 22), "Растрова")
    label(d, (80 + 20 * k, 52), "збільшили — видно пікселі", 18)
    label(d, (W - 80 - 20 * k, 22), "Векторна")
    label(d, (W - 80 - 20 * k, 52), "збільшили — так само чітко", 18)
    label(d, (W / 2, 425), "Растр — це пікселі (фото). Вектор — це формули ліній і фігур (логотипи).", 19)
    img.save(os.path.join(OUT, "raster-vector.png"), optimize=True)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    pixels()
    raster_vector()
    print("ok")
