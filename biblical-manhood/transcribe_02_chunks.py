#!/usr/bin/env python3
"""Transcribe 02 audio chunks with medium.en. Offsets applied. Keep audio."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from faster_whisper import WhisperModel

ROOT = Path("/workspace/biblical-manhood")
SRC = ROOT / "audio" / "02-consequences-of-an-absent-father.mp3"
WAVDIR = ROOT / "audio" / "02-chunks"
OUTDIR = ROOT / "transcripts" / "02-chunks"
COMBINED = ROOT / "transcripts" / "02-asr-chunks.jsonl"

# start_sec, duration, name
CHUNKS = [
    (0, 510, "c0-00m00-08m30"),
    (480, 510, "c1-08m00-16m30"),
    (960, 510, "c2-16m00-24m30"),
    (1440, 510, "c3-24m00-32m30"),
    (1920, 510, "c4-32m00-40m30"),
    (2400, 480, "c5-40m00-48m00"),
]


def ensure_wav(start: int, dur: int, name: str) -> Path:
    dest = WAVDIR / f"{name}.wav"
    if dest.exists() and dest.stat().st_size > 100_000:
        print(f"wav exists {dest}", flush=True)
        return dest
    cmd = [
        "ffmpeg", "-y", "-i", str(SRC),
        "-ss", str(start), "-t", str(dur),
        "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le",
        str(dest),
    ]
    print("extract", name, flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1000:], file=sys.stderr)
        raise SystemExit(1)
    return dest


def main() -> int:
    WAVDIR.mkdir(parents=True, exist_ok=True)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print("Loading medium.en cpu int8...", flush=True)
    model = WhisperModel("medium.en", device="cpu", compute_type="int8", cpu_threads=8)
    all_recs = []
    for start, dur, name in CHUNKS:
        wav = ensure_wav(start, dur, name)
        print(f"\n=== {name} offset={start}s ===", flush=True)
        segments, info = model.transcribe(
            str(wav),
            language="en",
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=700, speech_pad_ms=500),
            condition_on_previous_text=True,
            temperature=0.0,
            word_timestamps=False,
        )
        recs = []
        n = 0
        jsonl = OUTDIR / f"{name}.jsonl"
        with jsonl.open("w", encoding="utf-8") as jf:
            for s in segments:
                rec = {
                    "chunk": name,
                    "offset": start,
                    "start": round(float(s.start) + start, 3),
                    "end": round(float(s.end) + start, 3),
                    "local_start": round(float(s.start), 3),
                    "local_end": round(float(s.end), 3),
                    "text": (s.text or "").strip(),
                    "avg_logprob": round(float(s.avg_logprob), 4) if s.avg_logprob is not None else None,
                    "no_speech_prob": round(float(s.no_speech_prob), 4) if s.no_speech_prob is not None else None,
                }
                recs.append(rec)
                jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n += 1
                if n % 20 == 0:
                    print(f"  {n} t={rec['start']:.1f} {rec['text'][:90]}", flush=True)
        print(f"  done {n} segs last={recs[-1]['end'] if recs else 'none'} dur={info.duration:.1f}", flush=True)
        # quality summary
        bad = [r for r in recs if (r["avg_logprob"] or 0) < -1.0 or len(r["text"]) <= 2]
        print(f"  low-quality segs: {len(bad)}/{n}", flush=True)
        all_recs.extend(recs)
    # drop overlap: keep earlier chunk until midpoint of overlap, then later
    # simpler: when two recs overlap in time, prefer the one with better logprob
    all_recs.sort(key=lambda r: (r["start"], r["end"]))
    COMBINED.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in all_recs) + "\n",
        encoding="utf-8",
    )
    print(f"WROTE {COMBINED} n={len(all_recs)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
