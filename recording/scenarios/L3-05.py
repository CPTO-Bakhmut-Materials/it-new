# L3-05 Приватне вікно
# Needs: Firefox running.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L3-05")

caption("Крок 1. Ctrl+Shift+P — відкрити приватне вікно")
key("ctrl+shift+p", after=1.5)
box(1110, 8, 28, 28, dur=2.0)
wait(1.6)

caption("Після закриття приватного вікна Firefox забуде історію, cookie і введене")
box(355, 278, 570, 120, dur=3.5)
wait(3.5)

caption("Крок 2. Закрийте приватне вікно: Ctrl+Shift+W")
key("ctrl+shift+w", after=1.8)

stop(tail=0.6)
