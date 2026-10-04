#!/usr/bin/env python3
import json, os
from pathlib import Path
from faster_whisper import WhisperModel

os.environ.setdefault("OMP_NUM_THREADS", "6")
WAV = "/workspace/biblical-manhood/audio/02-chunks/hole-norm-16k.wav"
OUT = Path("/workspace/biblical-manhood/transcripts/02-chunks/hole-norm-small.jsonl")
OFFSET = 1800.0

print("Loading small.en threads=6...", flush=True)
model = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=6)
print("transcribing...", flush=True)
segments, info = model.transcribe(
    WAV,
    language="en",
    beam_size=5,
    vad_filter=False,
    condition_on_previous_text=True,
    temperature=0.0,
)
n=0; chars=0
with OUT.open("w", encoding="utf-8") as jf:
    for s in segments:
        rec={
            "start": round(float(s.start)+OFFSET,3),
            "end": round(float(s.end)+OFFSET,3),
            "text": (s.text or "").strip(),
            "avg_logprob": round(float(s.avg_logprob),4) if s.avg_logprob is not None else None,
            "no_speech_prob": round(float(s.no_speech_prob),4) if s.no_speech_prob is not None else None,
        }
        jf.write(json.dumps(rec, ensure_ascii=False)+"\n")
        n+=1; chars+=len(rec["text"])
        if n%12==0:
            print(f"  {n} t={rec['start']:.0f} lp={rec['avg_logprob']} {rec['text'][:100]}", flush=True)
print(f"DONE n={n} chars={chars} dur={info.duration:.0f}", flush=True)
