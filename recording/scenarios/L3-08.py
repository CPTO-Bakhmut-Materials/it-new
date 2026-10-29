# L3-08 Менеджер паролів Firefox
# Needs: Firefox running; starts the local practice server if needed.
import sys, os, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from rec import *

if subprocess.run(["curl", "-s", "-o", "/dev/null", "http://127.0.0.1:8765/"]).returncode:
    subprocess.Popen(["setsid", sys.executable, os.path.join(REC_DIR, "serve.py")])
    wait(1.0)
key("ctrl+l", show=False, after=0.2)
type_("http://localhost:8765/login-demo.html", delay=40, after=0.2)
key("Return", show=False, after=2.5)

start("L3-08")

caption("Навчальна сторінка реєстрації. Введіть ім’я користувача")
click(640, 361, after=0.3)
type_("oksana_zrazkova", after=0.6)

caption("Крок 1. Клацніть у полі «Пароль» — Firefox запропонує надійний пароль")
click(640, 459, after=1.4)
click(628, 526, box=(390, 505, 450, 52), after=1.4)

caption("Крок 2. «Зареєструватися» — Firefox запам’ятає пароль")
click(640, 538, box=(388, 512, 504, 53), after=2.5)
click(724, 314, after=1.2)

caption("Крок 3. Усі збережені паролі: кнопка меню праворуч угорі → «Паролі»")
click(1256, 65, box=(1242, 51, 28, 28), after=1.0)
click(876, 328, box=(834, 312, 434, 32), after=2.5)

caption("Тут видно сайт, ім’я користувача і пароль. Запам’ятовувати його не треба")
box(0, 242, 383, 72, dur=2.5)
wait(2.5)
key("ctrl+w", show=False, after=0.4)

stop(tail=0.4)
