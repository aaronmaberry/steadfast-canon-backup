#!/usr/bin/env python3
"""Apply the locked wrap-back copy (Sample D, Aaron 2026-10-01) to a-wrap.png, BACK PANEL ONLY.

Repaints the first BLEED_L + 6in px (the back panel incl. left bleed) and leaves the spine and
front byte-identical (asserted). Spine width is whatever a-wrap.png already has
(rebuild_wrap_spine.py). Does not write a-front-v2.png, thumbs, or archives.

History: Reed-signed hook layout (2026-09-05) -> creed swap + inheritance line (2026-10-01 AM)
-> Sample D layout picked by Aaron 2026-10-01 11:14 CT, with "Counsel for every season" changed
to "Straight talk for every season", then (Aaron 11:19 CT) to "Help for every season".
Pre-"Help" copies: /workspace/backups/back-cover-pre-D-2026-10-01/straight-talk-version-2026-10-01-1120/
Layout ported unchanged from
/workspace/print-build/back-cover-samples/render_back_samples.py (render_D).
Pre-D copies of this script, a-wrap.png, press.md and wrap-back-copy.md:
/workspace/backups/back-cover-pre-D-2026-10-01/
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/workspace/biblical-manhood/book/art/press")
FONTS = ROOT / "fonts"
WRAP = ROOT / "a-wrap.png"

# Wrap palette (sampled from the locked front): navy #0B1F38, gold #E3C572, bone #E6DDCC.
NAVY = (11, 31, 56)
GOLD = (227, 197, 114)
BONE = (230, 221, 204)
BONE_DIM = (196, 186, 168)

# ---- locked back copy (wrap-back-copy.md, Sample D) ----
HEADLINE = ["Still waiting for a", "better season?"]  # set as two lines
HOOK = ("Plenty of good men are. The kids get older, the job gets bigger, and the man you meant "
        "to be keeps getting moved to next year. This book says start on the Tuesday in front of you.")
INSIDE_LABEL = "INSIDE"
BULLETS = [
    "Four marks you can see on a man, and how to build each one",
    "Straight talk on fathers, anger, marriage, and kids",
    "Help for every season of a man's life",
    "One thing to do each week, and a brother to tell",
]
# Locked creed (Aaron 2026-10-01). Print once, commas as written, do not rewrite.
CREED = "A steadfast man stops waiting, picks up the weight, goes first, and works for God's pay, not the room's."
# Inheritance line under the creed (Aaron 2026-10-01). Col 3:24.
INHERITANCE = "God's pay is a Father's inheritance, not wages."
CATEGORY = "CHRISTIAN LIVING  /  MEN"
HUB = "walksteadfast.com"
AUTHOR = "WES HART"

DPI = 300
TRIM_W, TRIM_H = 6 * DPI, 9 * DPI
BLEED_L = 38
BLEED_T = 38
BACK_PANEL_W = BLEED_L + TRIM_W            # 1838
TRIM_X0, TRIM_Y0 = BLEED_L, BLEED_T
TRIM_X1, TRIM_Y1 = BLEED_L + TRIM_W, BLEED_T + TRIM_H

# Barcode block: 2.0 x 1.2 in, blank white, bottom right, 0.25 in in from trim bottom and spine side.
BC_W, BC_H = int(2.0 * DPI), int(1.2 * DPI)
BC_X1 = TRIM_X1 - int(0.25 * DPI)
BC_Y1 = TRIM_Y1 - int(0.25 * DPI)
BC_X0, BC_Y0 = BC_X1 - BC_W, BC_Y1 - BC_H

INSET = int(0.70 * DPI)
COL_X0, COL_X1 = TRIM_X0 + INSET, TRIM_X1 - INSET
COL_W = COL_X1 - COL_X0
ZONE_Y0 = TRIM_Y0 + int(0.75 * DPI)
ZONE_Y1 = BC_Y0 - int(0.45 * DPI)

DASHES = re.compile(r"[\u2010-\u2015\u2212-]")


def all_copy() -> list[str]:
    return [*HEADLINE, HOOK, INSIDE_LABEL, *BULLETS, CREED, INHERITANCE, CATEGORY, HUB, AUTHOR]


def copy_check() -> None:
    for t in all_copy():
        assert not DASHES.search(t), f"dash in back copy: {t!r}"
        assert "counsel" not in t.lower(), f"'counsel' in back copy: {t!r}"


def typo(s: str) -> str:
    """Display only: typographic apostrophes. Wording is untouched."""
    return s.replace("'", "\u2019")


def F(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def tracked_width(font, text, tracking=0.0):
    return sum(font.getlength(c) for c in text) + tracking * max(0, len(text) - 1)


def ink_h(font, text):
    l, t, r, b = font.getbbox(text, anchor="lt")
    return float(b - t)


def wrap_words(font, text, max_w, tracking=0.0):
    lines, cur = [], ""
    for w in text.split():
        trial = (cur + " " + w).strip()
        if tracked_width(font, trial, tracking) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def navy_cloth(w, h, seed=19):
    rng = np.random.default_rng(seed)
    img = np.full((h, w, 3), np.array(NAVY, np.float32), np.float32)
    y, x = np.indices((h, w))
    weave = (2.0 * np.sin(x * (2 * np.pi / 4.8)) + 1.5 * np.sin(y * (2 * np.pi / 6.2))
             + 1.1 * np.sin((x + y) * (2 * np.pi / 9.4))).astype(np.float32)
    nap = rng.normal(0, 1.45, (h, w)).astype(np.float32)
    img += (0.50 * weave + nap)[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def draw_tracked(d, x, y, text, font, fill, tracking=0.0):
    """Tracked text on one shared baseline (2026-10-01 hub-bounce fix). y = top of ink."""
    _l, t, _r, _b = font.getbbox(text, anchor="ls")
    base = y - t
    for ch in text:
        d.text((x, base), ch, font=font, fill=fill, anchor="ls")
        x += font.getlength(ch) + tracking
    return y + ink_h(font, text)


def para(d, text, font, fill, y, *, x0=COL_X0, width=COL_W, lead=1.32):
    """Left-aligned paragraph with fixed leading. y = top of first line."""
    lh = font.size * lead
    for ln in wrap_words(font, text, width):
        d.text((x0, y), ln, font=font, fill=fill, anchor="la")
        y += lh
    return y


class Null:
    """Draw stand-in for the measuring pass."""
    def __getattr__(self, _):
        return lambda *a, **k: None


def content(d, y):
    fq = F("PlayfairDisplay-Bold.ttf", 100)
    for ln in HEADLINE:
        d.text((COL_X0, y), typo(ln), font=fq, fill=GOLD, anchor="la")
        y += 100 * 1.18
    y += 46
    y = para(d, typo(HOOK), F("EBGaramond-Regular.ttf", 58), BONE, y, lead=1.32)
    y += 80
    draw_tracked(d, COL_X0, y, INSIDE_LABEL, F("LibreFranklin-Medium.ttf", 38), GOLD, tracking=7)
    y += 84
    fb = F("EBGaramond-Regular.ttf", 54)
    bx = COL_X0 + 60
    for b in BULLETS:
        d.rectangle([COL_X0 + 6, y + 24, COL_X0 + 23, y + 41], fill=GOLD)
        y = para(d, typo(b), fb, BONE, y, x0=bx, width=COL_X1 - bx, lead=1.24)
        y += 26
    y += 64
    rx = COL_X0 + 60
    d.rectangle([rx - 60, y, rx + 60, y + 3], fill=GOLD)
    y += 66
    y = para(d, typo(CREED), F("EBGaramond-Italic.ttf", 56), GOLD, y, lead=1.26)
    y += 22
    y = para(d, typo(INHERITANCE), F("EBGaramond-Regular.ttf", 46), BONE, y)
    return y


def footer(d):
    """Category / hub / author stacked bottom left; author bottom level with the barcode bottom."""
    fcat = F("LibreFranklin-Medium.ttf", 30)
    fhub = F("LibreFranklin-Medium.ttf", 34)
    fauth = F("LibreFranklin-Medium.ttf", 48)
    y_auth = BC_Y1 - ink_h(fauth, AUTHOR)
    y_hub = y_auth - 40 - ink_h(fhub, HUB)
    y_cat = y_hub - 28 - ink_h(fcat, CATEGORY)
    draw_tracked(d, COL_X0, y_cat, CATEGORY, fcat, BONE_DIM, 2.2)
    draw_tracked(d, COL_X0, y_hub, HUB, fhub, BONE, 1.5)
    draw_tracked(d, COL_X0, y_auth, AUTHOR, fauth, BONE, 8)


def paint_back(wrap: Image.Image) -> Image.Image:
    out = wrap.copy()
    out.paste(navy_cloth(BACK_PANEL_W, out.size[1], seed=19), (0, 0))
    d = ImageDraw.Draw(out)
    h = content(Null(), 0)
    slack = (ZONE_Y1 - ZONE_Y0) - h
    assert slack >= 0, f"back copy overflows by {-slack:.0f}px"
    content(d, ZONE_Y0 + slack * 0.45)
    footer(d)
    d.rectangle([BC_X0, BC_Y0, BC_X1 - 1, BC_Y1 - 1], fill=(255, 255, 255))
    return out


def main():
    copy_check()
    src = Image.open(WRAP).convert("RGB")
    assert src.size[1] == 2775 and src.size[0] >= 3840, src.size  # width grows with the spine
    wrap = paint_back(src)
    assert np.array_equal(np.asarray(wrap)[:, BACK_PANEL_W:], np.asarray(src)[:, BACK_PANEL_W:]), \
        "spine/front changed"
    assert wrap.size == src.size and wrap.mode == "RGB"
    wrap.save(WRAP, "PNG", optimize=True, dpi=(DPI, DPI))
    print(f"wrote {WRAP} {wrap.size} {wrap.mode}; spine+front byte-identical to input")

    md = ROOT / "press.md"
    text = md.read_text() if md.exists() else ""
    note = (
        "\n\n## Wrap back: Sample D locked (Aaron 2026-10-01 11:14 CT)\n"
        "Back panel replaced with Sample D (question opener + INSIDE bullets + creed + inheritance line),\n"
        "with the third bullet changed to \"Help for every season of a man's life\" (no \"counsel\" on the back).\n"
        "Wrap palette #0B1F38 / #E3C572; footer CHRISTIAN LIVING / MEN, walksteadfast.com, WES HART bottom left;\n"
        "blank white barcode block 2.0 x 1.2 in, bottom right, 0.25 in from trim. Copy: `wrap-back-copy.md`.\n"
        "Back panel only; spine (182 px, 242 pages) and front byte-identical. Not uploaded.\n"
        "Pre-D backup: /workspace/backups/back-cover-pre-D-2026-10-01/\n"
    )
    if "## Wrap back: Sample D locked" not in text:
        text = text.rstrip() + note
        md.write_text(text, encoding="utf-8")
        print("press.md noted")


if __name__ == "__main__":
    main()
