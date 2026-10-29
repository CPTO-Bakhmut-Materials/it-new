# L3-03 Вкладки
# Needs: L3-02 end state (one tab with Google results).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L3-03")

caption("Крок 1. Ctrl+T — нова вкладка. Введіть адресу сайту")
key("ctrl+t", after=0.8)
type_("uk.wikipedia.org", after=0.4)
key("Return", label="Enter", after=3.5)

caption("Крок 2. Клацніть вкладку вгорі, щоб перейти до неї")
click(130, 21, box=(2, 3, 266, 36), after=1.5)
click(400, 21, box=(272, 3, 266, 36), after=1.5)

caption("Крок 3. Хрестик на вкладці закриває її")
click(521, 21, box=(508, 9, 26, 26), after=1.5)

caption("Закрили випадково? Ctrl+Shift+T відкриває її знову")
key("ctrl+shift+t", after=2.5)

stop(tail=0.6)
