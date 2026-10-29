# L4-05 Простий калькулятор
# Needs: Geany running (L4-04 end state).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

CALC = open(os.path.join(REC_DIR, "..", "src", "lesson-4-programming-ai", "files", "calc.py"), encoding="utf-8").read()
clipboard(CALC)

start("L4-05")

caption("Крок 1. Новий файл: Ctrl+N. Наберіть або вставте код калькулятора")
key("ctrl+n", after=0.8)
key("ctrl+v", after=1.0)
clipboard_done()
box(78, 106, 560, 178, dur=2.5)
caption("int() перетворює введений текст на число; + − * / — дії з числами")
wait(3.0)

caption("Крок 2. Збережіть як calc.py (Ctrl+S) і запустіть (F5)")
key("ctrl+s", after=0.0)
wait(1.4)
type_("calc.py", after=0.4)
key("Return", label="Enter", after=1.0)
key("F5", after=2.0)

caption("Крок 3. Введіть два числа, після кожного — Enter")
type_("12", after=0.3)
key("Return", label="Enter", after=0.8)
type_("4", after=0.3)
key("Return", label="Enter", after=2.5)

caption("Готово: сума, різниця, добуток і частка. Enter — закрити вікно")
wait(1.5)
key("Return", show=False, after=0.8)

stop(tail=0.6)
