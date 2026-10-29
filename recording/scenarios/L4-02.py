# L4-02 Створюємо файл програми
# Needs: nothing; restarts Geany (project profile) with an empty document.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

restart_app("geany", ready_title="Geany", procname="geany")

start("L4-02")

caption("Geany відкрився з порожнім файлом. Спершу збережемо його")
box(10, 72, 136, 34, dur=2.0)
wait(2.0)

caption("Крок 1. «Файл» → «Зберегти як…»")
click(25, 13, box=(2, 2, 48, 22), after=0.7)
click(80, 204, box=(2, 192, 380, 24), after=0.0)
wait(1.4)

caption("Крок 2. Назва файлу з розширенням .py — це програма на Python")
key("ctrl+a", show=False, after=0.1)
type_("hello.py", after=0.6)
key("Return", label="Enter", after=1.2)

caption("Крок 3. Наберіть команду — Geany розфарбує її, бо знає Python")
type_('print("Привіт, світе!")', after=1.0)
box(78, 106, 300, 30, dur=2.2)
wait(2.2)

stop(tail=0.6)
