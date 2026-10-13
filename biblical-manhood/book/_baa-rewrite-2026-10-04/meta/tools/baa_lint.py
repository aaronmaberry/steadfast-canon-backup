#!/usr/bin/env python3
"""B-A-A rewrite lint (2026-10-04). Usage: baa_lint.py [files...]  (default: every chapter in ../../book)"""
import re, sys, json
from pathlib import Path
sys.path.insert(0, "/workspace/biblical-manhood/book/_opus55-second-pass-2026-10-01/meta/tools")
from checks import SWEEP_RE, EXTRA_RE, CREED_RE  # noqa
ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "book"
SLOP = re.compile(r"\b(additionally|crucial|delve|enduring|enhance|fostering|garner|interplay|intricate|pivotal|showcase|tapestry|testament to|underscore|vibrant|serves as|stands as|boasts|let's dive|if that sounds heavy|weeknights?)\b", re.I)
CHREF = re.compile(r"\b(chapter|ch\.?)\s+\d+|\b(next|last|previous|earlier|later) chapter\b|\bchapter (seven|eight|nine|ten|eleven|twelve|three|four|five|six|one|two)\b|\bin Part (One|Two|Three|Four|Five)\b", re.I)
PROSEREF = re.compile(r"\b(Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|Samuel|Kings|Chronicles|Nehemiah|Esther|Job|Psalms?|Proverbs|Ecclesiastes|Isaiah|Jeremiah|Ezekiel|Daniel|Hosea|Amos|Micah|Habakkuk|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|Corinthians|Galatians|Ephesians|Philippians|Colossians|Thessalonians|Timothy|Titus|Hebrews|James|Peter|Jude|Revelation)\s+\d+:\d+")
PROTECT = json.loads((Path(__file__).parent / "protected.json").read_text()) if (Path(__file__).parent / "protected.json").exists() else {}

def lint(p: Path) -> dict:
    raw = p.read_text()
    lines = raw.splitlines()
    out = {"file": p.name, "issues": []}
    I = out["issues"]
    m = re.match(r"^# (\d+)\. (.+)$", lines[0]) if lines else None
    num = int(m.group(1)) if m else 0
    # epigraph
    ep = re.search(r":::epigraph\n(.+?)\n(.+?)\n:::", raw)
    if not ep: I.append("no :::epigraph block")
    body = re.sub(r":::epigraph\n.*?\n:::", "", raw, flags=re.S)
    body = "\n".join(body.splitlines()[1:])
    breaks = body.count(":::break")
    prose = re.sub(r":::break\n:::", "", body)
    paras = [x.strip() for x in re.split(r"\n\s*\n", prose) if x.strip()]
    words = [len(re.findall(r"[A-Za-z0-9'’]+", x)) for x in paras]
    out.update(words=sum(words), paras=len(paras), avg=round(sum(words) / max(1, len(paras))), short=sum(1 for w in words if w <= 25), breaks=breaks)
    if not 2 <= breaks <= 4 and num: I.append(f"breaks={breaks} (want 2-4)")
    for i, x in enumerate(paras):
        tag = f"p{i+1}"
        if x.startswith("#"): I.append(f"{tag} heading: {x[:50]}")
        if "**" in x or "__" in x: I.append(f"{tag} bold")
        if x.startswith(":::"): I.append(f"{tag} stray fence {x[:30]}")
        if re.search("[\u2014\u2013]", x): I.append(f"{tag} dash")
        if re.search(r"[\u201c\u201d\u2018\u2019]", x): I.append(f"{tag} curly quote")
        for c in re.finditer(r"\w:\s+\S", x): I.append(f"{tag} colon: ...{x[max(0,c.start()-30):c.end()+20]}...")
        for rx, name in ((SWEEP_RE, "SWEEP"), (EXTRA_RE, "EXTRA"), (SLOP, "SLOP"), (CHREF, "CHREF"), (PROSEREF, "VERSEREF")):
            for h in rx.finditer(x): I.append(f"{tag} {name}: {h.group(0)}")
        if re.match(r"^(Name it|Do this week|Tell a brother|Be a brother|Carry this)\b", x, re.I): I.append(f"{tag} closer label")
        if re.search(r"Before you (turn|close)", x): I.append(f"{tag} before-you-turn")
        if re.match(r"^\s*(\d+\.|[-*])\s", x): I.append(f"{tag} list item")
    out["creed"] = len(CREED_RE.findall(raw))
    for s in PROTECT.get(str(num), []):
        norm = lambda t: re.sub(r"\s+", " ", t.replace("’", "'"))
        if norm(s).lower() not in norm(raw).lower(): I.append(f"PROTECTED missing: {s}")
    out["last"] = paras[-1][-140:] if paras else ""
    return out

if __name__ == "__main__":
    fs = [Path(a) for a in sys.argv[1:]] or sorted(p for p in BOOK.glob("[0-2][0-9]-*.md") if not p.name.startswith("00-c"))
    tot = 0
    for f in fs:
        r = lint(f); tot += r["words"]
        print(f"{r['file']}: words={r['words']} paras={r['paras']} avg={r['avg']} short<=25={r['short']} breaks={r['breaks']} creed={r['creed']}")
        for i in r["issues"]: print("   !", i)
        print("   last:", r["last"])
    print("TOTAL", tot)
