# L1-03 Обираємо пензель і колір
# Needs: Krita with an empty 1920x1080 canvas (L1-02 end state).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

# reset: remove earlier strokes, default preset and colours, move tool selected
os.system("xdotool key ctrl+z ctrl+z ctrl+z d t; xdotool mousemove 1110 637 click 1; xdotool key t; xdotool mousemove 640 400")
wait(1)

start("L1-03")

caption("Крок 1. Оберіть інструмент «Пензель»")
click(12, 160, box=(1, 149, 23, 23), after=1.0)

caption("Крок 2. Оберіть вид пензля в «Наборах пензлів»")
click(1110, 577, box=(1081, 547, 58, 60), after=1.0)

caption("Крок 3. Клацніть колір на колі, потім — яскравий кут трикутника")
click(1107, 130, box=(1099, 98, 84, 84), after=0.8)
click(1160, 148, after=1.0)

caption("Крок 4. Малюйте, утримуючи ліву кнопку миші")
drag(200, 450, 0, 0, dur=2.2, path=[(300, 350), (400, 450), (500, 350), (600, 450), (700, 350), (800, 450)])

stop(tail=2.0)
