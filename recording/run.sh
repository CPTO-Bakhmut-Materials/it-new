#!/bin/bash
# Record and annotate clips in order. Each scenario starts from the state the
# previous one left, so a lesson is recorded from its first clip.
# Usage: run.sh L1-02 L1-03 ...      (MP4 too: MP4=1 run.sh ...)
R="$(cd "$(dirname "$0")" && pwd)"
"$R/xstart.sh"
for clip in "$@"; do
  media=$(ls -d "$R"/../src/lesson-${clip:1:1}-*/media | head -1)
  python3 "$R/scenarios/$clip.py" || exit 1
  python3 "$R/annotate.py" "$clip" "$media" ${MP4:+--mp4} || exit 1
done
