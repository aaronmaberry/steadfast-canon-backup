#!/usr/bin/env python3
"""Turn dumped ASR text into VTT + cleaned markdown transcript."""
import re, sys, os, html

ROOT = "/workspace/biblical-manhood"

def fmt_ts(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"

def split_paras(text: str) -> list[str]:
    text = text.replace("\r\n", "\n").strip()
    # keep existing blank-line paras if present
    if "\n\n" in text:
        paras = [re.sub(r"\s+", " ", p).strip() for p in text.split("\n\n")]
        return [p for p in paras if p]
    # sentence-pack into ~400-800 char paragraphs
    parts = re.split(r"(?<=[.!?])\s+", text)
    paras, buf = [], ""
    for sent in parts:
        sent = sent.strip()
        if not sent:
            continue
        if buf and len(buf) + len(sent) > 700:
            paras.append(buf.strip())
            buf = sent
        else:
            buf = (buf + " " + sent).strip()
    if buf:
        paras.append(buf.strip())
    return paras

def write_vtt(path, paras, duration, note_lines):
    n = max(len(paras), 1)
    # proportional estimates; labeled as such in NOTE
    words = [max(len(p.split()), 1) for p in paras]
    total_w = sum(words) or 1
    acc = 0.0
    cues = []
    for p, w in zip(paras, words):
        start = acc
        dur = duration * (w / total_w)
        end = min(duration, start + max(dur, 1.0))
        acc = end
        cues.append((start, end, p))
    if cues:
        cues[-1] = (cues[-1][0], duration, cues[-1][2])
    lines = ["WEBVTT", "", "NOTE"]
    for nl in note_lines:
        lines.append(nl)
    lines.append("")
    for i, (a, b, p) in enumerate(cues, 1):
        lines.append(str(i))
        lines.append(f"{fmt_ts(a)} --> {fmt_ts(b)}")
        lines.append(p)
        lines.append("")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write("\n".join(lines))

if __name__ == "__main__":
    print("helper ready")
