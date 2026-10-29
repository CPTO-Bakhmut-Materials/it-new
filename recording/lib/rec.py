"""Scenario helper: drives the virtual screen with xdotool, records it with
ffmpeg and logs every action with a wallclock timestamp for annotate.py.

    from rec import *
    start("L1-03")
    caption("Крок 1: Оберіть інструмент «Пензель»")
    click(23, 160, box=(10, 150, 30, 30))
    ...
    stop()
"""
import atexit
import json
import math
import os
import signal
import subprocess
import sys
import time

REC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REC_DIR, "raw")
os.environ["DISPLAY"] = ":99"

_events = []
_ff = None
_id = None
_pos = [640, 400]


def _x(*args):
    subprocess.run(["xdotool", *map(str, args)], check=True)


def _log(kind, **kw):
    _events.append({"t": time.time(), "kind": kind, **kw})


def _mouse(x, y):
    _x("mousemove", x, y)
    _pos[:] = [x, y]
    _log("mouse", x=x, y=y)


def start(clip_id, lead=0.8):
    """Start recording; `lead` seconds of still screen before the first action."""
    global _ff, _id
    _id = clip_id
    os.makedirs(RAW, exist_ok=True)
    out = subprocess.run(["xdotool", "getmouselocation", "--shell"],
                         capture_output=True, text=True).stdout
    loc = dict(l.split("=") for l in out.split())
    _pos[:] = [int(loc["X"]), int(loc["Y"])]
    _ff = subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "x11grab", "-framerate", "25",
         "-video_size", "1280x800", "-i", ":99", "-c:v", "libx264", "-preset",
         "ultrafast", "-crf", "12", "-copyts", os.path.join(RAW, clip_id + ".mkv")],
        stdin=subprocess.PIPE)
    time.sleep(0.5)
    _log("mouse", x=_pos[0], y=_pos[1])
    _log("start")
    time.sleep(lead)


def stop(tail=1.5):
    """Hold the final state for `tail` seconds, then stop and save the event log."""
    time.sleep(tail)
    _log("end")
    _ff.stdin.write(b"q")
    _ff.stdin.flush()
    _ff.wait(timeout=30)
    with open(os.path.join(RAW, _id + ".events.json"), "w") as f:
        json.dump(_events, f, ensure_ascii=False, indent=1)
    print(f"recorded {_id}: {_events[-1]['t'] - _events[0]['t']:.1f} s")


def wait(s):
    time.sleep(s)


def caption(text):
    """Show `text` in the caption bar from now until the next caption."""
    _log("caption", text=text)


def box(x, y, w, h, dur=1.6):
    """Highlight a rectangle (screen coordinates) for `dur` seconds."""
    _log("box", x=x, y=y, w=w, h=h, dur=dur)


def mask(x, y, w, h, dur):
    """Blur a screen rectangle for `dur` seconds (hides private paths etc.)."""
    _log("mask", x=x, y=y, w=w, h=h, dur=dur)


def move(x, y, dur=0.6):
    """Glide the mouse to (x, y) so viewers can follow it."""
    x0, y0 = _pos
    steps = max(2, int(dur * 50))
    for i in range(1, steps + 1):
        k = i / steps
        k = 0.5 - math.cos(k * math.pi) / 2  # ease in/out
        _mouse(round(x0 + (x - x0) * k), round(y0 + (y - y0) * k))
        time.sleep(dur / steps)


def click(x, y, button=1, box=None, dur=0.6, after=0.6, double=False, triple=False):
    """Move to (x, y) and click; `box`=(x, y, w, h) highlights the target first."""
    if box:
        globals()["box"](*box, dur=dur + 0.55)
    move(x, y, dur)
    time.sleep(0.25)
    _log("click", x=x, y=y, button=button)
    n = 3 if triple else 2 if double else 1
    _x("click", *(["--repeat", n, "--delay", 80] if n > 1 else []), button)
    time.sleep(after)


