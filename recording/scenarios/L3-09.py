# L3-09 Встановлюємо блокувальник реклами uBlock Origin
# Needs: Firefox running, uBlock Origin not installed yet (golden profile).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L3-09")

caption("Крок 1. Відкрийте офіційний каталог додатків: addons.mozilla.org")
key("ctrl+l", show=False, after=0.3)
type_("addons.mozilla.org/uk/firefox/addon/ublock-origin/", delay=60, after=0.3)
key("Return", label="Enter", after=5.0)

caption("Перевірте: автор Raymond Hill, «Рекомендовані», мільйони користувачів")
box(150, 340, 360, 50, dur=2.5)
box(152, 480, 280, 160, dur=2.5)
wait(2.6)

caption("Крок 2. Натисніть «Додати до Firefox»")
click(951, 307, box=(682, 278, 540, 58), after=2.2)

caption("Крок 3. Firefox покаже дозволи розширення. Натисніть «Додати»")
click(1163, 486, box=(1112, 467, 104, 38), after=2.2)

caption("Крок 4. Галочка «Закріпити…» — значок uBlock буде на панелі. «OK»")
box(1206, 49, 30, 30, dur=2.6)
wait(1.8)
click(1221, 243, box=(1191, 225, 63, 38), after=1.4)

stop(tail=0.6)
