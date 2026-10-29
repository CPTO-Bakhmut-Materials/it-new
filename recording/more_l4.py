#!/usr/bin/env python3
"""Pictures and charts for lesson 4, page «Детальніше» (src/lesson-4-programming-ai/more.md).

Everything is real: the same program in five languages (compiled and run here),
Python speed measured on this computer, real Python error messages for bad
variable names, and real Duck.ai screenshots kept in recording/raw.

    python3 recording/more_l4.py
"""
import json
import os
import subprocess
import sys
import tempfile
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "src", "lesson-4-programming-ai", "media", "more")
RAW = os.path.join(HERE, "raw")
F_BOLD = os.path.join(HERE, "fonts", "FixelDisplay-Bold.otf")
F_SEMI = os.path.join(HERE, "fonts", "FixelText-SemiBold.otf")
F_TEXT = os.path.join(HERE, "fonts", "FixelText-Regular.otf")
MONO = "/usr/share/fonts/TTF/JetBrainsMonoNL-Regular.ttf"
INK = (30, 30, 30)
MUTED = (100, 100, 100)
RED = (215, 45, 45)
GREEN = (20, 130, 65)
BLUE = "#2a78d6"     # validated categorical slot 1 (single series)
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


def font(p, s):
    return ImageFont.truetype(p, s)


def save(img, name):
    img.save(os.path.join(OUT, name), optimize=True)
    print("wrote", name)


# --- 1. The same program in five languages -------------------------------------------

LANGS = [
    ("Python", "hello.py", 'print("Привіт, світе!")\n', None, ["python3", "hello.py"]),
    ("JavaScript", "hello.js", 'console.log("Привіт, світе!");\n', None, ["node", "hello.js"]),
    ("C", "hello.c", '#include <stdio.h>\n\nint main(void) {\n    printf("Привіт, світе!\\n");\n    return 0;\n}\n',
     ["gcc", "-o", "hc", "hello.c"], ["./hc"]),
    ("Java", "Hello.java", 'public class Hello {\n    public static void main(String[] args) {\n'
     '        System.out.println("Привіт, світе!");\n    }\n}\n', ["javac", "Hello.java"], ["java", "Hello"]),
    ("Rust", "hello.rs", 'fn main() {\n    println!("Привіт, світе!");\n}\n', ["rustc", "-o", "hr", "hello.rs"], ["./hr"]),
]


def languages():
    tmp = tempfile.mkdtemp()
    results = []
    for name, fn, code, build, run in LANGS:
        with open(os.path.join(tmp, fn), "w") as f:
            f.write(code)
        if build:
            subprocess.run(build, cwd=tmp, check=True, capture_output=True)
        out = subprocess.run(run, cwd=tmp, check=True, capture_output=True, text=True).stdout.strip()
        results.append((name, code.rstrip("\n"), out))
    numbers["languages_output"] = {n: o for n, _, o in results}
    W = 960
    hs = [40 + 22 * c.count("\n") + 60 for _, c, _ in results]
    H = sum(hs) + 20 * len(results) + 20
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    y = 20
    for (name, code, out), h in zip(results, hs):
        d.rounded_rectangle([20, y, W - 20, y + h], radius=12, fill=(247, 247, 247), outline=(200, 200, 200), width=2)
        d.text((40, y + 14), name, font=font(F_BOLD, 22), fill=INK)
        d.text((40, y + 48), code, font=font(MONO, 17), fill=INK, spacing=5)
        d.text((W - 40, y + 14), "результат:", font=font(F_TEXT, 16), fill=MUTED, anchor="ra")
        d.text((W - 40, y + 38), out, font=font(MONO, 18), fill=GREEN, anchor="ra")
        y += h + 20
    save(img, "languages.png")


# --- 2. How fast is Python ------------------------------------------------------------------

