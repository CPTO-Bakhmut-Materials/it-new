# L3-02 Шукаємо точніше
# Needs: nothing; restarts Firefox (project profile) on an empty tab.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

restart_app("firefox", "about:blank", ready_title="Firefox|Mozilla", procname="firefox")
wait(2)

start("L3-02")

caption("Крок 1. Клацніть в адресному рядку, введіть запит і натисніть Enter")
click(600, 65, after=0.3)
type_("як скласти резюме", after=0.4)
key("Return", label="Enter", after=4.0)

caption("Крок 2. Лапки — шукати саме цю фразу, слово в слово")
key("ctrl+l", show=False, after=0.3)
type_('"як скласти резюме"', after=0.4)
key("Return", label="Enter", after=4.0)

caption("Крок 3. site:gov.ua — шукати лише на державних сайтах")
key("ctrl+l", show=False, after=0.3)
type_('"як скласти резюме" site:gov.ua', after=0.4)
key("Return", label="Enter", after=3.0)
box(110, 50, 560, 30, dur=2.5)
wait(2.5)

stop(tail=0.6)
