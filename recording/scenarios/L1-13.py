# L1-13 Робимо фото світлішим
# Needs: L1-12 end state (photo 1200x700, fitted in the view).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-13")

caption("Крок 1. «Фільтри» → «Коригування» → «Коригування HSV/HSL» (Ctrl+U)")
click(392, 9, box=(363, 0, 58, 19), after=0.7)
move(432, 75, dur=0.5)
box(364, 65, 382, 21, dur=0.9)
wait(0.4)
move(520, 75, dur=0.3)
wait(0.4)
click(878, 229, box=(746, 219, 416, 21), after=1.5)

# the dialog opens where it was last left; move it above the photo
x, y, w, h = win_geom("HSV/HSL")
caption("Крок 2. Перетягніть вікно за заголовок вище, щоб бачити фото")
drag(x + 334, y - 13, 630, 57, dur=1.2, after=0.8)
x, y = 296, 70   # client area after the move

caption("Крок 3. Повзунок «Освітленість» праворуч — фото світлішає")
box(x + 102, y + 131, 486, 24, dur=3.0)
drag(x + 343, y + 153, 0, 0, dur=2.0, path=[(x + 380, y + 153), (x + 440, y + 153)], after=1.5)

caption("Крок 4. Натисніть «Гаразд»")
click(x + 511, y + 237, box=(x + 473, y + 226, 78, 23), after=2.0)

stop(tail=1.0)
