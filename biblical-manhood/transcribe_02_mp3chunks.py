#!/usr/bin/env python3
"""Low-priority medium.en on existing 02 mp3 chunks. Priority: c4,c5,c0,c3,c2,c1."""
from __future__ import annotations
import json, os, sys
from pathlib import Path
from faster_whisper import WhisperModel

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

ROOT = Path("/workspace/biblical-manhood")
CDIR = ROOT / "audio" / "02-chunks"
OUT = ROOT / "transcripts" / "02-chunks"
OUT.mkdir(parents=True, exist_ok=True)

# priority order: hole first
CHUNKS = [
    (1920, "c4-32m00-40m15.mp3", "c4"),
    (2400, "c5-40m00-47m50.mp3", "c5"),
    (0,    "c0-00m00-08m15.mp3", "c0"),
    (1440, "c3-24m00-32m15.mp3", "c3"),
    (960,  "c2-16m00-24m15.mp3", "c2"),
    (480,  "c1-08m00-16m15.mp3", "c1"),
]

def main() -> int:
    print("Loading medium.en int8 cpu_threads=1...", flush=True)
    model = WhisperModel("medium.en", device="cpu", compute_type="int8", cpu_threads=1, num_workers=1)
    print("model loaded", flush=True)
    for offset, fname, tag in CHUNKS:
        mp3 = CDIR / fname
        dest = OUT / f"{tag}.jsonl"
        if dest.exists() and dest.stat().st_size > 2000:
            print(f"SKIP {tag} exists {dest.stat().st_size}", flush=True)
            continue
        if not mp3.exists():
            print(f"MISSING {mp3}", flush=True)
            continue
        print(f"\n=== {tag} {mp3.name} offset={offset} ===", flush=True)
        segments, info = model.transcribe(
            str(mp3),
            language="en",
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=400, speech_pad_ms=400),
            condition_on_previous_text=False,
            temperature=0.0,
            initial_prompt="Biblical Manhood. Speaker Tim Hawks. Father wound. Ted Turner. Ephesians. Matthew.",
        )
        n = 0
        chars = 0
        with dest.open("w", encoding="utf-8") as jf:
            for s in segments:
                rec = {
                    "chunk": tag,
                    "offset": offset,
                    "start": round(float(s.start) + offset, 3),
                    "end": round(float(s.end) + offset, 3),
                    "local_start": round(float(s.start), 3),
                    "local_end": round(float(s.end), 3),
                    "text": (s.text or "").strip(),
                    "avg_logprob": round(float(s.avg_logprob), 4) if s.avg_logprob is not None else None,
                    "no_speech_prob": round(float(s.no_speech_prob), 4) if s.no_speech_prob is not None else None,
                }
                jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n += 1
                chars += len(rec["text"])
                if n % 15 == 0:
                    print(f"  {n} t={rec['start']:.0f}s lp={rec['avg_logprob']} {rec['text'][:80]}", flush=True)
        print(f"  DONE {tag} n={n} chars={chars} dur={info.duration:.0f} -> {dest}", flush=True)
    print("ALL CHUNKS DONE", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
