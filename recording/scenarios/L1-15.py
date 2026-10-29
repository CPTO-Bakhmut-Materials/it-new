# L1-15 Зберігаємо проєкт з шарами (.kra)
# Needs: L1-14 end state (drawing in the first tab, photo in the second).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-15")

caption("Повернімося до малюнка з шарами — вкладка зверху")
click(300, 71, box=(76, 60, 466, 22), after=1.2)
box(1020, 322, 258, 106, dur=1.8)
wait(1.8)

caption("Крок 1. Меню «Файл» → «Зберегти як…»")
click(26, 9, box=(6, 0, 42, 19), after=0.8)
click(78, 119, box=(8, 109, 476, 20), after=0.0)
mask(276, 165, 594, 24, dur=6.7)   # the folder path shows the user's name
wait(1.5)

caption("Крок 2. Введіть назву з розширенням .kra і натисніть «Зберегти»")
click(620, 512, double=True, box=(276, 501, 686, 23), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("листівка.kra", delay=150, after=0.8)
click(1017, 512, box=(968, 501, 99, 24), after=2.0)

caption("Готово! У файлі .kra збережено всі шари — можна редагувати далі")
box(76, 60, 466, 22, dur=2.5)
wait(2.5)

stop(tail=0.8)
