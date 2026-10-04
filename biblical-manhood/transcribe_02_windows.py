#!/usr/bin/env python3
from __future__ import annotations
import json, os
from pathlib import Path
from faster_whisper import WhisperModel

os.environ.setdefault("OMP_NUM_THREADS", "4")

ROOT = Path("/workspace/biblical-manhood")
WDIR = ROOT / "audio" / "02-chunks"
OUT = ROOT / "transcripts" / "02-chunks"
OUT.mkdir(parents=True, exist_ok=True)

# 2-min windows 30:00 through end (the PhD hole)
STARTS = list(range(1800, 2870, 120))

def main() -> int:
    print("Loading medium.en cpu_threads=4...", flush=True)
    model = WhisperModel("medium.en", device="cpu", compute_type="int8", cpu_threads=4)
    print("loaded", flush=True)
    combined = []
    for s in STARTS:
        wav = WDIR / f"w{s:04d}.wav"
        dest = OUT / f"w{s:04d}.jsonl"
        print(f"\n=== {wav.name} ===", flush=True)
        segments, info = model.transcribe(
            str(wav),
            language="en",
            beam_size=5,
            vad_filter=False,  # short window; don't drop speech
            condition_on_previous_text=False,
            temperature=0.0,
        )
        recs = []
        with dest.open("w", encoding="utf-8") as jf:
            for seg in segments:
                rec = {
                    "window": s,
                    "start": round(float(seg.start) + s, 3),
                    "end": round(float(seg.end) + s, 3),
                    "local_start": round(float(seg.start), 3),
                    "local_end": round(float(seg.end), 3),
                    "text": (seg.text or "").strip(),
                    "avg_logprob": round(float(seg.avg_logprob), 4) if seg.avg_logprob is not None else None,
                    "no_speech_prob": round(float(seg.no_speech_prob), 4) if seg.no_speech_prob is not None else None,
                }
                recs.append(rec)
                combined.append(rec)
                jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
        chars = sum(len(r["text"]) for r in recs)
        mean_lp = (sum(r["avg_logprob"] or 0 for r in recs) / len(recs)) if recs else 0
        print(f"  n={len(recs)} chars={chars} mean_lp={mean_lp:.3f} last={recs[-1]['text'][:70] if recs else ''}", flush=True)
        if recs:
            print(f"  first={recs[0]['text'][:90]}", flush=True)
    comb_path = OUT / "hole-1800-2870.jsonl"
    comb_path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in combined) + "\n")
    print(f"WROTE {comb_path} n={len(combined)}", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
