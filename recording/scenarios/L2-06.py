# L2-06 Маркований і нумерований список
# Needs: L2-05 end state.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-06")

caption("Крок 1. Виділіть рядки, які мають стати списком")
drag(219, 628, 487, 700, dur=1.4, after=0.8)

caption("Крок 2. «Маркований список» — для переліку")
click(1161, 85, box=(1147, 70, 29, 31), after=1.6)

caption("Крок 3. «Нумерований список» — коли важливий порядок (кроки, пункти)")
click(1205, 85, box=(1191, 70, 29, 31), after=1.8)

caption("Для навичок порядок не важливий — повертаємо маркери")
click(1161, 85, box=(1147, 70, 29, 31), after=1.2)
click(990, 398, after=1.0)

stop(tail=0.6)
