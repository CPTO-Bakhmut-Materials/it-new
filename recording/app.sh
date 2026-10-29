#!/bin/bash
# Start a program on the virtual screen with a project-local profile.
# Usage: app.sh krita [args...]
source "$(dirname "$0")/env.sh" 2>/dev/null
"$REC_DIR/xstart.sh"
app=$1; shift
P="$REC_DIR/profiles/$app"
mkdir -p "$P/home" "$P/config" "$P/data"
export HOME="$P/home" XDG_CONFIG_HOME="$P/config" XDG_DATA_HOME="$P/data" XDG_CACHE_HOME="$P/cache"
case $app in
  krita) exec setsid krita --nosplash "$@" >"$P/out.log" 2>&1 ;;
  firefox) export MOZ_ENABLE_WAYLAND=0
           exec setsid firefox --no-remote --profile "$P/ff" "$@" >"$P/out.log" 2>&1 ;;
  geany) rm -rf /tmp/kurs/programs; mkdir -p /tmp/kurs/programs; cd /tmp/kurs/programs   # short path, no user name in errors
         exec setsid geany -c "$P/geany" -i "$@" >"$P/out.log" 2>&1 ;;
  libreoffice) exec setsid libreoffice --nologo --norestore "$@" >"$P/out.log" 2>&1 ;;
  *) exec setsid "$app" "$@" >"$P/out.log" 2>&1 ;;
esac
