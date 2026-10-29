# L1-02 Створюємо нове полотно
# Needs: nothing; restarts Krita on the start page.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

restart_app("krita")

start("L1-02")

caption("Крок 1. Відкрийте меню «Файл» → «Створити…»")
click(26, 9, box=(6, 0, 42, 19), after=0.8)
click(70, 30, box=(8, 20, 476, 20), after=1.5)

caption("Крок 2. Вкажіть ширину й висоту в пікселях")
click(705, 210, double=True, box=(652, 199, 128, 23), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("1920")
click(705, 239, double=True, box=(652, 228, 128, 23), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("1080", after=1.0)

caption("Крок 3. Натисніть «Створити»")
click(789, 601, box=(743, 589, 93, 25), after=2.0)

stop(tail=1.5)
