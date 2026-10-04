#!/usr/bin/env python3
"""Local ASR for class-tape ingest. No paid API. Do not invent speech."""
from __future__ import annotations

import sys
from pathlib import Path


def write_md(md: Path, source: str, duration: str, body: str, engine: str) -> None:
    md.write_text(
        "\n".join(
            [
                f"# {Path(source).stem}",
                "",
                "Internal class tape. No publish. Original only for downstream. Do not rewrite the book from this file.",
                "",
                f"- Source: `{source}`",
                f"- Duration (seconds): {duration}",
                f"- ASR: {engine}",
                "",
                "## Transcript",
                "",
                body.strip() or "[unclear] empty ASR output. Do not invent speech.",
                "",
            ]
        )
        + "\n"
    )


def transcribe_faster(wav: Path) -> str:
    from faster_whisper import WhisperModel

    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(wav), language="en", vad_filter=True)
    lines = []
    for seg in segments:
        text = (seg.text or "").strip()
        if text:
            lines.append(text)
    if not lines:
        raise RuntimeError("faster-whisper produced no segments")
    return "\n\n".join(lines)


def transcribe_openai(wav: Path) -> str:
    import whisper

    model = whisper.load_model("base")
    result = model.transcribe(str(wav), language="en")
    text = (result.get("text") or "").strip()
    if not text:
        raise RuntimeError("openai-whisper produced no text")
    return text


def main() -> int:
    if len(sys.argv) < 4:
        print("usage: ingest_transcribe.py WAV MD SOURCE DURATION", file=sys.stderr)
        return 2
    wav = Path(sys.argv[1])
    md = Path(sys.argv[2])
    source = sys.argv[3]
    duration = sys.argv[4]
    if not wav.is_file():
        print(f"missing wav {wav}", file=sys.stderr)
        return 2

    errors = []
    for name, fn in (("faster-whisper", transcribe_faster), ("openai-whisper", transcribe_openai)):
        try:
            body = fn(wav)
            write_md(md, source, duration, body, name)
            print(f"transcript via {name}: {md}")
            return 0
        except Exception as exc:  # noqa: BLE001 — try next engine
            errors.append(f"{name}: {exc}")
            print(errors[-1], file=sys.stderr)

    print("ASR failed. Not inventing a transcript.", file=sys.stderr)
    for line in errors:
        print(line, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
