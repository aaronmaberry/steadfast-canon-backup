#!/usr/bin/env python3
"""Present-tense plug sweep for E002-E080 (SHOW-BIBLE section 8a).

Dry run by default: prints every old -> new line and writes nothing.
Run with --apply only after Aaron says yes. E001 is excluded (its spoken
lines need new audio, see episodes/E001/QA.md).
"""
import glob, re, sys

RULES = [
    ("The training session that matches today, session fifteen, The Problem Inside, comes out this week.", "The training session that matches today is session fifteen, The Problem Inside."),
    ("The training session for this one comes out this week too. Session nineteen,", "There's a training session for this one too. Session nineteen,"),
    ("The training session that goes with today, session eleven, When Home Never Handed You Off, comes out this week.", "The training session that goes with today is session eleven, When Home Never Handed You Off."),
    (" The book's coming. When it's out, it'll be at walksteadfast.com.", " The book's at walksteadfast.com."),
    (" The book's coming. It'll be at walksteadfast.com.", " The book's at walksteadfast.com."),
    (" It's Steadfast Men, and it's coming. walksteadfast.com.", " It's Steadfast Men, at walksteadfast.com."),
    (" It's coming at walksteadfast.com.", " It's at walksteadfast.com."),
    (" is coming at walksteadfast.com.", " is at walksteadfast.com."),
    (" (coming), at walksteadfast.com", ", at walksteadfast.com"),
    (" (coming)", ""),
]

def main(apply):
    total = 0
    for p in sorted(glob.glob('scripts/E0[0-9][0-9]-*.md')):
        n = int(re.search(r'E(\d{3})', p).group(1))
        if n == 1:
            continue
        lines = open(p).read().split('\n')
        changed = False
        for i, line in enumerate(lines):
            new = line
            for a, b in RULES:
                new = new.replace(a, b)
            if new != line:
                total += 1
                changed = True
                print(f"E{n:03d}:{i+1}\n  OLD {line}\n  NEW {new}")
                lines[i] = new
        if apply and changed:
            open(p, 'w').write('\n'.join(lines))
    print(f"{total} lines {'changed' if apply else 'would change (dry run)'}")

if __name__ == '__main__':
    main('--apply' in sys.argv)
