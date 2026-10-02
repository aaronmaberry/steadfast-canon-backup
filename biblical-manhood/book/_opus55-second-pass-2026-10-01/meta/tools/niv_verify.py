#!/usr/bin/env python3
"""Verify every :::margin block in book/ against the NIV (2011) text on Bible Gateway, raw.

Second-pass rule (Aaron, 2026-10-01; SECOND-PASS-BRIEF L2): each block reproduces the NIV
word for word and punctuation for punctuation, including the NIV's own em dashes. The one
allowance: a dangling quotation mark at the very start or end of a block, belonging to speech
that opens or closes outside the cited verses, may be dropped. Marks are never added, and
nested single quotes stay single.

Comparison is raw except for two typographic normalizations, both applied to the NIV side:
- curly quotes become straight quotes (the manuscript uses straight quotes throughout);
- whitespace around an em dash is closed up. Bible Gateway and BibleHub both show a space
  after a dash only where a verse number follows (e.g. Eph 2:8 "God— 9 not"); the NIV closes
  its em dashes in running text ("faith—and").

Statuses:
  EXACT                 identical to the cited verses
  EXACT-EDGE-DROP (...) identical after dropping the named dangling edge mark(s)
  EXCERPT (...)         a contiguous word-for-word part of the cited verses (edge drops noted)
  MISMATCH              anything else; with --propose, prints the NIV text the block should carry

Usage: python3 niv_verify.py [--propose] > report.tsv
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
        except Exception:
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
    chunk = re.sub(r"<span[^>]*small-caps[^>]*>(.*?)</span>", lambda m: m.group(1).upper(), chunk)
    chunk = re.sub(r"<div class='il-text'>.*", "", chunk, flags=re.S)
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    chunk = html.unescape(chunk).replace("passage-text\">", " ")
    chunk = re.sub(r"\s+", " ", chunk).strip()
    chunk = re.sub(r"\s+([,.;:!?\u2019\u201d])", r"\1", chunk)
    chunk = re.sub(r"([\u2018\u201c])\s+", r"\1", chunk)
    chunk = re.sub(r"\s*\u2014\s*", "\u2014", chunk)
    chunk = re.sub(r"^[\u05d0-\u05ea]\s+\w+\s+", "", chunk)  # Psalm 119 acrostic heading (e.g. "נ Nun")
    return chunk


def straight(s: str) -> str:
    return s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')


def dangling_edges(s: str) -> list[str]:
    """Names of dangling quote marks at the very start/end of curly text s."""
    stack, unmatched_close = [], []
    for i, ch in enumerate(s):
        if ch == "\u201c":
            stack.append(i)
        elif ch == "\u201d":
            if stack:
                stack.pop()
            else:
                unmatched_close.append(i)
    sstack, s_unmatched_close = [], []
    for i, ch in enumerate(s):
        prev_alpha = i > 0 and s[i - 1].isalpha()
        next_alpha = i + 1 < len(s) and s[i + 1].isalpha()
        if ch == "\u2018":
            sstack.append(i)
        elif ch == "\u2019" and not (prev_alpha and next_alpha):
            if sstack:
                sstack.pop()
            elif not (prev_alpha and s[i - 1] == "s"):
                s_unmatched_close.append(i)
    out = []
    lead = len(s) - len(s.lstrip())
    i = lead
    while i < len(s) and s[i] in "\u201c\u2018":
        if (s[i] == "\u201c" and i in stack) or (s[i] == "\u2018" and i in sstack):
            out.append(f"lead {'double' if s[i] == chr(0x201c) else 'single'} open")
        i += 1
    j = len(s.rstrip()) - 1
    while j >= 0 and s[j] in "\u201d\u2019":
        if (s[j] == "\u201d" and j in unmatched_close) or (s[j] == "\u2019" and j in s_unmatched_close):
            out.append(f"trail {'double' if s[j] == chr(0x201d) else 'single'} close")
        j -= 1
    return out


def drop_edges(s: str) -> tuple[str, list[str]]:
    names = dangling_edges(s)
    t = s
    for n in names:
        if n.startswith("lead"):
            t = t[1:] if t[:1] in "\u201c\u2018" else t
        else:
            t = t[:-1] if t[-1:] in "\u201d\u2019" else t
    # second round for stacked marks (e.g. a double and a single at the same edge)
    return t, names


WORD = re.compile(r"[A-Za-z0-9]+(?:['\u2019][A-Za-z]+)?")


def wordseq(s: str) -> list[str]:
    return [w.lower().replace("\u2019", "'") for w in WORD.findall(s)]


def excerpt_span(niv: str, body: str) -> str | None:
    """Raw NIV substring covering the same words as body (with adjacent punctuation)."""
    toks = list(WORD.finditer(niv))
    nw = [t.group(0).lower().replace("\u2019", "'") for t in toks]
    bw = wordseq(body)
    for i in range(len(nw) - len(bw) + 1):
        if nw[i:i + len(bw)] == bw:
            a = toks[i].start()
            while a > 0 and niv[a - 1] in "\u201c\u2018":
                a -= 1
            b = toks[i + len(bw) - 1].end()
            while b < len(niv) and niv[b] not in " ":
                b += 1
            return niv[a:b]
    return None


def expand(ref: str) -> list[str]:
    m = re.match(r"^(.+?) (\d+):(\d+)(?:-(\d+))?$", ref)
    if not m:
        return [ref]
    book, ch, a, b = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
    b = int(b) if b else a
    return [f"{book} {ch}:{v}" for v in range(a, b + 1)]


# Blocks whose edge marks belong to speech that opens before / closes after the cited verses
# even though the marks happen to pair up inside the excerpt (NIV paragraph-continuation marks).
CONTINUATION = {
    "Numbers 6:24-26": (1, 1, "lead double and single continuation marks of the LORD's and Moses' speech (vv. 22-23), trail single close of the same; the blessing's own double quotes kept"),
}


def classify(niv: str, body: str, ref: str = "") -> tuple[str, str]:
    """Return (status, the NIV text the block should carry)."""
    body = body.strip()
    if ref in CONTINUATION:
        lead_extra, trail_extra, note = CONTINUATION[ref]
        d, names = drop_edges(niv)
        d = d[lead_extra:]
        d = d[: len(d) - trail_extra] if trail_extra else d
        target = straight(d)
        return ("EXACT-EDGE-DROP (" + note + ")" if target == body else "MISMATCH"), target
    if straight(niv) == body:
        return "EXACT", straight(niv)
    dropped, names = drop_edges(niv)
    if names and straight(dropped) == body:
        return f"EXACT-EDGE-DROP ({', '.join(names)})", straight(dropped)
    if wordseq(niv) != wordseq(body):
        span = excerpt_span(niv, body)
        if span is not None:
            sd, snames = drop_edges(span)
            target = straight(sd)
            label = "EXCERPT" + (f" ({', '.join(snames)})" if snames else "")
            return (label if target == body else "MISMATCH " + label), target
    target = straight(dropped)
    return "MISMATCH", target


def main() -> None:
    propose = "--propose" in sys.argv
    unique: dict[str, list[str]] = {}
    n = 0
    for p in sorted(BOOK.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        for line_no, ref_line, body in margin_blocks(text):
            ref = re.sub(r"\s+NIV$", "", ref_line.strip().strip("*").strip())
            niv = passage_text(fetch(ref))
            status, target = classify(niv, body, ref)
            n += 1
            for v in expand(ref):
                unique.setdefault(v, []).append(p.name)
            row = [p.name, str(line_no), ref, status, body]
            if propose and status.startswith("MISMATCH"):
                row.append(target)
            print("\t".join(row))
    print(f"#blocks\t{n}")
    print(f"#unique_verses\t{len(unique)}")
    json.dump(unique, open("/tmp/niv-unique.json", "w"), indent=1)


if __name__ == "__main__":
    main()
