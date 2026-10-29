# L2-05 Вирівнювання абзаців
# Needs: L2-04 end state (heading styles applied).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-05")

caption("Крок 1. Клацніть в абзаці й натисніть «По центру»")
click(330, 281, after=0.4)
click(1056, 85, box=(1042, 70, 29, 31), after=1.0)
click(330, 319, after=0.4)
click(1056, 85, box=(1042, 70, 29, 31), after=1.2)

caption("Крок 2. Довгий абзац — «За шириною»: рівні краї з обох боків")
click(500, 537, after=0.4)
click(1123, 85, box=(1109, 70, 29, 31), after=1.6)
box(212, 512, 762, 48, dur=1.8)
wait(1.8)

stop(tail=0.6)
