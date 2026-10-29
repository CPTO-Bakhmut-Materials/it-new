# L4-13 ШІ для повсякденних задач
# Needs: Duck.ai open in Firefox.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

start("L4-13")

caption("ШІ допомагає не лише з кодом. Новий чат: попросіть написати лист")
click(94, 177, box=(14, 160, 120, 34), after=1.5)
click(800, 437, after=0.3)
type_("Напиши ввічливе повідомлення керівнику: завтра я прийду на роботу на годину пізніше, бо маю запис до лікаря.",
      delay=60, after=0.5)
key("Return", label="Enter", after=0.5)
cut_start()
wait_stable(460, 90, 740, 540, scroll_at=(800, 400))
cut_end()
wait(2.5)

caption("Не подобається? Уточніть: «Зроби коротше, до двох речень»")
click(800, 681, after=0.3)
type_("Зроби коротше, до двох речень.", delay=80, after=0.4)
key("Return", label="Enter", after=0.5)
cut_start()
wait_stable(460, 90, 740, 540, scroll_at=(800, 400))
cut_end()

caption("Готово. Перечитайте і виправте під себе перед надсиланням")
wait(4.0)

stop(tail=0.6)
