#!/usr/bin/env python3
"""Run the binder's own markdown parser (parse_md / parse_closer_sections, lifted from
book/tools/make_ebook_pdf.py by AST so reportlab is not needed) over the rewrite folder.

Reports, per chapter: parsed number and title, block counts, margin cites, closer sections,
and anything the binder would mis-handle (no cite, CHAPTER 0, missing closer section,
Carry this with write-in lines).
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
BOOK = HERE.parents[2] / "book"
BINDER = HERE.parents[3] / "tools" / "make_ebook_pdf.py"

WANTED = {"no_em", "clean_inline_md", "_match_closer_label", "parse_closer_sections", "parse_md"}
src = BINDER.read_text(encoding="utf-8")
tree = ast.parse(src)
ns: dict = {"re": re, "Path": Path}
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name in WANTED:
        exec(compile(ast.Module([node], []), str(BINDER), "exec"), ns)
    elif isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id in ("CLOSER_LABELS", "CHAPTER_FILES", "PARTS") for t in node.targets
    ):
        exec(compile(ast.Module([node], []), str(BINDER), "exec"), ns)

problems = 0
for fname in ["00-introduction.md", *ns["CHAPTER_FILES"]]:
    p = BOOK / fname
    if not p.exists():
        print(f"{fname}: MISSING")
        problems += 1
        continue
    title, num, blocks = ns["parse_md"](p)
    kinds: dict[str, int] = {}
    for b in blocks:
        kinds[b["type"]] = kinds.get(b["type"], 0) + 1
    msgs = []
    for b in blocks:
        if b["type"] == "margin" and not b["cite"]:
            msgs.append(f"margin with no cite: {b['text'][:40]!r}")
    closer = [b for b in blocks if b["type"] == "closer"]
    if fname != "00-introduction.md":
        if num == 0:
            msgs.append("CHAPTER 0")
        if not closer:
            msgs.append("no closer")
        else:
            secs = ns["parse_closer_sections"](closer[0]["lines"])
            keys = [s["key"] for s in secs]
            want = ["name it", "do this week", "be a brother" if num == 35 else "tell a brother", "carry this"]
            if keys != want:
                msgs.append(f"closer sections {keys}")
            for s in secs:
                if s["key"] == "carry this" and s["write_in"]:
                    msgs.append("carry this has write-in")
                if s["key"] != "carry this" and not s["write_in"]:
                    msgs.append(f"{s['key']} has no write-in lines")
    elif closer:
        msgs.append("intro parsed a closer (would drop text)")
    problems += len(msgs)
    print(f"{fname}: #{num} {title!r} {kinds} {'OK' if not msgs else '; '.join(msgs)}")
print(f"problems: {problems}")
sys.exit(1 if problems else 0)
