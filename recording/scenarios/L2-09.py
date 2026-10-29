# L2-09 Перевірка правопису
# Needs: L2-08 end state (the misspelled «Відповідалньа» visible at the top).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-09")

caption("Червона хвиляста лінія — можлива помилка в слові")
box(212, 270, 150, 30, dur=2.2)
wait(2.2)

caption("Крок 1. Клацніть по слову правою кнопкою миші")
click(285, 285, button=3, after=1.4)

caption("Крок 2. Оберіть правильний варіант угорі списку")
click(300, 315, box=(220, 303, 318, 25), after=1.8)

stop(tail=0.8)
