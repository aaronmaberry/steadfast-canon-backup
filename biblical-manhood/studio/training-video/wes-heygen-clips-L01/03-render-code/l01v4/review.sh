#!/bin/bash
cd /workspace/l01v4;V=L01-P7-ASSEMBLED-v4.mp4
ffmpeg -v error -y -i $V -vf "select='not(mod(n\,500))',scale=320:180,tile=8x8" -frames:v 1 -fps_mode vfr L01-P7-v4-CONTACT-every20s.jpg && echo contact
ffmpeg -v error -y -i $V -vf "scale=1280:720" -c:v libx264 -crf 26 -preset medium -c:a aac -b:a 128k L01-P7-v4-REVIEW-720p.mp4 && echo r720
ffmpeg -nostats -i $V -vf "blackdetect=d=0.2:pix_th=0.06,freezedetect=n=0.002:d=1.5" -an -f null - 2>&1 | grep -E "black_start|freeze_start|freeze_duration" > qc/black_freeze.txt; echo detect
ffmpeg -v error -y -ss 20 -t 30 -i $V -vf scale=1280:720 -c:v libx264 -crf 23 -c:a aac -b:a 128k L01-P7-v4-PREVIEW-720p-1-agenda-card-and-week-cut-A.mp4 && echo p1
ffmpeg -v error -y -ss 235 -t 35 -i $V -vf scale=1280:720 -c:v libx264 -crf 23 -c:a aac -b:a 128k L01-P7-v4-PREVIEW-720p-2-new-broll-light-leak-kinetic-cut-C.mp4 && echo p2
ffmpeg -v error -y -ss 1185 -t 40.14 -i $V -vf scale=1280:720 -c:v libx264 -crf 23 -c:a aac -b:a 128k L01-P7-v4-PREVIEW-720p-3-closing-gradient-and-logo.mp4 && echo p3
echo PREVDONE
echo REVIEWDONE
