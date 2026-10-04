#!/usr/bin/env python3
import pathlib, re

ROOT = pathlib.Path("/workspace/biblical-manhood")
EPS = [
    ("13-biblical-definition-of-manhood-p1", "1xtJgaOpmZ8", 2897, "Tim Hawks"),
    ("14-biblical-definition-of-manhood-p2", "a9P1EVOBbHE", 2952, "Tim Hawks"),
    ("15-a-man-and-his-wife-p1", "3Ps3ezdRO6Y", 2930, "Tim Hawks"),
    ("16-25-ways-to-be-a-servant-leader", "apJIZ8QYT_E", 3042, "Cindy Hawks"),
    ("17-a-man-and-his-wife-p2", "T4VCs8hIarg", 2936, "Tim Hawks"),
    ("18-a-man-and-his-sexuality", "KS3dzdmW_tU", 3016, "Tim Hawks"),
]

def hms(ms: int) -> str:
    if ms < 0:
        ms = 0
    h = ms // 3600000
    m = (ms % 3600000) // 60000
    s = (ms % 60000) // 1000
    milli = ms % 1000
    return f"{h:02d}:{m:02d}:{s:02d}.{milli:03d}"

def body_paragraphs(md: str):
    lines = md.splitlines()
    i = 0
    while i < len(lines) and (
        not lines[i].strip()
        or lines[i].startswith("#")
        or lines[i].startswith("Speaker:")
        or lines[i].startswith("Date:")
        or lines[i].startswith("Source:")
        or lines[i].startswith("YouTube:")
        or lines[i].startswith("Caption:")
    ):
        i += 1
    rest = "\n".join(lines[i:]).strip()
    paras = [p.strip() for p in re.split(r"\n\s*\n", rest) if p.strip()]
    return paras

def pack(slug, vid, duration_s, speaker):
    md_path = ROOT / "transcripts" / f"{slug}.md"
    text = md_path.read_text()
    paras = body_paragraphs(text)
    weights = [max(len(p), 1) for p in paras]
    total_w = sum(weights)
    duration_ms = duration_s * 1000
    # leave a tiny tail so last cue is not exactly duration if rounding
    cues = []
    t = 0
    acc = 0
    for idx, (p, w) in enumerate(zip(paras, weights)):
        acc += w
        end = int(round(duration_ms * acc / total_w))
        if idx == len(paras) - 1:
            end = duration_ms
        if end <= t:
            end = t + 400
        cues.append((t, end, p))
        t = end
    note = (
        "NOTE\n"
        f"video: https://www.youtube.com/watch?v={vid}\n"
        "kind: asr lang: en / en-orig\n"
        f"duration_s: {duration_s}\n"
        "ASR en-orig (no manual captions). Original YouTube cue times not recoverable: "
        "timedtext 429 from this host; WebFetch returned ASR text only.\n"
        "Cue timestamps below are proportional estimates from character counts vs video duration, "
        "not original YouTube times. Speech text is from YouTube ASR (cleaned of duplicate rolling cues)."
    )
    out = ["WEBVTT", "", note, ""]
    for n, (start, end, p) in enumerate(cues, 1):
        out.append(str(n))
        out.append(f"{hms(start)} --> {hms(end)}")
        out.append(p)
        out.append("")
    vtt_path = ROOT / "captions" / f"{slug}.en.vtt"
    vtt_path.write_text("\n".join(out) + "\n")
    return vtt_path, len(cues), vtt_path.stat().st_size

def main():
    for slug, vid, dur, speaker in EPS:
        path, n, size = pack(slug, vid, dur, speaker)
        print(f"{slug} cues={n} bytes={size}")

if __name__ == "__main__":
    main()