def speed_chart():
    ns = [10 ** k for k in range(3, 9)]
    times = []
    for n in ns:
        code = f"s = 0\nfor i in range({n}):\n    s += i\n"
        t0 = time.perf_counter()
        subprocess.run([sys.executable, "-c", code], check=True)
        t1 = time.perf_counter()
        base0 = time.perf_counter()
        subprocess.run([sys.executable, "-c", "pass"], check=True)
        base = time.perf_counter() - base0
        times.append(max(t1 - t0 - base, 1e-4))
    numbers["speed_seconds"] = {f"{n:,}".replace(",", " "): round(t, 4) for n, t in zip(ns, times)}
    labels = ["1 тис.", "10 тис.", "100 тис.", "1 млн", "10 млн", "100 млн"]
    fig, ax = plt.subplots(figsize=(9.6, 4.4), dpi=100)
    ax.bar(range(len(ns)), times, color=BLUE, width=0.6, zorder=3)
    ax.set_yscale("log")
    for i, t in enumerate(times):
        txt = f"{t * 1000:.1f} мс" if t < 1 else f"{t:.1f} с"
        ax.annotate(txt.replace(".", ","), (i, t), textcoords="offset points", xytext=(0, 5), ha="center",
                    fontsize=12, color="#0b0b0b")
    ax.set_xticks(range(len(ns)), labels)
    ax.set_xlabel("Скільки чисел додати (цикл for у Python)")
    ax.set_ylabel("Час (логарифмічна шкала)")
    ax.set_yticks([1e-3, 1e-2, 1e-1, 1, 10], ["1 мс", "10 мс", "0,1 с", "1 с", "10 с"])
    ax.minorticks_off()
    ax.grid(axis="x", visible=False)
    ax.set_title("Скільки часу Python додає числа (виміряно на звичайному ноутбуці)",
                 loc="left", fontsize=15, fontweight="semibold", color="#0b0b0b", pad=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "speed-chart.png"))
    plt.close(fig)
    print("wrote speed-chart.png")


# --- 3. Variable names: real Python messages --------------------------------------------------

NAMES = [
    ("price = 100", True),
    ("first_name = \"Оксана\"", True),
    ("ціна = 100", True),
    ("2price = 100", False),
    ("first-name = \"Оксана\"", False),
    ("class = 5", False),
]


