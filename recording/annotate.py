#!/usr/bin/env python3
"""Turn raw/<ID>.mkv + raw/<ID>.events.json into an annotated GIF (and MP4).

Draws a soft halo around the cursor, a red ripple on every click, red boxes
around highlighted targets, key-press badges and a caption bar under the
screen.

    annotate.py L1-03 ../src/lesson-1-graphics/media [--mp4] [--width 960]
"""
import argparse
import bisect
import json
import os
import shutil
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont

REC_DIR = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(REC_DIR, "raw")
FPS = 15
W, H, BAR = 1280, 800, 72
FONT = os.path.join(REC_DIR, "fonts", "FixelDisplay-SemiBold.otf")
FONT_KEY = "/usr/share/fonts/TTF/JetBrainsMono-Bold.ttf"
RED = (230, 40, 40)
YELLOW = (255, 220, 0)


def load(clip):
    with open(os.path.join(RAW, clip + ".events.json")) as f:
        ev = json.load(f)
    t0 = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "stream=start_time", "-of",
         "csv=p=0", os.path.join(RAW, clip + ".mkv")],
        capture_output=True, text=True, check=True).stdout)
    return ev, t0


def key_label(s):
    names = {"ctrl": "Ctrl", "shift": "Shift", "alt": "Alt", "Return": "Enter",
             "Escape": "Esc", "Delete": "Delete", "BackSpace": "Backspace"}
    return " + ".join(names.get(p, p.upper() if len(p) == 1 else p)
                      for p in s.split("+"))


