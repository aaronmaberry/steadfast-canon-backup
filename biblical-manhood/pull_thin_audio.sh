#!/bin/bash
set -euo pipefail
ROOT=/workspace/biblical-manhood
AUDIO="$ROOT/audio"
LOG="$ROOT/logs/thin-audio-pull.log"
mkdir -p "$AUDIO"
cd "$ROOT"

pull() {
  local slug="$1" vid="$2"
  local out="$AUDIO/${slug}.mp3"
  if [[ -f "$out" && $(stat -c%s "$out") -gt 1000000 ]]; then
    echo "skip_exists $slug $(stat -c%s "$out")" | tee -a "$LOG"
    return 0
  fi
  echo "start $slug $(date -Iseconds)" | tee -a "$LOG"
  # format 18 worked previously (SABR-safe). no-part avoids rename races.
  if yt-dlp --no-playlist --no-part --retries 8 --fragment-retries 8 \
      -f "18/bestaudio/best" \
      -x --audio-format mp3 --audio-quality 5 \
      --postprocessor-args "ffmpeg:-ac 1 -ar 16000" \
      -o "$AUDIO/${slug}.%(ext)s" \
      "https://www.youtube.com/watch?v=${vid}" >> "$LOG" 2>&1; then
    echo "ok $slug $(stat -c%s "$out")" | tee -a "$LOG"
  else
    echo "FAIL $slug" | tee -a "$LOG"
    return 1
  fi
}

pull 13-a-biblical-definition-of-manhood-part-1 1xtJgaOpmZ8
pull 14-a-biblical-definition-of-manhood-part-2 a9P1EVOBbHE
pull 15-a-man-and-his-wife-part-1 3Ps3ezdRO6Y
pull 16-25-ways-to-be-a-servant-leader apJIZ8QYT_E
pull 17-a-man-and-his-wife-part-2 T4VCs8hIarg
pull 18-a-man-and-his-sexuality KS3dzdmW_tU
pull 24-final-session-bold-action 4b6q9go_0eE

echo "done $(date -Iseconds)" | tee -a "$LOG"
ls -la "$AUDIO"/1*.mp3 "$AUDIO"/2*.mp3 2>/dev/null | tee -a "$LOG"
