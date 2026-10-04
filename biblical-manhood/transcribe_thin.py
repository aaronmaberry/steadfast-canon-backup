#!/usr/bin/env python3
"""Full-file faster-whisper transcription for sessions 13-18 and 24.

medium.en produced unusable fragments on this audio. small.en on opus/webm
(or 192k mp3 derived from opus 251) yields real speech. Do not invent text.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

ROOT = Path("/workspace/biblical-manhood")
AUDIO = ROOT / "audio"
HQ = AUDIO / "hq"
TR = ROOT / "transcripts"
RAW = ROOT / "asr-raw"
LOG = ROOT / "logs" / "thin-transcribe.log"

# small.en: medium.en on this lecture audio dropped most speech (see logs).
MODEL_NAME = os.environ.get("WHISPER_MODEL", "small.en")

SESSIONS = [
    {
        "num": "13",
        "slug": "13-a-biblical-definition-of-manhood-part-1",
        "md": "13-biblical-definition-of-manhood-p1.md",
        "title": "A Biblical Definition of Manhood - Part 1",
        "speaker": "Tim Hawks",
        "date": "2026-02-06",
        "url": "https://www.youtube.com/watch?v=1xtJgaOpmZ8",
        "prompt": "Biblical Manhood. Speaker Tim Hawks. Good morning gentlemen.",
    },
    {
        "num": "14",
        "slug": "14-a-biblical-definition-of-manhood-part-2",
        "md": "14-biblical-definition-of-manhood-p2.md",
        "title": "A Biblical Definition of Manhood - Part 2",
        "speaker": "Tim Hawks",
        "date": "2026-02-11",
        "url": "https://www.youtube.com/watch?v=a9P1EVOBbHE",
        "prompt": "Biblical Manhood. Speaker Tim Hawks. A real man rejects passivity.",
    },
    {
        "num": "15",
        "slug": "15-a-man-and-his-wife-part-1",
        "md": "15-a-man-and-his-wife-p1.md",
        "title": "A Man and His Wife - Part 1",
        "speaker": "Tim Hawks",
        "date": "2026-02-18",
        "url": "https://www.youtube.com/watch?v=3Ps3ezdRO6Y",
        "prompt": "Biblical Manhood. Speaker Tim Hawks. Ephesians 5. Husband and wife.",
    },
    {
        "num": "16",
        "slug": "16-25-ways-to-be-a-servant-leader",
        "md": "16-25-ways-to-be-a-servant-leader.md",
        "title": "25 Ways to be a Servant Leader",
        "speaker": "Cindy Hawks",
        "date": "2026-02-25",
        "url": "https://www.youtube.com/watch?v=apJIZ8QYT_E",
        "prompt": "Biblical Manhood. Speaker Cindy Hawks. Servant leader.",
    },
    {
        "num": "17",
        "slug": "17-a-man-and-his-wife-part-2",
        "md": "17-a-man-and-his-wife-p2.md",
        "title": "A Man and His Wife - Part 2",
        "speaker": "Tim Hawks",
        "date": "2026-03-04",
        "url": "https://www.youtube.com/watch?v=T4VCs8hIarg",
        "prompt": "Biblical Manhood. Speaker Tim Hawks. Helper. Complementarian.",
    },
    {
        "num": "18",
        "slug": "18-a-man-and-his-sexuality",
        "md": "18-a-man-and-his-sexuality.md",
        "title": "A Man and His Sexuality",
        "speaker": "Tim Hawks",
        "date": "2026-03-11",
        "url": "https://www.youtube.com/watch?v=KS3dzdmW_tU",
        "prompt": "Biblical Manhood. Speaker Tim Hawks. Sexuality. Marriage.",
    },
    {
        "num": "24",
        "slug": "24-final-session-bold-action",
        "md": "24-final-session-bold-action.md",
        "title": "Final Session: Bold Action",
        "speaker": "Host",
        "date": "2026-04-29",
        "url": "https://www.youtube.com/watch?v=4b6q9go_0eE",
        "prompt": "Biblical Manhood final session. Man cards. Man creed. Christ is my leader.",
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


def group_paragraphs(segs: list[dict], gap: float = 1.6, max_chars: int = 900) -> list[str]:
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
        if buf and buf_len > 260 and buf[-1].endswith((".", "?", "!")) and (s["start"] - buf_end) >= 0.5:
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


def pick_audio(slug: str) -> Path:
    webm = HQ / f"{slug}.webm"
    mp3 = AUDIO / f"{slug}.mp3"
    # Prefer opus webm (source). 192k mp3 is a transcode of the same.
    if webm.exists() and webm.stat().st_size > 1_000_000:
        return webm
    if mp3.exists() and mp3.stat().st_size > 1_000_000:
        return mp3
    raise FileNotFoundError(slug)


def transcribe_session(model: WhisperModel, sess: dict) -> int:
    slug = sess["slug"]
    src = pick_audio(slug)
    log(f"=== session {sess['num']} src={src} model={MODEL_NAME} ===")
    t0 = time.time()
    segments, info = model.transcribe(
        str(src),
        language="en",
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(
            min_silence_duration_ms=350,
            speech_pad_ms=500,
            threshold=0.35,
        ),
        condition_on_previous_text=True,
        temperature=0.0,
        log_prob_threshold=-1.6,
        no_speech_threshold=0.75,
        initial_prompt=sess["prompt"],
    )
    segs = []
    n = 0
    for s in segments:
        rec = {
            "start": round(float(s.start), 3),
            "end": round(float(s.end), 3),
            "text": light_fix(s.text),
            "avg_logprob": round(float(s.avg_logprob), 4) if s.avg_logprob is not None else None,
            "no_speech_prob": round(float(s.no_speech_prob), 4) if s.no_speech_prob is not None else None,
        }
        if rec["text"]:
            segs.append(rec)
            n += 1
            if n % 25 == 0:
                log(f"  {n} segs t={rec['end']:.0f}s lp={rec['avg_logprob']} :: {rec['text'][:80]}")
    dt = time.time() - t0
    log(f"  done n={n} dur={info.duration:.1f}s wall={dt:.0f}s span={segs[0]['start'] if segs else 0:.1f}->{segs[-1]['end'] if segs else 0:.1f}")

    paras = group_paragraphs(segs)
    speaker = sess["speaker"]
    num = sess["num"]
    title = sess["title"]
    dur = info.duration
    words_body = " ".join(paras)
    wpm = (len(words_body.split()) / (dur / 60.0)) if dur else 0
    header = [
        f"# {num}. {title}",
        "",
        f"Speaker: {speaker}",
        f"Date: {sess['date']}",
        f"YouTube: {sess['url']}",
        f"Source: faster-whisper {MODEL_NAME} from YouTube opus/251 audio (192k mp3 kept). YouTube timedtext was compressed ASR.",
        f"Audio duration: {dur:.0f}s. Segments: {len(segs)}. Approx {wpm:.0f} wpm. Speech is ASR, not invented.",
        "Note: medium.en on this audio dropped most speech; small.en retained intelligible lecture text.",
        "",
        f"{speaker}:",
        "",
    ]
    body = "\n\n".join(paras) + "\n"
    md_path = TR / sess["md"]
    md_path.write_text("\n".join(header) + body, encoding="utf-8")
    words = len(body.split())

    raw_dir = RAW / slug
    raw_dir.mkdir(parents=True, exist_ok=True)
    with (raw_dir / "segments.jsonl").open("w", encoding="utf-8") as f:
        for s in segs:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    txt_lines = [f"[{fmt_ts(s['start'])} --> {fmt_ts(s['end'])}] {s['text']}" for s in segs]
    (raw_dir / "timed.txt").write_text("\n".join(txt_lines) + "\n", encoding="utf-8")
    (TR / f"{num}.txt").write_text(body, encoding="utf-8")
    vtt = ["WEBVTT", "", f"NOTE faster-whisper {MODEL_NAME} {slug} duration={dur:.1f}s", ""]
    for s in segs:
        vtt.append(f"{fmt_ts(s['start'])} --> {fmt_ts(s['end'])}")
        vtt.append(s["text"])
        vtt.append("")
    (TR / f"{num}.vtt").write_text("\n".join(vtt), encoding="utf-8")
    log(f"WROTE {md_path} words={words} paras={len(paras)} segs={len(segs)} wpm={wpm:.1f}")
    return words


def main() -> int:
    only = sys.argv[1:]
    sessions = SESSIONS
    if only:
        sessions = [s for s in SESSIONS if s["num"] in only or s["slug"] in only]
    threads = int(os.environ.get("WHISPER_THREADS", "6"))
    log(f"Loading {MODEL_NAME} cpu int8 threads={threads}")
    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8", cpu_threads=threads)
    log("model ready")
    summary = []
    for sess in sessions:
        w = transcribe_session(model, sess)
        summary.append((sess["num"], w))
    log("SUMMARY " + " ".join(f"{n}:{w}" for n, w in summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
