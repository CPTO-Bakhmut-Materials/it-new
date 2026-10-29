# L4-11 ШІ шукає помилку
# Needs: Duck.ai open in Firefox; buggy.py copied to /tmp/kurs/programs.
import sys, os, subprocess, shutil
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

SRC = os.path.join(REC_DIR, "..", "src", "lesson-4-programming-ai", "files", "buggy.py")
os.makedirs("/tmp/kurs/programs", exist_ok=True)
shutil.copy(SRC, "/tmp/kurs/programs/buggy.py")
err = subprocess.run([sys.executable, "/tmp/kurs/programs/buggy.py"], capture_output=True, text=True,
                     input="").stderr.strip()
code = open(SRC, encoding="utf-8").read()
PROMPT = ("Моя програма на Python не запускається. Python пише:\n\n" + err +
          "\n\nОсь код. Знайди помилки і коротко поясни, як їх виправити:\n\n" + code)

start("L4-11")

caption("Крок 1. Новий чат. Вставте текст помилки і код програми")
click(94, 177, box=(14, 160, 120, 34), after=1.5)
clipboard(PROMPT)
click(800, 437, after=0.3)
key("ctrl+v", after=1.0)
clipboard_done()
wait(2.0)

caption("Крок 2. Надішліть і прочитайте пояснення")
key("Return", label="Enter", after=0.5)
cut_start()
wait_stable(460, 90, 740, 540, scroll_at=(800, 400))
cut_end()
scroll_down()
wait(1.0)

caption("ШІ знайшов обидві помилки й пояснив їх. Виправляйте самі — так ви вчитеся")
box(470, 120, 720, 380, dur=5.0)
wait(5.0)

stop(tail=0.6)
