#!/bin/bash
# post.sh DIR NN  (expects DIR/secNN.raw.mp3 and DIR/secNN.timing.txt) -> DIR/secNN.voice.wav (dry, retimed)
set -e; D=$1; N=$2; L=/workspace/training-ep01/locked
cd $D
python3 $L/words.py sec$N.raw.mp3 sec$N.words.json
ffmpeg -y -loglevel error -i sec$N.raw.mp3 -af atempo=0.93 -ar 44100 -ac 1 sec$N.slow.wav
python3 $L/retime.py sec$N.slow.wav sec$N.timing.txt sec$N.rt.wav x sec$N.words.json 1.0752688
python3 $L/capgaps.py sec$N.rt.wav sec$N.voice.wav
