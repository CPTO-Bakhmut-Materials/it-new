# L4-04 Змінні та введення
# Needs: L4-03 end state (hello.py open, run window closed).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L4-04")

caption("Крок 1. input() питає користувача, а змінна name запам’ятовує відповідь")
key("ctrl+a", show=False, after=0.2)
type_('name = input("Як вас звати? ")\nprint("Привіт,", name)', delay=90, after=1.0)
box(78, 106, 420, 60, dur=2.0)
wait(2.0)

caption("Крок 2. Ctrl+S, потім F5")
key("ctrl+s", after=0.6)
key("F5", after=2.5)

caption("Крок 3. Програма чекає: введіть ім’я і натисніть Enter")
type_("Оксана", after=0.5)
key("Return", label="Enter", after=2.0)

caption("Програма привіталася на ім’я. Enter — закрити вікно")
wait(1.5)
key("Return", label="Enter", after=1.0)

stop(tail=0.6)
