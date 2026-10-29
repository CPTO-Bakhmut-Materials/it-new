# L4-07 Читаємо помилку і виправляємо
# Needs: calc.py tab open (L4-05) — switches to it.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L4-07")

caption("Зробимо помилку: приберемо останню дужку в рядку 2")
click(150, 87, after=0.6)          # calc.py tab
click(700, 150, after=0.3)
key("End", show=False, after=0.4)
key("BackSpace", label="Backspace", after=1.0)
key("ctrl+s", show=False, after=0.3)

caption("Запускаємо (F5) — Python повідомляє про помилку")
key("F5", after=2.5)

caption("line 2 — номер рядка, SyntaxError — помилка в записі, ^ — де саме")
box(222, 404, 440, 112, dur=3.5)
wait(3.5)
key("Return", show=False, after=0.8)

caption("Повертаємо дужку в рядок 2, зберігаємо і запускаємо знову")
click(700, 150, after=0.3)
key("End", show=False, after=0.3)
type_(")", after=0.8)
key("ctrl+s", show=False, after=0.3)
key("F5", after=2.0)
type_("12", after=0.2)
key("Return", show=False, after=0.6)
type_("4", after=0.2)
key("Return", show=False, after=2.0)
caption("Тепер працює")
wait(1.5)
key("Return", show=False, after=0.6)

stop(tail=0.6)
