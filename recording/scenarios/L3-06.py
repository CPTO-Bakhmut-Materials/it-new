# L3-06 Перевіряємо адресу сайту
# Needs: Firefox running (normal window).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

key("ctrl+l", show=False, after=0.2)
type_("https://diia.gov.ua/", delay=40, after=0.2)
key("Return", show=False, after=7.0)

start("L3-06")

caption("Справжня адреса сайту — частина перед першою «/»: diia.gov.ua")
box(322, 52, 96, 26, dur=3.0)
wait(3.0)

caption("Крок 1. Клацніть значок ліворуч від адреси")
click(241, 65, box=(227, 51, 28, 28), after=1.6)

caption("Крок 2. «Захищене з’єднання» — дані між вами і сайтом зашифровані")
click(640, 105, box=(522, 92, 236, 28), after=1.8)
box(240, 132, 400, 30, dur=2.0)
wait(2.0)

caption("Але замок не гарантує чесності: шахрайські сайти теж бувають із замком")
wait(3.0)
key("Escape", show=False, after=0.6)

stop(tail=0.4)