def draw_frame(img, t, ev, mouse_t, mouse_xy, font, font_key):
    # blurred areas (private paths); a mask logged just after a click starts at
    # that click, because the dialog it hides can appear before the mask is logged
    for e in ev:
        if e["kind"] != "mask":
            continue
        start = e["t"]
        clicks = [c["t"] for c in ev if c["kind"] in ("click", "key") and 0 <= e["t"] - c["t"] <= 0.5]
        if clicks:
            start = max(clicks)
        if start <= t <= e["t"] + e["dur"]:
            area = (e["x"], e["y"], e["x"] + e["w"], e["y"] + e["h"])
            img.paste(img.crop(area).filter(ImageFilter.GaussianBlur(6)), area[:2])

    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)

    # boxes around targets (with a gentle pulse)
    for e in ev:
        if e["kind"] == "box" and e["t"] <= t <= e["t"] + e["dur"]:
            pad = 5 + 2 * (((t - e["t"]) * 2) % 1 < 0.5)
            d.rounded_rectangle([e["x"] - pad, e["y"] - pad, e["x"] + e["w"] + pad,
                                 e["y"] + e["h"] + pad], radius=8,
                                outline=RED + (255,), width=4)

    # cursor halo; red while the button is held (drag)
    i = bisect.bisect_right(mouse_t, t) - 1
    if i >= 0:
        mx, my = mouse_xy[i]
        held = False
        for e in ev:
            if e["kind"] == "press" and e["t"] <= t:
                held = True
            if e["kind"] == "release" and e["t"] <= t:
                held = False
        col = RED if held else YELLOW
        r = 20
        d.ellipse([mx - r, my - r, mx + r, my + r], fill=col + (80,))

    # click ripples
    for e in ev:
        if e["kind"] in ("click", "press") and 0 <= t - e["t"] <= 0.7:
            k = (t - e["t"]) / 0.7
            r = 10 + 32 * k
            a = int(255 * (1 - k))
            d.ellipse([e["x"] - r, e["y"] - r, e["x"] + r, e["y"] + r],
                      outline=RED + (a,), width=5)

    # key badge (top centre)
    for e in ev:
        if e["kind"] == "key" and 0 <= t - e["t"] <= 1.6:
            text = key_label(e["label"])
            tw = d.textlength(text, font=font_key)
            x0, y0 = (W - tw) / 2 - 22, 60
            d.rounded_rectangle([x0, y0, x0 + tw + 44, y0 + 64], radius=12,
                                fill=(20, 20, 20, 225), outline=YELLOW + (255,), width=3)
            d.text((x0 + 22, y0 + 12), text, font=font_key, fill=(255, 255, 255, 255))

    img = Image.alpha_composite(img, over)

    # caption bar under the screen
    cap = None
    for e in ev:
        if e["kind"] == "caption" and e["t"] <= t:
            cap = e["text"]
    full = Image.new("RGBA", (W, H + BAR), (30, 30, 30, 255))
    full.paste(img, (0, 0))
    if cap:
        dd = ImageDraw.Draw(full)
        dd.rectangle([0, H, 8, H + BAR], fill=RED + (255,))
        f = font
        while dd.textlength(cap, font=f) > W - 48 and f.size > 18:
            f = ImageFont.truetype(FONT, f.size - 1)
        dd.text((28, H + BAR / 2), cap, font=f, fill=(255, 255, 255, 255), anchor="lm")
    return full


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("outdir")
    ap.add_argument("--mp4", action="store_true", help="also write an MP4")
    ap.add_argument("--width", type=int, default=960)
    args = ap.parse_args()

    ev, t0 = load(args.clip)
    t_start = next(e["t"] for e in ev if e["kind"] == "start") - 0.3
    t_end = next(e["t"] for e in ev if e["kind"] == "end")
    mouse = [e for e in ev if e["kind"] == "mouse"]
    mouse_t = [e["t"] for e in mouse]
    mouse_xy = [(e["x"], e["y"]) for e in mouse]
    font = ImageFont.truetype(FONT, 30)
    font_key = ImageFont.truetype(FONT_KEY, 34)

    tmp = tempfile.mkdtemp(prefix="annot-")
    try:
        src = os.path.join(tmp, "src")
        os.mkdir(src)
        subprocess.run(
            ["ffmpeg", "-loglevel", "error", "-ss", f"{t_start - t0:.3f}", "-i",
             os.path.join(RAW, args.clip + ".mkv"), "-t", f"{t_end - t_start:.3f}",
             "-vf", f"fps={FPS}", os.path.join(src, "%05d.png")], check=True)
        out = os.path.join(tmp, "out")
        os.mkdir(out)
        # parts between cut_start and cut_end are skipped; 1 s of the first
        # frames of a cut stays, with a "skipped" note
        cuts, open_cut = [], None
        for e in ev:
            if e["kind"] == "cut_start":
                open_cut = e
            elif e["kind"] == "cut_end" and open_cut:
                cuts.append((open_cut["t"] + 1.0, e["t"], open_cut.get("label", "")))
                open_cut = None
        names = sorted(os.listdir(src))
        kept = []
        for n, name in enumerate(names):
            t = t_start + n / FPS
            if any(a <= t < b for a, b, _ in cuts):
                continue
            img = Image.open(os.path.join(src, name)).convert("RGBA")
            frame = draw_frame(img, t, ev, mouse_t, mouse_xy, font, font_key)
            for a, b, label in cuts:
                if a - 1.0 <= t < a:
                    dd = ImageDraw.Draw(frame)
                    text = label + "  (очікування пропущено)"
                    fl = ImageFont.truetype(FONT, 30)
                    tw = dd.textlength(text, font=fl)
                    dd.rounded_rectangle([(W - tw) / 2 - 24, 340, (W + tw) / 2 + 24, 400], radius=14,
                                         fill=(20, 20, 20, 230))
                    dd.text((W / 2, 370), text, font=fl, fill=(255, 255, 255), anchor="mm")
            name = f"{len(kept) + 1:05d}.png"
            frame.convert("RGB").save(os.path.join(out, name))
            kept.append(name)
        names = kept

        os.makedirs(args.outdir, exist_ok=True)
        gif = os.path.join(args.outdir, args.clip + ".gif")
        frames = [os.path.join(out, n) for n in names]
        subprocess.run(["gifski", "--quiet", "--fps", str(FPS), "--width",
                        str(args.width), "--quality", "85", "--motion-quality", "100", "--lossy-quality", "100", "-o", gif, *frames],
                       check=True)
        print(f"{gif}: {len(names) / FPS:.1f} s, {os.path.getsize(gif) / 1e6:.2f} MB")
        if args.mp4:
            mp4 = os.path.join(args.outdir, args.clip + ".mp4")
            subprocess.run(
                ["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i",
                 os.path.join(out, "%05d.png"), "-vf", "scale=1280:-2", "-c:v",
                 "libx264", "-pix_fmt", "yuv420p", "-crf", "23", "-movflags",
                 "+faststart", mp4], check=True)
            print(f"{mp4}: {os.path.getsize(mp4) / 1e6:.2f} MB")
        # middle frame kept for quick visual checks
        shutil.copy(frames[len(frames) // 2], os.path.join(RAW, args.clip + ".check.png"))
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
