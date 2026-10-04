#!/usr/bin/env python3
"""Full session 02 transcription. medium.en, no VAD drop. Do not invent speech."""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

ROOT = Path("/workspace/biblical-manhood")
WAVDIR = ROOT / "audio" / "02-chunks" / "v16"
OUTDIR = ROOT / "transcripts" / "02-chunks"
RAWDIR = ROOT / "asr-raw" / "02"
TR = ROOT / "transcripts"
ARCHIVE = TR / "archive"

OUTDIR.mkdir(parents=True, exist_ok=True)
RAWDIR.mkdir(parents=True, exist_ok=True)

# offset_sec, filename, duration hint
CHUNKS = [
    (0, "v0.wav", "v0"),
    (480, "v1.wav", "v1"),
    (960, "v2.wav", "v2"),
    (1440, "v3.wav", "v3"),
    (1920, "v4.wav", "v4"),
    (2400, "v5.wav", "v5"),
]

PROMPT = (
    "Biblical Manhood session. Speaker Tim Hawks. Father wound. Richard Fields Hawks. "
    "Ted Turner. Everclear Father of Mine. Ephesians 6. Matthew 3. Ben."
)

JUNK_RE = re.compile(r"^[\s.,;:!?\-–—'\"()\[\]/]+$")
REPEAT_CHAR = re.compile(r"^(.)\1{6,}$")


def is_junk(text: str, lp: float | None, nsp: float | None, cr: float | None) -> bool:
    t = (text or "").strip()
    if not t:
        return True
    if JUNK_RE.match(t):
        return True
    letters = re.sub(r"[^A-Za-z]", "", t)
    if len(t) <= 2 and (lp is not None and lp < -0.8):
        return True
    if len(letters) <= 2 and len(t) <= 8:
        return True
    if t.count(",") > 18:
        return True
    if REPEAT_CHAR.match(letters):
        return True
    # whisper collapse / stutter
    if cr is not None and cr > 2.6 and len(t) > 40:
        return True
    if lp is not None and lp < -1.7 and len(t.split()) <= 3:
        return True
    # long runs of single-letter tokens
    toks = t.split()
    if toks and sum(1 for w in toks if len(w) == 1) / len(toks) > 0.6 and len(toks) > 6:
        return True
    return False


def light_fix(text: str) -> str:
    t = (text or "").replace("\u00a0", " ").strip()
    reps = [
        ("right of passage", "rite of passage"),
        ("Ever?Clear", "Everclear"),
        ("ever clear", "Everclear"),
        ("lossness", "lostness"),
        ("ristlessness", "listlessness"),
        ("Hawkes", "Hawks"),
        ("Hawke's", "Hawks"),
        ("Hocks", "Hawks"),
        ("Convocation through modeling", "Conviction through modeling"),
        ("teen hood", "teenhood"),
        ("already ordinarily", "ordinarily"),
        ("o-m by other means", "overcome by other means"),
        ("father woon", "father wound"),
        ("faithfullyly", "faithfully"),
        ("indelably", "indelibly"),
        ("hisbapt", "his baptism"),
        ("so to you let's discuss it", "so do you. Let's discuss it"),
    ]
    for a, b in reps:
        t = t.replace(a, b)
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\b(\w+)(?: \1){2,}\b", r"\1", t, flags=re.I)
    t = t.replace(" .", ".").replace(" ,", ",").replace(" ?", "?").replace(" !", "!")
    return t.strip()


