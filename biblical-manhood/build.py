#!/usr/bin/env python3
"""Turn untimed YouTube ASR dumps into VTT + cleaned transcripts."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path("/workspace/biblical-manhood")
RAW = ROOT / "_raw"
CAP = ROOT / "captions"
TR = ROOT / "transcripts"

# video durations in seconds from yt-dlp
DURATION = {
    "07": 3044,
    "08": 3264,
    "09": 3062,
    "10": 2929,
    "11": 3377,
    "12": 3156,
}

META = {
    "07": {
        "slug": "07-making-friends-finding-a-mentor",
        "title": "Making Friends, Finding a Mentor",
        "date": "2025-10-24",
        "yt": "S5BreS-WwQk",
        "default_speaker": "Tim Hawks",
    },
    "08": {
        "slug": "08-the-depravity-wound",
        "title": "The Depravity Wound",
        "date": "2025-10-31",
        "yt": "z9AtC99ztt0",
        "default_speaker": "Tim Hawks",
    },
    "09": {
        "slug": "09-depravity-specifically-for-men",
        "title": "What Depravity Means Specifically for Men",
        "date": "2025-11-07",
        "yt": "T3vTHDPC__w",
        "default_speaker": "Tim Hawks",
    },
    "10": {
        "slug": "10-lack-of-masculine-vision-wound",
        "title": "The Lack of a Masculine Vision Wound",
        "date": "2025-11-14",
        "yt": "yVpugbFuJRw",
        "default_speaker": "Tim Hawks",
    },
    "11": {
        "slug": "11-first-semester-review",
        "title": "First Semester Review",
        "date": "2026-01-23",
        "yt": "xXUQ6JKRcdw",
        "default_speaker": "Tim Hawks",
    },
    "12": {
        "slug": "12-genesis-to-manhood",
        "title": "Genesis to Manhood",
        "date": "2026-01-30",
        "yt": "GLk605vgwks",
        "default_speaker": "Tim Hawks",
    },
}

SOUND = re.compile(r"\[(music|applause|laughter|clears throat|cough|snorts|snort)\]", re.I)

def ts(sec: float) -> str:
    if sec < 0:
        sec = 0
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"

def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    # keep existing punctuation; split on .!? followed by space+capital or end
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", text)
    out = []
    buf = ""
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if buf and len(buf) < 80:
            buf = buf + " " + p
        else:
            if buf:
                out.append(buf)
            buf = p
    if buf:
        out.append(buf)
    return out

def paragraphs(sents: list[str], target=4) -> list[str]:
    paras = []
    cur = []
    for s in sents:
        cur.append(s)
        if len(cur) >= target and s.endswith((".", "?", "!")):
            paras.append(" ".join(cur))
            cur = []
    if cur:
        paras.append(" ".join(cur))
    return paras

def cue_chunks(sents: list[str]) -> list[str]:
    """Shorter chunks for VTT cues."""
    chunks = []
    cur = []
    n = 0
    for s in sents:
        cur.append(s)
        n += len(s.split())
        if n >= 28:
            chunks.append(" ".join(cur))
            cur, n = [], 0
    if cur:
        chunks.append(" ".join(cur))
    return chunks

def write_episode(nn: str, raw: str, speaker_notes: str | None = None) -> dict:
    meta = META[nn]
    slug = meta["slug"]
    dur = DURATION[nn]
    raw = raw.strip()
    words = raw.split()
    sents = split_sentences(raw)
    paras = paragraphs(sents)
    chunks = cue_chunks(sents)

    # VTT with proportional times; flagged as estimates
    vtt_lines = [
        "WEBVTT",
        "Kind: captions",
        "Language: en",
        "",
        "NOTE",
        "Source: YouTube automatic captions (ASR, en-orig). No manual English subtitles.",
        "Authentic timed cues could not be downloaded (YouTube timedtext HTTP 429 from this host).",
        "Cue start/end times below are proportional estimates from video duration and word counts,",
        "not original YouTube timestamps. Speech text is ASR, not invented.",
        "",
    ]
    total_w = max(sum(len(c.split()) for c in chunks), 1)
    t = 0.0
    for c in chunks:
        w = len(c.split())
        dt = dur * (w / total_w)
        start, end = t, min(dur, t + dt)
        text = SOUND.sub(lambda m: f"[{m.group(1).title()}]", c)
        vtt_lines.append(f"{ts(start)} --> {ts(end)}")
        vtt_lines.append(text)
        vtt_lines.append("")
        t = end
    cap_path = CAP / f"{slug}.en.vtt"
    cap_path.write_text("\n".join(vtt_lines), encoding="utf-8")

    md = []
    md.append(f"# {meta['title']}")
    md.append("")
    md.append(f"- Session: {nn}")
    md.append(f"- Speaker: {meta['default_speaker']}")
    md.append(f"- Date: {meta['date']}")
    md.append(f"- YouTube: https://www.youtube.com/watch?v={meta['yt']}")
    md.append("- Caption source: YouTube ASR (en-orig). No manual English subtitles.")
    md.append("- Cleaning: duplicate/run-on ASR flattened into paragraphs. Sound tags kept in brackets. Speaker is Tim Hawks unless a caption stretch clearly belongs to someone else.")
    if speaker_notes:
        md.append(f"- Other voices: {speaker_notes}")
    md.append("")
    md.append(f"**{meta['default_speaker']}**")
    md.append("")
    for p in paras:
        md.append(p)
        md.append("")
    tr_path = TR / f"{slug}.md"
    tr_path.write_text("\n".join(md), encoding="utf-8")
    return {
        "nn": nn,
        "slug": slug,
        "words": len(words),
        "sents": len(sents),
        "paras": len(paras),
        "cues": len(chunks),
        "dur": dur,
        "cap": str(cap_path),
        "tr": str(tr_path),
        "starts": raw[:80],
        "ends": raw[-80:],
    }

if __name__ == "__main__":
    print("builder loaded")
