#!/usr/bin/env python3
"""Set a v2 script's Wardrobe header row from production/WARDROBE.md. Usage: set_wardrobe.py FILE..."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.join(HERE, "..", "..", "..", "production", "WARDROBE.md")
rows = {}
for line in open(W):
    m = re.match(r"\| (E\d{3}) \|[^|]*\|[^|]*\| ([^|]*) \| ([^|]*) \| ([^|]*)\|", line)
    if m: rows[m.group(1)] = (m.group(2).strip(), m.group(3).strip(), m.group(4).strip())
for f in sys.argv[1:]:
    ep = os.path.basename(f)[:4]; w, j, n = rows[ep]
    val = f"Wes: {w}. Jonathon: {j}." + (f" Note: {n}" if n else "")
    s = open(f).read()
    s2 = re.sub(r"^\| Wardrobe \(production only\) \|.*\|$", f"| Wardrobe (production only) | {val} |", s, count=1, flags=re.M)
    open(f, "w").write(s2); print(ep, "changed" if s2 != s else "same", "|", val)
