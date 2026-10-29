# L2-08 Створюємо таблицю
# Needs: L2-07 end state.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

# scroll down so «Досвід роботи» is in view (not recorded)
os.system("xdotool mousemove 600 500 click --repeat 4 --delay 100 5")
wait(1.0)

start("L2-08")

caption("Крок 1. Клацніть у кінці заголовка «Досвід роботи» і натисніть Enter")
click(404, 527, after=0.3)
key("End", show=False, after=0.2)
key("Return", label="Enter", after=1.0)

caption("Крок 2. «Таблиця» → «Вставити таблицю…»")
click(433, 13, box=(398, 2, 72, 22), after=0.8)
click(497, 41, box=(398, 30, 448, 22), after=1.4)

x, y, w, h = win_geom("Вставити таблицю")
caption("Крок 3. Вкажіть кількість стовпчиків і рядків, натисніть «Вставити»")
box(x + 17, y + 73, 588, 34, dur=2.0)
wait(2.0)
click(x + 545, y + 524, box=(x + 487, y + 508, 117, 33), after=1.2)

caption("Крок 4. Заповніть клітинки. Tab — перехід до наступної клітинки")
type_("Роки", after=0.3)
key("Tab", after=0.3)
type_("Місце роботи і посада", after=0.3)
key("Tab", after=0.3)
type_("2022 — тепер", after=0.3)
key("Tab", after=0.3)
type_("ТОВ «Приклад», адміністраторка офісу", after=0.6)

caption("Tab в останній клітинці додає новий рядок")
key("Tab", after=1.0)
type_("2019 — 2022", after=0.3)
key("Tab", after=0.3)
type_("Магазин «Зразок», продавчиня", after=0.8)

caption("Крок 5. Ctrl+A двічі виділяє всю таблицю — змініть шрифт, як у тексті")
key("ctrl+a", after=0.4)
key("ctrl+a", after=0.8)
click(390, 85, box=(291, 70, 230, 31), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("Liberation Sans", delay=110, after=0.3)
key("Return", show=False, after=1.2)
click(700, 720, after=1.0)

stop(tail=0.6)
