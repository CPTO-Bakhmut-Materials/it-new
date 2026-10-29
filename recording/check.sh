#!/bin/bash
# Contact sheet of a finished clip: one frame every N seconds (default 2).
# Usage: check.sh L1-04 [seconds] [lesson media dir]
R="$(cd "$(dirname "$0")" && pwd)"
clip=$1; step=${2:-2}
media=${3:-$(ls -d "$R"/../src/lesson-${clip:1:1}-*/media | head -1)}
mkdir -p "$R/raw/chk"
ffmpeg -loglevel error -y -i "$media/$clip.gif" \
  -vf "fps=1/$step,scale=640:-1,tile=2x5" -frames:v 1 "$R/raw/chk/$clip.png"
echo "$R/raw/chk/$clip.png"
