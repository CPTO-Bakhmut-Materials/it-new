# L2-11 Експорт у PDF
# Needs: L2-10 end state.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-11")

caption("Крок 1. Кнопка «Експортувати безпосередньо як PDF»")
click(161, 46, box=(147, 32, 29, 29), after=0.0)
mask(205, 168, 630, 40, dur=4.5)   # the folder path shows the user's name
wait(1.6)

x, y, w, h = win_geom("Експорт")
caption("Крок 2. Назва вже є, формат — PDF. Натисніть «Експорт»")
box(x + 120, y + 401, 616, 80, dur=1.8)
wait(1.8)
click(x + 804, y + 419, box=(x + 746, y + 403, 117, 33), after=1.8)

caption("Готово! PDF виглядає однаково на будь-якому пристрої — його й надсилайте")
wait(2.0)

stop(tail=0.6)
