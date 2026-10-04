#!/usr/bin/env python3
"""Transcribe one mp3 with faster-whisper small.en and write cleaned markdown."""
import argparse
import os
import re
import sys

from faster_whisper import WhisperModel

FILLERS = re.compile(r"\b(um+|uh+|er+|ah+)\b", re.I)
MULTI_SPACE = re.compile(r" {2,}")
SPACE_PUNCT = re.compile(r"\s+([,.;:!?])")


def clean_text(t: str) -> str:
    t = t.replace("\u2014", "-").replace("\u2013", "-").replace("\u2018", "'").replace("\u2019", "'")
    t = t.replace("\u201c", '"').replace("\u201d", '"')
    t = FILLERS.sub("", t)
    t = SPACE_PUNCT.sub(r"\1", t)
    t = MULTI_SPACE.sub(" ", t)
    t = t.strip()
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    return t


def group_paragraphs(items, gap=1.4, max_chars=900):
    paras = []
    buf = []
    buf_end = None
    buf_len = 0
    for start, end, text in items:
        text = clean_text(text)
        if not text:
            continue
        new_para = False
        if buf and buf_end is not None and (start - buf_end) >= gap:
            new_para = True
        if buf and buf_len > 280 and buf[-1].endswith((".", "?", "!")) and (start - buf_end) >= 0.55:
            new_para = True
        if buf and buf_len + len(text) > max_chars and buf[-1].endswith((".", "?", "!", ":")):
            new_para = True
        if new_para:
            paras.append(" ".join(buf))
            buf = [text]
            buf_len = len(text)
        else:
            buf.append(text)
            buf_len += len(text) + 1
        buf_end = end
    if buf:
        paras.append(" ".join(buf))
    return paras


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mp3")
    ap.add_argument("out_md")
    ap.add_argument("--title", required=True)
    ap.add_argument("--speaker", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--model", default="small.en")
    args = ap.parse_args()

    print(f"Loading model {args.model}...", flush=True)
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    print(f"Transcribing {args.mp3}...", flush=True)
    segments, info = model.transcribe(
        args.mp3,
        language="en",
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
        word_timestamps=False,
    )
    items = []
    n = 0
    for seg in segments:
        n += 1
        items.append((seg.start, seg.end, seg.text))
        if n % 40 == 0:
            print(f"  {n} segments, {seg.end:.0f}s", flush=True)
    dur = items[-1][1] if items else 0
    print(f"Done: {n} segments, {dur:.0f}s audio, lang={info.language}", flush=True)
    paras = group_paragraphs(items)
    num = os.path.basename(args.out_md).split("-", 1)[0]
    header = [
        f"# {num}. {args.title}",
        "",
        f"Speaker: {args.speaker}",
        f"Date: {args.date}",
        f"YouTube: {args.url}",
        "Source: faster-whisper small.en from audio because YouTube timedtext 429",
        "",
        f"{args.speaker}:",
        "",
    ]
    body = "\n\n".join(paras) + "\n"
    os.makedirs(os.path.dirname(args.out_md) or ".", exist_ok=True)
    with open(args.out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(header) + body)
    print(f"Wrote {args.out_md} ({len(paras)} paragraphs)", flush=True)


if __name__ == "__main__":
    main()
