# Source this: sets up the local locale and the virtual display variables.
REC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export DISPLAY=:99
export LOCPATH="$REC_DIR/locale"
export LANG=uk_UA.UTF-8 LANGUAGE=uk LC_ALL=uk_UA.UTF-8
export XDG_SESSION_TYPE=x11 QT_QPA_PLATFORM=xcb GDK_BACKEND=x11
unset WAYLAND_DISPLAY
