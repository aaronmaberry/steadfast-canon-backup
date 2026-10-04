#!/usr/bin/env python3
"""Full ASR for session 24. medium.en float32, 90s chunks, 36s overlap,
no_speech_threshold=1.0 so first windows are not dropped. Do not invent names.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

ROOT = Path("/workspace/biblical-manhood")
AUDIO = ROOT / "audio"
TR = ROOT / "transcripts"
RAW = ROOT / "asr-raw"
LOG = ROOT / "logs" / "transcribe-24.log"

MODEL_NAME = "medium.en"
GAIN_DB = 12.0
CHUNK_SEC = 90.0
OVERLAP_SEC = 36.0  # cover a dropped first 30s whisper window
SAMPLE_RATE = 16000

SESS = {
    "num": "24",
    "slug": "24-final-session-bold-action",
    "md_names": ["24-final-session-bold-action.md"],
    "title": "Final Session: Bold Action",
    "speaker": "Host",
    "date": "2026-04-29",
    "url": "https://www.youtube.com/watch?v=4b6q9go_0eE",
    "prompt": "Biblical Manhood final session. Host speaking. Man cards. Man creed. Christ is my leader. Christ is my teacher. These men are my brothers.",
}


def log(msg: str) -> None:
    line = f"{time.strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def light_fix(text: str) -> str:
    import re
    text = (text or "").replace("\u00a0", " ").strip()
    text = text.replace(" .", ".").replace(" ,", ",").replace(" ?", "?").replace(" !", "!")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\b(\w+)( \1){3,}\b", r"\1", text, flags=re.I)
    return text


def transcribe_array(model: WhisperModel, audio, prompt: str) -> list[dict]:
    segments, _info = model.transcribe(
        audio,
        language="en",
        beam_size=5,
        vad_filter=False,
        condition_on_previous_text=False,
        temperature=0.0,
        word_timestamps=True,
        initial_prompt=prompt,
        no_speech_threshold=1.0,
        log_prob_threshold=-2.0,
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
        if getattr(s, "words", None):
            rec["words"] = [
                {
                    "w": light_fix(w.word),
                    "p": round(float(w.probability), 3) if w.probability is not None else None,
                    "t": round(float(w.start), 3) if w.start is not None else None,
                }
                for w in s.words
                if w.word and w.word.strip()
            ]
        if rec["text"]:
            out.append(rec)
    return out


def chunk_ranges(duration: float) -> list[tuple[float, float]]:
    ranges = []
    start = 0.0
    while start < duration:
        end = min(start + CHUNK_SEC + OVERLAP_SEC, duration)
        remaining_after = duration - (start + CHUNK_SEC)
        if 0 < remaining_after < 40:
            end = duration
        ranges.append((start, end))
        if end >= duration:
            break
        start += CHUNK_SEC
    return ranges


def stitch(chunk_results: list[tuple[float, list[dict]]]) -> list[dict]:
    stitched: list[dict] = []
    for i, (offset, segs) in enumerate(chunk_results):
        keep_after = 0.0 if i == 0 else OVERLAP_SEC * 0.45
        prev = [s["text"].lower() for s in stitched[-10:]]
        for s in segs:
            if s["start"] < keep_after:
                continue
            t = s["text"]
            if t.lower() in prev:
                continue
            rec = dict(s)
            rec["start"] = round(offset + s["start"], 3)
            rec["end"] = round(offset + s["end"], 3)
            if "words" in rec:
                rec["words"] = [
                    {**w, "t": round(w["t"] + offset, 3) if w.get("t") is not None else None}
                    for w in rec["words"]
                ]
            stitched.append(rec)
            prev.append(t.lower())
            if len(prev) > 14:
                prev = prev[-14:]
    return stitched


def group_paragraphs(segs: list[dict], gap: float = 1.4, max_chars: int = 900) -> list[str]:
    paras: list[str] = []
    buf: list[str] = []
    buf_end = None
    buf_len = 0
    for s in segs:
        text = s["text"]
        if not text:
            continue
        new_para = False
        if buf and buf_end is not None and (s["start"] - buf_end) >= gap:
            new_para = True
        if buf and buf_len > 260 and buf[-1].endswith((".", "?", "!")) and (s["start"] - buf_end) >= 0.45:
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
        buf_end = s["end"]
    if buf:
        paras.append(" ".join(buf))
    merged: list[str] = []
    for p in paras:
        if merged and len(p) < 70:
            merged[-1] = merged[-1] + " " + p
        else:
            merged.append(p)
    return merged


def fmt_ts(t: float) -> str:
    if t < 0:
        t = 0.0
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    if h:
        return f"{h:02d}:{m:02d}:{s:06.3f}"
    return f"{m:02d}:{s:06.3f}"


def write_outputs(sess: dict, segs: list[dict], duration: float) -> int:
    paras = group_paragraphs(segs)
    speaker = sess["speaker"]
    num = sess["num"]
    title = sess["title"]
    low_names = []
    for s in segs:
        for w in s.get("words") or []:
            if w.get("p") is not None and w["p"] < 0.45 and w["w"][:1].isupper() and len(w["w"]) > 2:
                low_names.append(f"{w['w']}@{fmt_ts(w.get('t') or s['start'])} p={w['p']}")
    header = [
        f"# {num}. {title}",
        "",
        f"- Title: Biblical Manhood - {num} - {title}",
        f"- Speaker: {speaker} (not Tim Hawks; Tim in Orlando per session 23). Catalog lists Tim Hawks.",
        f"- Date: {sess['date']}",
        f"- Video: {sess['url']}",
        f"- Caption source: faster-whisper {MODEL_NAME} from full session audio (+{GAIN_DB:.0f} dB). No invented speech. Names are ASR; low-confidence tokens are not corrected.",
        f"- Audio duration: {duration:.0f}s. Segments: {len(segs)}.",
        "",
        "## Transcript",
        "",
    ]
    body_paras = []
    first = True
    for p in paras:
        if first:
            body_paras.append(f"**{speaker}:** {p}")
            first = False
        else:
            body_paras.append(p)
    body = "\n\n".join(body_paras) + "\n"
    if low_names:
        body += (
            "\n## Low-confidence capitalized ASR tokens (not verified names)\n\n"
            + ", ".join(low_names[:80])
            + "\n"
        )
    text = "\n".join(header) + body
    for name in sess["md_names"]:
        path = TR / name
        if path.is_symlink():
            path.unlink()
        path.write_text(text, encoding="utf-8")
    words = len(body.split())
    raw_dir = RAW / sess["slug"]
    raw_dir.mkdir(parents=True, exist_ok=True)
    with (raw_dir / "segments.jsonl").open("w", encoding="utf-8") as f:
        for s in segs:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    txt_lines = [f"[{fmt_ts(s['start'])} --> {fmt_ts(s['end'])}] {s['text']}" for s in segs]
    (raw_dir / "timed.txt").write_text("\n".join(txt_lines) + "\n", encoding="utf-8")
    (TR / f"{num}.txt").write_text(body, encoding="utf-8")
    vtt = ["WEBVTT", "", f"NOTE faster-whisper {MODEL_NAME} {sess['slug']} duration={duration:.1f}s", ""]
    for s in segs:
        vtt.append(f"{fmt_ts(s['start'])} --> {fmt_ts(s['end'])}")
        vtt.append(s["text"])
        vtt.append("")
    (TR / f"{num}.vtt").write_text("\n".join(vtt), encoding="utf-8")
    span0 = segs[0]["start"] if segs else 0
    span1 = segs[-1]["end"] if segs else 0
    wpm = (words / (duration / 60.0)) if duration else 0
    log(f"WROTE {sess['md_names'][0]} words={words} paras={len(paras)} segs={len(segs)} span={span0:.1f}->{span1:.1f} wpm={wpm:.1f}")
    return words


def resolve_audio(slug: str) -> Path:
    for p in (
        AUDIO / "hq" / f"{slug}.webm",
        AUDIO / f"{slug}.mp3",
        AUDIO / "full" / f"{slug}.mp3",
    ):
        if p.exists() and p.stat().st_size > 1_000_000:
            return p
    raise FileNotFoundError(slug)


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        text=True,
    ).strip()
    return float(out)


def extract_wav(src: Path, dest: Path, start: float, length: float, db: float) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-nostdin",
        "-ss", f"{start:.3f}", "-t", f"{length:.3f}",
        "-i", str(src),
        "-ac", "1", "-ar", "16000",
        "-af", f"volume={db:.1f}dB",
        "-c:a", "pcm_s16le", str(dest),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def transcribe_session(model: WhisperModel, sess: dict) -> int:
    slug = sess["slug"]
    log(f"=== session {sess['num']} {slug} ===")
    src = resolve_audio(slug)
    duration = ffprobe_duration(src)
    log(f"  source {src} size={src.stat().st_size} duration={duration:.1f}s")
    ranges = chunk_ranges(duration)
    raw_dir = RAW / slug
    wav_dir = AUDIO / "chunks-full" / slug
    raw_dir.mkdir(parents=True, exist_ok=True)
    wav_dir.mkdir(parents=True, exist_ok=True)
    chunk_results = []
    for i, (start, end) in enumerate(ranges):
        length = end - start
        cache = raw_dir / f"ff-{i:02d}.jsonl"
        wav = wav_dir / f"c{i:02d}-{int(start):04d}.wav"
        extract_wav(src, wav, start, length, GAIN_DB)
        t0 = time.time()
        log(f"  transcribe chunk {i+1}/{len(ranges)} {start:.0f}-{end:.0f}s {wav.name}")
        segs = transcribe_array(model, str(wav), sess["prompt"])
        words = sum(len(s["text"].split()) for s in segs)
        dt = time.time() - t0
        last = segs[-1]["end"] if segs else 0
        with cache.open("w", encoding="utf-8") as f:
            for s in segs:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
        log(f"    {len(segs)} segs words={words} last={last:.1f}s in {dt:.0f}s")
        chunk_results.append((start, segs))
        try:
            wav.unlink()
        except FileNotFoundError:
            pass
    stitched = stitch(chunk_results)
    return write_outputs(sess, stitched, duration)


def main() -> int:
    log(f"Loading {MODEL_NAME} cpu float32 ...")
    threads = int(os.environ.get("WHISPER_THREADS", "4"))
    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="float32", cpu_threads=threads)
    log(f"model ready threads={threads}")
    w = transcribe_session(model, SESS)
    log(f"SUMMARY 24:{w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
