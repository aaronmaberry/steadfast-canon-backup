"""Rebuild WebVTT from ASR paragraph text. Cue times are proportional to character
weight across known YouTube duration because box IP 429s timedtext file download
and the fetch converter strips cue timestamps. Speech text is not invented.
"""
from __future__ import annotations

def ts(ms: int) -> str:
    if ms < 0:
        ms = 0
    h = ms // 3600000
    m = (ms % 3600000) // 60000
    s = (ms % 60000) // 1000
    milli = ms % 1000
    return f"{h:02d}:{m:02d}:{s:02d}.{milli:03d}"


def split_cues(text: str) -> list[str]:
    paras = [p.strip() for p in text.split("\n") if p.strip() and not p.startswith("#")]
    cues: list[str] = []
    for p in paras:
        # skip markdown headers and speaker-only lines for VTT body if they are meta
        if p.startswith("**") and p.endswith("**") and len(p) < 80:
            continue
        if p.startswith("*") and "caption" in p.lower():
            continue
        # split long paras on sentence boundaries into ~220 char chunks
        buf = ""
        parts: list[str] = []
        for token in p.replace("? ", "?|").replace("! ", "!|").replace(". ", ".|").split("|"):
            token = token.strip()
            if not token:
                continue
            if buf and len(buf) + 1 + len(token) > 220:
                parts.append(buf.strip())
                buf = token
            else:
                buf = (buf + " " + token).strip()
        if buf:
            parts.append(buf.strip())
        cues.extend(parts)
    return cues


def write_vtt(path: str, text: str, duration_s: int) -> int:
    cues = split_cues(text)
    weights = [max(len(c), 1) for c in cues]
    total = sum(weights) or 1
    dur_ms = duration_s * 1000
    lines = ["WEBVTT", "Kind: captions", "Language: en", ""]
    t = 0
    for i, (c, w) in enumerate(zip(cues, weights)):
        span = max(int(dur_ms * w / total), 800)
        start = t
        end = min(t + span, dur_ms)
        if i == len(cues) - 1:
            end = dur_ms
        if end <= start:
            end = start + 800
        lines.append(str(i + 1))
        lines.append(f"{ts(start)} --> {ts(end)}")
        lines.append(c)
        lines.append("")
        t = end
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return len(cues)
