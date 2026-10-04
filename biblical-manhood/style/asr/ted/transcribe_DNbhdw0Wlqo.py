#!/usr/bin/env python3
"""ASR Ted Cunningham DNbhdw0Wlqo. faster-whisper medium.en float32 (int8 collapsed)."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

CHUNKS = Path("/workspace/biblical-manhood/style/audio/ted-chunks")
OUT = Path("/workspace/biblical-manhood/style/asr/ted")
OUT.mkdir(parents=True, exist_ok=True)
MODEL_NAME = "medium.en"
CHUNK_OFFSETS = {
    "DNbhdw0Wlqo-00.mp3": 0.0,
    "DNbhdw0Wlqo-01.mp3": 720.0,
    "DNbhdw0Wlqo-02.mp3": 1440.0,
}


def fmt_ts(t: float) -> str:
    if t < 0:
        t = 0.0
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    if h:
        return f"{h:02d}:{m:02d}:{s:06.3f}"
    return f"{m:02d}:{s:06.3f}"


def transcribe_one(model, mp3: Path) -> list[dict]:
    dest = OUT / f"{mp3.stem}.jsonl"
    if dest.exists() and dest.stat().st_size > 2000:
        recs = [json.loads(l) for l in dest.read_text(encoding="utf-8").splitlines() if l.strip()]
        words = sum(len(r.get("text", "").split()) for r in recs)
        if words >= 600:
            print(f"SKIP {mp3.name} words={words}", flush=True)
            return recs
        print(f"REDO {mp3.name} words={words} too low", flush=True)
    print(f"ASR {mp3.name} ({mp3.stat().st_size} bytes)", flush=True)
    t1 = time.time()
    segments, info = model.transcribe(
        str(mp3),
        language="en",
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=700, speech_pad_ms=400),
        condition_on_previous_text=False,
        temperature=0.0,
        word_timestamps=False,
    )
    recs = []
    n = 0
    with dest.open("w", encoding="utf-8") as jf:
        for s in segments:
            rec = {
                "start": round(float(s.start), 3),
                "end": round(float(s.end), 3),
                "text": (s.text or "").strip(),
                "avg_logprob": round(float(s.avg_logprob), 4) if s.avg_logprob is not None else None,
                "no_speech_prob": round(float(s.no_speech_prob), 4) if s.no_speech_prob is not None else None,
                "compression_ratio": round(float(s.compression_ratio), 4) if s.compression_ratio is not None else None,
            }
            recs.append(rec)
            jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            jf.flush()
            n += 1
            if n % 8 == 0:
                print(
                    f"  {mp3.stem} n={n} t={rec['end']:.1f}s logp={rec['avg_logprob']} :: {rec['text'][:110]}",
                    flush=True,
                )
    words = sum(len(r["text"].split()) for r in recs)
    print(
        f"OK {mp3.name} segs={n} words={words} dur={info.duration:.1f}s elapsed={time.time()-t1:.0f}s",
        flush=True,
    )
    return recs


def main() -> int:
    files = [CHUNKS / name for name in sorted(CHUNK_OFFSETS)]
    for f in files:
        if not f.exists():
            print(f"MISSING {f}", file=sys.stderr)
            return 2
    print("loading medium.en cpu float32", flush=True)
    t0 = time.time()
    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="float32", cpu_threads=4)
    print(f"model loaded in {time.time()-t0:.1f}s", flush=True)
    all_recs = []
    for mp3 in files:
        recs = transcribe_one(model, mp3)
        off = CHUNK_OFFSETS[mp3.name]
        for r in recs:
            all_recs.append({**r, "start": round(r["start"] + off, 3), "end": round(r["end"] + off, 3), "chunk": mp3.stem})
    jsonl = OUT / "DNbhdw0Wlqo.jsonl"
    txt = OUT / "DNbhdw0Wlqo.txt"
    vtt = OUT / "DNbhdw0Wlqo.vtt"
    with jsonl.open("w", encoding="utf-8") as jf:
        for rec in all_recs:
            jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
    txt_lines = []
    vtt_lines = ["WEBVTT", "", "NOTE model=faster-whisper medium.en cpu float32 source=yt-dlp audio-only DNbhdw0Wlqo.m4a", ""]
    for rec in all_recs:
        txt_lines.append(f"[{fmt_ts(rec['start'])} --> {fmt_ts(rec['end'])}] {rec['text']}")
        vtt_lines.append(f"{fmt_ts(rec['start'])} --> {fmt_ts(rec['end'])}")
        vtt_lines.append(rec["text"])
        vtt_lines.append("")
    txt.write_text("\n".join(txt_lines).rstrip() + "\n", encoding="utf-8")
    vtt.write_text("\n".join(vtt_lines).rstrip() + "\n", encoding="utf-8")
    words = sum(len(r["text"].split()) for r in all_recs)
    print(f"WROTE {jsonl} {txt} {vtt} segs={len(all_recs)} words={words}", flush=True)
    if all_recs:
        print(f"span {all_recs[0]['start']:.1f}s -> {all_recs[-1]['end']:.1f}s", flush=True)
    if words < 2500:
        print("WARNING low word count", flush=True)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
