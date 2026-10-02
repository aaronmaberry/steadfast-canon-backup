#!/usr/bin/env python3
"""Steadfast Men Opus 5.5 IP rewrite: manuscript checks.

Usage:
  python3 checks.py sweep  [files...]   banned-phrase sweep, creed count, mark mentions, format
  python3 checks.py sim    [files...]   word count + similarity vs the panel-rev base
  python3 checks.py ngram  [files...]   8-word overlap vs biblical-manhood/transcripts/*.md
  python3 checks.py margins [files...]  list every margin block (ref + text)

With no files, runs over every .md in the rewrite book/ folder.
"""
from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "book"
BASE = ROOT.parent / "_grok47-panel-rev-2026-09-25" / "book"
FIRST = ROOT.parent / "_opus55-ip-rewrite-2026-10-01" / "book"
TRANSCRIPTS = ROOT.parents[1] / "transcripts"

SWEEP_RE = re.compile(
    r"rejects? passivity|accepts? responsibility|leads? courageously|greater reward|God'?s reward|"
    r"invests? eternally|real man|Robert Lewis|\bLewis\b|Modern-Day Knight|Men'?s Fraternity|"
    r"Authentic Manhood|Fellowship Bible|Little Rock|Better Man|knight|squire",
    re.I,
)
# Extra fences from the brief (synonym rebuilds, triads, sub-points). Reported, not part of the
# brief's required-zero regex.
EXTRA_RE = re.compile(
    r"reject(s|ing|ed)? (the )?passiv|accept(s|ing|ed)? (the )?responsib|lead(s|ing)? with courage|"
    r"courageous(ly)? lead|expect(s|ing)? (the |a )?(greater |God'?s )?reward|invest(s|ing)? eternal|"
    r"refuses? inaction|embraces? duty|owns? responsibility|gave it to us|bearers? of destiny|"
    r"nurturers? of life|will to obey|woman to love|work to do, a|direction, protection|"
    r"protection, (and )?provision|conventional manhood|authentic man|page stage|\bsquires?\b|"
    r"manhood ceremony|three things every son|used under license|original to us|Go First (podcast|course|workbook)|"
    r"\bMead\b|Keillor|Newsweek|Levinson|\bgibbor\b|\bzaken\b|weeknight",
    re.I,
)
CREED_RE = re.compile(
    r"stops waiting,\s*picks up the weight,\s*goes first,\s*and works for God'?s pay,\s*not the room'?s",
    re.I,
)
MARKS = ["Stop Waiting", "Pick Up the Weight", "Go First", "Work for God's Pay"]
CLOSER_LABEL_RE = re.compile(r"^\*{0,2}(name it|do this week|tell a brother|be a brother|carry this)\b", re.I)
DASH_RE = re.compile("[\u2014\u2013]")
WORD_RE = re.compile(r"[A-Za-z0-9']+")


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def files_from(args: list[str], root: Path = BOOK) -> list[Path]:
    if args:
        return [Path(a) if Path(a).is_absolute() else root / a for a in args]
    return sorted(p for p in root.glob("*.md"))


def strip_margins(text: str) -> str:
    out, inside = [], False
    for ln in text.splitlines():
        if ln.startswith(":::margin"):
            inside = True
            continue
        if inside and ln.startswith(":::"):
            inside = False
            continue
        if not inside:
            out.append(ln)
    return "\n".join(out)


def margin_blocks(text: str) -> list[tuple[int, str, str]]:
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        if lines[i].startswith(":::margin"):
            start = i + 1
            j = i + 1
            body = []
            while j < len(lines) and not lines[j].startswith(":::"):
                body.append(lines[j])
                j += 1
            ref = body[0] if body else ""
            out.append((start + 1, ref, " ".join(b.strip() for b in body[1:] if b.strip())))
            i = j + 1
            continue
        i += 1
    return out


def format_problems(path: Path, text: str) -> list[str]:
    probs = []
    lines = text.splitlines()
    name = path.name
    numbered = re.match(r"^(\d\d)-", name) and name[:2] not in ("00", "36", "37")
    if numbered:
        if not re.match(rf"^# {int(name[:2])}\. \S", lines[0] if lines else ""):
            probs.append("line 1 is not '# N. Title'")
        if "## Your Turn" not in text:
            probs.append("missing ## Your Turn")
    # closer label at line start outside the closer
    in_closer = False
    for n, ln in enumerate(lines, 1):
        if re.match(r"^##\s+Your Turn\s*$", ln):
            in_closer = True
        if not in_closer and CLOSER_LABEL_RE.match(ln.strip()):
            probs.append(f"line {n}: prose line starts with a closer label")
    for n, ref, body in margin_blocks(text):
        if not re.match(r"^\*\*[1-3]? ?[A-Z][A-Za-z ]+ \d+:\d+(-\d+)?(, ?\d+(-\d+)?)? NIV\*\*$", ref.strip()):
            probs.append(f"line {n}: margin ref not '**Ref NIV**': {ref!r}")
    if in_closer:
        closer = text.split("## Your Turn", 1)[1]
        m = re.search(r"\*\*Carry this\*\*(.*)$", closer, re.S)
        if m and ":::notes" in m.group(1):
            probs.append("Carry this has a :::notes block")
        for lab in ("Name it", "Do this week"):
            if f"**{lab}**" not in closer:
                probs.append(f"closer missing **{lab}**")
        if "**Tell a brother**" not in closer and "**Be a brother**" not in closer:
            probs.append("closer missing **Tell a brother** / **Be a brother**")
        if "**Carry this**" not in closer:
            probs.append("closer missing **Carry this**")
    prose = strip_margins(text)
    if DASH_RE.search(prose):
        probs.append(f"{len(DASH_RE.findall(prose))} em/en dash(es) in prose (outside :::margin)")
    for n, ref, body in margin_blocks(text):
        if "\u2013" in body:
            probs.append(f"line {n}: en dash inside a margin block")
    return probs


