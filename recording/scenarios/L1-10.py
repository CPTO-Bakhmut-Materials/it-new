# L1-10 Відкриваємо фото
# Needs: Krita running (any document); photo.jpg in the profile home folder.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-10")

caption("Крок 1. Меню «Файл» → «Відкрити…»")
click(26, 9, box=(6, 0, 42, 19), after=0.8)
click(68, 52, box=(8, 42, 476, 20), after=0.0)
mask(276, 165, 594, 24, dur=5.7)   # the folder path shows the user's name
wait(1.5)

caption("Крок 2. Клацніть файл фото, потім «Відкрити»")
click(358, 225, box=(306, 215, 498, 20), after=1.0)
click(1017, 513, box=(968, 501, 99, 24), after=4.5)

stop(tail=1.0)
