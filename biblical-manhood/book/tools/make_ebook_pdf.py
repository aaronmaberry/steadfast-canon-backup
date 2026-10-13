#!/usr/bin/env python3
"""Steadfast Men ebook PDF binder. Cloth Store colors. Live .md only.
Script lives in book/tools/ and is never deleted by the build.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
import uuid
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

try:  # B-A-A typesetting (2026-10-04): soft hyphenation for justified body text
    import pyphen
    _HY = pyphen.Pyphen(lang="en_US", left=3, right=3)
except Exception:  # pragma: no cover
    _HY = None

BOOK = Path("/workspace/biblical-manhood/book")
ART = BOOK / "art"
PRESS = ART / "press"
FONTS = PRESS / "fonts"
OUT = BOOK / "export" / "steadfast-men-ebook.pdf"
BUILD = BOOK / "export" / "_build"

NAVY = (11 / 255, 31 / 255, 56 / 255)
GOLD = (227 / 255, 197 / 255, 114 / 255)
# Aaron 2026-09-08: ACCENT on BONE for colorblind contrast — never gold-on-bone.
# Prefer navy #0B1F38 (NAVY), deep teal #134E4A (ACCENT), or charcoal #2C2C2C; gold only on navy.
ACCENT = (19 / 255, 78 / 255, 74 / 255)  # #134E4A deep teal
BONE = (230 / 255, 221 / 255, 204 / 255)
INK = (22 / 255, 28 / 255, 36 / 255)
INK_SOFT = (70 / 255, 78 / 255, 88 / 255)
RULE = (168 / 255, 164 / 255, 154 / 255)
# Closer-box gold standard (matches art/render_01_closer.py)
CLOSER_PANEL = (244 / 255, 239 / 255, 228 / 255)  # light bone panel
CARRY_BAND = (236 / 255, 228 / 255, 212 / 255)  # shaded CARRY THIS band
CLOSER_RAIL = (44 / 255, 41 / 255, 36 / 255)  # near-black iron rail
CLOSER_LABEL = (122 / 255, 74 / 255, 50 / 255)  # rust labels/ticks
CLOSER_RULE = (192 / 255, 184 / 255, 168 / 255)  # light section rules

PAGE_W = 6 * inch
PAGE_H = 9 * inch
GUTTER = 0.72 * inch
OUTSIDE = 0.58 * inch
TOP = 0.68 * inch
BOTTOM = 0.68 * inch

BODY_SIZE = 10.5
BODY_LEADING = 14.4
TITLE_SIZE = 20

# In-chapter section heads (2026-10-02, Aaron: smaller, lighter, tighter). Color unchanged (NAVY).
# Was Libre-Bold 11.5/16 (h2) and 10.5/14 (h3), 10 pt above / 6 pt below.
HEAD_FONT = "Libre-Medium"
HEAD_SIZE = {2: 11.0, 3: 10.5}
HEAD_LEADING = {2: 14.0, 3: 13.0}
HEAD_ABOVE = {2: 7.0, 3: 5.0}
HEAD_BELOW = {2: 3.0, 3: 2.0}

# Opener placement (2026-10-02 review). Default = current house style: every opener on a recto.
# STEADFAST_OPEN_ANY=chapters -> chapters/intro/back-matter sections open on the next page;
#                               part pages stay recto with a blank back.
# STEADFAST_OPEN_ANY=all      -> part pages too.
_OPEN_ANY = os.environ.get("STEADFAST_OPEN_ANY", "").strip().lower()


def _force_recto(kind: str) -> bool:
    if _OPEN_ANY == "all":
        return False
    if _OPEN_ANY == "chapters":
        return kind == "part"
    return True
MARGIN_SIZE = 8.5
MARGIN_LEADING = 11.0

PARTS = {
    1: ("PART ONE", "The Man You Were Built to Be"),
    8: ("PART TWO", "What You Inherited, and What Is Yours"),
    18: ("PART THREE", "The Story That Names You"),
    21: ("PART FOUR", "The House"),
    30: ("PART FIVE", "The Long Road"),
}

CHAPTER_FILES = [
    "01-a-quiet-tuesday.md",
    "02-you-are-not-crazy.md",
    "03-the-four-marks.md",
    "04-stop-waiting.md",
    "05-pick-up-the-weight.md",
    "06-go-first.md",
    "07-live-for-a-reward-that-lasts.md",
    "08-the-empty-chair.md",
    "09-anger-the-itch-and-the-drift.md",
    "10-the-father-who-does-not-leave.md",
    "11-when-home-never-handed-you-off.md",
    "12-leave-without-slamming-the-door.md",
    "13-a-man-with-no-brothers.md",
    "14-ask-the-man.md",
    "15-the-problem-inside.md",
    "16-how-that-looks-on-a-man.md",
    "17-no-fixed-star.md",
    "18-before-the-fall.md",
    "19-two-men-two-ways.md",
    "20-destiny-is-not-a-vibe.md",
    "21-if-there-is-no-wife-yet.md",
    "22-know-her.md",
    "23-lay-it-down.md",
    "24-what-she-actually-needs.md",
    "25-the-bed-is-a-covenant.md",
    "26-your-daughter-is-watching.md",
    "27-give-your-son-a-name.md",
    "28-give-your-son-a-hill.md",
    "29-give-your-son-a-day-he-will-not-forget.md",
    "30-you-were-made-for-a-work.md",
    "31-feelings-are-the-dash-not-the-wheel.md",
    "32-every-season-still-counts.md",
    "33-what-you-are-building-when-nobody-claps.md",
    "34-write-the-next-move.md",
    "35-these-men-are-my-brothers.md",
]

CLOSER_ART = set()  # all chapters use typeset closer_box (gold-standard); no PNG split
FIGURES = {
    3: ART / "03-four-marks.png",
    34: ART / "34-man-plan.png",
}


# 2026-10-03c (Aaron: "make it for the margins and look professional"): the ch3 four-marks
# figure is typeset as a full-measure callout (vector, book fonts/colors) instead of the
# narrow PNG. Set False to fall back to the PNG.
TYPESET_FOUR_MARKS = True
FOUR_MARKS = ("Stop Waiting", "Pick Up the Weight", "Go First", "Work for God’s Pay")

# ch3 figure goes right after the first paragraph containing one of these.
FIG3_TRIGGERS = (
    "A steadfast man stops waiting, picks up the weight, goes first, and works for God's pay",
    "Passivity. Responsibility. Courage. Reward.",  # pre-2026-10-01 manuscripts
)


# ---------------------------------------------------------------------------------------------
# B-A-A layout (Aaron, 2026-10-04). A manuscript folder that carries `book.json` with
# "layout": "baa" gets the approved ch10-sample v2 typesetting:
#   - one NIV anchor verse (:::epigraph) under each chapter title; no verse boxes in the body
#   - paragraphs: first-line indent 1.2em, NO space between paragraphs, justified with light
#     pyphen hyphenation (lowercase words of 7+ letters, 3+3 letters, never two hyphens running
#     past two lines), widows/orphans 2
#   - no indent on the first paragraph after the title rule, the epigraph, a figure, or a break
#   - :::break = exactly two body lines (28.8 pt) with a small centered teal diamond
#   - Your Turn moves to a back-of-book section, one page per chapter (typeset closer_box)
#   - Scripture notes at the back, keyed by phrase
# Without book.json the binder behaves exactly as it did for 03d (classic layout).
# ---------------------------------------------------------------------------------------------
LAYOUT = "classic"
BACK_MATTER = [
    ("About the Author", "36-about-the-author.md", "section"),
    ("Condensed Training", "37-condensed-training.md", "section"),
]
FIG3_CHAPTER = 3
MANPLAN_CHAPTER = 34
PARA_INDENT = 1.2 * 10.5  # 1.2em at BODY_SIZE
CONTENTS_NOTE_PREFIXES = ("Every chapter ends", "Each chapter")


def load_manifest() -> dict:
    """Read BOOK/book.json (if present) and repoint chapter list, parts, figures, back matter."""
    global LAYOUT, CHAPTER_FILES, PARTS, BACK_MATTER, FIG3_CHAPTER, MANPLAN_CHAPTER, FIGURES
    mf = BOOK / "book.json"
    if not mf.exists():
        return {}
    data = json.loads(mf.read_text(encoding="utf-8"))
    LAYOUT = data.get("layout", "classic")
    if data.get("chapters"):
        CHAPTER_FILES = list(data["chapters"])
    if data.get("parts"):
        PARTS = {int(k): tuple(v) for k, v in data["parts"].items()}
    if data.get("back_matter"):
        BACK_MATTER = [tuple(x) for x in data["back_matter"]]
    if data.get("figures"):
        FIGURES = {int(k): ART / v for k, v in data["figures"].items()}
    FIG3_CHAPTER = int(data.get("fig3_chapter", FIG3_CHAPTER))
    MANPLAN_CHAPTER = int(data.get("manplan_chapter", MANPLAN_CHAPTER))
    return data


def no_em(s: str) -> str:
    """House rule for PROSE only: no em or en dashes print in body text, headings, closers.

    NEVER call this on Scripture. :::margin (NIV verse) blocks keep the NIV 2011's own em
    dashes exactly as printed (Aaron, 2026-10-01). parse_md() tags those blocks
    {"type": "margin", "verse": True} and margin_block() draws them verbatim.
    """
    return (
        s.replace("\u2014", " - ")
        .replace("\u2013", "-")
        .replace("—", " - ")
        .replace("–", "-")
    )


_ELISIONS = ("em", "til", "tis", "twas", "cause", "n", "round", "bout", "nuff", "neath")
_OPEN_CTX = set(" \t\n([{/\u201c\u2018")
_DASHES = set("\u2014\u2013")


def smart_quotes(s: str) -> str:
    """Straight -> typographic quotes for print (2026-10-01). Applied to prose, titles,
    headings, closers, contents, copyright AND NIV margin blocks (the NIV prints curly).
    The manuscript keeps straight quotes; niv_verify compares straight-normalized text.
    - " opens at start or after space/([{/opening quote; closes otherwise.
    - ' inside a word (don't, God's) is an apostrophe.
    - ' starting an elision ('em, 'til, 'cause) or a year/decade ('68, '90s) is an apostrophe.
    - ' after space/start/opening bracket or quote opens a nested quote; otherwise it closes
      (closing single quote or plural possessive: fathers').
    - After an em/en dash, a quote opens only if a word follows it.
    Idempotent: curly input passes through."""
    if "'" not in s and '"' not in s:
        return s
    out: list[str] = []
    n = len(s)
    for i, ch in enumerate(s):
        prev = out[-1] if out else ""
        nxt = s[i + 1] if i + 1 < n else ""
        if ch not in "'\"":
            out.append(ch)
            continue
        if prev in _DASHES:
            opening = bool(nxt) and nxt.isalnum()
        else:
            opening = (not prev) or prev in _OPEN_CTX
        if ch == '"':
            out.append("\u201c" if opening else "\u201d")
            continue
        if prev and prev.isalnum() and nxt.isalnum():
            out.append("\u2019")
        elif opening:
            rest = s[i + 1 :]
            if re.match(r"\d\d", rest) or re.match(r"(%s)\b" % "|".join(_ELISIONS), rest, re.I):
                out.append("\u2019")
            elif nxt and not nxt.isspace():
                out.append("\u2018")
            else:
                out.append("\u2019")
        else:
            out.append("\u2019")
    return "".join(out)


def register_fonts() -> None:
    pairs = [
        ("Playfair", "PlayfairDisplay-Regular.ttf"),
        ("Playfair-Bold", "PlayfairDisplay-Bold.ttf"),
        ("Playfair-Italic", "PlayfairDisplay-Italic.ttf"),
        ("EBGaramond", "EBGaramond-Regular.ttf"),
        ("EBGaramond-Bold", "EBGaramond-Bold.ttf"),
        ("EBGaramond-Italic", "EBGaramond-Italic.ttf"),
        ("Libre", "LibreFranklin-Regular.ttf"),
        ("Libre-Bold", "LibreFranklin-Bold.ttf"),
        ("Libre-Medium", "LibreFranklin-Medium.ttf"),
    ]
    for name, fn in pairs:
        pdfmetrics.registerFont(TTFont(name, str(FONTS / fn)))


def clean_inline_md(text: str) -> str:
    """Strip leftover markdown markers so they never print raw in the PDF."""
    t = text.strip()
    # leading heading hashes that slipped into paragraph text
    t = re.sub(r"^#{1,6}\s+", "", t)
    # bold/italic markers (simple; keep inner text)
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", t)
    return t.strip()



CLOSER_LABELS = (
    ("name it", "NAME IT"),
    ("do this week", "DO THIS WEEK"),
    ("tell a brother", "TELL A BROTHER"),
    ("be a brother", "BE A BROTHER"),  # ch35 intentional variant
    ("carry this", "CARRY THIS"),
)


def _match_closer_label(line: str) -> tuple[str, str, str] | None:
    """Return (key, DISPLAY, rest) if line starts a closer section label."""
    raw = line.strip()
    if not raw or raw in ("---", "—", "-", "–"):
        return None
    if re.match(r"^#{1,6}\s+Your Turn\s*$", raw, re.I):
        return None
    # Strip wrapping ** / __ for matching
    plain = re.sub(r"^\*{1,2}", "", raw)
    plain = re.sub(r"\*{1,2}$", "", plain)
    plain = plain.strip()
    plain = re.sub(r"^#{1,6}\s+", "", plain)
    low = plain.lower()
    for key, display in CLOSER_LABELS:
        if low == key or low.startswith(key + ".") or low.startswith(key + ":") or low.startswith(key + " "):
            rest = plain[len(key) :].lstrip(".: ").strip()
            rest = smart_quotes(clean_inline_md(rest))
            return key, display, rest
    return None


def parse_closer_sections(lines: list[str]) -> list[dict]:
    """Parse Your Turn markdown into structured sections for closer_box.

    - Labels may be **Name it**, Name it, Name it. rest, etc.
    - Body paragraphs until next label or :::notes
    - :::notes underscore lines -> write_in count (1–2); empty notes skipped
    - CARRY THIS never gets write-in rules (shaded band only)
    - Strips leftover ## / ** / ---
    """
    sections: list[dict] = []
    current: dict | None = None
    body_buf: list[str] = []

    def flush_body() -> None:
        nonlocal body_buf, current
        if current is None:
            body_buf = []
            return
        text = " ".join(x.strip() for x in body_buf if x.strip()).strip()
        text = smart_quotes(clean_inline_md(no_em(text)))
        if text:
            if current["body"]:
                current["body"] = (current["body"] + " " + text).strip()
            else:
                current["body"] = text
        body_buf = []

    def start_section(key: str, display: str, rest: str) -> None:
        nonlocal current
        flush_body()
        current = {
            "key": key,
            "label": display,
            "body": rest or "",
            "write_in": 0,
            "prompt": None,
        }
        sections.append(current)

    i = 0
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()

        if stripped.startswith(":::notes"):
            flush_body()
            i += 1
            nls: list[str] = []
            while i < len(lines) and not lines[i].startswith(":::"):
                if lines[i].strip():
                    nls.append(lines[i].strip())
                i += 1
            if i < len(lines) and lines[i].startswith(":::"):
                i += 1
            if current is None or current["key"] == "carry this":
                # Gold standard: no write-in void under CARRY THIS; skip empty/orphan notes
                continue
            if not nls:
                continue
            rules = 0
            prompts: list[str] = []
            for nl in nls:
                # underscore / rule lines
                if re.fullmatch(r"[_—–\-\s\.·]{6,}", nl) or set(nl) <= set("_—–- .·"):
                    rules += 1
                else:
                    prompts.append(smart_quotes(clean_inline_md(nl)))
            if rules:
                current["write_in"] = min(3, max(1, rules))  # 2026-10-04: Your Turn pages may carry 3
            elif prompts:
                # prompt-only notes: still offer one write-in line
                current["write_in"] = 1
            if prompts:
                current["prompt"] = " ".join(prompts)
            continue

        hit = _match_closer_label(ln)
        if hit:
            start_section(*hit)
            i += 1
            continue

        if not stripped or stripped in ("---", "—", "-", "–"):
            flush_body()
            i += 1
            continue
        if re.match(r"^#{1,6}\s+Your Turn\s*$", stripped, re.I):
            i += 1
            continue
        if re.match(r"^#{1,6}\s+", stripped):
            # stray heading inside closer — treat cleaned text as body
            body_buf.append(re.sub(r"^#{1,6}\s+", "", stripped))
            i += 1
            continue

        body_buf.append(stripped)
        i += 1

    flush_body()
    # Drop empty non-carry sections with no body and no write-in
    out = []
    for sec in sections:
        if sec["key"] == "carry this":
            if sec["body"]:
                out.append(sec)
            continue
        if sec["body"] or sec["write_in"]:
            out.append(sec)
    return out


def parse_md(path: Path) -> tuple[str, int, list[dict]]:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    title_line = lines[0] if lines else path.stem
    m = re.match(r"^#\s+(\d+)\.\s+(.*)$", title_line)
    if m:
        num, title = int(m.group(1)), smart_quotes(m.group(2).strip())
    else:
        m2 = re.match(r"^#\s+(.*)$", title_line)
        title = smart_quotes(m2.group(1).strip()) if m2 else path.stem
        # Filename fallback: NN-slug.md -> chapter N (never emit CHAPTER 0 for numbered files)
        fm = re.match(r"^(\d+)-", path.name)
        num = int(fm.group(1)) if fm else 0

    blocks: list[dict] = []
    i = 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    buf: list[str] = []

    def flush() -> None:
        nonlocal buf
        text = " ".join(x.strip() for x in buf).strip()
        buf = []
        if text:
            # Prose: dash-free house rule applies here (Scripture blocks are exempt).
            blocks.append({"type": "p", "text": smart_quotes(clean_inline_md(no_em(text)))})

    while i < len(lines):
        line = lines[i]
        if line.startswith(":::epigraph"):
            flush()
            i += 1
            elines: list[str] = []
            while i < len(lines) and not lines[i].startswith(":::"):
                if lines[i].strip():
                    elines.append(lines[i].strip())
                i += 1
            i += 1
            # NIV anchor verse: verbatim, NO no_em(). Last line is the reference.
            cite = elines[-1] if len(elines) > 1 else ""
            body = elines[:-1] if len(elines) > 1 else elines
            blocks.append({"type": "epigraph", "cite": smart_quotes(cite), "text": smart_quotes(" ".join(body)), "verse": True})
            continue
        if line.startswith(":::break"):
            flush()
            i += 1
            while i < len(lines) and not lines[i].startswith(":::"):
                i += 1
            i += 1
            blocks.append({"type": "break"})
            continue
        if line.startswith(":::margin"):
            flush()
            i += 1
            mlines: list[str] = []
            while i < len(lines) and not lines[i].startswith(":::"):
                mlines.append(lines[i])
                i += 1
            i += 1
            cite, body = "", []
            for j, ml in enumerate(mlines):
                if j == 0 and ml.startswith("**") and "NIV" in ml:
                    cite = ml.strip("*").strip()
                elif ml.strip():
                    body.append(ml.strip())
            # NIV verse block: verbatim, NO no_em(); the NIV's em dashes must survive.
            blocks.append({"type": "margin", "cite": smart_quotes(cite), "text": smart_quotes(" ".join(body)), "verse": True})
            continue
        if line.startswith(":::notes"):
            flush()
            i += 1
            nlines: list[str] = []
            while i < len(lines) and not lines[i].startswith(":::"):
                if lines[i].strip():
                    nlines.append(lines[i].strip())
                i += 1
            i += 1
            # Empty notes: skip entirely (do not invent blank write-in lines)
            if nlines:
                blocks.append({"type": "notes", "lines": nlines})
            continue
        # Closer starts ONLY at ## Your Turn. Do not key off bare **Name it** —
        # Introduction explains those four lines in narrative; Name it alone used to
        # open closer mode and truncate the rest of the intro (Aaron 2026-09-21).
        if re.match(r"^##\s+Your Turn\s*$", line, re.I):
            flush()
            closer = [line]
            i += 1
            while i < len(lines):
                closer.append(lines[i])
                i += 1
            blocks.append({"type": "closer", "lines": closer})
            break
        # Subheads: parse ## / ### as heading blocks (never leave hashes in body text)
        hm = re.match(r"^(#{2,3})\s+(.+?)\s*$", line)
        if hm and not re.match(r"^##\s+Your Turn\s*$", line, re.I):
            flush()
            level = len(hm.group(1))
            htext = smart_quotes(clean_inline_md(hm.group(2)))
            blocks.append({"type": "h2" if level == 2 else "h3", "text": htext})
            i += 1
            continue
        if not line.strip():
            flush()
            i += 1
            continue
        # 2026-10-01: markdown list items ("1. ..." / "- ...") are one block each, so a
        # list never collapses into a run-on paragraph (Condensed Training week list).
        if re.match(r"^\s*(\d+\.|[-*])\s+\S", line):
            flush()
            buf.append(line)
            flush()
            i += 1
            continue
        buf.append(line)
        i += 1
    flush()
    return title, num, blocks


class Ebook:
    def __init__(self, pdf_path: Path, asset_dir: Path) -> None:
        self.pdf_path = pdf_path
        self.asset_dir = asset_dir
        self.asset_dir.mkdir(parents=True, exist_ok=True)
        self.c = canvas.Canvas(str(pdf_path), pagesize=(PAGE_W, PAGE_H))
        self.physical = 0  # pages written (after showPage count via _pageNumber)
        self.folio = 0  # arabic numbers for body
        self.number_folios = False
        self.running = ""
        self.left = GUTTER
        self.right = PAGE_W - OUTSIDE
        self.measure = self.right - self.left
        self.y = PAGE_H - TOP
        self.on_recto = True
        self.page_map: dict[str, int] = {}
        self.cover_front = False
        self.closer_35 = False
        self.used_wrap_back = False
        self.missing: list[str] = []
        self._open = True

    def _fill_bone(self) -> None:
        self.c.setFillColorRGB(*BONE)
        self.c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    def _margins_for_folio(self) -> None:
        # folio odd = recto (gutter left)
        self.on_recto = (self.folio % 2 == 1) if self.number_folios and self.folio else True
        if self.on_recto:
            self.left = GUTTER
            self.right = PAGE_W - OUTSIDE
        else:
            self.left = OUTSIDE
            self.right = PAGE_W - GUTTER
        self.measure = self.right - self.left

    def _footer(self) -> None:
        if not self.number_folios or self.folio <= 0:
            return
        self.c.setFillColorRGB(*INK_SOFT)
        self.c.setFont("EBGaramond", 8)
        s = str(self.folio)
        if self.on_recto:
            self.c.drawRightString(self.right, BOTTOM - 16, s)
            self.c.setFillColorRGB(*RULE)
            self.c.setFont("EBGaramond-Italic", 8)
            self.c.drawString(self.left, BOTTOM - 16, no_em(self.running)[:42])
        else:
            self.c.drawString(self.left, BOTTOM - 16, s)
            self.c.setFillColorRGB(*RULE)
            self.c.setFont("EBGaramond-Italic", 8)
            self.c.drawRightString(self.right, BOTTOM - 16, no_em(self.running)[:42])

    def show(self) -> None:
        self.c.showPage()
        self.physical += 1

    def blank_bone(self, *, number: bool = False) -> None:
        """Start a fresh page."""
        if self.physical > 0 or self.c._code:  # noqa: SLF001
            # if current page has content already committed via prior ops without show,
            # we only show when advancing from a finished page. Caller manages.
            pass
        self._fill_bone()
        if number:
            self.number_folios = True
            self.folio += 1
            self._margins_for_folio()
            self._footer()
        else:
            self.left = GUTTER
            self.right = PAGE_W - OUTSIDE
            self.measure = self.right - self.left
        self.y = PAGE_H - TOP

    def advance(self, *, number: bool | None = None, blank_if_verso: bool = False) -> None:
        """Finish current page and open a new one.
        blank_if_verso: opener pre-advance; an intentionally blank verso gets no footer (folio still counts)."""
        self.show()
        use_number = self.number_folios if number is None else number
        if use_number:
            self.number_folios = True
            self.folio += 1
            self._fill_bone()
            self._margins_for_folio()
            if not (blank_if_verso and not self.on_recto):
                self._footer()
        else:
            self._fill_bone()
            self.left = GUTTER
            self.right = PAGE_W - OUTSIDE
            self.measure = self.right - self.left
        self.y = PAGE_H - TOP

    def ensure(self, h: float) -> None:
        if self.y - h < BOTTOM + 14:
            self.advance()

    def tracked(self, text: str, x: float, y: float, font: str, size: float, color, tracking: float = 2.0) -> None:
        self.c.setFillColorRGB(*color)
        self.c.setFont(font, size)
        cx = x
        for ch in text:
            self.c.drawString(cx, y, ch)
            cx += self.c.stringWidth(ch, font, size) + tracking

    def wrap(self, text: str, font: str, size: float, width: float) -> list[str]:
        words = text.split()
        lines: list[str] = []
        cur = ""
        for w in words:
            trial = w if not cur else f"{cur} {w}"
            if self.c.stringWidth(trial, font, size) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines or [""]

    def para(self, text: str, *, size=BODY_SIZE, leading=BODY_LEADING, font="EBGaramond", color=INK, indent=11.0, after: float = 0.36) -> None:
        text = clean_inline_md(text)
        if not text:
            return
        words = text.split()
        lines: list[str] = []
        cur = ""
        first_limit = self.measure - indent
        for w in words:
            trial = w if not cur else f"{cur} {w}"
            limit = first_limit if not lines else self.measure
            if self.c.stringWidth(trial, font, size) <= limit:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        for i, line in enumerate(lines):
            self.ensure(leading)
            x = self.left + (indent if i == 0 else 0)
            self.c.setFillColorRGB(*color)
            self.c.setFont(font, size)
            self.c.drawString(x, self.y - size, line)
            self.y -= leading
        self.y -= leading * after

    # ----- B-A-A body typesetting (2026-10-04) -----
    def _hyph_split(self, word: str, room: float, font: str, size: float):
        """Split `word` so its head (with a hyphen) fits in `room`. Lowercase words only."""
        sw = lambda t: self.c.stringWidth(t, font, size)  # noqa: E731
        m = re.fullmatch(r"([a-z]+)-([a-z][a-z\-]*[a-z])([.,;:!?)\u2019\u201d'\"]*)", word)
        if m and sw(m.group(1) + "-") <= room:  # existing compound hyphen
            return m.group(1) + "-", m.group(2) + m.group(3)
        m = re.fullmatch(r"([a-z]{7,})([.,;:!?)\u2019\u201d'\"]*)", word)
        if not m or _HY is None:
            return None
        core, trail = m.group(1), m.group(2)
        for pos in sorted(_HY.positions(core), reverse=True):
            if sw(core[:pos] + "-") <= room:
                return core[:pos] + "-", core[pos:] + trail
        return None

    def _set_lines(self, text: str, font: str, size: float, first_indent: float) -> list[list[str]]:
        sw = lambda t: self.c.stringWidth(t, font, size)  # noqa: E731
        sp = sw(" ")
        words = text.split()
        lines: list[list[str]] = []
        cur: list[str] = []
        hy_run = 0
        width = lambda ws: sum(sw(w) for w in ws) + sp * max(0, len(ws) - 1)  # noqa: E731
        i = 0
        while i < len(words):
            w = words[i]
            limit = self.measure - (first_indent if not lines else 0)
            if not cur or width(cur + [w]) <= limit:
                cur.append(w)
                i += 1
                continue
            slack = limit - width(cur)
            piece = None
            if slack > 2.2 * sp and hy_run < 2:
                piece = self._hyph_split(w, slack - sp, font, size)
            if piece:
                cur.append(piece[0])
                words[i] = piece[1]
                hy_run += 1
            else:
                hy_run = 0
            lines.append(cur)
            cur = []
        if cur:
            lines.append(cur)
        return lines

    def para_baa(self, text: str, *, font: str = "EBGaramond", size: float = BODY_SIZE,
                 leading: float = BODY_LEADING, color=INK) -> None:
        text = clean_inline_md(text)
        if not text:
            return
        indent = 0.0 if getattr(self, "_noindent", False) else PARA_INDENT
        self._noindent = False
        lines = self._set_lines(text, font, size, indent)
        n, idx = len(lines), 0
        sp = self.c.stringWidth(" ", font, size)
        while idx < n:
            k = int((self.y - (BOTTOM + 14) + 0.01) // leading)
            rem = n - idx
            if k <= 0:
                self.advance()
                continue
            if rem <= k:
                take = rem
            elif k == 1:  # orphan: never leave one line of a paragraph at a page foot
                self.advance()
                continue
            elif rem - k == 1:  # widow: never carry one line to the next page
                if k >= 3:
                    take = k - 1
                else:
                    self.advance()
                    continue
            else:
                take = k
            for j in range(idx, idx + take):
                ws = lines[j]
                x = self.left + (indent if j == 0 else 0)
                avail = self.right - x
                last = j == n - 1
                nat = sum(self.c.stringWidth(w, font, size) for w in ws)
                gap = sp if (last or len(ws) < 2) else (avail - nat) / (len(ws) - 1)
                if not last and gap > 3.2 * sp:  # pathological loose line: set ragged
                    gap = sp
                self.c.setFillColorRGB(*color)
                self.c.setFont(font, size)
                for w in ws:
                    self.c.drawString(x, self.y - size, w)
                    x += self.c.stringWidth(w, font, size) + gap
                self.y -= leading
            idx += take
            if idx < n:
                self.advance()

    def section_break(self) -> None:
        """Quiet break: exactly two body lines with a small centered teal diamond."""
        if self.y - 4 * BODY_LEADING < BOTTOM + 14:  # keep two text lines under the ornament
            self.advance()
        cx = (self.left + self.right) / 2
        cy = self.y - BODY_LEADING + 2.6  # optical centre of the two-line slot (x-height)
        r = 2.6
        self.c.setFillColorRGB(*ACCENT)
        pth = self.c.beginPath()
        pth.moveTo(cx, cy + r); pth.lineTo(cx + r, cy); pth.lineTo(cx, cy - r); pth.lineTo(cx - r, cy); pth.close()
        self.c.drawPath(pth, fill=1, stroke=0)
        self.y -= 2 * BODY_LEADING
        self._noindent = True

    def epigraph(self, cite: str, text: str) -> None:
        """Chapter anchor verse (NIV, verbatim) under the title rule."""
        inset = 0.35 * inch
        width = self.measure - 2 * inset
        lines = self.wrap(text, "EBGaramond-Italic", 9.5, width)
        self.c.setFillColorRGB(*INK_SOFT)
        for ln in lines:
            self.c.setFont("EBGaramond-Italic", 9.5)
            self.c.drawString(self.left + inset, self.y - 9.5, ln)
            self.y -= 12.6
        if cite:
            self.y -= 4
            self.tracked(no_em(cite.upper()), self.left + inset, self.y - 7, "Libre-Medium", 7, ACCENT, 1.4)
            self.y -= 9
        self.y -= BODY_LEADING
        self._noindent = True

    def margin_block(self, cite: str, text: str) -> None:
        pad = 8
        cite_lines = self.wrap(cite, "Libre-Bold", 7.5, self.measure - 2 * pad) if cite else []
        body_lines = self.wrap(text, "EBGaramond-Italic", MARGIN_SIZE, self.measure - 2 * pad)
        # 2026-10-01: rail ends just under the last line's descenders (was ~19 pt past the text).
        h = 12 + len(cite_lines) * 10 + (len(body_lines) - 1) * MARGIN_LEADING + 5
        self.ensure(h + 6)
        self.y -= 4
        top = self.y
        bottom = self.y - h
        self.c.setStrokeColorRGB(*ACCENT)
        self.c.setLineWidth(1.6)
        self.c.line(self.left, bottom, self.left, top)
        yy = top - 12
        self.c.setFillColorRGB(*NAVY)
        for cl in cite_lines:
            self.c.setFont("Libre-Bold", 7.5)
            self.c.drawString(self.left + pad, yy, cl)
            yy -= 10
        self.c.setFillColorRGB(*INK)
        for bl in body_lines:
            self.c.setFont("EBGaramond-Italic", MARGIN_SIZE)
            self.c.drawString(self.left + pad, yy, bl)
            yy -= MARGIN_LEADING
        self.y = bottom - 9

    def notes(self, lines: list[str]) -> None:
        if not lines:
            return
        self.ensure(8 + len(lines) * 18)
        self.c.setStrokeColorRGB(*RULE)
        self.c.setLineWidth(0.6)
        for _ in lines:
            self.y -= 16
            self.c.line(self.left, self.y, self.right, self.y)
        self.y -= 10

    def heading(self, text: str, *, level: int = 2) -> None:
        """Styled subhead — Libre-Bold NAVY; never prints # characters."""
        clean = clean_inline_md(text)
        if not clean:
            return
        lv = 2 if level <= 2 else 3
        size, leading = HEAD_SIZE[lv], HEAD_LEADING[lv]
        self.y -= HEAD_ABOVE[lv]
        self.ensure(leading + 6 + 2 * BODY_LEADING)  # keep the head with at least two body lines
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont(HEAD_FONT, size)
        for ln in self.wrap(no_em(clean), HEAD_FONT, size, self.measure):
            self.ensure(leading)
            self.c.drawString(self.left, self.y - size, ln)
            self.y -= leading
        self.y -= HEAD_BELOW[lv]

    def _tracked_width(self, text: str, font: str, size: float, tracking: float) -> float:
        return self.c.stringWidth(text, font, size) + tracking * (len(text) - 1)

    def four_marks_callout(self) -> None:
        """Full-measure callout for the four marks (ch3, after the creed sentence).

        Light bone panel spanning the text block, navy rules top and bottom (heading color),
        a small tracked teal label with a short teal rule (the chapter-label treatment), then
        the four marks as tracked Libre Franklin Medium caps in navy, centered on equal pitch.
        Kept whole on one page.
        """
        label, label_font, label_size, label_track = "THE FOUR MARKS", "Libre-Medium", 7.5, 2.0
        mark_font, mark_size, mark_track = "Libre-Medium", 11.0, 1.6
        cap = 0.72  # cap height / em for Libre Franklin
        pad = 15.0  # equal optical padding above the label caps and below the last mark
        label_to_rule, rule_to_first, pitch = 7.0, 21.0, 21.0
        rule_w, rule_lw, accent_w = 1.2, 1.0, 26.0
        space_above, space_below = 10.0, 14.0

        h = pad + label_size * cap + label_to_rule + rule_to_first + pitch * (len(FOUR_MARKS) - 1) + pad
        at_top = abs(self.y - (PAGE_H - TOP)) < 0.5
        if not at_top:
            self.y -= space_above
        if self.y - h < BOTTOM + 14:
            self.advance()
        left, right = self.left, self.right
        cx = (left + right) / 2
        top, bottom = self.y, self.y - h

        c = self.c
        c.setFillColorRGB(*CLOSER_PANEL)
        c.rect(left, bottom, right - left, h, fill=1, stroke=0)
        c.setStrokeColorRGB(*NAVY)
        c.setLineWidth(rule_w)
        c.line(left, top, right, top)
        c.line(left, bottom, right, bottom)

        yy = top - pad - label_size * cap
        lw = self._tracked_width(label, label_font, label_size, label_track)
        self.tracked(label, cx - lw / 2, yy, label_font, label_size, ACCENT, tracking=label_track)
        yy -= label_to_rule
        c.setStrokeColorRGB(*ACCENT)
        c.setLineWidth(rule_lw)
        c.line(cx - accent_w / 2, yy, cx + accent_w / 2, yy)
        yy -= rule_to_first
        for i, mk in enumerate(FOUR_MARKS):
            s = mk.upper()
            w = self._tracked_width(s, mark_font, mark_size, mark_track)
            self.tracked(s, cx - w / 2, yy, mark_font, mark_size, NAVY, tracking=mark_track)
            if i < len(FOUR_MARKS) - 1:
                yy -= pitch
        self.y = bottom - space_below

    def image(
        self,
        path: Path,
        max_w: float | None = None,
        max_h: float | None = None,
        *,
        center_alone: bool = False,
    ) -> None:
        if not path.exists():
            self.missing.append(path.name)
            return
        if TYPESET_FOUR_MARKS and path.name == "03-four-marks.png":
            self.four_marks_callout()
            return
        im = PILImage.open(path)
        if im.mode == "RGBA":
            bg = PILImage.new("RGB", im.size, tuple(int(x * 255) for x in BONE))
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        iw, ih = im.size
        max_w = max_w or self.measure
        max_h = max_h or (PAGE_H - TOP - BOTTOM - 36)
        scale = min(max_w / iw, max_h / ih, 1.0)
        dw, dh = iw * scale, ih * scale
        self.ensure(dh + 14)
        tmp = self.asset_dir / f"{path.stem}-{uuid.uuid4().hex[:8]}.jpg"
        im.save(tmp, "JPEG", quality=90)
        # 2026-10-03 (Aaron): a figure that lands alone on a fresh page (the ch3 four-marks
        # block, the ch34 man-plan) is centered on the page horizontally AND vertically,
        # and nothing else is set on that page.
        if center_alone and abs(self.y - (PAGE_H - TOP)) < 0.5:
            # 2026-10-03c: horizontally on the text block (flush with the body margins when
            # full-measure), vertically on the page.
            x = self.left + (self.measure - dw) / 2
            y_bottom = (PAGE_H - dh) / 2
            self.c.drawImage(str(tmp), x, y_bottom, width=dw, height=dh)
            self.centered_figures = getattr(self, "centered_figures", []) + [(path.name, self.folio)]
            self.y = BOTTOM  # page is done; the next block opens a fresh page
            return
        self.y -= 6
        x = self.left + (self.measure - dw) / 2
        self.c.drawImage(str(tmp), x, self.y - dh, width=dw, height=dh)
        self.y -= dh + 12

    # ----- pages -----
    def page_cover_front(self) -> None:
        src = PRESS / "cloth-store" / "cover-front-walksteadfast-locked-2026-09-14.png"
        im = PILImage.open(src).convert("RGB")
        target_aspect = PAGE_W / PAGE_H
        w, h = im.size
        aspect = w / h
        if aspect > target_aspect:
            nw = int(h * target_aspect)
            left = (w - nw) // 2
            im = im.crop((left, 0, left + nw, h))
        else:
            nh = int(w / target_aspect)
            top = (h - nh) // 2
            im = im.crop((0, top, w, top + nh))
        tmp = self.asset_dir / "cover-front.jpg"
        im.save(tmp, "JPEG", quality=92)
        self.c.setFillColorRGB(*NAVY)
        self.c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        self.c.drawImage(str(tmp), 0, 0, width=PAGE_W, height=PAGE_H)
        self.cover_front = True
        self.show()
        self.physical = max(self.physical, 1)

    def page_title(self) -> None:
        self._fill_bone()
        cx = PAGE_W / 2
        y = PAGE_H - 2.5 * inch
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont("Playfair-Bold", 32)
        self.c.drawCentredString(cx, y, no_em("Steadfast Men"))
        y -= 34
        self.c.setStrokeColorRGB(*ACCENT)
        self.c.setLineWidth(1)
        self.c.line(cx - 36, y, cx + 36, y)
        y -= 28
        self.c.setFillColorRGB(*INK_SOFT)
        self.c.setFont("EBGaramond-Italic", 13)
        self.c.drawCentredString(cx, y, no_em("The way of Godly Men"))
        y -= 52
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont("Libre-Medium", 11)
        self.c.drawCentredString(cx, y, no_em("Wes Hart"))
        self.c.setFillColorRGB(*INK_SOFT)
        self.c.setFont("EBGaramond", 9)
        self.c.drawCentredString(cx, 1.25 * inch, no_em("walksteadfast.com"))
        self.show()

    # ----- copyright page: rendered from BOOK/00-copyright.md (2026-10-01) -----
    @staticmethod
    def _copyright_paragraphs(raw: str) -> list[dict]:
        """Split 00-copyright.md into paragraphs. Single newlines inside a paragraph are
        kept as line breaks (e.g. title / subtitle). '&nbsp;' paragraphs become spacers.
        A paragraph that is only **bold** becomes a small heading."""
        raw = smart_quotes(re.sub(r"</?div[^>]*>", "", raw))
        out: list[dict] = []
        for chunk in re.split(r"\n\s*\n", raw.strip()):
            chunk = chunk.strip()
            if not chunk:
                continue
            if chunk.replace("&nbsp;", "").strip() == "":
                out.append({"kind": "space"})
                continue
            lines = [ln.strip() for ln in chunk.splitlines() if ln.strip()]
            if len(lines) == 1 and re.fullmatch(r"\*\*[^*]+\*\*", lines[0]):
                out.append({"kind": "head", "text": lines[0].strip("*").strip()})
                continue
            out.append({"kind": "para", "lines": lines})
        return out

    @staticmethod
    def _rich_runs(text: str) -> list[list[tuple[str, str]]]:
        """**bold** / *italic* markdown -> words, each a list of (segment, style) so that
        punctuation hugging an italic title, e.g. "(*Title*, 1997)", gets no stray spaces."""
        runs: list[tuple[str, str]] = []
        pos = 0
        for m_ in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*", text):
            if m_.start() > pos:
                runs.append((text[pos : m_.start()], "r"))
            runs.append((m_.group(1) or m_.group(2), "b" if m_.group(1) else "i"))
            pos = m_.end()
        if pos < len(text):
            runs.append((text[pos:], "r"))
        words: list[list[tuple[str, str]]] = []
        cur: list[tuple[str, str]] = []
        for chunk, style in runs:
            for piece in re.split(r"(\s+)", chunk):
                if not piece:
                    continue
                if piece.isspace():
                    if cur:
                        words.append(cur)
                        cur = []
                else:
                    cur.append((piece, style))
        if cur:
            words.append(cur)
        return words

    def _draw_copyright(self, paras: list[dict], size: float, draw: bool, y0: float | None = None) -> float:
        fonts = {"r": "EBGaramond", "b": "EBGaramond-Bold", "i": "EBGaramond-Italic"}
        leading = size * 1.32
        left, right = 0.62 * inch, PAGE_W - 0.62 * inch
        width = right - left
        y = PAGE_H - TOP - 0.15 * inch if y0 is None else y0
        for p in paras:
            if p["kind"] == "space":
                y -= leading * 0.6
                continue
            if p["kind"] == "head":
                if draw:
                    self.c.setFillColorRGB(*NAVY)
                    self.c.setFont("Libre-Bold", size - 0.5)
                    self.c.drawString(left, y - size, p["text"])
                y -= leading + 1
                continue
            for src_line in p["lines"]:
                words = self._rich_runs(src_line)
                sp = self.c.stringWidth(" ", "EBGaramond", size)

                def wwidth(word: list[tuple[str, str]]) -> float:
                    return sum(self.c.stringWidth(t, fonts[st], size) for t, st in word)

                line: list[list[tuple[str, str]]] = []
                lw = 0.0

                def emit(ln: list[list[tuple[str, str]]]) -> None:
                    nonlocal y
                    if draw:
                        x = left
                        self.c.setFillColorRGB(*INK)
                        for word in ln:
                            for t, st in word:
                                self.c.setFont(fonts[st], size)
                                self.c.drawString(x, y - size, t)
                                x += self.c.stringWidth(t, fonts[st], size)
                            x += sp
                    y -= leading

                for word in words:
                    ww = wwidth(word)
                    add = ww if not line else ww + sp
                    if line and lw + add > width:
                        emit(line)
                        line, lw = [word], ww
                    else:
                        line.append(word)
                        lw += add
                if line:
                    emit(line)
            y -= leading * 0.45
        return y

    def page_copyright(self) -> None:
        """Copyright page = the book's own 00-copyright.md, verbatim (Robert Lewis note,
        full Biblica NIV notice, disclaimer). No hard-coded review-draft text. Shrinks the
        type until it fits one page. No no_em(): legal text prints exactly as written."""
        self._fill_bone()
        path = BOOK / "00-copyright.md"
        if not path.exists():
            self.missing.append("00-copyright.md")
            self.show()
            return
        paras = self._copyright_paragraphs(path.read_text(encoding="utf-8"))
        size = 8.5
        while size > 6.5 and self._draw_copyright(paras, size, draw=False) < BOTTOM:
            size -= 0.25
        self.copyright_size = size
        # 2026-10-01: set the block to the bottom of the page (traditional copyright verso).
        top = PAGE_H - TOP - 0.15 * inch
        end = self._draw_copyright(paras, size, draw=False, y0=top)
        drop = max(0.0, end - (BOTTOM + 0.1 * inch))
        self._draw_copyright(paras, size, draw=True, y0=top - drop)
        self.show()

    def page_dedication(self) -> None:
        text = (BOOK / "00-dedication.md").read_text(encoding="utf-8")
        body = re.sub(r"^#\s+Dedication\s*\n+", "", text).strip()
        parts = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        self._fill_bone()
        self.left = GUTTER
        self.right = PAGE_W - OUTSIDE
        self.measure = self.right - self.left
        self.y = PAGE_H - 2.6 * inch
        self.tracked("DEDICATION", self.left + self.measure / 2 - 42, self.y, "Libre-Medium", 8, ACCENT, 2.2)
        self.y -= 36
        parts = [smart_quotes(p) for p in parts]
        for para in parts:
            if para == "Dad":
                self.y -= 16
                self.c.setFillColorRGB(*INK)
                self.c.setFont("EBGaramond-Italic", 12)
                self.c.drawString(self.left, self.y, para)
                continue
            self.para(para, indent=0)
        self.show()

    def page_contents(self, page_map: dict[str, int]) -> None:
        raw = (BOOK / "00-contents.md").read_text(encoding="utf-8")
        # Dedication just called show(); canvas is already on a fresh blank page.
        self.running = "Contents"
        self.number_folios = True
        self.folio = 1
        self._fill_bone()
        self._margins_for_folio()
        self._footer()
        self.y = PAGE_H - TOP
        self.page_map["Contents"] = self.folio

        self.c.setFillColorRGB(*NAVY)
        self.c.setFont("Playfair-Bold", 22)
        self.c.drawString(self.left, self.y - 22, no_em("Contents"))
        self.y -= 38
        self.c.setFillColorRGB(*ACCENT)
        self.c.rect(self.left, self.y, 42, 2, fill=1, stroke=0)
        self.y -= 20

        expect_part_subtitle = False
        part_subtitles = {no_em(sub) for _lab, sub in PARTS.values()}
        for line in raw.splitlines():
            line = line.rstrip()
            if not line or line.startswith("# "):
                continue
            # Atomic Habits / Extreme Ownership PART bands — never markdown ##
            if re.match(r"^PART\s+(ONE|TWO|THREE|FOUR|FIVE|I{1,3}|IV|V|\d+)\b", line, re.I):
                self.ensure(40)
                self.y -= 16
                self.c.setFillColorRGB(*NAVY)
                self.c.setFont("Libre-Bold", 10.5)
                self.c.drawString(self.left, self.y - 11, no_em(line.strip()).upper())
                self.y -= 16
                expect_part_subtitle = True
                continue
            label = smart_quotes(no_em(line.strip()).strip("*").strip())
            if expect_part_subtitle or label in part_subtitles:
                expect_part_subtitle = False
                self.ensure(18)
                self.c.setFillColorRGB(*NAVY)
                self.c.setFont("Libre-Medium", 9)
                self.c.drawString(self.left, self.y - 10, label)
                self.y -= 18
                continue
            if label.startswith(CONTENTS_NOTE_PREFIXES):
                self.ensure(28)
                self.y -= 8
                self.c.setFillColorRGB(*INK_SOFT)
                self.c.setFont("EBGaramond-Italic", 9)
                for wrap_ln in self.wrap(label, "EBGaramond-Italic", 9, self.measure):
                    self.c.drawString(self.left, self.y - 10, wrap_ln)
                    self.y -= 12
                continue
            self.ensure(15)
            folio = None
            if label in page_map:
                folio = page_map[label]
            else:
                m = re.match(r"^(\d+)\.\s+(.*)$", label)
                if m:
                    folio = page_map.get(m.group(1)) or page_map.get(m.group(2).strip()) or page_map.get(label)
                elif label == "Introduction":
                    folio = page_map.get("Introduction")
                elif label == "Dedication":
                    folio = None
                elif label == "Contents":
                    folio = 1
            self.c.setFillColorRGB(*INK)
            self.c.setFont("EBGaramond", 10)
            self.c.drawString(self.left, self.y - 10, label)
            if folio:
                fs = str(folio)
                self.c.drawRightString(self.right, self.y - 10, fs)
                lw = self.c.stringWidth(label, "EBGaramond", 10)
                rw = self.c.stringWidth(fs, "EBGaramond", 10)
                x = self.left + lw + 6
                end = self.right - rw - 6
                self.c.setFillColorRGB(*RULE)
                self.c.setFont("EBGaramond", 7)
                while x < end:
                    self.c.drawString(x, self.y - 10, ".")
                    x += 3.5
            self.y -= 14.5

    def page_intro(self) -> None:
        title, num, blocks = parse_md(BOOK / "00-introduction.md")
        self.running = "Introduction"
        self.advance(blank_if_verso=_force_recto("intro"))
        if not self.on_recto and _force_recto("intro"):
            self.advance()
        self.page_map["Introduction"] = self.folio
        self.tracked("INTRODUCTION", self.left, self.y - 8, "Libre-Bold", 8, ACCENT, 2.4)
        self.y -= 28
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont("Playfair-Bold", TITLE_SIZE)
        self.c.drawString(self.left, self.y - TITLE_SIZE, no_em("Introduction"))
        self.y -= TITLE_SIZE + 8
        self.c.setFillColorRGB(*ACCENT)
        self.c.rect(self.left, self.y, 42, 2.2, fill=1, stroke=0)
        self.y -= 18
        self._noindent = True
        for block in blocks:
            if block["type"] == "epigraph":
                self.epigraph(block["cite"], block["text"])
            elif block["type"] == "break":
                self.section_break()
            elif block["type"] == "p" and LAYOUT == "baa":
                self.para_baa(block["text"])
            elif block["type"] == "margin":
                self.margin_block(block["cite"], block["text"])
            elif block["type"] == "h2":
                self.heading(block["text"], level=2)
            elif block["type"] == "h3":
                self.heading(block["text"], level=3)
            elif block["type"] == "p":
                self.para(block["text"])
            elif block["type"] == "notes":
                self.notes(block["lines"])


    def page_section(self, label: str, filename: str) -> None:
        """Back-matter section (About / Condensed) — intro-style opener, no CHAPTER N."""
        title, _num, blocks = parse_md(BOOK / filename)
        self.running = title
        self.advance(blank_if_verso=_force_recto("section"))
        if not self.on_recto and _force_recto("section"):
            self.advance()
        self.page_map[title] = self.folio
        self._section_head(label, title)
        for block in blocks:
            if block["type"] == "h2":
                self.heading(block["text"], level=2)
                continue
            if block["type"] == "h3":
                self.heading(block["text"], level=3)
                continue
            if block["type"] != "p":
                continue
            raw = block["text"]
            clean = clean_inline_md(raw.replace("&nbsp;", ""))
            if not clean:
                continue
            # numbered / bullet lines: keep as paragraphs with less indent
            if re.match(r"^(\d+\.|[-*])\s+", clean):
                clean = re.sub(r"^[-*]\s+", "\u2022 ", clean)  # bullet glyph, not a hyphen
                self.para(clean, indent=0, size=10, leading=13, after=0.08)
                self._noindent = True
            elif LAYOUT == "baa":
                self.para_baa(clean)
            else:
                self.para(clean)

    def part_page(self, label: str, subtitle: str) -> None:
        self.running = label
        self.advance(blank_if_verso=_force_recto("part"))
        if not self.on_recto and _force_recto("part"):
            self.advance()
        self._after_part = _force_recto("part")  # part page keeps a blank back; next chapter opens recto
        cx = (self.left + self.right) / 2
        self.y = PAGE_H / 2 + 36
        self.c.setFillColorRGB(*ACCENT)
        self.c.setFont("Libre-Medium", 9)
        self.c.drawCentredString(cx, self.y, no_em(label.upper()))
        self.y -= 28
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont("Playfair-Bold", 22)
        for ln in self.wrap(no_em(subtitle), "Playfair-Bold", 22, self.measure - 24):
            self.c.drawCentredString(cx, self.y, ln)
            self.y -= 28
        self.c.setStrokeColorRGB(*ACCENT)
        self.c.setLineWidth(1)
        self.c.line(cx - 28, self.y, cx + 28, self.y)

    def chapter_open(self, num: int, title: str) -> None:
        self.running = title
        recto = _force_recto("chapter") or getattr(self, "_after_part", False)
        self._after_part = False
        self.advance(blank_if_verso=recto)
        if not self.on_recto and recto:
            self.advance()
        self.page_map[f"{num}. {title}"] = self.folio
        self.page_map[str(num)] = self.folio
        self.page_map[title] = self.folio
        mark = ART / "opener-mark.png"
        if mark.exists():
            im = PILImage.open(mark).convert("RGBA")
            tw = 0.42 * inch
            scale = tw / im.size[0]
            dw, dh = im.size[0] * scale, im.size[1] * scale
            bg = PILImage.new("RGB", im.size, tuple(int(x * 255) for x in BONE))
            bg.paste(im, mask=im.split()[-1])
            tmp = self.asset_dir / "opener-mark.jpg"
            bg.save(tmp, "JPEG", quality=95)
            self.c.drawImage(str(tmp), self.left, self.y - dh, width=dw, height=dh)
            self.y -= dh + 10
        else:
            self.missing.append("opener-mark.png")
        self.tracked(no_em(f"CHAPTER {num}"), self.left, self.y - 8, "Libre-Bold", 8, ACCENT, 2.4)
        self.y -= 26
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont("Playfair-Bold", TITLE_SIZE)
        for ln in self.wrap(no_em(title), "Playfair-Bold", TITLE_SIZE, self.measure):
            self.ensure(TITLE_SIZE + 6)
            self.c.drawString(self.left, self.y - TITLE_SIZE, ln)
            self.y -= TITLE_SIZE + 4
        self.y -= 4
        self.c.setFillColorRGB(*ACCENT)
        self.c.rect(self.left, self.y, 42, 2.2, fill=1, stroke=0)
        self.y -= 18
        self._noindent = True


    def closer_art(self, num: int) -> None:
        """Deprecated: PNG closer boxes disabled. Kept for reference only."""
        path = ART / f"{num:02d}-closer-box.png"
        if not path.exists():
            self.missing.append(path.name)
            return
        if self.y < PAGE_H - TOP - 100:
            self.advance()
        self.image(path, max_w=self.measure, max_h=PAGE_H - TOP - BOTTOM - 24)
        if num == 35:
            self.closer_35 = True

    def closer_box(
        self,
        num: int,
        lines: list[str],
        body_size: float = 10,
        body_leading: float = 13,
        max_write: int = 3,
        measure_only: bool = False,
    ) -> float:
        """Gold-standard Your Turn closer for EVERY chapter (typeset, not PNG).

        Layout: light bone panel, dark left rail + ticks, header `NN · YOUR TURN`,
        four sections (NAME IT / DO THIS WEEK / TELL A BROTHER / CARRY THIS),
        thin rules, 1–2 write-in lines from :::notes (not under CARRY THIS),
        shaded CARRY THIS band with larger italic carry line.
        """
        sections = parse_closer_sections(lines)
        if not sections:
            return 0.0

        pad_x = 12
        pad_t = 14
        pad_b = 12
        rail_w = 1.6
        rail_inset = 8
        tick_w = 7
        label_size = 8
        carry_size = 12
        carry_leading = 15
        header_size = 8.5
        rule_gap = 8
        section_gap = 10

        panel_left = self.left
        panel_right = self.right
        panel_w = panel_right - panel_left
        text_left = panel_left + rail_inset + 12
        text_w = panel_right - pad_x - text_left

        # Measure content height
        h = pad_t
        h += header_size + 10  # header
        measured: list[dict] = []
        for i, sec in enumerate(sections):
            is_carry = sec["key"] == "carry this"
            top = h
            h += label_size + 5
            font = "EBGaramond-Italic" if is_carry else "EBGaramond"
            size = carry_size if is_carry else body_size
            lead = carry_leading if is_carry else body_leading
            body_lines = self.wrap(no_em(sec["body"]), font, size, text_w) if sec["body"] else []
            body_h = lead * len(body_lines)
            h += body_h
            prompt_h = 0
            write_n = 0 if is_carry else min(max_write, int(sec.get("write_in") or 0))
            if sec.get("prompt") and not is_carry:
                prompt_h = 12
                h += 6 + prompt_h
            if write_n:
                h += 4 + write_n * 14
            bottom = h
            measured.append(
                {
                    "sec": sec,
                    "top": top,
                    "body_lines": body_lines,
                    "body_h": body_h,
                    "write_n": write_n,
                    "prompt_h": prompt_h,
                    "bottom": bottom,
                    "is_carry": is_carry,
                }
            )
            if i < len(sections) - 1:
                h += rule_gap + 1 + section_gap
        h += pad_b
        if measure_only:
            return h

        # Prefer keeping the whole box on one page
        if self.y - h < BOTTOM + 18:
            self.advance()

        # If still too tall for a full page, allow modest shrink of gaps is skipped —
        # content should fit; worst case it may run long (rare).
        box_top = self.y
        box_bottom = self.y - h
        # Panel fill
        self.c.setFillColorRGB(*CLOSER_PANEL)
        self.c.setStrokeColorRGB(*CLOSER_RULE)
        self.c.setLineWidth(0.7)
        self.c.roundRect(panel_left, box_bottom, panel_w, h, 2, fill=1, stroke=1)

        # CARRY band first (under last section)
        last = measured[-1]
        if last["is_carry"]:
            band_top_y = box_top - (last["top"] - 6)
            # y decreases downward: band from slightly above carry label to box bottom+1
            band_y = box_bottom + 1
            band_h = band_top_y - band_y
            if band_h > 0:
                self.c.setFillColorRGB(*CARRY_BAND)
                self.c.rect(panel_left + 1, band_y, panel_w - 2, band_h, fill=1, stroke=0)

        # Iron rail
        rail_x = panel_left + rail_inset
        self.c.setFillColorRGB(*CLOSER_RAIL)
        self.c.rect(rail_x, box_bottom + 6, rail_w, h - 12, fill=1, stroke=0)

        # Header: NN · YOUR TURN
        header = f"{num:02d} · YOUR TURN"
        hy = box_top - pad_t - header_size
        self.tracked(no_em(header), text_left, hy, "Libre-Bold", header_size, CLOSER_LABEL, tracking=1.8)

        for i, m in enumerate(measured):
            sec = m["sec"]
            y_label = box_top - m["top"] - label_size
            # tick
            tick_y = y_label + label_size * 0.35
            self.c.setFillColorRGB(*CLOSER_RAIL)
            self.c.rect(rail_x - 0.5, tick_y - 1.1, tick_w, 2.4, fill=1, stroke=0)
            # label
            self.tracked(
                sec["label"],
                text_left,
                y_label,
                "Libre-Bold",
                label_size,
                CLOSER_LABEL,
                tracking=1.6,
            )
            # body
            yy = y_label - 5
            if m["is_carry"]:
                font, size, lead = "EBGaramond-Italic", carry_size, carry_leading
                color = INK
            else:
                font, size, lead = "EBGaramond", body_size, body_leading
                color = INK
            for bl in m["body_lines"]:
                yy -= lead
                self.c.setFillColorRGB(*color)
                self.c.setFont(font, size)
                self.c.drawString(text_left, yy, bl)

            # optional italic prompt + write-in rules
            if not m["is_carry"]:
                if sec.get("prompt"):
                    yy -= 10
                    self.c.setFillColorRGB(*INK_SOFT)
                    self.c.setFont("EBGaramond-Italic", 9.5)
                    self.c.drawString(text_left, yy, no_em(sec["prompt"]))
                for _ in range(m["write_n"]):
                    yy -= 14
                    self.c.setStrokeColorRGB(*CLOSER_RULE)
                    self.c.setLineWidth(0.7)
                    self.c.line(text_left, yy, panel_right - pad_x, yy)

            # section rule (between sections, not after last)
            if i < len(measured) - 1:
                rule_y = box_top - m["bottom"] - rule_gap
                self.c.setStrokeColorRGB(*CLOSER_RULE)
                self.c.setLineWidth(0.6)
                self.c.line(text_left, rule_y, panel_right - pad_x, rule_y)

        # redraw rail over carry band
        self.c.setFillColorRGB(*CLOSER_RAIL)
        self.c.rect(rail_x, box_bottom + 6, rail_w, h - 12, fill=1, stroke=0)

        self.y = box_bottom - 10
        if num == 35:
            self.closer_35 = True

    def closer_text(self, lines: list[str]) -> None:
        """Back-compat alias — always use gold-standard closer_box (num unknown -> 0)."""
        # Prefer callers pass through closer_box(num, lines)
        self.closer_box(0, lines)

    def render_chapter_blocks(self, num: int, blocks: list[dict]) -> None:
        fig = FIGURES.get(num)
        fig_done = False
        for block in blocks:
            if block["type"] == "closer":
                if num == MANPLAN_CHAPTER and fig and not fig_done:
                    # 2026-10-01: if most of the page is still free, shrink the man-plan to fit it
                    # instead of leaving the page ~80% empty. Never below 60% of full height.
                    full_h = PAGE_H - TOP - BOTTOM - 40
                    avail = self.y - (BOTTOM + 14) - 26
                    max_h = avail if avail >= 0.60 * full_h else full_h
                    self.image(fig, max_w=self.measure, max_h=max_h, center_alone=True)
                    fig_done = True
                # Always typeset gold-standard closer box from markdown (never PNG split)
                self.closer_box(num, block["lines"])
                continue
            if block["type"] == "epigraph":
                self.epigraph(block["cite"], block["text"])
                continue
            if block["type"] == "break":
                self.section_break()
                continue
            if block["type"] == "margin":
                self.margin_block(block["cite"], block["text"])
                continue
            if block["type"] == "notes":
                self.notes(block["lines"])
                continue
            if block["type"] == "h2":
                self.heading(block["text"], level=2)
                continue
            if block["type"] == "h3":
                self.heading(block["text"], level=3)
                continue
            if block["type"] == "p":
                if LAYOUT == "baa":
                    self.para_baa(block["text"])
                else:
                    self.para(block["text"])
                if (
                    num == FIG3_CHAPTER
                    and fig
                    and not fig_done
                    and any(
                        # 2026-10-03: the parsed paragraph has curly apostrophes (God’s) while
                        # the triggers are typed straight, so compare with quotes normalized.
                        t.replace("\u2019", "'") in block["text"].replace("\u2019", "'")
                        for t in FIG3_TRIGGERS
                    )
                ):
                    self.image(fig, max_w=min(self.measure, 3.1 * inch), max_h=3.3 * inch)
                    fig_done = True
                    self._noindent = True
        if fig and not fig_done and num == FIG3_CHAPTER:
            self.image(fig, max_w=min(self.measure, 3.1 * inch), max_h=3.3 * inch, center_alone=True)

    def _section_head(self, label: str, title: str) -> None:
        self.tracked(label.upper(), self.left, self.y - 8, "Libre-Bold", 8, ACCENT, 2.4)
        self.y -= 28
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont("Playfair-Bold", TITLE_SIZE)
        self.c.drawString(self.left, self.y - TITLE_SIZE, no_em(title))
        self.y -= TITLE_SIZE + 8
        self.c.setFillColorRGB(*ACCENT)
        self.c.rect(self.left, self.y, 42, 2.2, fill=1, stroke=0)
        self.y -= 18
        self._noindent = True

    def _open_section(self, label: str, title: str) -> None:
        self.running = title
        self.advance(blank_if_verso=_force_recto("section"))
        if not self.on_recto and _force_recto("section"):
            self.advance()
        self.page_map[title] = self.folio
        self._section_head(label, title)

    @staticmethod
    def _split_entries(raw: str) -> tuple[str, list[tuple[int, str, list[str]]]]:
        """Split a back-matter file into (title, intro lines, [(num, chapter title, lines)])."""
        lines = raw.splitlines()
        title = re.sub(r"^#\s+", "", lines[0]).strip() if lines else ""
        intro: list[str] = []
        entries: list[tuple[int, str, list[str]]] = []
        for ln in lines[1:]:
            m = re.match(r"^##\s+(\d+)\.\s+(.+?)\s*$", ln)
            if m:
                entries.append((int(m.group(1)), smart_quotes(m.group(2)), []))
            elif entries:
                entries[-1][2].append(ln)
            else:
                intro.append(ln)
        return title, intro, entries

    def _intro_paras(self, intro: list[str]) -> None:
        for chunk in re.split(r"\n\s*\n", "\n".join(intro)):
            t = " ".join(x.strip() for x in chunk.splitlines()).strip()
            if t:
                self.para_baa(smart_quotes(no_em(t)))

    def page_yourturn(self, label: str, filename: str) -> None:
        """Back-of-book Your Turn: short intro, then one page per chapter (typeset closer_box)."""
        title, intro, entries = self._split_entries((BOOK / filename).read_text(encoding="utf-8"))
        self._open_section(label, title)
        self._intro_paras(intro)
        for num, ctitle, lines in entries:
            self.running = "Your Turn"
            self.advance()
            self.page_map[f"yt-{num}"] = self.folio
            self.tracked(no_em(f"CHAPTER {num}"), self.left, self.y - 8, "Libre-Bold", 7.5, ACCENT, 2.2)
            self.y -= 22
            self.c.setFillColorRGB(*NAVY)
            for ln in self.wrap(no_em(ctitle), "Playfair-Bold", 14, self.measure):
                self.c.setFont("Playfair-Bold", 14)
                self.c.drawString(self.left, self.y - 14, ln)
                self.y -= 18
            self.y -= 8
            # One page per chapter (2026-10-04): fit the box to the space left under
            # the heading. Step down write-in lines (3 -> 2), then body size, before
            # ever letting the box jump to a second page.
            box_lines = ["## Your Turn", *lines]
            avail = self.y - (BOTTOM + 18)
            fit = dict(body_size=10, body_leading=13, max_write=3)
            for opt in (
                dict(body_size=10, body_leading=13, max_write=3),
                dict(body_size=10, body_leading=13, max_write=2),
                dict(body_size=9.5, body_leading=12.4, max_write=2),
                dict(body_size=9.2, body_leading=11.8, max_write=2),
                dict(body_size=9.2, body_leading=11.8, max_write=1),
            ):
                fit = opt
                if self.closer_box(num, box_lines, measure_only=True, **opt) <= avail:
                    break
            else:
                print(f"WARN: Your Turn {num} does not fit one page even at the tightest setting", file=sys.stderr)
            self.closer_box(num, box_lines, **fit)
            fig = FIGURES.get(num)
            if num == MANPLAN_CHAPTER and fig:
                self.advance()
                self.image(fig, max_w=self.measure, max_h=PAGE_H - TOP - BOTTOM - 40, center_alone=True)

    # ----- Small-Group Guide + Scripture Notes (2026-10-12e) -----
    GUIDE_LABELS = (
        ("Host's note.", "FOR THE HOST"), ("Open.", "OPEN"), ("Read aloud.", "READ ALOUD"),
        ("Talk.", "TALK"), ("Going deeper.", "GOING DEEPER"), ("Before you leave.", "BEFORE YOU LEAVE"),
    )

    def _label_panel(self, rows, *, size=9.6, leading=12.6, measure_only=False) -> float:
        """Your Turn-style panel (bone fill, iron rail, rust ticks + tracked labels, light rules).
        rows: [(label, [(kind, text)])], kind 'p' body, 'i' italic note, 'n' numbered item."""
        pad_t, pad_b, rail_inset, label_size, gap = 12, 10, 8, 7.6, 8
        x0, x1 = self.left, self.right
        tl = x0 + rail_inset + 12
        tw = x1 - 12 - tl
        hang = 12
        meas = []
        h = pad_t
        for r, (label, items) in enumerate(rows):
            top = h
            h += label_size + 4
            lines = []
            for kind, text in items:
                text = smart_quotes(no_em(clean_inline_md(text)))
                if kind == "n":
                    mm = re.match(r"^(\d+)\.\s+(.*)$", text)
                    num, body = (mm.group(1) + ".", mm.group(2)) if mm else ("", text)
                    for k, ln in enumerate(self.wrap(body, "EBGaramond", size, tw - hang)):
                        lines.append(("EBGaramond", ln, tl + hang, num if k == 0 else ""))
                else:
                    f = "EBGaramond-Italic" if kind == "i" else "EBGaramond"
                    for ln in self.wrap(text, f, size, tw):
                        lines.append((f, ln, tl, ""))
                lines.append(None)  # small gap between items
            if lines:
                lines.pop()
            nh = sum(leading if l else 3 for l in lines)
            h += nh
            meas.append((top, label, lines, h))
            if r < len(rows) - 1:
                h += gap + 1 + gap
        h += pad_b
        if measure_only:
            return h
        top_y = self.y
        c = self.c
        c.setFillColorRGB(*CLOSER_PANEL); c.setStrokeColorRGB(*CLOSER_RULE); c.setLineWidth(0.7)
        c.roundRect(x0, top_y - h, x1 - x0, h, 2, fill=1, stroke=1)
        rx = x0 + rail_inset
        c.setFillColorRGB(*CLOSER_RAIL)
        c.rect(rx, top_y - h + 6, 1.6, h - 12, fill=1, stroke=0)
        for r, (top, label, lines, bottom) in enumerate(meas):
            yl = top_y - top - label_size
            c.setFillColorRGB(*CLOSER_RAIL)
            c.rect(rx - 0.5, yl + label_size * 0.35 - 1.1, 7, 2.4, fill=1, stroke=0)
            self.tracked(label, tl, yl, "Libre-Bold", label_size, CLOSER_LABEL, tracking=1.5)
            yy = yl - 4
            for l in lines:
                if l is None:
                    yy -= 3
                    continue
                f, ln, x, num = l
                yy -= leading
                c.setFillColorRGB(*(INK_SOFT if f.endswith("Italic") else INK))
                if num:
                    c.setFont("Libre-Medium", size - 1.6)
                    c.setFillColorRGB(*CLOSER_LABEL)
                    c.drawString(tl, yy, num)
                    c.setFillColorRGB(*INK)
                c.setFont(f, size)
                c.drawString(x, yy, ln)
            if r < len(meas) - 1:
                ry = top_y - bottom - gap
                c.setStrokeColorRGB(*CLOSER_RULE); c.setLineWidth(0.6)
                c.line(tl, ry, x1 - 12, ry)
        self.y = top_y - h - 14
        return h

    def _fit_panel(self, rows, reserve: float = 0.0) -> None:
        """Keep a panel whole: move to a new page if it won't fit; shrink type only if a full page can't hold it."""
        full = PAGE_H - TOP - BOTTOM - 18 - reserve
        opt = dict(size=9.6, leading=12.6)
        for o in (dict(size=9.6, leading=12.6), dict(size=9.3, leading=12.0), dict(size=9.0, leading=11.4)):
            opt = o
            if self._label_panel(rows, measure_only=True, **o) <= full:
                break
        return opt

    def _guide_session(self, head: str, paras: list[str]) -> None:
        m = re.match(r"^Chapter\s+(\d+)\.\s+(.+?)(?:,\s+(first|second)\s+meeting)?(?:\s+\(class week (\d+)\))?\s*$", head)
        num, title, meet, week = m.groups() if m else ("", head, None, None)
        kicker = " · ".join(x for x in (f"CHAPTER {num}" if num else "", f"{meet.upper()} MEETING" if meet else "",
                                         f"CLASS WEEK {week}" if week else "") if x)
        rows, cur = [], None
        for t in paras:
            for pref, lab in self.GUIDE_LABELS:
                if t.startswith(pref):
                    rest = t[len(pref):].strip()
                    cur = (lab, [])
                    rows.append(cur)
                    if rest:
                        cur[1].append(("i" if lab in ("FOR THE HOST", "GOING DEEPER") else "p", rest))
                    break
            else:
                if cur is None:
                    cur = ("FOR THE HOST", []); rows.append(cur)
                cur[1].append(("n" if re.match(r"^\d+\.\s", t) else "p", t))
        title_lines = self.wrap(no_em(smart_quotes(title)), "Playfair-Bold", 14, self.measure)
        head_h = 22 + 18 * len(title_lines) + 10
        opt = self._fit_panel(rows, reserve=head_h)
        need = head_h + self._label_panel(rows, measure_only=True, **opt)
        if self.y - need < BOTTOM + 18:
            self.advance()
        self.tracked(no_em(kicker), self.left, self.y - 8, "Libre-Bold", 7.5, ACCENT, 2.2)
        self.y -= 22
        self.c.setFillColorRGB(*NAVY)
        for ln in title_lines:
            self.c.setFont("Playfair-Bold", 14)
            self.c.drawString(self.left, self.y - 14, ln)
            self.y -= 18
        self.y -= 10
        self._label_panel(rows, **opt)

    def page_guide(self, label: str, filename: str) -> None:
        """Small-Group Guide: leader intro, then one consistent panel per meeting, kept whole."""
        raw = (BOOK / filename).read_text(encoding="utf-8").splitlines()
        title = re.sub(r"^#\s+", "", raw[0]).strip()
        secs: list[tuple[int, str, list[str]]] = [(0, "", [])]
        buf: list[str] = []

        def flush():
            t = " ".join(x.strip() for x in buf).strip()
            if t:
                secs[-1][2].append(t)
            buf.clear()

        for ln in raw[1:]:
            mm = re.match(r"^(#{2,3})\s+(.+?)\s*$", ln)
            if mm:
                flush(); secs.append((len(mm.group(1)), mm.group(2), [])); continue
            if not ln.strip() or re.match(r"^(\d+\.|[-*])\s+", ln.strip()):
                flush()
            buf.append(ln)
            if not ln.strip():
                buf.clear()
        flush()
        self._open_section(label, title)
        for t in secs[0][2]:
            self.para_baa(smart_quotes(no_em(t)))
        for lvl, head, paras in secs[1:]:
            self.running = title
            if lvl == 3:
                self._guide_session(head, paras)
                continue
            pm = re.match(r"^(Part \w+):\s+(.+)$", head)
            bullets = [p for p in paras if re.match(r"^[-*]\s", p)]
            if pm:
                self.advance()
                self.tracked(no_em(pm.group(1).upper()), self.left, self.y - 8, "Libre-Bold", 8, ACCENT, 2.4)
                self.y -= 24
                self.c.setFillColorRGB(*NAVY)
                for ln in self.wrap(no_em(pm.group(2)), "Playfair-Bold", 17, self.measure):
                    self.c.setFont("Playfair-Bold", 17)
                    self.c.drawString(self.left, self.y - 17, ln)
                    self.y -= 21
                self.y -= 4
                self.c.setFillColorRGB(*ACCENT)
                self.c.rect(self.left, self.y, 42, 2.2, fill=1, stroke=0)
                self.y -= 16
                self._noindent = True
                for t in paras:
                    self.para_baa(smart_quotes(no_em(t)))
                self.y -= 16
                continue
            if bullets:
                rows = []
                for b in bullets:
                    b = re.sub(r"^[-*]\s+", "", b)
                    bm = re.match(r"^(.+?)\s+\((\d+ minutes)\)\.\s*(.*)$", b)
                    if bm:
                        rows.append((f"{bm.group(1).upper()} · {bm.group(2).upper()}", [("p", bm.group(3))]))
                    else:
                        rows.append(("", [("p", b)]))
                opt = self._fit_panel(rows)
                lead_in = sum(len(self.wrap(t, "EBGaramond", BODY_SIZE, self.measure)) for t in paras if not re.match(r"^[-*]\s", t))
                if self.y - (40 + lead_in * BODY_LEADING + self._label_panel(rows, measure_only=True, **opt)) < BOTTOM + 18:
                    self.advance()  # keep the heading, its lead-in and the panel together
                self.heading(head, level=2)
                self._noindent = True
                for t in paras:
                    if not re.match(r"^[-*]\s", t):
                        self.para_baa(smart_quotes(no_em(t)))
                self.y -= 8
                self._label_panel(rows, **opt)
                continue
            if head.startswith("Twenty Minutes"):
                self.advance()
            self.y -= 6
            self.heading(head, level=2)
            self.y -= 3
            self._noindent = True
            for t in paras:
                self.para_baa(smart_quotes(no_em(t)))
            self.y -= 4

    def page_scripture_notes(self, label: str, filename: str) -> None:
        """Back-of-book Scripture notes (2026-10-12e): chapter kicker + title, opening verse set
        apart, then a two-column list (phrase left, reference right), each chapter kept whole."""
        title, intro, entries = self._split_entries((BOOK / filename).read_text(encoding="utf-8"))
        self._open_section(label, title)
        for chunk in re.split(r"\n\s*\n", "\n".join(intro)):
            t = " ".join(x.strip() for x in chunk.splitlines()).strip()
            if t:
                self.para(smart_quotes(no_em(clean_inline_md(t))), font="EBGaramond-Italic", size=9.5, leading=12.6, indent=0, after=0.5, color=INK_SOFT)
        c = self.c
        fs, lead = 9.2, 11.6
        for idx, (num, ctitle, lines) in enumerate(entries):
            items = [" ".join(x.split()) for x in re.split(r"\n\s*\n", "\n".join(lines)) if x.strip()]
            ref_w = 0.40 * self.measure
            ph_w = self.measure - ref_w - 10
            opening, rows = None, []
            for it in items:
                t = smart_quotes(no_em(clean_inline_md(it)))
                om = re.match(r"^Opening verse:\s*(.+?)\.?$", t)
                if om:
                    opening = om.group(1)
                    continue
                sm = re.match(r"^(\u201c.+\u201d|\".+\"):\s*(.+?)\.?$", t)
                rows.append((sm.group(1), sm.group(2)) if sm else (t, ""))
            def row_lines(ph, ref):
                return (self.wrap(ph, "EBGaramond-Italic", fs, ph_w), self.wrap(ref, "EBGaramond", fs, ref_w) if ref else [])
            laid = [row_lines(*r) for r in rows]
            body_h = sum(max(len(a), len(b)) * lead + 4 for a, b in laid)
            head_h = 10 + 18 + (16 if opening else 0) + 8
            pm = self.page_map.get(str(num)) if num else self.page_map.get("Introduction")
            ensure_h = head_h + sum(max(len(a), len(b)) * lead + 4 for a, b in laid[:3])  # heading + first rows together
            if self.y - ensure_h < BOTTOM + 14:
                self.advance()
            elif idx:
                self.y -= 4
                c.setStrokeColorRGB(*CLOSER_RULE); c.setLineWidth(0.6)
                c.line(self.left, self.y, self.right, self.y)
                self.y -= 12
            kick = (f"CHAPTER {num}" if num else "BEFORE CHAPTER 1") + (f" · PAGE {pm}" if pm else "")
            self.tracked(no_em(kick), self.left, self.y - 7, "Libre-Bold", 7, ACCENT, 1.8)
            self.y -= 12
            c.setFillColorRGB(*NAVY); c.setFont("Libre-Medium", 10.5)
            c.drawString(self.left, self.y - 10.5, no_em(ctitle))
            self.y -= 18
            if opening:
                c.setFillColorRGB(*CLOSER_LABEL)
                self.tracked("OPENING VERSE", self.left, self.y - 8, "Libre-Bold", 6.8, CLOSER_LABEL, 1.4)
                c.setFillColorRGB(*INK); c.setFont("EBGaramond", fs)
                c.drawString(self.left + self._tracked_width("OPENING VERSE", "Libre-Bold", 6.8, 1.4) + 8, self.y - 8.5, opening)
                self.y -= 16
            self.y -= 2
            for (a, b) in laid:
                n = max(len(a), len(b))
                self.ensure(n * lead + 2)
                for k in range(n):
                    yy = self.y - fs - k * lead
                    if k < len(a):
                        c.setFillColorRGB(*INK); c.setFont("EBGaramond-Italic", fs)
                        c.drawString(self.left, yy, a[k])
                    if k < len(b):
                        c.setFillColorRGB(*NAVY); c.setFont("EBGaramond", fs)
                        c.drawRightString(self.right, yy, b[k])
                self.y -= n * lead + 4
            self.y -= 4

    def page_back(self) -> None:
        self.show()  # finish last chapter page
        # 2026-10-01: keep the even-page signature. The back cover must be an even physical
        # page so the PDF has an even count; if it would land odd, insert one blank bone page.
        if self.c.getPageNumber() % 2 == 1:
            self._fill_bone()
            self.show()
            self.pad_pages = getattr(self, "pad_pages", 0) + 1
        # Prefer signed back panel from a-wrap.png (back | spine | front).
        # Front cover: walksteadfast.com locked Wes Hart hardcover (2026-09-14).
        wrap_path = PRESS / "a-wrap.png"
        used_wrap = False
        if wrap_path.exists():
            wrap = PILImage.open(wrap_path).convert("RGB")
            DPI = 300
            trim_w, trim_h = 6 * DPI, 9 * DPI
            bleed_l, bleed_t = 38, 38
            back = wrap.crop((bleed_l, bleed_t, bleed_l + trim_w, bleed_t + trim_h))
            # Fit 1800x2700 into 6x9 page (exact aspect)
            tmp = self.asset_dir / "cover-back-from-wrap.jpg"
            back.save(tmp, "JPEG", quality=92)
            self.c.setFillColorRGB(*NAVY)
            self.c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
            self.c.drawImage(str(tmp), 0, 0, width=PAGE_W, height=PAGE_H)
            used_wrap = True
            self.used_wrap_back = True
        if not used_wrap:
            self.c.setFillColorRGB(*NAVY)
            self.c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
            cx = PAGE_W / 2
            y = PAGE_H - 2.3 * inch
            self.c.setFillColorRGB(*GOLD)
            self.c.setFont("Playfair-Bold", 28)
            self.c.drawCentredString(cx, y, no_em("STEADFAST"))
            y -= 34
            self.c.drawCentredString(cx, y, no_em("MEN"))
            y -= 26
            self.c.setStrokeColorRGB(*GOLD)
            self.c.setLineWidth(0.7)
            self.c.line(cx - 40, y, cx + 40, y)
            y -= 26
            self.c.setFillColorRGB(*BONE)
            self.c.setFont("EBGaramond-Italic", 12)
            self.c.drawCentredString(cx, y, no_em("The way of Godly Men"))
            y -= 48
            self.c.setFillColorRGB(*GOLD)
            self.c.setFont("Libre-Medium", 11)
            self.c.drawCentredString(cx, y, no_em("WES HART"))
            self.c.setFillColorRGB(*GOLD)
            self.c.setFont("Libre", 10)
            self.c.drawCentredString(cx, 1.1 * inch, no_em("walksteadfast.com"))

    def save(self) -> None:
        self.c.save()
        self._open = False


def render_book(pdf_path: Path, asset_dir: Path, page_map_in: dict[str, int] | None) -> Ebook:
    book = Ebook(pdf_path, asset_dir)
    book.page_cover_front()
    book.page_title()
    book.page_copyright()
    book.page_dedication()
    # After dedication.show(), reportlab already opened a fresh blank page.
    # page_contents draws onto that blank page.
    book.page_contents(page_map_in or {})
    book.page_intro()
    for fname in CHAPTER_FILES:
        title, num, blocks = parse_md(BOOK / fname)
        if num in PARTS:
            pl, pt = PARTS[num]
            book.part_page(pl, pt)
        book.chapter_open(num, title)
        book.render_chapter_blocks(num, blocks)
    for label, fname, kind in BACK_MATTER:
        if kind == "yourturn":
            book.page_yourturn(label, fname)
        elif kind == "notes":
            book.page_scripture_notes(label, fname)
        elif kind == "guide":
            book.page_guide(label, fname)
        else:
            book.page_section(label, fname)
    book.page_back()
    book.save()
    return book


def main() -> None:
    load_manifest()
    register_fonts()
    BUILD.mkdir(parents=True, exist_ok=True)
    run_id = uuid.uuid4().hex[:10]
    run_dir = BUILD / f"run-{run_id}"
    run_dir.mkdir(parents=True, exist_ok=True)

    probe_pdf = run_dir / "probe.pdf"
    probe_assets = run_dir / "probe-assets"
    print(f"probe -> {probe_pdf}")
    probe = render_book(probe_pdf, probe_assets, page_map_in={})
    page_map = dict(probe.page_map)
    (run_dir / "page_map.json").write_text(json.dumps(page_map, indent=2), encoding="utf-8")
    print(f"probe pages physical~ folio_end={probe.folio} map_keys={len(page_map)}")

    final_pdf = run_dir / "steadfast-men-ebook.pdf"
    final_assets = run_dir / "final-assets"
    print(f"final -> {final_pdf}")
    final = render_book(final_pdf, final_assets, page_map_in=page_map)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(final_pdf, OUT)

    # compact missing notes
    missing = [
        ("all closers: Your Turn back section, typeset closer_box" if LAYOUT == "baa"
         else "all 35 closers: shared typeset closer_box (CLOSER_ART empty; no PNG split)"),
        "no two-Adams figure (ch 19) - not on disk",
    ]

    report = {
        "path": str(OUT),
        "folio_end": final.folio,
        "cover_front": final.cover_front,
        "closer_35": final.closer_35,
        "wrap_back": final.used_wrap_back,
        "missing_art": missing,
        "run_dir": str(run_dir),
    }
    (run_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("REPORT", json.dumps(report))


if __name__ == "__main__":
    main()
