#!/usr/bin/env python3
import json, os
from pathlib import Path
from faster_whisper import WhisperModel

os.environ.setdefault("OMP_NUM_THREADS", "6")
WAV = "/workspace/biblical-manhood/audio/02-chunks/hole-norm-16k.wav"
OUT = Path("/workspace/biblical-manhood/transcripts/02-chunks/hole-norm.jsonl")
OFFSET = 1800.0

print("Loading medium.en threads=6...", flush=True)
model = WhisperModel("medium.en", device="cpu", compute_type="int8", cpu_threads=6)
print("transcribing hole...", flush=True)
segments, info = model.transcribe(
    WAV,
    language="en",
    beam_size=5,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=350, speech_pad_ms=450),
    condition_on_previous_text=False,
    temperature=0.0,
)
n=0
chars=0
recs=[]
with OUT.open("w", encoding="utf-8") as jf:
    for s in segments:
        rec={
            "start": round(float(s.start)+OFFSET,3),
            "end": round(float(s.end)+OFFSET,3),
            "text": (s.text or "").strip(),
            "avg_logprob": round(float(s.avg_logprob),4) if s.avg_logprob is not None else None,
            "no_speech_prob": round(float(s.no_speech_prob),4) if s.no_speech_prob is not None else None,
        }
        recs.append(rec)
        jf.write(json.dumps(rec, ensure_ascii=False)+"\n")
        n+=1
        chars+=len(rec["text"])
        if n%10==0:
            print(f"  {n} t={rec['start']:.0f} lp={rec['avg_logprob']} {rec['text'][:90]}", flush=True)
print(f"DONE n={n} chars={chars} dur={info.duration:.0f}", flush=True)
# quality
good=[r for r in recs if (r['avg_logprob'] or -9)>-0.8 and len(r['text'])>20]
print(f"good segs {len(good)}/{n} good_chars {sum(len(r['text']) for r in good)}", flush=True)
for r in recs:
    if (r['avg_logprob'] or -9)>-0.9:
        print(f"{r['start']:7.1f} {r['avg_logprob']:.2f} {r['text'][:120]}", flush=True)
