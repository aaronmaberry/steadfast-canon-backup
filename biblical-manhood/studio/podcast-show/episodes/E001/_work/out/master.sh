#!/bin/bash
# master.sh GAIN_DB : compress -> gain -> 4x oversampled limiter -> 44.1k float master
PRE="highpass=f=70,acompressor=threshold=0.063:ratio=2.5:attack=10:release=200:knee=4"
ffmpeg -y -hide_banner -loglevel error -i dialogue.wav -af "$PRE,volume=${1}dB,aresample=176400,alimiter=limit=0.8:attack=1:release=60:level=disabled,aresample=44100" -c:a pcm_f32le master_f32.wav
ffmpeg -hide_banner -nostats -i master_f32.wav -af ebur128=peak=true -f null - 2>&1 | rg -A12 "Summary" | rg "I:|Peak:|LRA:"