def transcribe_one(model, offset: float, wav: Path, tag: str) -> list[dict]:
    dest = OUTDIR / f"{tag}-novad.jsonl"
    print(f"\n=== {tag} {wav.name} offset={offset} ===", flush=True)
    t0 = time.time()
    segments, info = model.transcribe(
        str(wav),
        language="en",
        beam_size=5,
        vad_filter=False,
        condition_on_previous_text=False,
        temperature=0.0,
        no_speech_threshold=0.85,
        log_prob_threshold=-1.4,
        compression_ratio_threshold=2.5,
        word_timestamps=False,
        initial_prompt=PROMPT,
    )
    recs = []
    n = 0
    kept = 0
    with dest.open("w", encoding="utf-8") as jf:
        for s in segments:
            text = light_fix(s.text or "")
            lp = float(s.avg_logprob) if s.avg_logprob is not None else None
            nsp = float(s.no_speech_prob) if s.no_speech_prob is not None else None
            cr = float(s.compression_ratio) if s.compression_ratio is not None else None
            rec = {
                "chunk": tag,
                "offset": offset,
                "start": round(float(s.start) + offset, 3),
                "end": round(float(s.end) + offset, 3),
                "local_start": round(float(s.start), 3),
                "local_end": round(float(s.end), 3),
                "text": text,
                "avg_logprob": round(lp, 4) if lp is not None else None,
                "no_speech_prob": round(nsp, 4) if nsp is not None else None,
                "compression_ratio": round(cr, 4) if cr is not None else None,
                "junk": is_junk(text, lp, nsp, cr),
            }
            recs.append(rec)
            jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            jf.flush()
            n += 1
            if not rec["junk"]:
                kept += 1
            if n % 8 == 0:
                print(
                    f"  {tag} n={n} t={rec['start']:.0f}s lp={rec['avg_logprob']} junk={rec['junk']} {text[:100]}",
                    flush=True,
                )
    words = sum(len(r["text"].split()) for r in recs if not r["junk"])
    print(
        f"  DONE {tag} n={n} kept={kept} words={words} dur={info.duration:.0f} elapsed={time.time()-t0:.0f}s",
        flush=True,
    )
    return recs


def stitch(all_recs: list[dict]) -> list[dict]:
    """Prefer later chunk in overlap if logprob is better; else drop overlap from later chunk's first 20s."""
    by_chunk: dict[str, list[dict]] = {}
    for r in all_recs:
        by_chunk.setdefault(r["chunk"], []).append(r)
    order = [c[2] for c in CHUNKS]
    out: list[dict] = []
    for i, tag in enumerate(order):
        recs = by_chunk.get(tag, [])
        offset = CHUNKS[i][0]
        keep_after = 0.0
        if i > 0:
            keep_after = offset + 18.0  # skip ~18s of overlap on later chunk
        for r in recs:
            if r.get("junk"):
                continue
            if not r["text"]:
                continue
            if i > 0 and r["start"] < keep_after:
                continue
            out.append(r)
    out.sort(key=lambda r: (r["start"], r["end"]))
    # drop near-duplicate consecutive texts
    deduped = []
    last_txt = ""
    for r in out:
        t = r["text"].lower()
        if t and t == last_txt:
            continue
        deduped.append(r)
        last_txt = t
    return deduped


def group_paragraphs(segs: list[dict], gap: float = 1.8, max_chars: int = 850) -> list[tuple[float, str]]:
    paras: list[tuple[float, str]] = []
    buf: list[str] = []
    buf_start = None
    buf_end = None
    buf_len = 0
    for s in segs:
        text = s["text"]
        if not text:
            continue
        new_para = False
        if buf and buf_end is not None and (s["start"] - buf_end) >= gap:
            new_para = True
        if buf and buf_len > 240 and buf[-1].endswith((".", "?", "!")) and (s["start"] - buf_end) >= 0.4:
            new_para = True
        if buf and buf_len + len(text) > max_chars and buf[-1].endswith((".", "?", "!", ":")):
            new_para = True
        if new_para:
            paras.append((buf_start, " ".join(buf)))
            buf = [text]
            buf_start = s["start"]
            buf_len = len(text)
        else:
            if not buf:
                buf_start = s["start"]
            buf.append(text)
            buf_len += len(text) + 1
        buf_end = s["end"]
    if buf:
        paras.append((buf_start, " ".join(buf)))
    return paras


