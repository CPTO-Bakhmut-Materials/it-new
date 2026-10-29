# L3-11 Вимикаємо блокувальник для одного сайту
# Needs: L3-10 end state (sinoptik.ua open, uBlock on).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L3-11")

caption("Крок 1. Клацніть значок uBlock і велику кнопку живлення")
click(1215, 65, box=(1201, 47, 36, 34), after=1.2)
click(1066, 197, box=(1006, 137, 120, 120), after=1.2)

caption("Крок 2. Оновіть сторінку (F5) — тепер видно рекламу")
key("Escape", show=False, after=0.3)
key("F5", after=7.0)

caption("Увімкніть знову: значок → кнопка живлення → F5")
click(1215, 65, box=(1201, 47, 36, 34), after=1.2)
click(1066, 197, box=(1006, 137, 120, 120), after=1.0)
key("Escape", show=False, after=0.3)
key("F5", after=6.0)

stop(tail=0.4)
