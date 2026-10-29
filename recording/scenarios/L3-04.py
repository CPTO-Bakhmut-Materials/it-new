# L3-04 Додаємо закладку
# Needs: L3-03 end state (Wikipedia tab active).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L3-04")

caption("Крок 1. Зірочка в адресному рядку — додати сторінку до закладок")
click(1076, 65, box=(1062, 51, 28, 28), after=1.2)

caption("Крок 2. Назву можна змінити. Натисніть «Зберегти»")
box(668, 162, 403, 42, dur=1.6)
wait(1.6)
click(1011, 380, box=(953, 361, 118, 39), after=1.2)

caption("Крок 3. Ctrl+Shift+B — показати панель закладок під адресним рядком")
key("ctrl+shift+b", after=1.0)
box(2, 86, 300, 34, dur=2.5)
wait(2.5)

stop(tail=0.6)
os.system("xdotool key ctrl+shift+b")   # hide the bar again (not recorded)
