#!/usr/bin/env python3
"""Pictures for the lesson 4 page: program-flow.png and L4-09.png (weak vs good AI request)."""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "src", "lesson-4-programming-ai", "media")
BOLD = os.path.join(HERE, "fonts", "FixelDisplay-Bold.otf")
SEMI = os.path.join(HERE, "fonts", "FixelText-SemiBold.otf")
TEXT = os.path.join(HERE, "fonts", "FixelText-Regular.otf")
MONO = "/usr/share/fonts/TTF/JetBrainsMonoNL-Regular.ttf"
INK = (30, 30, 30)
MUTED = (100, 100, 100)
RED = (215, 45, 45)
GREEN = (20, 130, 65)


def font(p, s):
    return ImageFont.truetype(p, s)


def arrow(d, a, b):
    d.line([a, b], fill=(90, 90, 90), width=4)
    d.polygon([b, (b[0] - 16, b[1] - 9), (b[0] - 16, b[1] + 9)], fill=(90, 90, 90))


def program_flow():
    W, H = 960, 330
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    cols = [("Вхід", "input()", ["Перше число: 12", "Друге число: 4"], (234, 242, 252)),
            ("Обробка", "+  −  *  /", ["a + b", "a − b", "a * b", "a / b"], (253, 244, 228)),
            ("Вихід", "print()", ["Сума: 16", "Різниця: 8", "Добуток: 48", "Частка: 3.0"], (232, 246, 236))]
    for i, (title, sub, lines, fill) in enumerate(cols):
        x = 20 + i * 320
        d.rounded_rectangle([x, 20, x + 270, 280], radius=16, fill=fill, outline=(170, 170, 170), width=2)
        d.text((x + 135, 52), title, font=font(BOLD, 26), fill=INK, anchor="mm")
        d.text((x + 135, 88), sub, font=font(MONO, 20), fill=MUTED, anchor="mm")
        for k, line in enumerate(lines):
            d.text((x + 30, 126 + k * 34), line, font=font(MONO, 19), fill=INK)
        if i < 2:
            arrow(d, (x + 276, 150), (x + 314, 150))
    d.text((W / 2, 310), "Будь-яка програма: отримує дані → щось із ними робить → показує результат",
           font=font(TEXT, 18), fill=MUTED, anchor="mm")
    img.save(os.path.join(OUT, "program-flow.png"), optimize=True)
    print("wrote program-flow.png")


def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > width:
            lines.append(cur)
            cur = w
        else:
            cur = t
    lines.append(cur)
    return lines


def prompts():
    W, H = 960, 520
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    cards = [
        ("Слабкий запит", RED, "поясни код",
         ["незрозуміло, хто питає і навіщо", "немає самого коду", "незрозуміло, якою має бути відповідь"]),
        ("Добрий запит", GREEN,
         "Я новачок у програмуванні. Поясни коротко, простими словами, що робить кожен рядок "
         "цієї програми на Python: [код програми]",
         ["хто ви: «я новачок»", "що зробити: «поясни кожен рядок»",
          "як: «коротко, простими словами»", "дані: сам код"]),
    ]
    for i, (title, col, prompt, notes) in enumerate(cards):
        x = 20 + i * 470
        d.text((x + 10, 30), title, font=font(BOLD, 26), fill=col)
        d.rounded_rectangle([x, 70, x + 450, 250], radius=14, fill=(246, 246, 246), outline=col, width=3)
        for k, line in enumerate(wrap(d, prompt, font(TEXT, 20), 410)):
            d.text((x + 20, 88 + k * 30), line, font=font(TEXT, 20), fill=INK)
        sym = font("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 20)
        for k, n in enumerate(notes):
            y = 280 + k * 40
            d.text((x + 12, y), "✗" if i == 0 else "✓", font=sym, fill=col)
            d.text((x + 42, y), n, font=font(TEXT, 20), fill=INK)
    d.text((W / 2, 490), "Формула доброго запиту: хто ви + що зробити + як (довжина, стиль) + потрібні дані",
           font=font(SEMI, 19), fill=INK, anchor="mm")
    img.save(os.path.join(OUT, "L4-09.png"), optimize=True)
    print("wrote L4-09.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    program_flow()
    prompts()
