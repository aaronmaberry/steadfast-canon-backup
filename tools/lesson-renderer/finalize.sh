#!/bin/bash
set -e
WORK=${LESSON_WORK:-/workspace/l08}
VER=${1:-v1}
LC=$WORK/lesson.json
B=$(python3 -c "import json;print(json.load(open('$LC'))['build'].rstrip('/'))")
NN=$(python3 -c "import json;print(json.load(open('$LC'))['nn'])")
TITLE=$(python3 -c "import json;print(json.load(open('$LC'))['title'].replace(' ','-'))")
AUDIO=$(python3 -c "import json;print(json.load(open('$WORK/p7/inputs.json'))['audio'])")
cd "$WORK"
ls p7/chunks/c*.mp4 | sort | sed "s#^#file '$WORK/#; s#\$#'#" > p7/chunks/vlist.txt
OUT=$B/L${NN}-P7-ASSEMBLED-${VER}.mp4
ffmpeg -v error -y -f concat -safe 0 -i p7/chunks/vlist.txt -i "$AUDIO" \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 1 \
  -movflags +faststart "$OUT"
# captions
/workspace/cvenv/bin/python build/captions.py L${NN}-P7-ASSEMBLED-${VER} "$B"
# burn-in free 720p review
REV=$B/L${NN}-P7-REVIEW-720p-${VER}.mp4
ffmpeg -v error -y -i "$OUT" -vf scale=1280:720 -c:v libx264 -preset fast -crf 20 -c:a aac -b:a 128k -movflags +faststart "$REV"
ffprobe -v error -show_entries stream=codec_name,width,height,duration,nb_frames -of compact "$OUT"
ls -la "$OUT" "$REV"
echo FINALIZED
