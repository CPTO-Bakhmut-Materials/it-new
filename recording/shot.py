#!/usr/bin/env python3
"""Annotated screenshot: numbered red boxes on the current virtual screen.

    shot.py OUT.png "x,y,w,h" "x,y,w,h" ...     (boxes numbered 1, 2, …)
    shot.py OUT.png --from raw.png "x,y,w,h" …  (use an existing screenshot)
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
RED = (230, 40, 40)


def main():
    out, args = sys.argv[1], sys.argv[2:]
    if args[0] == "--from":
        src, args = args[1], args[2:]
    else:
        src = os.path.join(tempfile.mkdtemp(), "s.png")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "x11grab", "-video_size",
                        "1280x800", "-i", ":99", "-frames:v", "1", src], check=True,
                       env={**os.environ, "DISPLAY": ":99"})
    img = Image.open(src).convert("RGBA")
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    font = ImageFont.truetype(FONT, 22)
    for n, a in enumerate(args, 1):
        a, _, at = a.partition("@")          # optional "@bx,by": badge position
        x, y, w, h = map(int, a.split(","))
        d.rounded_rectangle([x, y, x + w, y + h], radius=6, outline=RED + (255,), width=4)
        r = 16
        if at:
            cx, cy = map(int, at.split(","))
        elif h < 40:   # small target: badge below it, so it does not hide the icon
            cx = min(max(x + w / 2, r + 2), img.width - r - 2)
            cy = y + h + r + 4
        else:
            cx = min(max(x + w - 6, r + 2), img.width - r - 2)
            cy = min(max(y + 6, r + 2), img.height - r - 2)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED + (255,),
                  outline=(255, 255, 255, 255), width=2)
        d.text((cx, cy), str(n), font=font, fill=(255, 255, 255, 255), anchor="mm")
    img = Image.alpha_composite(img, over).convert("RGB")
    img = img.resize((960, 600), Image.LANCZOS)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    img.save(out, optimize=True)
    print(out)


if __name__ == "__main__":
    main()
