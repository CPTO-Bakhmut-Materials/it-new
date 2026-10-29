#!/bin/bash
# Start the virtual screen (1280x800) with openbox, if not running yet.
source "$(dirname "$0")/env.sh" 2>/dev/null
if ! xdotool getdisplaygeometry >/dev/null 2>&1; then
  Xvfb :99 -screen 0 1280x800x24 -nolisten tcp >/dev/null 2>&1 &
  sleep 1
  openbox --config-file "$REC_DIR/profiles/openbox/rc.xml" >/dev/null 2>&1 &
  sleep 0.5
fi
