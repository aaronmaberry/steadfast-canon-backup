#!/usr/bin/env bash
# Class-tape ingest. Internal. No spend. No publish. Do not rewrite the book.
# Usage:
#   ./ingest-class-tape.sh
#   ./ingest-class-tape.sh /path/to/IMG_6475.MOV
set -euo pipefail

ROOT="/workspace/biblical-manhood/training"
SRC_DIR="${ROOT}/source"
STEM="${STEM:-IMG_6475}"
IN="${1:-${SRC_DIR}/${STEM}.MOV}"

if [[ ! -f "${IN}" ]]; then
  echo "WAIT: source not on disk: ${IN}"
  echo "Drop the iPhone MOV at ${SRC_DIR}/${STEM}.MOV then re-run."
  echo "Do not invent a transcript."
  exit 2
fi

OUT_DIR="$(cd "$(dirname "${IN}")" && pwd)"
BASE="${OUT_DIR}/${STEM}"
MP4="${BASE}-1080p.mp4"
WAV="${BASE}.wav"
MP3="${BASE}.mp3"
MD="${BASE}.md"

mkdir -p "${OUT_DIR}"

echo "== probe =="
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_type,codec_name,width,height -of default=noprint_wrappers=1 "${IN}"
DUR="$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "${IN}")"
echo "duration_sec=${DUR}"

echo "== 1080p mp4 =="
ffmpeg -y -i "${IN}" -vf "scale=-2:1080" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 160k "${MP4}"

echo "== wav 16k mono =="
ffmpeg -y -i "${IN}" -vn -ac 1 -ar 16000 "${WAV}"

echo "== mp3 =="
ffmpeg -y -i "${IN}" -vn -codec:a libmp3lame -q:a 4 "${MP3}"

echo "== transcript =="
TRANSCRIPT_OK=0
PY="${ROOT}/ingest_transcribe.py"
if [[ -f "${PY}" ]]; then
  if python3 "${PY}" "${WAV}" "${MD}" "${IN}" "${DUR}"; then
    TRANSCRIPT_OK=1
  fi
fi

if [[ "${TRANSCRIPT_OK}" -ne 1 ]]; then
  {
    echo "# ${STEM}"
    echo
    echo "Internal class tape. No publish. Original: \`${IN}\`."
    echo
    echo "- Duration (seconds): ${DUR}"
    echo "- 1080p: \`${MP4}\`"
    echo "- wav: \`${WAV}\`"
    echo "- mp3: \`${MP3}\`"
    echo
    echo "Transcript not written. Local ASR did not complete. Do not invent speech."
  } > "${MD}"
fi

echo "== done =="
ls -lh "${IN}" "${MP4}" "${WAV}" "${MP3}" "${MD}"
echo "duration_sec=${DUR}"
echo "paths:"
echo "  original ${IN}"
echo "  mp4 ${MP4}"
echo "  wav ${WAV}"
echo "  mp3 ${MP3}"
echo "  md ${MD}"
