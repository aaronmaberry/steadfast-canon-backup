#!/usr/bin/env python3
"""Verify every :::margin block in book/ against the NIV (2011) text on Bible Gateway.

Fetches each passage once (cached under /tmp/niv-cache, not in the repo), compares the
word sequence, and reports punctuation-only differences separately. Also expands ranges
to count unique verses.

Usage: python3 niv_verify.py [--book DIR] [--fix] > report.tsv
  --book DIR  verify DIR/*.md instead of the sibling book/ folder
  --fix       rewrite margin text to the fetched NIV wording, punctuation for punctuation
              (curly quotes straightened; the NIV's own em dashes are KEPT, per Aaron's
              2026-10-01 lock). The only allowed change is dropping a dangling speech mark
              at an excerpt edge. Marks are never added and nested quotes keep the NIV's levels.

Statuses: EXACT, EXACT-EDGE-DROP (identical except a dangling edge quote mark was dropped),
EXCERPT-OK, WORDS-OK punct-diff (fix needed), MISMATCH (fix needed).
2026-10-01 box patch: house_style() no longer turns dashes into commas.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from checks import BOOK, margin_blocks  # noqa: E402

CACHE = Path("/tmp/niv-cache")
CACHE.mkdir(exist_ok=True)


def fetch(ref: str) -> str:
    key = hashlib.sha1(ref.encode()).hexdigest()
    cp = CACHE / f"{key}.html"
    if cp.exists():
        return cp.read_text(encoding="utf-8")
    url = "https://www.biblegateway.com/passage/?" + urllib.parse.urlencode(
        {"search": ref, "version": "NIV", "interface": "print"}
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                t = r.read().decode("utf-8", errors="ignore")
            cp.write_text(t, encoding="utf-8")
            time.sleep(0.4)
            return t
        except Exception:  # network retry
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError(f"fetch failed: {ref}")


def passage_text(page: str) -> str:
    start = page.find("passage-text")
    end = page.find('class="full-chap-link"', start)
    if end == -1:
        end = page.find("crossrefs", start)
    chunk = page[start:end]
    chunk = re.sub(r"<h3.*?</h3>", " ", chunk, flags=re.S)
    chunk = re.sub(r"<sup[^>]*class=['\"](crossreference|footnote)['\"].*?</sup>", "", chunk, flags=re.S)
    chunk = re.sub(r"<sup class=\"versenum\">.*?</sup>", " ", chunk, flags=re.S)
    chunk = re.sub(r"<span class=\"chapternum\">.*?</span>", " ", chunk, flags=re.S)
    chunk = re.sub(r"<span style=\"font-variant: small-caps\" class=\"small-caps\">Lord</span>", "LORD", chunk)
    chunk = re.sub(r"<span[^>]*small-caps[^>]*>(.*?)</span>", lambda m: m.group(1).upper(), chunk)
    chunk = re.sub(r"<div class='il-text'>.*", "", chunk, flags=re.S)
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    chunk = html.unescape(chunk)
    chunk = chunk.replace("passage-text\">", " ")
    chunk = re.sub(r"\s+", " ", chunk).strip()
    chunk = re.sub(r"\s+([,.;:!?\u2019\u201d])", r"\1", chunk)
    chunk = re.sub(r"([\u2018\u201c])\s+", r"\1", chunk)
    # NIV em dashes are closed. A space next to one is only where a verse number was
    # stripped (e.g. Eph 2:8-9 "gift of God\u2014 9 not by works"), so close it up.
    chunk = re.sub(r"\s*\u2014\s*", "\u2014", chunk)
    # Psalm 119 acrostic section heading (e.g. "\u05e0 Nun") is not verse text.
    chunk = re.sub(r"^[\u05d0-\u05ea]\s+\w+\s+", "", chunk)
    return chunk


def normalize_quotes(s: str) -> str:
    return s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')


def house_style(s: str) -> str:
    """Straight quotes only. Em dashes stay exactly as the NIV prints them (Aaron, 2026-10-01).
    Prose outside :::margin blocks stays dash-free; that rule is enforced elsewhere."""
    return normalize_quotes(s).strip()


def _drop_dangling_edges(s: str) -> str:
    """Drop a dangling double quote mark at an excerpt edge. Never add a mark.

    Works on the NIV's curly marks, where \u201c opens and \u201d closes. Only an unmatched
    opener that is the very first character (the speech closes after the cited verses) or an
    unmatched closer that is the very last character (the speech opened before them) is dropped.
    Every other mark, including unmatched ones mid-text, prints as the NIV has it."""
    s = s.strip()
    # NIV nested continuation marks, e.g. Num 6:24 opens with a run like \u201c\u2018\u201c: the
    # leading marks before the last one continue speeches that opened earlier, and the trailing
    # closers after the first one close those outer speeches. Both are edge marks; drop them.
    lead = re.match(r"^[\u201c\u2018]{2,}", s)
    if lead:
        keep = lead.group(0)[-1]
        s = keep + s[lead.end():]
        close = "\u201d" if keep == "\u201c" else "\u2019"
        trail = re.search(r"[\u201d\u2019]{2,}$", s)
        if trail and trail.group(0)[0] == close:
            s = s[: trail.start()] + close
        return s.strip()
    stack: list[int] = []
    unmatched_close: list[int] = []
    for i, ch in enumerate(s):
        if ch == "\u201c":
            stack.append(i)
        elif ch == "\u201d":
            if stack:
                stack.pop()
            else:
                unmatched_close.append(i)
    drop = set()
    if stack and stack[0] == 0:
        drop.add(0)
    if unmatched_close and unmatched_close[-1] == len(s) - 1:
        drop.add(len(s) - 1)
    if drop:
        s = "".join(ch for i, ch in enumerate(s) if i not in drop).strip()
    return s


def canonical(niv: str) -> str:
    """NIV wording, punctuation for punctuation, straight quotes, with only the edge-drop
    allowance. Nested single quotes are left at the NIV's level (never raised to double)."""
    return house_style(_drop_dangling_edges(niv))


