#!/bin/bash
# Step 1 (video): AUDIO_WORDS/AUDIO_LINES/WES env -> ${VOUT:-../work/INTRO-v4-video.mp4} (silent).  Step 2: ./mux_v4.sh AUDIO.wav
set -e;cd "$(dirname "$0")"
T=$(python3 -c "import render_v3 as r;print(r.TOTAL)" 2>/dev/null|tail -1);N=6;pids=""
for i in $(seq 0 $((N-1)));do a=$(python3 -c "print($T*$i/$N)");b=$(python3 -c "print($T*($i+1)/$N)");python3 render_v3.py $a $b /tmp/v11_$i.mp4 & pids="$pids $!";done;wait $pids
printf "file /tmp/v11_%d.mp4\n" 0 1 2 3 4 5 >/tmp/v11.txt
ffmpeg -v error -y -f concat -safe 0 -i /tmp/v11.txt -c copy ${VOUT:-../work/INTRO-v4-video.mp4}
