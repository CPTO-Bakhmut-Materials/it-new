# L2-07 Вставляємо фото
# Needs: L2-06 end state (document scrolled to the top); photo.jpg (300 dpi) in the profile home.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L2-07")

caption("Крок 1. Клацніть біля місця для фото, далі «Вставка» → «Зображення…»")
click(330, 361, after=0.5)
click(232, 13, box=(198, 2, 72, 22), after=0.8)
click(276, 95, box=(198, 84, 362, 22), after=0.0)
mask(105, 182, 595, 40, dur=5.2)   # the folder path shows the user's name
wait(1.6)

caption("Крок 2. Оберіть файл фото й натисніть «Відкрити»")
click(334, 274, box=(276, 263, 686, 22), after=0.6)
click(905, 522, box=(847, 506, 117, 33), after=1.8)

caption("Крок 3. Перетягніть фото праворуч — текст обтікатиме його зліва")
drag(603, 474, 888, 474, dur=1.6, after=1.2)

caption("Крок 4. Потягніть за кутовий маркер — фото зменшиться без спотворення")
drag(773, 618, 833, 538, dur=1.4, after=1.2)

caption("Клацніть у тексті, щоб зняти виділення з фото")
click(600, 446, after=1.0)

stop(tail=0.6)