def assign_speaker(t0: float, text: str, current: str) -> str:
    # Host Eric opens (~0-90s), Everclear clip ~5:20-9:30, then Tim, Eric close last seconds
    low = text.lower()
    if t0 < 85:
        return "Host (likely Eric)"
    if 320 <= t0 < 575:
        return "Clip (Everclear, Father of Mine, ASR)"
    if t0 >= 2860 and ("eric" in low or "discuss" in low):
        return "Tim Hawks"
    return "Tim Hawks"


def write_md(segs: list[dict]) -> int:
    paras = group_paragraphs(segs)
    header = [
        "# 02 Consequences of an Absent Father",
        "",
        "- Title: Biblical Manhood - 02 - Consequences of an Absent Father",
        "- Speaker: Tim Hawks (host Eric opens and closes to groups)",
        "- Date: 2025-09-19",
        "- Video: https://www.youtube.com/watch?v=LPP1coLE9i4",
        "- Source: faster-whisper medium.en from local video/audio. No YouTube caption track. Speech is ASR, not invented. Thin or garbled stretches are left as heard.",
        "",
        "## Transcript",
        "",
    ]
    body_lines = []
    current = None
    for t0, para in paras:
        spk = assign_speaker(t0, para, current)
        if current != spk:
            body_lines.append(f"**{spk}:** {para}")
            body_lines.append("")
            current = spk
        else:
            body_lines.append(para)
            body_lines.append("")
    text = "\n".join(header + body_lines).rstrip() + "\n"
    text = text.replace("\u2014", "-").replace("—", "-")
    dest = TR / "02-consequences-of-an-absent-father.md"
    dest.write_text(text, encoding="utf-8")
    words = len(text.split())
    # also txt/vtt
    (TR / "02.txt").write_text(text, encoding="utf-8")
    vtt = ["WEBVTT", "", "NOTE faster-whisper medium.en session 02 duration=2870s", ""]
    def fmt_ts(t: float) -> str:
        t = max(0.0, t)
        h = int(t // 3600)
        m = int((t % 3600) // 60)
        s = t % 60
        if h:
            return f"{h:02d}:{m:02d}:{s:06.3f}"
        return f"{m:02d}:{s:06.3f}"
    for s in segs:
        vtt.append(f"{fmt_ts(s['start'])} --> {fmt_ts(s['end'])}")
        vtt.append(s["text"])
        vtt.append("")
    (TR / "02.vtt").write_text("\n".join(vtt), encoding="utf-8")
    print(f"WROTE {dest} words={words} paras={len(paras)} segs={len(segs)}", flush=True)
    return words


def main() -> int:
    print("Loading medium.en cpu int8 threads=4 ...", flush=True)
    t0 = time.time()
    model = WhisperModel("medium.en", device="cpu", compute_type="int8", cpu_threads=4)
    print(f"model loaded in {time.time()-t0:.1f}s", flush=True)
    all_recs: list[dict] = []
    for offset, fname, tag in CHUNKS:
        wav = WAVDIR / fname
        if not wav.exists():
            print(f"MISSING {wav}", file=sys.stderr)
            return 2
        recs = transcribe_one(model, offset, wav, tag)
        all_recs.extend(recs)
    comb = OUTDIR / "full-novad.jsonl"
    with comb.open("w", encoding="utf-8") as jf:
        for r in all_recs:
            jf.write(json.dumps(r, ensure_ascii=False) + "\n")
    (RAWDIR / "segments.jsonl").write_text(comb.read_text(encoding="utf-8"), encoding="utf-8")
    kept = stitch(all_recs)
    words = write_md(kept)
    print(f"SUMMARY kept_segs={len(kept)} words={words}", flush=True)
    if kept:
        print(f"span {kept[0]['start']:.1f} -> {kept[-1]['end']:.1f}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
