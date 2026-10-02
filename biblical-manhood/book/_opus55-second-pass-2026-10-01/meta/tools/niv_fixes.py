#!/usr/bin/env python3
"""Apply the second-pass NIV fixes (SECOND-PASS-BRIEF L2) to book/.

Every replacement text is taken from the fetched NIV, never typed by hand:
- MISMATCH blocks get the NIV wording for their cited verses, with only dangling edge marks dropped.
- Four blocks are re-cut so the excerpt does not open or close inside speech (no marks are ever added):
    Judges 7:17      -> Judges 7:17-18 (Gideon's speech closes at the end of v18)
    Luke 15:20       -> starts at "But while" (the NIV's paragraph-continuation mark at the edge drops)
    Habakkuk 2:2     -> starts at "Write down" (the speech's opening mark at the edge drops)
    John 14:9        -> starts at "Don't you know me" (same)
Prints a before/after log.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from checks import BOOK, margin_blocks  # noqa: E402
from niv_verify import classify, drop_edges, fetch, passage_text, straight  # noqa: E402

RECUT = {
    "Judges 7:17": ("Judges 7:17-18", None),
    "Luke 15:20": ("Luke 15:20", "\u201cBut while"),
    "Habakkuk 2:2": ("Habakkuk 2:2", "\u201cWrite down"),
    "John 14:9": ("John 14:9", "\u201cDon\u2019t you know me"),
}


def main() -> None:
    for p in sorted(BOOK.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        new = text
        for _ln, ref_line, body in margin_blocks(text):
            ref = ref_line.strip().strip("*").strip().removesuffix(" NIV").strip()
            if ref in RECUT:
                new_ref, start = RECUT[ref]
                niv = passage_text(fetch(new_ref))
                if start:
                    i = niv.find(start)
                    assert i >= 0, (ref, start)
                    niv = niv[i:]
                target = straight(drop_edges(niv)[0])
                new_ref_line = f"**{new_ref} NIV**"
            else:
                niv = passage_text(fetch(ref))
                status, target = classify(niv, body, ref)
                if not status.startswith("MISMATCH"):
                    continue
                new_ref_line = ref_line.strip()
            if target == body and new_ref_line == ref_line.strip():
                continue
            old_block = f"{ref_line}\n{body}\n"
            assert old_block in new, (p.name, ref)
            new = new.replace(old_block, f"{new_ref_line}\n{target}\n", 1)
            print(f"{p.name}\t{ref} -> {new_ref_line.strip('*')}\n  OLD: {body}\n  NEW: {target}")
        if new != text:
            p.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