def names():
    rows = []
    for code, _ in NAMES:
        r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
        msg = r.stderr.strip().splitlines()[-1].split(". ")[0] if r.returncode else "працює"
        rows.append((code, r.returncode == 0, msg))
    numbers["names"] = rows
    W, rh = 960, 58
    H = 60 + rh * len(rows) + 20
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((30, 18), "Рядок коду", font=font(F_SEMI, 18), fill=MUTED)
    d.text((400, 18), "Що каже Python", font=font(F_SEMI, 18), fill=MUTED)
    sym = font("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 22)
    for i, (code, ok, msg) in enumerate(rows):
        y = 60 + i * rh
        d.rounded_rectangle([20, y, W - 20, y + rh - 8], radius=8, fill=(240, 248, 242) if ok else (252, 238, 238))
        d.text((34, y + 25), "✓" if ok else "✗", font=sym, fill=GREEN if ok else RED, anchor="lm")
        d.text((66, y + 25), code, font=font(MONO, 18), fill=INK, anchor="lm")
        d.text((400, y + 25), msg[:62], font=font(MONO, 15), fill=GREEN if ok else RED, anchor="lm")
    save(img, "names.png")


# --- 4. Interpreter -------------------------------------------------------------------------

def interpreter():
    W, H = 960, 300
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    boxes = [("Ваш код", "hello.py", (234, 242, 252)), ("Інтерпретатор", "python3", (253, 244, 228)),
             ("Результат", "Привіт, світе!", (232, 246, 236))]
    for i, (t, s, fill) in enumerate(boxes):
        x = 20 + i * 320
        d.rounded_rectangle([x, 30, x + 270, 190], radius=16, fill=fill, outline=(170, 170, 170), width=2)
        d.text((x + 135, 80), t, font=font(F_BOLD, 24), fill=INK, anchor="mm")
        d.text((x + 135, 130), s, font=font(MONO, 19), fill=MUTED, anchor="mm")
        if i < 2:
            d.line([(x + 276, 110), (x + 314, 110)], fill=(90, 90, 90), width=4)
            d.polygon([(x + 314, 110), (x + 298, 101), (x + 298, 119)], fill=(90, 90, 90))
    d.text((W / 2, 230), "Інтерпретатор читає програму рядок за рядком і одразу виконує кожен рядок.",
           font=font(F_TEXT, 18), fill=INK, anchor="mm")
    d.text((W / 2, 262), "Помилку запису (SyntaxError) він помічає ще до запуску — тому програма не виконується зовсім.",
           font=font(F_TEXT, 17), fill=MUTED, anchor="mm")
    save(img, "interpreter.png")


# --- 5. How a language model writes: next-word prediction (illustration) ----------------------

def next_word():
    words = [("мова", 0.62), ("змія", 0.21), ("програма", 0.09), ("книга", 0.05), ("річка", 0.03)]
    fig, ax = plt.subplots(figsize=(9.6, 3.8), dpi=100)
    ys = list(range(len(words)))
    ax.barh(ys, [p for _, p in words], color=BLUE, height=0.55, zorder=3)
    for y, (w, p) in zip(ys, words):
        ax.annotate(f"{p:.0%}", (p, y), textcoords="offset points", xytext=(6, 0), va="center", fontsize=13)
    ax.set_yticks(ys, [w for w, _ in words], fontsize=14)
    ax.invert_yaxis()
    ax.set_xlim(0, 0.75)
    ax.xaxis.set_visible(False)
    ax.grid(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_title("«Python — це популярна …»  Яке слово далі? (умовний приклад)",
                 loc="left", fontsize=15, fontweight="semibold", color="#0b0b0b", pad=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "next-word.png"))
    plt.close(fig)
    print("wrote next-word.png")


# --- 6. Real Duck.ai screenshots --------------------------------------------------------------------

def two_answers():
    """The same request (L4-11) on two recording runs: different wording, same fix."""
    # run 1: only the annotated GIF frame is left, so crop inside the red box
    a = Image.open(os.path.join(RAW, "chk", "ai-ends.png")).convert("RGB").crop((356, 92, 892, 376))
    # run 2: clean frame from the raw recording (1280 px) scaled to the same 960-px space
    b = Image.open(os.path.join(RAW, "L4-11-final.png")).convert("RGB").resize((960, 600), Image.LANCZOS)
    b = b.crop((356, 92, 892, 376))
    W = a.width * 2 + 60
    img = Image.new("RGB", (W, a.height + 60), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for i, (im, t) in enumerate(((a, "Спроба 1"), (b, "Спроба 2"))):
        x = 20 + i * (a.width + 20)
        img.paste(im, (x, 50))
        d.rectangle([x, 50, x + a.width, 50 + a.height], outline=(170, 170, 170), width=2)
        d.text((x + a.width / 2, 26), t, font=font(F_BOLD, 22), fill=INK, anchor="mm")
    img = img.resize((960, int(img.height * 960 / img.width)), Image.LANCZOS)
    save(img, "two-answers.png")


def honest_answer():
    im = Image.open(os.path.join(RAW, "hall1.png")).convert("RGB").crop((460, 95, 1210, 335))
    save(im, "no-such-function.png")


def privacy_note():
    im = Image.open(os.path.join(RAW, "d11.png")).convert("RGB").crop((470, 140, 1200, 200))
    save(im, "privacy-note.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    languages()
    speed_chart()
    names()
    interpreter()
    next_word()
    two_answers()
    honest_answer()
    privacy_note()
    print(json.dumps(numbers, ensure_ascii=False, indent=1))
