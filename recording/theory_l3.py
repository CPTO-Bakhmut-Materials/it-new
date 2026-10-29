#!/usr/bin/env python3
"""Pictures for the lesson 3 page: url-anatomy.png and L3-07.png (fictional
phishing email). Brands and domains in the email are made up («ТвійБанк»)."""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "src", "lesson-3-internet", "media")
BOLD = os.path.join(HERE, "fonts", "FixelDisplay-Bold.otf")
SEMI = os.path.join(HERE, "fonts", "FixelText-SemiBold.otf")
TEXT = os.path.join(HERE, "fonts", "FixelText-Regular.otf")
MONO = "/usr/share/fonts/TTF/JetBrainsMono-Regular.ttf"
MONO_B = "/usr/share/fonts/TTF/JetBrainsMono-Bold.ttf"
RED = (230, 40, 40)
GREEN = (20, 140, 70)
BLUE = (40, 110, 210)
GREY = (120, 120, 120)
INK = (30, 30, 30)


def font(p, s):
    return ImageFont.truetype(p, s)


def url_row(d, x, y, parts, f):
    """Draw URL parts side by side; returns list of (x0, x1) per part."""
    spans = []
    for text, col in parts:
        w = d.textlength(text, font=f)
        d.text((x, y), text, font=f, fill=col)
        spans.append((x, x + w))
        x += w
    return spans


def brace(d, x0, x1, y, label, col, f):
    d.line([(x0 + 2, y), (x1 - 2, y)], fill=col, width=3)
    d.line([(x0 + 2, y - 8), (x0 + 2, y)], fill=col, width=3)
    d.line([(x1 - 2, y - 8), (x1 - 2, y)], fill=col, width=3)
    d.text(((x0 + x1) / 2, y + 22), label, font=f, fill=col, anchor="mm")


def url_anatomy():
    W, H = 960, 430
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    f = font(MONO, 25)
    fl = font(SEMI, 18)
    d.text((30, 24), "Справжній сайт", font=font(BOLD, 21), fill=GREEN)
    s = url_row(d, 30, 66, [("https://", GREY), ("osvita.", BLUE), ("diia.gov.ua", GREEN),
                            ("/courses/resume", GREY)], f)
    brace(d, *s[0], 110, "протокол", GREY, fl)
    brace(d, s[1][0], s[2][1], 110, "домен — до першої «/»", BLUE, fl)
    brace(d, *s[3], 110, "шлях: сторінка на сайті", GREY, fl)
    d.text((30, 165), "Власник сайту — diia.gov.ua (останні частини домену перед «/»)",
           font=font(TEXT, 18), fill=INK)

    d.line([(30, 205), (W - 30, 205)], fill=(220, 220, 220), width=2)
    d.text((30, 222), "Підробка: схожа назва на початку, але інший власник", font=font(BOLD, 21), fill=RED)
    s = url_row(d, 30, 264, [("https://", GREY), ("diia.gov.ua.", (150, 150, 150)), ("verify-login.com", RED),
                             ("/diia", GREY)], f)
    brace(d, s[1][0], s[2][1], 308, "домен — до першої «/»", RED, fl)
    d.text((30, 360), "Читайте домен з кінця: власник — verify-login.com, а не Дія.",
           font=font(TEXT, 18), fill=INK)
    d.text((30, 388), "Замок (https) є і тут: він означає шифрування, а не чесність сайту.",
           font=font(TEXT, 18), fill=INK)
    img.save(os.path.join(OUT, "url-anatomy.png"), optimize=True)
    print("wrote url-anatomy.png")


def phishing_email():
    W, H = 1280, 800
    img = Image.new("RGB", (W, H), (244, 246, 249))
    d = ImageDraw.Draw(img)
    # mail client chrome
    d.rectangle([0, 0, W, 56], fill=(52, 72, 110))
    d.text((24, 28), "Пошта", font=font(BOLD, 24), fill=(255, 255, 255), anchor="lm")
    d.rectangle([0, 56, 230, H], fill=(232, 236, 242))
    for i, t in enumerate(["Вхідні (1)", "Надіслані", "Чернетки", "Спам"]):
        d.text((24, 92 + i * 40), t, font=font(SEMI if i == 0 else TEXT, 19), fill=INK)
    # message
    x0 = 260
    d.rounded_rectangle([x0, 76, W - 30, H - 24], radius=10, fill=(255, 255, 255), outline=(215, 218, 224))
    d.text((x0 + 30, 104), "ТЕРМІНОВО!!! Ваш рахунок заблоковано", font=font(BOLD, 28), fill=INK)
    d.text((x0 + 30, 152), "Від:", font=font(SEMI, 18), fill=GREY)
    d.text((x0 + 76, 152), "Служба безпеки ТвійБанк <support@tviybank-secure-mail.com>",
           font=font(TEXT, 18), fill=INK)
    d.text((x0 + 30, 180), "Кому: вам", font=font(TEXT, 18), fill=GREY)
    body = ["Шановний клієнт,",
            "",
            "через підозрілу активність ваш рахунок буде заблоковано протягом 2 годин.",
            "Щоб зберегти доступ до коштів, негайно підтвердіть свої дані:",
            "номер картки, термін дії, CVV-код та код з SMS.",
            "",
            "Якщо не підтвердити дані сьогодні, кошти будуть заморожені безтерміново.",
            "",
            "З повагою, служба безпекі ТвійБанк"]
    for i, line in enumerate(body):
        d.text((x0 + 30, 236 + i * 32), line, font=font(TEXT, 20), fill=INK)
    btn = (x0 + 30, 548, x0 + 330, 600)
    d.rounded_rectangle(btn, radius=8, fill=(30, 140, 80))
    d.text(((btn[0] + btn[2]) / 2, 574), "Підтвердити дані", font=font(SEMI, 21), fill=(255, 255, 255), anchor="mm")
    # hover tooltip with the real link
    d.rounded_rectangle([x0 + 30, 616, x0 + 560, 650], radius=6, fill=(60, 60, 60))
    d.text((x0 + 42, 633), "http://tviybank-ua.secure-check.com/login", font=font(MONO, 17),
           fill=(255, 255, 255), anchor="lm")
    d.polygon([(x0 + 190, 598), (x0 + 200, 614), (x0 + 210, 598)], fill=(60, 60, 60))

    marks = [  # (box, number)
        ((x0 + 22, 96, x0 + 640, 140), 1),     # urgency in subject
        ((x0 + 72, 146, x0 + 650, 176), 2),    # strange sender domain
        ((x0 + 22, 324, x0 + 640, 394), 3),    # asks for card, CVV and SMS code
        ((x0 + 22, 610, x0 + 568, 656), 4),    # link goes to a different domain
        ((x0 + 22, 486, x0 + 470, 518), 5),    # spelling mistake
    ]
    for (a, b, c, e), n in marks:
        d.rounded_rectangle([a, b, c, e], radius=6, outline=RED, width=4)
        r = 18
        cx, cy = c + 4, b + 4
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED, outline=(255, 255, 255), width=2)
        d.text((cx, cy), str(n), font=font(BOLD, 22), fill=(255, 255, 255), anchor="mm")
    # stamp
    d.text((W - 60, H - 52), "НАВЧАЛЬНИЙ ПРИКЛАД · вигаданий банк", font=font(SEMI, 16), fill=(170, 170, 170), anchor="rm")
    img = img.resize((960, 600), Image.LANCZOS)
    img.save(os.path.join(OUT, "L3-07.png"), optimize=True)
    print("wrote L3-07.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    url_anatomy()
    phishing_email()
