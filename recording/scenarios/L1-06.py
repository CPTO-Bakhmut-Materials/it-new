# L1-06 Працюємо з шарами
# Needs: L1-05 end state (brush tool, red zigzag + lines on «Шар малювання 1»).
import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-06")

caption("Крок 1. Додайте новий шар кнопкою «+» на панелі «Шари»")
click(1034, 466, box=(1022, 455, 24, 23), after=1.2)
box(1020, 322, 258, 24, dur=1.2)
wait(1.2)

caption("Крок 2. Оберіть інший колір і малюйте на новому шарі")
click(1161, 166, box=(1099, 98, 84, 84), after=0.5)
click(1160, 148, after=0.6)
cx, cy, r = 700, 360, 70
circle = [(round(cx + r * math.sin(a / 24 * 2 * math.pi)),
           round(cy - r * math.cos(a / 24 * 2 * math.pi))) for a in range(1, 26)]
drag(cx, cy - r, 0, 0, dur=2.0, path=circle, after=0.8)

caption("Крок 3. «Око» ховає шар і показує його знову")
click(1031, 333, box=(1021, 323, 21, 21), after=1.3)
click(1031, 333, after=1.3)

caption("Крок 4. Стрілка опускає шар нижче — тепер він під червоними лініями")
click(1109, 466, box=(1097, 455, 25, 23), after=1.8)

stop(tail=1.2)
