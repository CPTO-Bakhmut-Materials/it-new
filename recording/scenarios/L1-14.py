# L1-14 Зберігаємо готову картинку (експорт у JPG)
# Needs: L1-13 end state (edited photo open).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-14")

caption("Крок 1. Меню «Файл» → «Експортувати…»")
click(26, 9, box=(6, 0, 42, 19), after=0.8)
click(80, 189, box=(8, 179, 476, 20), after=0.0)
mask(276, 165, 594, 24, dur=8.7)   # the folder path shows the user's name
wait(1.5)

caption("Крок 2. Оберіть теку, введіть назву файлу з розширенням .jpg")
click(243, 234, box=(194, 223, 106, 23), after=0.8)
click(620, 512, box=(276, 501, 686, 23), after=0.3)
type_("гори.jpg", delay=150, after=0.6)

caption("Крок 3. Натисніть «Зберегти»")
click(1017, 512, box=(968, 501, 99, 24), after=1.8)

caption("Крок 4. Якість JPG: більше — краще, але файл важчий. «Гаразд»")
box(618, 219, 264, 21, dur=2.0)
wait(2.0)
click(758, 559, box=(720, 548, 77, 23), after=2.0)

stop(tail=1.0)
