# L2-02 Вставляємо і виділяємо текст
# Needs: nothing; restarts Writer with an empty document.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

TEXT = os.path.join(REC_DIR, "..", "src", "lesson-2-writer", "files", "text.txt")

restart_app("libreoffice", "--writer", ready_title="Writer", procname="soffice.bin")
clipboard(open(TEXT, encoding="utf-8").read())

start("L2-02")

caption("Крок 1. Скопіюйте текст із файлу text.txt і вставте: Ctrl+V")
key("ctrl+v", after=1.8)
clipboard_done()

caption("Крок 2. Подвійне клацання виділяє одне слово")
click(318, 256, double=True, after=1.6)

caption("Крок 3. Протягніть мишею з натиснутою кнопкою — виділяться рядки")
drag(219, 411, 749, 433, dur=1.6, after=1.6)

caption("Крок 4. Ctrl+A виділяє весь текст")
key("ctrl+a", after=1.8)

caption("Клацніть будь-де в тексті, щоб зняти виділення")
click(600, 650, after=1.0)

stop(tail=0.8)
