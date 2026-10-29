# L1-04 Змінюємо розмір пензля
# Needs: L1-03 end state (brush tool, red colour, canvas with a zigzag).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

# reset brush size to 40 (not recorded)
os.system("xdotool mousemove 985 36 click --repeat 2 --delay 80 1 sleep 0.3 key ctrl+a type 40; xdotool key Return mousemove 640 600")
wait(0.8)

start("L1-04")

caption("Крок 1. Потягніть повзунок «Розмір» праворуч — лінія товща")
box(875, 25, 223, 23, dur=3.2)
drag(946, 36, 962, 36, dur=1.2, after=0.8)
drag(200, 560, 0, 0, dur=1.4, path=[(450, 540), (700, 560)])

caption("Крок 2. Потягніть ліворуч — лінія тонша")
box(875, 25, 223, 23, dur=3.2)
drag(962, 36, 925, 36, dur=1.2, after=0.8)
drag(200, 630, 0, 0, dur=1.4, path=[(450, 610), (700, 630)])

stop(tail=1.5)
