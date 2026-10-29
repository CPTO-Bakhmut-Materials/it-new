# L4-03 Перша програма: запуск
# Needs: L4-02 end state (hello.py with one print line).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L4-03")

caption("Крок 1. Збережіть файл: Ctrl+S")
key("ctrl+s", after=1.0)

caption("Крок 2. Запустіть програму: кнопка «Виконати» або F5")
box(590, 33, 30, 30, dur=1.6)
wait(1.2)
key("F5", after=2.5)

caption("Програма вивела текст! Нижче — службове повідомлення Geany")
box(222, 404, 400, 34, dur=2.5)
wait(2.8)

caption("Натисніть Enter, щоб закрити вікно виконання")
key("Return", label="Enter", after=1.2)

stop(tail=0.6)
