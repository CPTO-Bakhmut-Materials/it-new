# L1-08 Заливка кольором
# Needs: L1-07 end state (blue rectangle and ellipse on the selected layer).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-08")

caption("Крок 1. Оберіть інструмент «Заливка» (відерце)")
click(12, 388, box=(1, 377, 23, 23), after=0.8)

caption("Крок 2. Оберіть колір заливки")
click(1118, 110, box=(1099, 98, 84, 84), after=0.5)
click(1160, 148, after=0.8)

caption("Крок 3. Клацніть усередині замкненої фігури")
click(890, 245, after=1.2)
click(880, 570, after=1.5)

stop(tail=1.0)
