#!/usr/bin/env python3
"""Pack ASR transcript text into a single-cue VTT using known duration."""
import sys, pathlib, re

def hms(seconds: int) -> str:
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}.000"

def main():
    md_path = pathlib.Path(sys.argv[1])
    vtt_path = pathlib.Path(sys.argv[2])
    duration = int(sys.argv[3])
    text = md_path.read_text()
    # drop markdown header until first blank after speaker block
    parts = text.split("\n\n", 3)
    # keep body after metadata
    body = text
    if body.startswith("#"):
        # skip title + meta lines
        lines = body.splitlines()
        i = 0
        while i < len(lines) and (not lines[i].strip() or lines[i].startswith("#") or lines[i].startswith("Speaker:") or lines[i].startswith("Date:") or lines[i].startswith("Source:") or lines[i].startswith("YouTube:") or lines[i].startswith("Caption:")):
            i += 1
        if i < len(lines) and lines[i].endswith(":") and len(lines[i].split()) <= 3:
            i += 1  # speaker label
        body = "\n".join(lines[i:]).strip()
    # collapse extra blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    note = (
        "NOTE YouTube automatic captions (ASR, language en-orig). "
        "No manual English track exists. Direct timedtext/VTT download returned HTTP 429 from this host. "
        "Cue span is the player duration from yt-dlp metadata, not authentic per-line caption times. "
        "Speech text is the ASR transcript, not invented."
    )
    vtt = f"WEBVTT\n\n{note}\n\n00:00:00.000 --> {hms(duration)}\n{body}\n"
    vtt_path.write_text(vtt)
    print("wrote", vtt_path, "chars", len(vtt))

if __name__ == "__main__":
    main()