def drag(x1, y1, x2, y2, dur=1.2, button=1, after=0.5, path=None):
    """Press at (x1, y1), drag to (x2, y2) (or along `path` points), release."""
    move(x1, y1)
    time.sleep(0.2)
    _log("press", x=x1, y=y1)
    _x("mousedown", button)
    pts = path or [(x2, y2)]
    for px, py in pts:
        move(px, py, dur / len(pts))
    time.sleep(0.15)
    _x("mouseup", button)
    _log("release", x=_pos[0], y=_pos[1])
    time.sleep(after)


def key(combo, label=None, after=0.6, show=True):
    """Press a key combo (xdotool syntax, e.g. 'ctrl+z'); `label` is shown on
    screen as a key badge unless show=False."""
    if show:
        _log("key", label=label or combo)
    _x("key", "--clearmodifiers", combo)
    time.sleep(after)


def type_(text, delay=120, after=0.4):
    """Type text like a person; "\n" in `text` presses Enter."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line:
            _type_line(line, delay)
        if i < len(lines) - 1:
            _x("key", "Return")
            time.sleep(0.15)
    time.sleep(after)


def _type_line(text, delay):
    """Type text like a person. Unicode works, but Cyrillic needs delay >= ~100 ms
    on Xvfb (faster typing garbles letters)."""
    _x("type", "--delay", delay, text)


def window_shot(path):
    """Plain screenshot of the whole virtual screen (for planning coordinates)."""
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "x11grab",
                    "-video_size", "1280x800", "-i", ":99", "-frames:v", "1", path],
                   check=True)


def _display_pids(name):
    """PIDs of `name` processes running on the virtual screen only."""
    out = subprocess.run(["pgrep", "-x", name], capture_output=True, text=True).stdout
    pids = []
    for p in out.split():
        try:
            with open(f"/proc/{p}/environ", "rb") as f:
                if b"DISPLAY=:99\0" in f.read():
                    pids.append(int(p))
        except OSError:
            pass
    return pids


def pixel(x, y):
    """RGB of one pixel on the virtual screen."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "x11grab", "-video_size",
                          "1280x800", "-i", ":99", "-frames:v", "1", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    i = (y * 1280 + x) * 3
    return tuple(raw[i:i + 3])


def wait_pixel(x, y, rgb, timeout=180):
    """Wait until pixel (x, y) has colour `rgb` (e.g. a program's menu bar)."""
    t_end = time.time() + timeout
    while time.time() < t_end:
        if pixel(x, y) == tuple(rgb):
            return
        time.sleep(1)
    raise RuntimeError(f"pixel {x},{y} never became {rgb}")


def restart_app(name, *args, ready=((20, 8), (71, 71, 71)), ready_title=None, procname=None):
    """Kill `name` on the virtual screen (never the user's own copy), restore
    its golden profile (profiles/<name>.golden) if there is one, start it again
    through app.sh and wait until pixel ready[0] has colour ready[1]."""
    for p in _display_pids(procname or name):
        os.kill(p, signal.SIGKILL)
    time.sleep(1)
    prof = os.path.join(REC_DIR, "profiles", name)
    golden = prof + ".golden"
    if os.path.isdir(golden):
        subprocess.run(["rm", "-rf", prof], check=True)
        subprocess.run(["cp", "-a", golden, prof], check=True)
    subprocess.Popen([os.path.join(REC_DIR, "app.sh"), name, *args])
    time.sleep(3)
    if ready_title:
        win_geom(ready_title, timeout=120)
    else:
        wait_pixel(*ready[0], ready[1])
    time.sleep(3)
    _x("mousemove", 640, 400)


