# L3-10 Сторінка з блокувальником
# Needs: uBlock Origin installed and pinned (L3-09).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L3-10")

caption("Відкриємо сайт прогнозу погоди — реклами на ньому немає")
key("ctrl+l", show=False, after=0.3)
type_("sinoptik.ua", delay=80, after=0.3)
key("Return", label="Enter", after=7.0)
r, g, b = pixel(40, 560)
if r > 200 and g > 170 and b < 140:   # the site's own yellow "allow location?" banner
    click(302, 727, after=1.0)        # «Не зараз»

caption("Число на значку uBlock — скільки елементів заблоковано")
box(1201, 47, 36, 34, dur=2.5)
wait(2.5)

caption("Клацніть значок — побачите подробиці")
click(1215, 65, after=1.8)
box(905, 285, 322, 160, dur=3.0)
wait(3.0)
key("Escape", show=False, after=0.6)

stop(tail=0.4)
