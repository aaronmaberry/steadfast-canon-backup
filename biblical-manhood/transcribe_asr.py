#!/usr/bin/env python3
"""Transcribe one mp3 with faster-whisper small.en and write cleaned markdown."""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from faster_whisper import WhisperModel

ROOT = Path("/workspace/biblical-manhood")
TR = ROOT / "transcripts"
AUDIO = ROOT / "audio"

def collapse_ws(s: str) -> str:
    s = s.replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def light_fix(text: str) -> str:
    """Light ASR cleanup. Do not invent content."""
    text = collapse_ws(text)
    # common whisper artifacts
    text = text.replace(" .", ".").replace(" ,", ",").replace(" ?", "?").replace(" !", "!")
    text = re.sub(r"\.{2,}", "...", text)
    # stagger repeats like "the the"
    text = re.sub(r"\b(\w+)( \1){2,}\b", r"\1", text, flags=re.I)
    return text


def segments_to_paragraphs(segs, pause_break: float = 1.6, max_chars: int = 850) -> list[str]:
    paras: list[str] = []
    cur: list[str] = []
    cur_len = 0
    prev_end = None
    for s in segs:
        t = light_fix(s["text"])
        if not t:
            continue
        gap = 0.0 if prev_end is None else (s["start"] - prev_end)
        should_break = bool(cur) and (gap >= pause_break or cur_len >= max_chars)
        if should_break:
            paras.append(" ".join(cur))
            cur, cur_len = [], 0
        cur.append(t)
        cur_len += len(t) + 1
        prev_end = s["end"]
    if cur:
        paras.append(" ".join(cur))
    # merge tiny leftover paras into previous
    merged: list[str] = []
    for p in paras:
        if merged and len(p) < 80:
            merged[-1] = merged[-1] + " " + p
        else:
            merged.append(p)
    return merged


def detect_speakers(paras: list[str], default: str) -> list[tuple[str, str]]:
    """Tag host opening if first paras look like welcome/prayer, else default speaker."""
    out: list[tuple[str, str]] = []
    host_mode = True
    host_used = False
    host_end_re = re.compile(
        r"\b(tim('s| is)|pastor tim|tim hawks|i'm going to introduce|tim's going)\b",
        re.I,
    )
    amen_re = re.compile(r"\bin jesus'? name\.?\s*amen\b", re.I)
    tim_start_re = re.compile(
        r"\b(well,?\s+good morning|amen\.?\s+(well|good morning)|good morning,? gentlemen|good morning,? guys)\b",
        re.I,
    )
    for i, p in enumerate(paras):
        speaker = default
        if host_mode and i < 6:
            if tim_start_re.search(p) and host_used:
                host_mode = False
                speaker = default
            elif amen_re.search(p) or host_end_re.search(p) or re.search(
                r"\b(welcome|let's pray|grab your coffee|come on in)\b", p, re.I
            ):
                speaker = "Host"
                host_used = True
                if amen_re.search(p):
                    host_mode = False
            else:
                if host_used and not re.search(r"\b(father|lord|pray|jesus)\b", p, re.I):
                    host_mode = False
                    speaker = default
                elif host_used:
                    speaker = "Host"
        out.append((speaker, p))
    return out


def write_md(path: Path, title: str, speaker: str, date: str, url: str, tagged: list[tuple[str, str]]) -> None:
    lines = [
        f"# {title}",
        "",
        f"- Title: {title}",
        f"- Speaker: {speaker}",
        f"- Date: {date}",
        f"- YouTube: {url}",
        "- Source: faster-whisper small.en from audio because YouTube timedtext 429",
        "",
        "## Transcript",
        "",
    ]
    prev = None
    for sp, p in tagged:
        if sp != prev:
            lines.append(f"**{sp}:** {p}")
            lines.append("")
            prev = sp
        else:
            lines.append(p)
            lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mp3")
    ap.add_argument("--title", required=True)
    ap.add_argument("--speaker", default="Tim Hawks")
    ap.add_argument("--date", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--keep-audio", action="store_true")
    args = ap.parse_args()

    mp3 = Path(args.mp3)
    if not mp3.exists():
        print(f"MISSING {mp3}", file=sys.stderr)
        return 2

    print(f"Loading small.en on CPU int8...", flush=True)
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    print(f"Transcribing {mp3} ...", flush=True)
    segments, info = model.transcribe(
        str(mp3),
        language="en",
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
        condition_on_previous_text=True,
    )
    segs = []
    n = 0
    for s in segments:
        segs.append({"start": s.start, "end": s.end, "text": s.text})
        n += 1
        if n % 50 == 0:
            print(f"  {n} segments, t={s.end:.1f}s", flush=True)
    print(f"Done: {n} segments, duration={info.duration:.1f}s lang={info.language}", flush=True)

    paras = segments_to_paragraphs(segs)
    tagged = detect_speakers(paras, args.speaker)
    out = TR / f"{args.slug}.md"
    write_md(out, args.title, args.speaker, args.date, args.url, tagged)
    print(f"WROTE {out} ({out.stat().st_size} bytes, {len(paras)} paras)", flush=True)

    raw = AUDIO / f"{args.slug}.asr.jsonl"
    # don't keep jsonl; user didn't ask. skip.

    if not args.keep_audio:
        try:
            mp3.unlink()
            print(f"DELETED {mp3}", flush=True)
        except FileNotFoundError:
            pass
        # leftover video
        for ext in (".mp4", ".webm", ".mkv"):
            p = mp3.with_suffix(ext)
            if p.exists():
                p.unlink()
                print(f"DELETED {p}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
