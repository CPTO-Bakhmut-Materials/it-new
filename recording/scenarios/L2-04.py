# L2-04 Стилі заголовків
# Needs: L2-03 end state.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-04")

caption("Крок 1. Клацніть у рядку з іменем і оберіть стиль «Заголовок 1»")
click(330, 257, after=0.4)
click(90, 85, box=(5, 70, 210, 31), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("Заголовок 1", delay=120, after=0.3)
key("Return", show=False, after=1.4)

caption("Крок 2. Назви розділів — «Заголовок 2», швидко: Ctrl+2")
# bottom-up, so the lines above do not move
for y in (655, 631, 511, 439):
    click(250, y, after=0.3)
    key("ctrl+2", after=0.6)
click(250, 343, after=0.3)
key("ctrl+2", after=1.2)

caption("Крок 3. «Навігатор» (Alt+4) показує план документа з заголовків")
click(1251, 295, box=(1236, 280, 30, 30), after=0.8)
box(950, 274, 272, 172, dur=2.4)
wait(1.2)
caption("Подвійне клацання в «Навігаторі» — перехід до розділу")
click(1050, 436, double=True, after=1.4)
click(1070, 311, double=True, after=1.2)
click(1251, 295, after=1.0)   # close the Navigator again

stop(tail=0.6)
