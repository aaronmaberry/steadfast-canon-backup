#!/usr/bin/env python3
"""Swap one swappable name everywhere. Dry run by default.
usage: swap_names.py KEY NEW_VALUE [--apply]
KEY is one of the keys in _build/names.json (show_name, jonathon_surname, wife, daughter, son).
Whole-word, case-sensitive. Possessives (Dani's) follow automatically. Tied forms of the show name
(domain, handle, hashtag) are NOT touched; change those by hand if the domain changes.
After --apply: names.json is updated and NAME-SWAP-INDEX.md is regenerated. Re-run lint and timing
(spoken length changes slightly)."""
import json, re, sys, pathlib, subprocess
root = pathlib.Path(__file__).resolve().parent.parent
cfgp = root/'_build/names.json'; cfg = json.load(open(cfgp))
if len(sys.argv) < 3 or sys.argv[1] not in cfg: sys.exit(__doc__)
key, new, apply = sys.argv[1], sys.argv[2], '--apply' in sys.argv
old = cfg[key]['value']
rx = re.compile(r"(?<![#\w])" + re.escape(old) + r"\b")
total = 0
for f in sorted(root.rglob('*.md')):
    if f.name == 'NAME-SWAP-INDEX.md': continue
    s = f.read_text(encoding='utf-8'); n = len(rx.findall(s))
    if n:
        total += n; print(f"{n:4d}  {f.relative_to(root)}")
        if apply: f.write_text(rx.sub(new, s), encoding='utf-8')
print(f"{total} occurrences of {old!r} -> {new!r}" + ("" if apply else "  (dry run; add --apply)"))
if apply:
    cfg[key]['value'] = new; json.dump(cfg, open(cfgp, 'w'), indent=2)
    subprocess.run([sys.executable, str(root/'_build/name_index.py')])
