# L2-03 Шрифт, розмір, жирний, курсив
# Needs: L2-02 end state (CV text pasted, Liberation Serif 12 pt).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-03")

caption("Крок 1. Виділіть весь текст (Ctrl+A) і оберіть шрифт у списку")
key("ctrl+a", after=0.6)
click(390, 85, box=(291, 70, 230, 31), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("Liberation Sans", delay=110, after=0.3)
key("Return", show=False, after=1.2)

caption("Крок 2. Поруч — розмір шрифту, наприклад 13")
click(565, 85, box=(531, 70, 105, 31), after=0.2)
key("ctrl+a", show=False, after=0.1)
type_("13", delay=200, after=0.3)
key("Return", show=False, after=1.2)
click(600, 690, after=0.6)

caption("Крок 3. Виділіть рядок і натисніть I — курсив")
click(300, 281, triple=True, after=0.6)  # triple click: the whole sentence (= the line)
click(694, 85, box=(680, 70, 29, 31), after=1.2)

caption("Крок 4. Виділіть слово і натисніть B — жирний")
click(262, 329, double=True, after=0.5)
click(660, 85, box=(646, 70, 29, 31), after=1.2)

caption("Те саме клавішами: Ctrl+B — жирний, Ctrl+I — курсив, Ctrl+U — підкреслений")
click(240, 377, double=True, after=0.5)
key("ctrl+b", after=1.2)
click(600, 690, after=1.2)

stop(tail=0.8)