def cmd_sweep(args: list[str]) -> None:
    total = 0
    for p in files_from(args):
        t = p.read_text(encoding="utf-8")
        hits = []
        for n, ln in enumerate(t.splitlines(), 1):
            for m in SWEEP_RE.finditer(ln):
                hits.append(f"  SWEEP L{n}: {m.group(0)!r}")
            for m in EXTRA_RE.finditer(ln):
                hits.append(f"  extra L{n}: {m.group(0)!r}")
        creed = len(CREED_RE.findall(t))
        marks = {mk: len(re.findall(re.escape(mk), t, re.I)) for mk in MARKS}
        fp = format_problems(p, t)
        total += sum(1 for h in hits if "SWEEP" in h)
        mk = ", ".join(f"{k}={v}" for k, v in marks.items() if v)
        print(f"{p.name}: words={len(words(t))} creed={creed} marks[{mk}]")
        for h in hits:
            print(h)
        for f in fp:
            print("  FORMAT", f)
    print(f"TOTAL brief-regex hits: {total}")


def cmd_sim(args: list[str]) -> None:
    for p in files_from(args):
        base = BASE / p.name
        new = words(p.read_text(encoding="utf-8").lower())
        if not base.exists():
            print(f"{p.name}: after={len(new)} (no base)")
            continue
        old_text = base.read_text(encoding="utf-8")
        old = words(old_text.lower())
        sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
        new_prose = words(strip_margins(p.read_text(encoding="utf-8")).lower())
        old_prose = words(strip_margins(old_text).lower())
        ng_new = [tuple(new_prose[i : i + 6]) for i in range(len(new_prose) - 5)]
        ng_old = ngrams(old_prose, 6)
        reuse = sum(1 for g in ng_new if g in ng_old) / max(1, len(ng_new))
        fp = FIRST / p.name
        fw = len(words(fp.read_text(encoding="utf-8"))) if fp.exists() else 0
        print(
            f"{p.name}: base={len(old)} first_pass={fw} now={len(new)} vs_first={len(new)-fw:+d} "
            f"sim_base={sm.ratio():.2f} prose6gram_reuse_base={reuse:.2f}"
        )


def ngrams(ws: list[str], n: int = 8) -> set[tuple[str, ...]]:
    return {tuple(ws[i : i + n]) for i in range(len(ws) - n + 1)}


def cmd_ngram(args: list[str]) -> None:
    trans = {}
    for tp in sorted(TRANSCRIPTS.glob("*.md")):
        trans[tp.name] = ngrams(words(tp.read_text(encoding="utf-8", errors="ignore").lower()))
    grand = {"scripture": 0, "other": 0}
    for p in files_from(args):
        t = p.read_text(encoding="utf-8")
        body_ws = words(strip_margins(t).lower())
        margin_ws = set()
        for _n, _r, b in margin_blocks(t):
            margin_ws |= ngrams(words(b.lower()))
        hits = []
        seen_runs = set()
        for i in range(len(body_ws) - 7):
            g = tuple(body_ws[i : i + 8])
            for tn, tg in trans.items():
                if g in tg:
                    hits.append((i, tn, g))
                    break
        for _n, _r, b in margin_blocks(t):
            mws = words(b.lower())
            for i in range(len(mws) - 7):
                g = tuple(mws[i : i + 8])
                for tn, tg in trans.items():
                    if g in tg:
                        key = ("m", g)
                        if key not in seen_runs:
                            seen_runs.add(key)
                            grand["scripture"] += 1
                        break
        # merge consecutive body hits into runs
        runs = []
        for i, tn, g in hits:
            if runs and i <= runs[-1][1] + 1 and runs[-1][2] == tn:
                runs[-1][1] = i
            else:
                runs.append([i, i, tn])
        for a, b, tn in runs:
            span = " ".join(body_ws[a : b + 8])
            kind = "scripture" if any(tuple(body_ws[k : k + 8]) in margin_ws for k in range(a, b + 1)) else "other"
            grand[kind] += 1
            print(f"{p.name}: [{kind}] \"{span}\" ({tn})")
    print(f"TOTAL runs: scripture-in-margin={grand['scripture']} body-matching-a-margin-verse/other={grand}")


def cmd_margins(args: list[str]) -> None:
    for p in files_from(args):
        for n, ref, body in margin_blocks(p.read_text(encoding="utf-8")):
            print(f"{p.name}\tL{n}\t{ref.strip('*').strip()}\t{body}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    {"sweep": cmd_sweep, "sim": cmd_sim, "ngram": cmd_ngram, "margins": cmd_margins}[sys.argv[1]](sys.argv[2:])
