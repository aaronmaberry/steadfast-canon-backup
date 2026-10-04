#!/usr/bin/env python3
"""Retry weak ASR clips with no VAD and no previous-text conditioning."""
from __future__ import annotations
import re, time
from pathlib import Path
from faster_whisper import WhisperModel

AUD = Path("/workspace/biblical-manhood/style/audio")
OUT = Path("/workspace/biblical-manhood/style/asr")
RETRY = [
    "gods-will-ethan-0-12m.wav",
    "kill-control-freak-doug-0-12m.wav",
    "kill-control-freak-doug-1500s.wav",
    "healthy-holy-ryan-doug-0-12m.wav",
    "three-ways-hear-god-doug-0-12m.wav",
    "better-not-easier-ethan-0-12m.wav",
    "start-with-one-ryan-1680s.wav",
    "lost-loving-feeling-doug-0-12m.wav",
    "lost-loving-feeling-doug-1500s.wav",
    "tough-to-love-ryan-0-12m.wav",
    "wield-the-weapon-ethan-0-12m.wav",
    "start-with-one-ryan-0-12m.wav",
]

def collapse(s: str) -> str:
    s = re.sub(r"\s+", " ", s.replace("\u00a0", " ")).strip()
    s = s.replace(" .", ".").replace(" ,", ",").replace(" ?", "?").replace(" !", "!")
    s = re.sub(r"\.{2,}", "...", s)
    s = re.sub(r"\b(\w+)( \1){2,}\b", r"\1", s, flags=re.I)
    return s

def segs_to_paras(segs, pause=1.5, max_chars=900):
    paras, cur, cur_len, prev_end = [], [], 0, None
    for s in segs:
        t = collapse(s["text"])
        if not t:
            continue
        gap = 0.0 if prev_end is None else (s["start"] - prev_end)
        if cur and (gap >= pause or cur_len >= max_chars):
            paras.append(" ".join(cur)); cur, cur_len = [], 0
        cur.append(t); cur_len += len(t)+1; prev_end = s["end"]
    if cur:
        paras.append(" ".join(cur))
    merged=[]
    for p in paras:
        if merged and len(p) < 70:
            merged[-1] = merged[-1] + " " + p
        else:
            merged.append(p)
    return merged

def main() -> None:
    print("loading small.en retry", flush=True)
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    for name in RETRY:
        wav = AUD / name
        dest = OUT / f"{wav.stem}.retry.md"
        print(f"RETRY {name}", flush=True)
        t1=time.time()
        segments, info = model.transcribe(
            str(wav),
            language="en",
            beam_size=5,
            best_of=5,
            temperature=0.0,
            vad_filter=False,
            condition_on_previous_text=False,
            word_timestamps=False,
        )
        segs=[{"start": s.start, "end": s.end, "text": s.text} for s in segments]
        paras = segs_to_paras(segs)
        body = "\n\n".join(paras)
        dur = segs[-1]["end"] if segs else 0
        md = (
            f"# ASR retry {wav.name}\n\n"
            f"- source: official Red Rocks Austin podcast audio clip (Anchor/Spotify RSS), not YouTube captions\n"
            f"- file: {wav.name}\n"
            f"- model: faster-whisper small.en int8 cpu\n"
            f"- settings: vad_filter=False condition_on_previous_text=False temperature=0 beam=5\n"
            f"- speech_end_s: {dur:.1f}\n"
            f"- elapsed_s: {time.time()-t1:.1f}\n\n"
            f"---\n\n{body}\n"
        )
        dest.write_text(md)
        # replace original if retry is substantially better
        orig = OUT / f"{wav.stem}.md"
        orig_len = len(orig.read_text()) if orig.exists() else 0
        print(f"  chars={len(body)} orig={orig_len} speech={dur:.0f}s in {time.time()-t1:.0f}s", flush=True)
        if len(body) > orig_len * 1.15 or (orig_len < 1500 and len(body) > orig_len):
            orig.write_text(md)
            print("  REPLACED original", flush=True)
    print("RETRY_DONE", flush=True)

if __name__ == "__main__":
    main()