def win_geom(title_regex, timeout=10):
    """(x, y, w, h) of the first window whose title matches, client area."""
    t_end = time.time() + timeout
    while time.time() < t_end:
        r = subprocess.run(["xdotool", "search", "--onlyvisible", "--name", title_regex],
                           capture_output=True, text=True)
        ids = r.stdout.split()
        if ids:
            out = subprocess.run(["xdotool", "getwindowgeometry", "--shell", ids[-1]],
                                 capture_output=True, text=True).stdout
            g = dict(l.split("=") for l in out.split())
            return int(g["X"]), int(g["Y"]), int(g["WIDTH"]), int(g["HEIGHT"])
        time.sleep(0.3)
    raise RuntimeError(f"no window {title_regex!r}")


_clip = None


def clipboard(text):
    """Put `text` on the X clipboard (a small Tk process owns it until
    clipboard_done() or the end of the scenario)."""
    global _clip
    clipboard_done()
    code = ("import sys, tkinter as tk; r = tk.Tk(); r.withdraw(); r.clipboard_clear(); "
            "r.clipboard_append(sys.stdin.read()); r.update(); r.mainloop()")
    _clip = subprocess.Popen([sys.executable, "-c", code], stdin=subprocess.PIPE)
    _clip.stdin.write(text.encode())
    _clip.stdin.close()
    time.sleep(1.0)


def clipboard_done():
    global _clip
    if _clip:
        _clip.kill()
        _clip = None


@atexit.register
def _cleanup():
    """A scenario that crashes must not leave the recorder or clipboard running."""
    clipboard_done()
    if _ff and _ff.poll() is None:
        _ff.kill()


def cut_start(label="ШІ думає…"):
    """Start a part of the recording that the GIF skips (long waits);
    a short note with `label` is shown at the cut."""
    _log("cut_start", label=label)


def cut_end():
    _log("cut_end")


def _grab(x, y, w, h):
    return subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "x11grab", "-video_size",
                           f"{w}x{h}", "-i", f":99.0+{x},{y}", "-frames:v", "1", "-f", "rawvideo",
                           "-pix_fmt", "gray", "-"], capture_output=True).stdout


def wait_stable(x, y, w, h, scroll_at=None, every=2.0, min_wait=4.0, timeout=90):
    """Wait until the screen area stops changing (e.g. an AI answer finished).
    If `scroll_at`=(sx, sy) is given, scroll down there before every check."""
    t0 = time.time()
    time.sleep(min_wait)
    last, same = None, 0
    while time.time() - t0 < timeout:
        if scroll_at:
            _x("mousemove", *scroll_at)
            _x("click", "--repeat", 8, "--delay", 30, 5)
            time.sleep(0.5)
        cur = _grab(x, y, w, h)
        same = same + 1 if cur == last else 0
        if same >= 2:
            return
        last = cur
        time.sleep(every)


def find_code_copy_button():
    """Screen position of the copy button of the lowest code block in a Duck.ai
    answer (its grey header row has the icon at the right end), or None."""
    from PIL import Image
    import tempfile
    p = os.path.join(tempfile.gettempdir(), "rec-find.png")
    window_shot(p)
    im = Image.open(p).convert("RGB")
    best = None
    for y in range(95, 640):
        r, g, b = im.getpixel((900, y))
        if not (232 <= r <= 245 and abs(r - g) < 4 and abs(g - b) < 4):
            continue                       # not the grey header/frame of a code block
        dark = [x for x in range(1150, 1190) if sum(im.getpixel((x, y))) < 450]
        if dark:
            best = (sum(dark) // len(dark), y)   # keep the lowest hit
    return best


def activate(name_regex):
    """Bring the window whose title matches to the front."""
    r = subprocess.run(["xdotool", "search", "--onlyvisible", "--name", name_regex],
                       capture_output=True, text=True)
    ids = r.stdout.split()
    if ids:
        _x("windowactivate", "--sync", ids[-1])
        time.sleep(0.6)


def scroll_down(x=800, y=400, steps=8):
    """Scroll the page under (x, y) down."""
    _x("mousemove", x, y)
    _x("click", "--repeat", steps, "--delay", 30, 5)
    time.sleep(0.4)
