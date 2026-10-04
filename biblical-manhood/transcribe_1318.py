#!/usr/bin/env python3
"""Full ASR for Steadfast Men sessions 13-18.

Decode once, apply +12 dB in numpy (no ffmpeg limiter), transcribe 3-min
chunks with faster-whisper medium.en. Do not invent speech. Do not touch 02.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel
from faster_whisper.audio import decode_audio

ROOT = Path("/workspace/biblical-manhood")
AUDIO = ROOT / "audio"
TR = ROOT / "transcripts"
RAW = ROOT / "asr-raw"
LOG = ROOT / "logs" / "transcribe-1318.log"

MODEL_NAME = "medium.en"
GAIN_DB = 12.0
CHUNK_SEC = 90.0
OVERLAP_SEC = 6.0
SAMPLE_RATE = 16000
MIN_WORDS_PER_MIN = 70  # retry louder if below this

SESSIONS = [
    {
        "num": "13",
        "slug": "13-a-biblical-definition-of-manhood-part-1",
        "md_names": [
            "13-a-biblical-definition-of-manhood-part-1.md",
            "13-biblical-definition-of-manhood-p1.md",
        ],
        "title": "A Biblical Definition of Manhood - Part 1",
        "speaker": "Tim Hawks",
        "date": "2026-02-06",
        "url": "https://www.youtube.com/watch?v=1xtJgaOpmZ8",
        "prompt": "Biblical Manhood session. Speaker Tim Hawks. Genesis. Adam. Eve. Robert Lewis.",
    },
    {
        "num": "14",
        "slug": "14-a-biblical-definition-of-manhood-part-2",
        "md_names": [
            "14-a-biblical-definition-of-manhood-part-2.md",
            "14-biblical-definition-of-manhood-p2.md",
        ],
        "title": "A Biblical Definition of Manhood - Part 2",
        "speaker": "Tim Hawks",
        "date": "2026-02-11",
        "url": "https://www.youtube.com/watch?v=a9P1EVOBbHE",
        "prompt": "Biblical Manhood session. Speaker Tim Hawks. A real man rejects passivity, accepts responsibility, leads courageously.",
    },
    {
        "num": "15",
        "slug": "15-a-man-and-his-wife-part-1",
        "md_names": [
            "15-a-man-and-his-wife-part-1.md",
            "15-a-man-and-his-wife-p1.md",
        ],
        "title": "A Man and His Wife - Part 1",
        "speaker": "Tim Hawks",
        "date": "2026-02-18",
        "url": "https://www.youtube.com/watch?v=3Ps3ezdRO6Y",
        "prompt": "Biblical Manhood session. Speaker Tim Hawks. Ephesians 5. husband. wife. servant leader.",
    },
    {
        "num": "16",
        "slug": "16-25-ways-to-be-a-servant-leader",
        "md_names": ["16-25-ways-to-be-a-servant-leader.md"],
        "title": "25 Ways to be a Servant Leader",
        "speaker": "Cindy Hawks",
        "date": "2026-02-25",
        "url": "https://www.youtube.com/watch?v=apJIZ8QYT_E",
        "prompt": "Biblical Manhood session. Speaker Cindy Hawks. Twenty-five ways to be a servant leader.",
    },
    {
        "num": "17",
        "slug": "17-a-man-and-his-wife-part-2",
        "md_names": [
            "17-a-man-and-his-wife-part-2.md",
            "17-a-man-and-his-wife-p2.md",
        ],
        "title": "A Man and His Wife - Part 2",
        "speaker": "Tim Hawks",
        "date": "2026-03-04",
        "url": "https://www.youtube.com/watch?v=T4VCs8hIarg",
        "prompt": "Biblical Manhood session. Speaker Tim Hawks. helper. complementarian. Ephesians 5.",
    },
    {
        "num": "18",
        "slug": "18-a-man-and-his-sexuality",
        "md_names": ["18-a-man-and-his-sexuality.md"],
        "title": "A Man and His Sexuality",
        "speaker": "Tim Hawks",
        "date": "2026-03-11",
        "url": "https://www.youtube.com/watch?v=KS3dzdmW_tU",
        "prompt": "Biblical Manhood session. Speaker Tim Hawks. sexuality. Song of Solomon. marriage.",
    },
]


def log(msg: str) -> None:
    line = f"{time.strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def light_fix(text: str) -> str:
    text = (text or "").replace("\u00a0", " ").strip()
    text = text.replace(" .", ".").replace(" ,", ",").replace(" ?", "?").replace(" !", "!")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\b(\w+)( \1){3,}\b", r"\1", text, flags=re.I)
    return text


def boost(audio: np.ndarray, db: float) -> np.ndarray:
    g = 10.0 ** (db / 20.0)
    out = audio * g
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def transcribe_array(model: WhisperModel, audio, prompt: str) -> list[dict]:
    segments, _info = model.transcribe(
        audio,
        language="en",
        beam_size=5,
        vad_filter=False,
        condition_on_previous_text=False,
        temperature=0.0,
        word_timestamps=False,
        initial_prompt=prompt,
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
    """Keep long segments that start in the overlap but extend past it."""
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
    header = [
        f"# {num}. {title}",
        "",
        f"- Title: Biblical Manhood - {num} - {title}",
        f"- Speaker: {speaker}",
        f"- Date: {sess['date']}",
        f"- Video: {sess['url']}",
        f"- Caption source: faster-whisper {MODEL_NAME} from full session audio (+{GAIN_DB:.0f} dB). No invented speech.",
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
    text = "\n".join(header) + body
    for name in sess["md_names"]:
        path = TR / name
        if path.is_symlink() or path.exists():
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
        AUDIO / "full" / f"{slug}.mp3",
        AUDIO / "hq" / f"{slug}.webm",
        AUDIO / "hq" / f"{slug}.mp4",
        AUDIO / f"{slug}.mp3",
    ):
        if p.exists() and p.stat().st_size > 1_000_000:
            return p
    raise FileNotFoundError(slug)



def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output(
        ["ffprobe","-v","error","-show_entries","format=duration",
         "-of","default=noprint_wrappers=1:nokey=1", str(path)],
        text=True,
    ).strip()
    return float(out)


def extract_wav(src: Path, dest: Path, start: float, length: float, db: float) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg","-y","-nostdin",
        "-ss", f"{start:.3f}", "-t", f"{length:.3f}",
        "-i", str(src),
        "-ac","1","-ar","16000",
        "-af", f"volume={db:.1f}dB",
        "-c:a","pcm_s16le", str(dest),
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
        mins = length / 60.0
        cache = raw_dir / f"ff-{i:02d}.jsonl"
        if cache.exists() and cache.stat().st_size > 400:
            segs = [json.loads(l) for l in cache.read_text().splitlines() if l.strip()]
            words = sum(len(s["text"].split()) for s in segs)
            log(f"  resume chunk {i+1}/{len(ranges)} {start:.0f}-{end:.0f}s words={words}")
            if words >= 80 * mins:
                chunk_results.append((start, segs))
                continue
            log("    cache thin — retranscribing")
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
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    sessions = SESSIONS
    if only:
        sessions = [s for s in SESSIONS if s["num"] in only or s["slug"] in only]
    log(f"Loading {MODEL_NAME} cpu float32 ...")
    threads = int(os.environ.get("WHISPER_THREADS", "4"))
    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="float32", cpu_threads=threads)
    log(f"model ready threads={threads} sessions={[s['num'] for s in sessions]}")
    summary = []
    for sess in sessions:
        w = transcribe_session(model, sess)
        summary.append((sess["num"], w))
    log("SUMMARY " + " ".join(f"{n}:{w}" for n, w in summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
