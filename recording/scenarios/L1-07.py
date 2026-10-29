# L1-07 Малюємо фігури
# Needs: L1-06 end state (blue colour, blue-circle layer selected).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

# outline width 15 (not recorded)
os.system("xdotool mousemove 985 36 click --repeat 2 --delay 80 1 sleep 0.3 key ctrl+a type 15; xdotool key Return mousemove 640 600")
wait(0.8)

start("L1-07")

caption("Крок 1. Оберіть інструмент «Прямокутник»")
click(12, 184, box=(1, 173, 23, 23), after=0.8)

caption("Крок 2. Протягніть мишею — від одного кута до протилежного")
drag(800, 500, 960, 640, dur=1.4, after=1.0)

caption("Крок 3. Інструмент «Еліпс» працює так само")
click(36, 184, box=(25, 173, 23, 23), after=0.8)
drag(820, 190, 960, 300, dur=1.4, after=1.2)

stop(tail=1.2)
