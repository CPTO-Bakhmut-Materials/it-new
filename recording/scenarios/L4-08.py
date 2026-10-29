# L4-08 Відкриваємо ШІ-помічника (Duck.ai)
# Needs: nothing; restarts Firefox (project profile, Duck.ai never used).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

restart_app("firefox", "about:blank", ready_title="Firefox|Mozilla", procname="firefox")
wait(1)

start("L4-08")

caption("Крок 1. Відкрийте duck.ai — реєстрація не потрібна")
key("ctrl+l", show=False, after=0.3)
type_("duck.ai", after=0.3)
key("Return", label="Enter", after=5.0)

caption("Крок 2. Напишіть запитання в полі і натисніть Enter")
click(800, 437, after=0.3)
type_("Що таке Python? Відповідай одним реченням.", delay=90, after=0.5)
key("Return", label="Enter", after=3.0)

caption("Крок 3. Перший раз — погодьтеся з умовами: «Продовжити»")
click(556, 529, box=(480, 509, 156, 42), after=0.5)
move(1000, 600, dur=0.5)
wait(7.0)

caption("Готово — ШІ відповів на запитання")
box(470, 395, 720, 85, dur=2.5)
wait(2.5)
caption("Зверніть увагу на підпис унизу: «ШІ може помилятися»")
box(678, 778, 300, 22, dur=3.0)
wait(3.0)

stop(tail=0.6)
