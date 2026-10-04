#!/usr/bin/env python3
"""ASR short official-podcast clips of Red Rocks Austin sermons. Internal style notes only."""
from __future__ import annotations
import re, time
from pathlib import Path
from faster_whisper import WhisperModel

AUD = Path("/workspace/biblical-manhood/style/audio")
OUT = Path("/workspace/biblical-manhood/style/asr")
OUT.mkdir(parents=True, exist_ok=True)
LOG = Path("/workspace/biblical-manhood/style/asr/_log.txt")

def collapse(s: str) -> str:
    s = s.replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s).strip()
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
    files = sorted(AUD.glob("*.wav"))
    print(f"loading small.en, {len(files)} files", flush=True)
    t0=time.time()
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    print(f"model loaded in {time.time()-t0:.1f}s", flush=True)
    log=[]
    for i, wav in enumerate(files, 1):
        dest = OUT / f"{wav.stem}.md"
        if dest.exists() and dest.stat().st_size > 400:
            msg=f"SKIP {wav.name}"
            print(msg, flush=True); log.append(msg); continue
        print(f"[{i}/{len(files)}] {wav.name} ({wav.stat().st_size} bytes)", flush=True)
        t1=time.time()
        segments, info = model.transcribe(
            str(wav),
            language="en",
            beam_size=1,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=700),
            word_timestamps=False,
        )
        segs=[]
        for s in segments:
            segs.append({"start": s.start, "end": s.end, "text": s.text})
        paras = segs_to_paras(segs)
        body = "\n\n".join(paras)
        dur = segs[-1]["end"] if segs else 0
        md = (
            f"# ASR {wav.name}\n\n"
            f"- source: official Red Rocks Austin podcast audio clip (Anchor/Spotify RSS), not YouTube captions\n"
            f"- file: {wav.name}\n"
            f"- model: faster-whisper small.en int8 cpu\n"
            f"- speech_end_s: {dur:.1f}\n"
            f"- elapsed_s: {time.time()-t1:.1f}\n"
            f"- language: {getattr(info,'language', 'en')}\n\n"
            f"---\n\n{body}\n"
        )
        dest.write_text(md)
        msg=f"OK {wav.name} chars={len(body)} speech={dur:.0f}s in {time.time()-t1:.0f}s -> {dest.name}"
        print(msg, flush=True)
        log.append(msg)
    LOG.write_text("\n".join(log)+"\n")
    print("ALL_DONE", flush=True)

if __name__ == "__main__":
    main()
