#!/usr/bin/env python3
"""Full-session 02 transcription with timestamps. Keep audio. Do not invent speech."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from faster_whisper import WhisperModel

ROOT = Path("/workspace/biblical-manhood")
MP3 = ROOT / "audio" / "02-consequences-of-an-absent-father.mp3"
OUT_DIR = ROOT / "transcripts"
RAW_JSONL = OUT_DIR / "02-asr-medium.en.jsonl"
RAW_VTT = OUT_DIR / "02-asr-medium.en.vtt"
RAW_TXT = OUT_DIR / "02-asr-medium.en.txt"

MODEL_NAME = "medium.en"


def fmt_ts(t: float) -> str:
    if t < 0:
        t = 0.0
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    if h:
        return f"{h:02d}:{m:02d}:{s:06.3f}"
    return f"{m:02d}:{s:06.3f}"


def main() -> int:
    if not MP3.exists():
        print(f"MISSING {MP3}", file=sys.stderr)
        return 2

    print(f"Loading {MODEL_NAME} cpu int8...", flush=True)
    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8", cpu_threads=8)
    print(f"Transcribing {MP3} ...", flush=True)
    segments, info = model.transcribe(
        str(MP3),
        language="en",
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=400, speech_pad_ms=400),
        condition_on_previous_text=False,
        temperature=0.0,
        word_timestamps=False,
        initial_prompt=(
            "Biblical Manhood session. Speaker Tim Hawks. Father wound. "
            "Richard Hawks. Ted Turner. Everclear. Ephesians 6. Matthew 3."
        ),
    )

    segs = []
    n = 0
    vtt_lines = ["WEBVTT", "", f"NOTE model={MODEL_NAME} duration={info.duration:.1f}s", ""]
    txt_lines = []

    with RAW_JSONL.open("w", encoding="utf-8") as jf:
        for s in segments:
            rec = {
                "start": round(float(s.start), 3),
                "end": round(float(s.end), 3),
                "text": (s.text or "").strip(),
                "avg_logprob": round(float(s.avg_logprob), 4) if s.avg_logprob is not None else None,
                "no_speech_prob": round(float(s.no_speech_prob), 4) if s.no_speech_prob is not None else None,
                "compression_ratio": round(float(s.compression_ratio), 4) if s.compression_ratio is not None else None,
            }
            segs.append(rec)
            jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
            start, end, text = rec["start"], rec["end"], rec["text"]
            vtt_lines.append(f"{fmt_ts(start)} --> {fmt_ts(end)}")
            vtt_lines.append(text)
            vtt_lines.append("")
            txt_lines.append(f"[{fmt_ts(start)} --> {fmt_ts(end)}] {text}")
            if n % 25 == 0:
                print(
                    f"  {n} segs t={end:.1f}s logp={rec['avg_logprob']} :: {text[:80]}",
                    flush=True,
                )

    RAW_VTT.write_text("\n".join(vtt_lines).rstrip() + "\n", encoding="utf-8")
    RAW_TXT.write_text("\n".join(txt_lines).rstrip() + "\n", encoding="utf-8")
    print(
        f"Done: {n} segments, duration={info.duration:.1f}s lang={info.language}",
        flush=True,
    )
    print(f"WROTE {RAW_JSONL} {RAW_VTT} {RAW_TXT}", flush=True)
    if segs:
        print(f"span {segs[0]['start']:.1f}s -> {segs[-1]['end']:.1f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
