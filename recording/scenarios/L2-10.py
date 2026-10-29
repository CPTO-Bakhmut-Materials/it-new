# L2-10 Зберігаємо документ (ODT і DOCX)
# Needs: L2-09 end state; the document has never been saved.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-10")

caption("Крок 1. «Файл» → «Зберегти як…»")
click(26, 13, box=(2, 2, 50, 22), after=0.8)
click(79, 367, box=(2, 356, 360, 22), after=0.0)
mask(205, 168, 630, 40, dur=6.6)   # the folder path shows the user's name
wait(1.4)

x, y, w, h = win_geom("Зберегти як")
caption("Крок 2. Введіть назву. Тип ODT — основний формат LibreOffice")
click(x + 403, y + 361, triple=True, box=(x + 107, y + 345, 593, 33), after=0.2)
type_("Резюме", after=0.5)
box(x + 107, y + 385, 627, 33, dur=1.6)
wait(1.6)
click(x + 804, y + 361, box=(x + 746, y + 345, 117, 33), after=1.6)

caption("Крок 3. Для тих, у кого Word: знову «Зберегти як…», тип — .docx")
key("ctrl+shift+s", after=0.0)
mask(205, 168, 630, 40, dur=7.0)
wait(1.6)
x, y, w, h = win_geom("Зберегти як")
click(x + 420, y + 401, box=(x + 107, y + 385, 627, 33), after=1.0)
click(x + 230, y + 21, box=(x + 108, y + 10, 622, 22), after=0.8)
click(x + 804, y + 361, box=(x + 746, y + 345, 117, 33), after=1.6)

caption("Крок 4. Підтвердіть: «Використати формат Документ Word»")
click(841, 504, box=(651, 489, 381, 32), after=1.8)

stop(tail=0.8)
