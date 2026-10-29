# L1-11 Кадруємо фото
# Needs: L1-10 end state (photo.jpg open, fitted to the view).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L1-11")

caption("Крок 1. Оберіть інструмент «Кадрування»")
click(12, 310, box=(1, 299, 23, 23), after=0.8)

caption("Крок 2. Протягніть рамку навколо потрібної частини фото")
drag(150, 260, 930, 715, dur=1.6, after=1.2)

caption("Крок 3. Натисніть Enter — усе поза рамкою зникне")
key("Return", label="Enter", after=2.0)

stop(tail=1.0)
