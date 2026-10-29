# L4-12 ШІ доповнює програму — і ми її перевіряємо
# Needs: L4-10 end state (the explanation chat open); Geany running with calc.py (L4-07).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L4-12")

caption("Крок 1. Попросіть змінити програму в тому самому чаті")
clipboard("Додай у програму перевірку: якщо друге число 0, писати «На нуль ділити не можна». Покажи всю програму.")
click(800, 681, after=0.3)
key("ctrl+v", after=1.0)
clipboard_done()
key("Return", label="Enter", after=0.5)
cut_start()
wait_stable(460, 90, 740, 540, scroll_at=(800, 400))
cut_end()

caption("Крок 2. Скопіюйте код кнопкою над ним")
pos = find_code_copy_button()
click(*pos, box=(pos[0] - 16, pos[1] - 16, 32, 32), after=1.2)

caption("Крок 3. У Geany: виділіть увесь код (Ctrl+A), вставте (Ctrl+V), збережіть")
activate("Geany")
click(150, 87, after=0.6)      # calc.py tab
key("ctrl+a", after=0.4)
key("ctrl+v", after=0.8)
key("ctrl+s", after=1.5)

caption("Крок 4. Обов’язково перевірте: запустіть і введіть 0 другим числом")
key("F5", after=2.0)
type_("10", after=0.2)
key("Return", show=False, after=0.6)
type_("0", after=0.2)
key("Return", label="Enter", after=2.5)

caption("Працює: програма не ламається, а пояснює. Enter — закрити")
wait(1.5)
key("Return", show=False, after=0.6)

stop(tail=0.6)
activate("Firefox")
