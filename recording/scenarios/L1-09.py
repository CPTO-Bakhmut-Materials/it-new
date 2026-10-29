# L1-09 Додаємо текст
# Needs: L1-08 end state. Leaves the extra «Властивості тексту» panel closed.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-09")

caption("Крок 1. Оберіть колір тексту")
click(1140, 110, box=(1099, 98, 84, 84), after=0.8)

caption("Крок 2. Оберіть інструмент «Текст» і протягніть рамку")
click(36, 82, box=(25, 71, 23, 23), after=0.6)
drag(120, 230, 600, 290, dur=1.2, after=0.8)

caption("Крок 3. Надрукуйте текст")
type_("Вітаю!", delay=150, after=1.0)

caption("Крок 4. Виділіть текст: Ctrl+A")
key("ctrl+a", after=1.0)

caption("Крок 5. «Параметри інструмента» → «Відкрити властивості тексту»")
click(1215, 68, box=(1158, 57, 120, 22), after=0.8)
click(1141, 211, box=(1022, 200, 238, 23), after=1.2)

caption("Крок 6. Вкладка «Символ» → «Розмір шрифту»: 48")
click(1148, 680, box=(1106, 671, 86, 18), after=0.6)
click(1130, 720, double=True, box=(1022, 708, 196, 24), after=0.3)
key("ctrl+a", show=False, after=0.1)
type_("48", delay=200)
key("Return", show=False, after=1.5)

caption("Готово! Клацніть поза текстом, щоб закінчити")
click(400, 640, after=1.0)

stop(tail=1.2)

# tidy up (not recorded): close the text panel, back to the colour tab, brush tool
os.system("xdotool mousemove 1269 661 click 1 sleep 0.5 mousemove 1085 68 click 1 sleep 0.3 key b")
