#!/usr/bin/env python3
"""Fill >=8s holes left by 90s-chunk ASR (first 30s window often dropped).

Uses medium.en float32, VAD off, no_speech_threshold=1.0. Does not invent speech.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

# Reuse session metadata + writers from the running 13-18 job.
sys.path.insert(0, "/workspace/biblical-manhood")
from transcribe_1318 import (  # noqa: E402
    SESSIONS,
    TR,
    RAW,
    AUDIO,
    GAIN_DB,
    MODEL_NAME,
    light_fix,
    resolve_audio,
    write_outputs,
    log as base_log,
)

LOG = Path("/workspace/biblical-manhood/logs/gap-fill.log")
GAP_MIN = 8.0
PAD = 1.5
MIN_NEW_WORDS = 4


def log(msg: str) -> None:
    line = f"{time.strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    ).strip()
    return float(out)


def extract_wav(src: Path, dest: Path, start: float, length: float, db: float) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-nostdin",
        "-ss",
        f"{start:.3f}",
        "-t",
        f"{length:.3f}",
        "-i",
        str(src),
        "-ac",
        "1",
        "-ar",
        "16000",
        "-af",
        f"volume={db:.1f}dB",
        "-c:a",
        "pcm_s16le",
        str(dest),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def transcribe_wav(model: WhisperModel, wav: Path, prompt: str) -> list[dict]:
    segments, _info = model.transcribe(
        str(wav),
        language="en",
        beam_size=5,
        vad_filter=False,
        condition_on_previous_text=False,
        temperature=0.0,
        word_timestamps=False,
        initial_prompt=prompt,
        no_speech_threshold=1.0,
        log_prob_threshold=-2.0,
        compression_ratio_threshold=2.6,
    )
    out = []
    for s in segments:
        rec = {
            "start": round(float(s.start), 3),
            "end": round(float(s.end), 3),
            "text": light_fix(s.text),
            "avg_logprob": round(float(s.avg_logprob), 4) if s.avg_logprob is not None else None,
            "no_speech_prob": round(float(s.no_speech_prob), 4) if s.no_speech_prob is not None else None,
        }
        if rec["text"]:
            out.append(rec)
    return out


def find_gaps(segs: list[dict], duration: float) -> list[tuple[float, float]]:
    gaps = []
    t = 0.0
    for s in segs:
        if s["start"] - t >= GAP_MIN:
            gaps.append((t, s["start"]))
        t = max(t, s["end"])
    if duration - t >= GAP_MIN:
        gaps.append((t, duration))
    return gaps


def fill_session(model: WhisperModel, sess: dict) -> int:
    slug = sess["slug"]
    raw_dir = RAW / slug
    segs_path = raw_dir / "segments.jsonl"
    if not segs_path.exists():
        log(f"SKIP {sess['num']} no segments.jsonl")
        return 0
    segs = [json.loads(l) for l in segs_path.read_text().splitlines() if l.strip()]
    segs.sort(key=lambda s: s["start"])
    src = resolve_audio(slug)
    duration = ffprobe_duration(src)
    gaps = find_gaps(segs, duration)
    log(f"=== fill {sess['num']} gaps={len(gaps)} words_now={sum(len(s['text'].split()) for s in segs)} dur={duration:.1f} ===")
    if not gaps:
        return write_outputs(sess, segs, duration)

    wav_dir = AUDIO / "chunks-gaps" / slug
    wav_dir.mkdir(parents=True, exist_ok=True)
    added = []
    for i, (g0, g1) in enumerate(gaps):
        start = max(0.0, g0 - PAD)
        end = min(duration, g1 + PAD)
        length = end - start
        wav = wav_dir / f"g{i:02d}-{int(start):04d}.wav"
        extract_wav(src, wav, start, length, GAIN_DB)
        t0 = time.time()
        new = transcribe_wav(model, wav, sess["prompt"])
        for s in new:
            s["start"] = round(s["start"] + start, 3)
            s["end"] = round(s["end"] + start, 3)
        # keep only speech that lands inside the hole (tiny pad)
        hole0, hole1 = g0 - 0.15, g1 + 0.15
        kept = [s for s in new if s["end"] > hole0 and s["start"] < hole1 and s["text"]]
        words = sum(len(s["text"].split()) for s in kept)
        dt = time.time() - t0
        log(
            f"  gap {i+1}/{len(gaps)} {g0:.1f}-{g1:.1f}s -> {len(kept)} segs words={words} in {dt:.0f}s"
            f" :: {(kept[0]['text'][:70] if kept else '')}"
        )
        if words >= MIN_NEW_WORDS:
            added.extend(kept)
        try:
            wav.unlink()
        except FileNotFoundError:
            pass

    # merge, drop near-duplicate timestamps
    all_segs = segs + added
    all_segs.sort(key=lambda s: (s["start"], s["end"]))
    merged: list[dict] = []
    for s in all_segs:
        if merged:
            prev = merged[-1]
            overlap = min(prev["end"], s["end"]) - max(prev["start"], s["start"])
            if overlap > 0.6 and s["text"].lower() == prev["text"].lower():
                continue
            # if new segment is almost entirely inside an existing one, skip
            if s["start"] >= prev["start"] - 0.2 and s["end"] <= prev["end"] + 0.2:
                if s["text"].lower() in prev["text"].lower() or prev["text"].lower() in s["text"].lower():
                    continue
        merged.append(s)

    words = write_outputs(sess, merged, duration)
    log(f"  filled {sess['num']} now words={words} segs={len(merged)} added={len(added)}")
    return words


def main() -> int:
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    sessions = SESSIONS
    if only:
        sessions = [s for s in SESSIONS if s["num"] in only or s["slug"] in only]
    threads = int(os.environ.get("WHISPER_THREADS", "4"))
    log(f"Loading {MODEL_NAME} cpu float32 threads={threads} sessions={[s['num'] for s in sessions]}")
    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="float32", cpu_threads=threads)
    log("model ready")
    summary = []
    for sess in sessions:
        w = fill_session(model, sess)
        summary.append((sess["num"], w))
    log("SUMMARY " + " ".join(f"{n}:{w}" for n, w in summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
