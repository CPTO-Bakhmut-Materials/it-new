# L4-06 Умова: якщо… інакше…
# Needs: Geany running.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

AGE = 'age = int(input("Скільки вам років? "))\nif age >= 18:\n    print("Ви повнолітні")\nelse:\n    print("Ви ще неповнолітні")\n'
clipboard(AGE)

start("L4-06")

caption("Новий файл age.py. if — «якщо», else — «інакше»")
key("ctrl+n", after=0.6)
key("ctrl+v", after=0.8)
clipboard_done()
key("ctrl+s", show=False, after=0.0)
wait(1.4)
type_("age.py", after=0.3)
key("Return", show=False, after=1.0)
box(78, 135, 260, 30, dur=2.0)
box(78, 193, 120, 30, dur=2.0)
wait(2.0)

caption("Відступ (4 пробіли) показує, що виконувати в кожному випадку")
box(78, 164, 420, 30, dur=2.6)
box(78, 222, 470, 30, dur=2.6)
wait(2.6)

caption("Запуск 1: вводимо 20 — умова виконується")
key("F5", after=2.0)
type_("20", after=0.3)
key("Return", label="Enter", after=2.0)
key("Return", show=False, after=0.8)

caption("Запуск 2: вводимо 15 — спрацьовує else")
key("F5", after=2.0)
type_("15", after=0.3)
key("Return", label="Enter", after=2.0)
key("Return", show=False, after=0.8)

stop(tail=0.6)
