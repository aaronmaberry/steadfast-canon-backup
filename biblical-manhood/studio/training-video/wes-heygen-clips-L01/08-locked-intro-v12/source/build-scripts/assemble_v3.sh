#!/bin/bash
# Swappable audio: AUDIO=/path.wav AUDIO_WORDS=... AUDIO_LINES=... WES=new heygen mp4 (set in plan via env) ./assemble_calm.sh
set -e;cd "$(dirname "$0")"
A=${AUDIO:-/workspace/artifacts/training/audio-podcast-voice-2026-10-26/INTRO-classroom-2026-10-27/v5-old-intro-voice/INTRO-classroom-v5-old-intro-voice.wav}
T=$(python3 -c "import plan_calm as p;print(p.TOTAL)");N=6;pids=""
for i in $(seq 0 $((N-1)));do a=$(python3 -c "print($T*$i/$N)");b=$(python3 -c "print($T*($i+1)/$N)");python3 render_v3.py $a $b /tmp/v3_$i.mp4 & pids="$pids $!";done;wait $pids
printf "file /tmp/v3_%d.mp4\n" 0 1 2 3 4 5 >/tmp/v3.txt
ffmpeg -v error -y -f concat -safe 0 -i /tmp/v3.txt -i "$A" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t $T ../INTRO-FINAL-v3.mp4
ffmpeg -v error -y -i ../INTRO-FINAL-v3.mp4 -c:v libx264 -preset slow -b:v 7M -maxrate 8M -bufsize 14M -pix_fmt yuv420p -c:a aac -b:a 160k ../INTRO-FINAL-v3-preview-1080p.mp4 && ffmpeg -v error -y -i ../INTRO-FINAL-v3.mp4 -vf scale=640:-2 -c:v libx264 -crf 26 -c:a aac -b:a 64k -ac 1 ../INTRO-FINAL-v3-preview-64k.mp4
