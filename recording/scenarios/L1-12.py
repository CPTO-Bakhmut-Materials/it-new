# L1-12 Змінюємо розмір фото
# Needs: L1-11 end state (cropped photo 1900x1109).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-12")

caption("Крок 1. «Зображення» → «Масштабувати зображення…»")
click(222, 9, box=(180, 0, 86, 19), after=0.8)
click(358, 279, box=(181, 269, 426, 21), after=1.5)

caption("Крок 2. Введіть нову ширину — висота зміниться сама")
click(605, 213, double=True, box=(555, 202, 108, 23), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("1200", delay=200, after=0.3)
key("Tab", show=False, after=0.6)
box(555, 231, 108, 23, dur=1.4)
box(818, 212, 20, 30, dur=1.4)
wait(1.6)

caption("Крок 3. Натисніть «Гаразд»")
click(743, 535, box=(705, 524, 76, 23), after=0.6)
box(706, 774, 152, 22, dur=1.8)
wait(1.6)

stop(tail=1.0)
