# L1-05 Гумка і скасування дії
# Needs: L1-04 end state (brush tool, canvas with zigzag and two lines).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-05")

caption("Крок 1. Увімкніть гумку кнопкою на панелі (або клавішею E)")
click(512, 36, box=(499, 24, 27, 25), after=1.0)

caption("Крок 2. Зробіть гумку більшою повзунком «Розмір»")
box(875, 25, 223, 23, dur=2.0)
drag(925, 36, 958, 36, dur=1.0, after=0.6)

caption("Крок 3. Проведіть по малюнку — лінії стираються")
drag(450, 300, 0, 0, dur=1.6, path=[(455, 480), (450, 670)], after=1.0)

caption("Крок 4. Помилились? Ctrl+Z скасовує останню дію")
key("ctrl+z", after=1.8)

caption("Крок 5. Вимкніть гумку тією ж кнопкою, щоб знову малювати")
click(512, 36, box=(499, 24, 27, 25), after=1.0)

stop(tail=1.2)