WORD = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?")


def wordseq(s: str) -> list[str]:
    return [w.lower() for w in WORD.findall(normalize_quotes(s))]


BOOKS_ONE_CHAPTER = {"Jude", "Philemon", "Obadiah", "2 John", "3 John"}


def expand(ref: str) -> list[str]:
    m = re.match(r"^(.+?) (\d+):(\d+)(?:-(\d+))?$", ref)
    if not m:
        return [ref]
    book, ch, a, b = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
    b = int(b) if b else a
    return [f"{book} {ch}:{v}" for v in range(a, b + 1)]


def main() -> None:
    global BOOK
    fix = "--fix" in sys.argv
    if "--book" in sys.argv:
        BOOK = Path(sys.argv[sys.argv.index("--book") + 1])
    rows = []
    unique: dict[str, list[str]] = {}
    for p in sorted(BOOK.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        new_text = text
        for line_no, ref_line, body in margin_blocks(text):
            ref = ref_line.strip().strip("*").strip()
            ref = re.sub(r"\s+NIV$", "", ref)
            niv = passage_text(fetch(ref))
            nw, bw = wordseq(niv), wordseq(body)
            ok_words = nw == bw
            partial = (not ok_words) and len(bw) > 3 and any(
                nw[i : i + len(bw)] == bw for i in range(len(nw) - len(bw) + 1)
            )
            niv_house = canonical(niv)
            raw = house_style(niv)
            if normalize_quotes(body) == raw:
                status = "EXACT"
            elif normalize_quotes(body) == niv_house:
                status = "EXACT-EDGE-DROP"
            elif ok_words:
                status = "WORDS-OK punct-diff"
            elif partial:
                status = "EXCERPT-OK (contiguous part of the cited verses)"
            else:
                status = "MISMATCH"
            rows.append((p.name, line_no, ref, status, body, niv_house))
            for v in expand(ref):
                unique.setdefault(v, []).append(p.name)
            if fix and (status.startswith("WORDS-OK") or status == "MISMATCH"):
                new_text = new_text.replace(f"{ref_line}\n{body}\n", f"{ref_line}\n{niv_house}\n", 1)
            elif fix and status.startswith("EXCERPT") and body != normalize_quotes(body):
                new_text = new_text.replace(f"{ref_line}\n{body}\n", f"{ref_line}\n{normalize_quotes(body)}\n", 1)
        if fix and new_text != text:
            p.write_text(new_text, encoding="utf-8")
    for r in rows:
        print("\t".join(str(x) for x in r))
    print(f"#blocks\t{len(rows)}")
    print(f"#unique_verses\t{len(unique)}")
    json.dump(unique, open("/tmp/niv-unique.json", "w"), indent=1)


if __name__ == "__main__":
    main()
