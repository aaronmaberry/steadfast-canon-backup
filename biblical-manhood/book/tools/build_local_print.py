#!/usr/bin/env python3
"""LOCAL print build for Steadfast Men (6x9). Modeled on /workspace/tmp-binder-test/build_test.py.

Points the binder (book/tools/make_ebook_pdf.py) at any manuscript folder, repoints ART / PRESS /
FONTS / FIGURES explicitly (the binder computes them from its default BOOK at import time), builds,
then runs print checks and optional PNG proofs. Local only: never uploads, never edits the manuscript.

Usage:
  python3 build_local_print.py MANUSCRIPT_DIR [--out PDF] [--build DIR] [--proofs DIR]
                               [--art DIR] [--press DIR] [--fonts DIR] [--target-pages 240]
                               [--orig-fonts] [--strict]

  MANUSCRIPT_DIR  either the pass folder (…/_opus55-second-pass-2026-10-01) or its book/ subfolder.
  --out           output PDF (default: /workspace/print-build/<folder-name>/Steadfast-Men-<folder-name>.pdf)
  --proofs        write PNG proofs (copyright, ch3 figure, back wrap, a chapter spread, contents)
  --strict        exit non-zero if any check FAILs (WARNs never fail the run)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import make_ebook_pdf as m  # noqa: E402

DEFAULT_ART = Path("/workspace/biblical-manhood/book/art")
# Same fonts with unique PostScript names (see README there). Without this, ReportLab merges
# Bold/Medium into Regular and all bold titles and labels print regular.
PSFIXED_FONTS = Path("/workspace/print-build/fonts-psfixed")
LOCKED_FRONT_SHA = "f3312da16a026255d06e03552b08f5b9d87b0ab6fb2e880b45a57b5e04fe7a64"
CREED = "A steadfast man stops waiting, picks up the weight, goes first, and works for God's pay, not the room's."
CH7_TITLE = "Work for God's Pay"
RETIRED = [
    r"rejects? passivity", r"accepts? responsibility", r"leads? courageously", r"greater reward",
    r"Review draft", r"Not for distribution", r"Not for sale or public distribution", r"Original work\.",
    r"\breal man\b",
]
DASHES = "\u2014\u2013"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def resolve_book(d: Path) -> Path:
    d = d.resolve()
    if (d / "book" / "01-a-quiet-tuesday.md").exists():
        return d / "book"
    if (d / "01-a-quiet-tuesday.md").exists():
        return d
    sys.exit(f"no manuscript found in {d} (expected 01-a-quiet-tuesday.md in it or in its book/)")


def split_margins(text: str) -> tuple[str, list[str]]:
    """Return (prose with margin blocks removed, list of margin verse texts)."""
    verses, prose_lines, inside, cur = [], [], False, []
    for ln in text.splitlines():
        if ln.startswith(":::margin") or ln.startswith(":::epigraph"):
            inside, cur = True, []
            continue
        if inside:
            if ln.startswith(":::"):
                inside = False
                verses.append(" ".join(x.strip() for x in cur if x.strip() and not (x.startswith("**") and "NIV" in x)))
                if verses and cur and ln.startswith(":::") and cur[-1].strip() and re.match(r"^[1-3]?\s?[A-Z][a-z]+ \d+:\d", cur[-1].strip()):
                    verses[-1] = " ".join(x.strip() for x in cur[:-1] if x.strip())  # epigraph: drop the reference line
            else:
                cur.append(ln)
            continue
        prose_lines.append(ln)
    return "\n".join(prose_lines), verses


class Checks:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []

    def add(self, status: str, name: str, detail: str = "") -> None:
        self.rows.append((status, name, detail))
        print(f"  [{status}] {name}{(': ' + detail) if detail else ''}")

    def ok(self, cond: bool, name: str, detail: str = "", warn: bool = False) -> None:
        self.add("PASS" if cond else ("WARN" if warn else "FAIL"), name, detail)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("manuscript")
    ap.add_argument("--out")
    ap.add_argument("--build")
    ap.add_argument("--proofs")
    ap.add_argument("--art", default=str(DEFAULT_ART))
    ap.add_argument("--press")
    ap.add_argument("--fonts")
    ap.add_argument("--orig-fonts", action="store_true", help="use press/fonts as-is (bold faces collapse to regular)")
    ap.add_argument("--target-pages", type=int, default=240)
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    book = resolve_book(Path(a.manuscript))
    tag = book.parent.name if book.name == "book" else book.name
    out = Path(a.out) if a.out else Path("/workspace/print-build") / tag / f"Steadfast-Men-{tag}.pdf"
    build = Path(a.build) if a.build else out.parent / "_build"
    art = Path(a.art)
    press = Path(a.press) if a.press else art / "press"
    if a.fonts:
        fonts = Path(a.fonts)
    elif not a.orig_fonts and PSFIXED_FONTS.exists():
        fonts = PSFIXED_FONTS
    else:
        fonts = press / "fonts"

    # ---- repoint the binder ----
    m.BOOK, m.ART, m.PRESS, m.FONTS = book, art, press, fonts
    m.FIGURES = {3: art / "03-four-marks.png", 34: art / "34-man-plan.png"}
    m.OUT, m.BUILD = out, build
    manifest = m.load_manifest()  # B-A-A (2026-10-04): book.json repoints chapters, parts, figures, back matter
    if manifest:
        print(f"MANIFEST layout={m.LAYOUT} chapters={len(m.CHAPTER_FILES)} back={[b[1] for b in m.BACK_MATTER]}")
    print(f"BOOK {m.BOOK}\nART {m.ART}\nPRESS {m.PRESS}\nFONTS {m.FONTS}\nOUT {m.OUT}")

    ck = Checks()
    print("PREFLIGHT")
    need = ["00-copyright.md", "00-dedication.md", "00-contents.md", "00-introduction.md",
            *[b[1] for b in m.BACK_MATTER], *m.CHAPTER_FILES]
    missing = [f for f in need if not (book / f).exists()]
    ck.ok(not missing, "manuscript files present (CHAPTER_FILES + front/back matter)", ", ".join(missing))
    for p in [*m.FIGURES.values(), press / "a-wrap.png", art / "opener-mark.png"]:
        ck.ok(p.exists(), f"art present: {p.name}")
    front = press / "cloth-store" / "cover-front-walksteadfast-locked-2026-09-14.png"
    ck.ok(front.exists() and sha(front) == LOCKED_FRONT_SHA, "locked front cover unchanged (sha256)")
    ck.ok(fonts.exists() and any(fonts.glob("EBGaramond-*.ttf")), "fonts dir")

    prose_dashes, verse_dash_texts, ms_creed = [], [], {}
    for f in sorted(book.glob("*.md")):
        if f.name.startswith("wrap-"):
            continue
        prose, verses = split_margins(f.read_text(encoding="utf-8"))
        for i, ln in enumerate(prose.splitlines(), 1):
            if any(c in ln for c in DASHES):
                prose_dashes.append(f"{f.name}: {ln.strip()[:70]}")
        verse_dash_texts += [v for v in verses if any(c in v for c in DASHES)]
        ms_creed[f.name] = prose.count(CREED)
    ck.ok(not prose_dashes, "manuscript prose has no em/en dashes (outside :::margin)",
          f"{len(prose_dashes)} hit(s): " + " | ".join(prose_dashes[:3]))
    ck.add("INFO", "NIV margin blocks carrying the NIV's own em dashes", str(len(verse_dash_texts)))
    spaced_dash = [v[:60] for v in verse_dash_texts if re.search(r"\s\u2014|\u2014\s", v)]
    ck.ok(not spaced_dash, "NIV em dashes are closed (no space beside them; NIV style)",
          " | ".join(spaced_dash[:3]))
    if len(m.CHAPTER_FILES) >= 7:
        h1_7 = (book / m.CHAPTER_FILES[6]).read_text(encoding="utf-8").splitlines()[0]
        ck.ok(h1_7.strip() == f"# 7. {CH7_TITLE}", "ch7 H1 is '# 7. Work for God's Pay'", h1_7, warn=True)

    # ---- instrument the binder (no binder edits): page of each image, folio of each page ----
    events = {"images": [], "folios": {}}
    orig_image, orig_show = m.Ebook.image, m.Ebook.show

    def image(self, path, *aa, **kw):
        r = orig_image(self, path, *aa, **kw)  # may advance a page first; record where it landed
        events["images"].append((path.name, self.c.getPageNumber()))
        return r

    def show(self):
        events["folios"][self.c.getPageNumber()] = self.folio if self.number_folios else None
        return orig_show(self)

    m.Ebook.image, m.Ebook.show = image, show

    print("BUILD")
    m.main()  # two-pass probe + final; copies to OUT
    final_events = {"images": events["images"][len(events["images"]) // 2:],
                    "folios": events["folios"]}  # second (final) render overwrote folios

    print("POSTFLIGHT")
    info = subprocess.run(["pdfinfo", str(out)], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    size = re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info)
    ck.ok(size and abs(float(size.group(1)) - 432) < 1 and abs(float(size.group(2)) - 648) < 1, "trim 6x9 (432x648 pt)", size.group(0) if size else "")
    ck.ok(abs(pages - a.target_pages) <= 12, f"page count near {a.target_pages}", f"{pages} pages", warn=True)
    ck.ok(pages % 2 == 0, "even page count", str(pages), warn=True)

    pf = subprocess.run(["pdffonts", str(out)], capture_output=True, text=True).stdout
    faces = sorted({ln.split()[0].split("+")[-1] for ln in pf.splitlines()[2:] if ln.strip()})
    ck.ok(any("Bold" in f for f in faces), "bold faces embedded (titles/labels really bold)", ", ".join(faces), warn=True)
    txt = subprocess.run(["pdftotext", "-layout", str(out), "-"], capture_output=True, text=True).stdout
    # Typographic quotes (binder smart_quotes, 2026-10-01): the PDF should carry curly marks only.
    curly = sum(txt.count(c) for c in "\u2018\u2019\u201c\u201d")
    straight_lines = [ln.strip() for ln in txt.splitlines() if ("'" in ln or '"' in ln)]
    ck.ok(curly > 0 and not straight_lines, "PDF quotes/apostrophes are typographic (no straight ' or \")",
          f"{curly} curly marks; {len(straight_lines)} line(s) with straight marks" + (": " + " | ".join(straight_lines[:3]) if straight_lines else ""), warn=True)
    # From here on compare against the (straight-quoted) manuscript, so fold curly back to straight.
    txt = txt.translate(str.maketrans({"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"'}))
    pg = txt.split("\f")
    flat = re.sub(r"\s+", " ", txt)

    # copyright page
    cp_idx = next((i for i, t in enumerate(pg[:8]) if "Biblica" in t), None)
    cp = re.sub(r"\s+", " ", pg[cp_idx]) if cp_idx is not None else ""
    ck.ok(cp_idx is not None, "copyright page rendered from 00-copyright.md", f"physical page {cp_idx + 1 if cp_idx is not None else '?'}")
    ck.ok("Robert Lewis" in cp and "Raising a Modern-Day Knight" in cp, "copyright page carries the Lewis acknowledgment")
    biblica = "Scripture quotations taken from The Holy Bible, New International Version® NIV® Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.™ Used by permission. All rights reserved worldwide."
    ck.ok(biblica in cp, "copyright page carries the full Biblica NIV notice, verbatim")
    ck.ok("Review draft" not in re.sub(r"\s+", " ", " ".join(pg[:4])), "no 'Review draft' on title/copyright pages")
    for pat in RETIRED:
        hits = len(re.findall(pat, flat, re.I))
        ck.ok(hits == 0, f"retired wording absent from PDF: /{pat}/", f"{hits} hit(s)")

    # contents
    toc_idx = next((i for i, t in enumerate(pg[:10]) if re.search(r"^\s*Contents\s*$", t, re.M)), None)
    toc = pg[toc_idx] if toc_idx is not None else ""
    ck.ok(CH7_TITLE in toc, "TOC shows ch7 as 'Work for God's Pay'", "" if CH7_TITLE in toc else "TOC still shows: " + (re.search(r"Live for a Reward That Lasts", toc) and "Live for a Reward That Lasts" or "?"), warn=True)

    # dashes: every dash in the PDF must sit inside an NIV verse; prose none
    verse_norm = [re.sub(r"\s+", " ", v) for v in verse_dash_texts]
    pdf_dash_lines = [ln.strip() for ln in txt.splitlines() if any(c in ln for c in DASHES)]
    stray = [ln for ln in pdf_dash_lines if not any(re.sub(r"\s+", " ", ln) in v for v in verse_norm)]
    ck.ok(not stray, "PDF prose has no em/en dashes (every dash is inside an NIV margin block)",
          f"{len(stray)} stray: " + " | ".join(stray[:3]))
    survived = sum(1 for v in verse_norm if all(re.sub(r"\s+", " ", seg).strip() in flat for seg in re.split(r"(?<=\u2014)", v)[:1]))
    dash_in_pdf = flat.count("\u2014")
    ms_dash = sum(v.count("\u2014") for v in verse_norm)
    ck.ok(dash_in_pdf == ms_dash, "NIV em dashes survive into the PDF (count matches margin blocks)",
          f"manuscript margin dashes {ms_dash}, PDF dashes {dash_in_pdf}", warn=(ms_dash == 0))
    spaced = len(re.findall(r"\w - \w", flat))
    ck.ok(spaced == 0, "no ' - ' left by no_em() conversion", f"{spaced} hit(s)", warn=True)

    # creed
    pdf_creed = flat.replace("’", "'").count(CREED)
    ck.add("INFO", "creed occurrences in PDF body", f"{pdf_creed} (manuscript prose: {sum(ms_creed.values())}; back wrap is an image)")

    # figure + wrap
    imgs = final_events["images"]
    fig3 = next((pgno for name, pgno in imgs if name == "03-four-marks.png"), None)
    ck.ok(fig3 is not None, "ch3 four-marks figure placed", f"physical page {fig3}")
    ck.add("INFO", "figure source", f"{m.FIGURES[3]} sha {sha(m.FIGURES[3])[:12]}")
    ck.add("INFO", "back wrap source", f"{press / 'a-wrap.png'} sha {sha(press / 'a-wrap.png')[:12]} (creed + inheritance line: check proof)")

    report = {
        "pdf": str(out), "pages": pages, "book": str(book),
        "figure_pages": imgs, "copyright_page": (cp_idx + 1) if cp_idx is not None else None,
        "checks": ck.rows,
    }

    # proofs
    if a.proofs:
        pdir = Path(a.proofs)
        pdir.mkdir(parents=True, exist_ok=True)

        def render(pageno: int, name: str) -> Path:
            stem = pdir / name
            subprocess.run(["pdftoppm", "-png", "-r", "110", "-f", str(pageno), "-l", str(pageno), "-singlefile", str(out), str(stem)], check=True)
            return stem.with_suffix(".png")

        proofs = {}
        if cp_idx is not None:
            proofs["copyright"] = str(render(cp_idx + 1, f"{tag}-proof-copyright"))
        if fig3:
            proofs["figure"] = str(render(fig3, f"{tag}-proof-ch3-figure"))
        proofs["back_wrap"] = str(render(pages, f"{tag}-proof-back-wrap"))
        if toc_idx is not None:
            proofs["contents"] = str(render(toc_idx + 1, f"{tag}-proof-contents"))
        # spread: page holding the first NIV dash block (else ch7 opener) plus its facing page
        target = None
        if verse_norm:
            key = re.sub(r"\s+", " ", verse_norm[0])[:40]
            target = next((i + 1 for i, t in enumerate(pg) if key[:25] in re.sub(r"\s+", " ", t)), None)
        if target is None:
            target = next((i + 1 for i, t in enumerate(pg) if "CHAPTER 7" in t), None)
        if target:
            folio = final_events["folios"].get(target)
            verso = target if (folio and folio % 2 == 0) else target - 1
            from PIL import Image
            left, right = render(verso, f"{tag}-_l"), render(verso + 1, f"{tag}-_r")
            L, R = Image.open(left), Image.open(right)
            sp = Image.new("RGB", (L.width + R.width + 6, max(L.height, R.height)), (120, 120, 120))
            sp.paste(L, (0, 0)); sp.paste(R, (L.width + 6, 0))
            sp_path = pdir / f"{tag}-proof-spread-p{verso}-{verso + 1}.png"
            sp.save(sp_path); left.unlink(); right.unlink()
            proofs["spread"] = str(sp_path)
        report["proofs"] = proofs
        print("PROOFS", json.dumps(proofs, indent=1))

    rp = out.with_suffix(".checks.json")
    rp.write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
    fails = [r for r in ck.rows if r[0] == "FAIL"]
    warns = [r for r in ck.rows if r[0] == "WARN"]
    print(f"DONE {out} pages={pages} FAIL={len(fails)} WARN={len(warns)} report={rp}")
    return 1 if (a.strict and fails) else 0


if __name__ == "__main__":
    sys.exit(main())
