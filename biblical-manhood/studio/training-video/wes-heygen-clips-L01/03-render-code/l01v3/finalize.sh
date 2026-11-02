#!/bin/bash
set -e
cd /workspace/l01v3
ls chunks/c0?.mp4 | sed "s#^#file '/workspace/l01v3/#; s#\$#'#" > chunks/vlist.txt
ffmpeg -v error -y -f concat -safe 0 -i chunks/vlist.txt -i audio/L01-v3-weekfree-minus26-LUFS.mp3 -map 0:v -map 1:a -c copy -movflags +faststart L01-P7-ASSEMBLED-v3.mp4
ffprobe -v error -show_entries stream=codec_name,nb_frames,duration -of compact L01-P7-ASSEMBLED-v3.mp4
echo FINALIZED
