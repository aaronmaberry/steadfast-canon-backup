#!/usr/bin/env python3
"""Re-stitch cached faster-whisper chunks without dropping long overlap segments."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from transcribe_1318 import RAW, SESSIONS, ffprobe_duration, resolve_audio, write_outputs

CHUNK_SEC = 90.0


def load_chunks(slug: str) -> list[tuple[float, list[dict]]]:
    raw = RAW / slug
    files = sorted(raw.glob("ff-*.jsonl"))
    if not files:
        raise FileNotFoundError(raw)
    out = []
    for p in files:
        i = int(p.stem.split("-")[1])
        start = i * CHUNK_SEC
        segs = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
        out.append((start, segs))
    return out


def stitch_keep_overlap(chunk_results: list[tuple[float, list[dict]]]) -> list[dict]:
    stitched: list[dict] = []
    covered_end = -1.0
    recent: list[str] = []
    for i, (offset, segs) in enumerate(chunk_results):
        for s in segs:
            abs_start = round(offset + s["start"], 3)
            abs_end = round(offset + s["end"], 3)
            t = s["text"]
            if abs_end <= covered_end + 0.15:
                continue
            in_overlap = i > 0 and abs_start < covered_end
            if in_overlap and t.lower() in recent:
                continue
            rec = dict(s)
            rec["start"] = abs_start
            rec["end"] = abs_end
            stitched.append(rec)
            recent.append(t.lower())
            if len(recent) > 14:
                recent = recent[-14:]
            covered_end = max(covered_end, abs_end)
    return stitched


def main() -> int:
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    sessions = SESSIONS
    if only:
        sessions = [s for s in SESSIONS if s["num"] in only or s["slug"] in only]
    for sess in sessions:
        chunks = load_chunks(sess["slug"])
        segs = stitch_keep_overlap(chunks)
        src = resolve_audio(sess["slug"])
        duration = ffprobe_duration(src)
        n = write_outputs(sess, segs, duration)
        print(f"restitched {sess['num']} words={n} segs={len(segs)} chunks={len(chunks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
