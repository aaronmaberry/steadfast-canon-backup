#!/bin/bash
# mix.sh IN_DRY_WAV OUT_MP3
O=/workspace/training-ep01/audio-v3/onetake
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1")
ffmpeg -y -loglevel error -i "$1" -i $O/hall-ir.wav -stream_loop -1 -i $O/roomtone.wav -filter_complex "[0:a]asplit[d][w];[w][1:a]afir,highpass=f=200,lowpass=f=7000,volume=15dB[wet];[d][wet]amix=inputs=2:normalize=0[v];[v][2:a]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11" -t $D -ar 44100 -b:a 192k "$2"
