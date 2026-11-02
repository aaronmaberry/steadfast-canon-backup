#!/bin/bash
# one continuous audio file, never cut: pad end with silence to picture length (fade-out tail), no trims at layout changes
set -e;cd "$(dirname "$0")";A=$1;O=${2:-../INTRO-FINAL-v4}
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 ${VOUT:-../work/INTRO-v4-video.mp4})
ffmpeg -v error -y -i ${VOUT:-../work/INTRO-v4-video.mp4} -i "$A" -map 0:v -map 1:a -c:v copy -af "apad" -c:a aac -b:a 256k -ar 48000 -t $D -movflags +faststart $O.mp4
ffmpeg -v error -y -i $O.mp4 -c:v libx264 -preset slow -b:v 6M -maxrate 8M -bufsize 12M -pix_fmt yuv420p -c:a copy -movflags +faststart $O-preview-1080p.mp4
