# L4-10 ШІ пояснює код
# Needs: L4-08 end state (Duck.ai open, terms accepted).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

CALC = open(os.path.join(REC_DIR, "..", "src", "lesson-4-programming-ai", "files", "calc.py"), encoding="utf-8").read()
PROMPT = ("Я новачок у програмуванні. Поясни коротко, простими словами, "
          "що робить кожен рядок цієї програми на Python:\n\n" + CALC)

# open a new chat and close Duck.ai's "now with PDF" promo card (not recorded)
click(94, 177, after=1.5)
click(1130, 657, after=0.8)

start("L4-10")

caption("Крок 1. «Новий чат». Напишіть, хто ви і що потрібно, і вставте код")
click(94, 177, box=(14, 160, 120, 34), after=1.5)
clipboard(PROMPT)
click(800, 437, after=0.3)
key("ctrl+v", after=1.0)
clipboard_done()
box(455, 330, 745, 280, dur=2.5)
wait(2.5)

caption("Крок 2. Надішліть: Enter")
key("Return", label="Enter", after=0.5)
cut_start()
wait_stable(460, 90, 740, 540, scroll_at=(800, 400))
cut_end()

caption("ШІ пояснив кожен рядок. Перевіряйте пояснення — ШІ може помилятися")
scroll_down()
wait(1.0)
box(470, 160, 720, 330, dur=4.0)
wait(4.0)

stop(tail=0.6)
r, g, b = pixel(190, 500)
if 220 <= r <= 240 and abs(r - b) < 6:     # dismiss the sidebar tip «Зрозуміло!»
    os.system("xdotool mousemove 84 535 click 1")
