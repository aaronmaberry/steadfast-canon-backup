#!/usr/bin/env python3
"""Steadfast Men — Amazon-ready front covers. Typeset in real fonts. No AI imagery."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/workspace/biblical-manhood/book/art/press")
FONTS = ROOT / "fonts"

W, H = 1600, 2560
CX = W / 2.0
FOOT = 200  # author ink sits above the bottom by this much

TITLE = "STEADFAST"
TITLE2 = "MEN"
SUB = "The way of Godly Men"
AUTHOR = "WES HART"


def F(name: str, size: float) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def tracked_width(font: ImageFont.FreeTypeFont, text: str, tracking: float) -> float:
    if not text:
        return 0.0
    w = 0.0
    for i, ch in enumerate(text):
        w += font.getlength(ch)
        if i < len(text) - 1:
            w += tracking
    return w


def ink_height(font: ImageFont.FreeTypeFont, text: str) -> float:
    l, t, r, b = font.getbbox(text, anchor="lt")
    return float(b - t)


def fit_size(
    font_name: str,
    text: str,
    target_w: float,
    tracking_em: float = 0.06,
    lo: float = 24,
    hi: float = 520,
) -> tuple[float, float]:
    best = lo
    for _ in range(22):
        mid = (lo + hi) * 0.5
        font = F(font_name, mid)
        tr = tracking_em * mid
        w = tracked_width(font, text, tr)
        if w <= target_w:
            best = mid
            lo = mid
        else:
            hi = mid
    return best, tracking_em * best


def draw_lt(
    draw: ImageDraw.ImageDraw,
    cx: float,
    y_top: float,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill,
    tracking: float,
) -> float:
    """Draw tracked text with em-top at y_top. Returns ink bottom."""
    width = tracked_width(font, text, tracking)
    x = cx - width / 2.0
    for i, ch in enumerate(text):
        draw.text((x, y_top), ch, font=font, fill=fill, anchor="lt")
        x += font.getlength(ch) + tracking
    return y_top + ink_height(font, text)


def draw_author_foot(draw, font, fill, tracking: float) -> None:
    y = H - FOOT - ink_height(font, AUTHOR)
    draw_lt(draw, CX, y, AUTHOR, font, fill, tracking)


def hrule(draw: ImageDraw.ImageDraw, cx: float, y: float, width: float, thickness: float, fill):
    x0 = cx - width / 2.0
    draw.rectangle([x0, y, x0 + width, y + thickness], fill=fill)


def plumb_mark(draw: ImageDraw.ImageDraw, cx: float, y_top: float, color,
               bar_h=108, bar_w=14, base_w=70, base_h=7) -> float:
    """Upright bar sitting on a short baseline. Standing / plumb. Not a cross."""
    x0 = cx - bar_w / 2.0
    draw.rectangle([x0, y_top, x0 + bar_w, y_top + bar_h], fill=color)
    bx0 = cx - base_w / 2.0
    yb = y_top + bar_h
    draw.rectangle([bx0, yb, bx0 + base_w, yb + base_h], fill=color)
    return y_top + bar_h + base_h


def navy_cloth(w: int, h: int) -> Image.Image:
    rng = np.random.default_rng(17)
    base = np.array([11, 31, 56], dtype=np.float32)  # #0B1F38
    img = np.full((h, w, 3), base, np.float32)
    y, x = np.indices((h, w))
    weave = (
        2.0 * np.sin(x * (2 * np.pi / 4.8))
        + 1.5 * np.sin(y * (2 * np.pi / 6.2))
        + 1.1 * np.sin((x + y) * (2 * np.pi / 9.4))
    ).astype(np.float32)
    nap = rng.normal(0, 1.45, (h, w)).astype(np.float32)
    img += (0.50 * weave + nap)[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def cream_paper(w: int, h: int) -> Image.Image:
    rng = np.random.default_rng(23)
    base = np.array([242, 235, 218], dtype=np.float32)  # #F2EBDA
    img = np.full((h, w, 3), base, np.float32)
    y, x = np.indices((h, w))
    grain = rng.normal(0, 2.05, (h, w)).astype(np.float32)
    tooth = 0.85 * np.sin(x * 0.73) * np.sin(y * 0.51)
    mottle = 1.5 * np.sin(x / 140.0) * np.sin(y / 180.0)
    img += (grain + tooth + mottle)[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def charcoal_field(w: int, h: int) -> Image.Image:
    rng = np.random.default_rng(29)
    base = np.array([74, 73, 68], dtype=np.float32)  # #4A4944  — charcoal, distinct from D
    img = np.full((h, w, 3), base, np.float32)
    grain = rng.normal(0, 1.25, (h, w)).astype(np.float32)
    img += grain[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def near_black_field(w: int, h: int) -> Image.Image:
    rng = np.random.default_rng(31)
    base = np.array([14, 14, 13], dtype=np.float32)  # #0E0E0D
    img = np.full((h, w, 3), base, np.float32)
    grain = rng.normal(0, 1.05, (h, w)).astype(np.float32)
    img += grain[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def flatten_rgb(im: Image.Image) -> Image.Image:
    if im.mode != "RGB":
        bg = Image.new("RGB", im.size, (0, 0, 0))
        bg.paste(im, mask=im.split()[-1] if im.mode == "RGBA" else None)
        return bg
    return im


def save(im: Image.Image, path: Path) -> None:
    im = flatten_rgb(im)
    assert im.size == (W, H), im.size
    assert im.mode == "RGB", im.mode
    im.save(path, "PNG", optimize=True)
    thumb = im.resize((160, 256), Image.Resampling.LANCZOS)
    tpath = path.with_name(path.stem + "-thumb.png")
    thumb.save(tpath, "PNG", optimize=True)
    print(f"wrote {path.name} {im.size} {im.mode}  thumb {thumb.size}")


# ---------------------------------------------------------------------------
# A — Navy cloth + gold serif. Small original plumb mark.
# ---------------------------------------------------------------------------
def cover_a() -> Image.Image:
    GOLD = (220, 186, 106)      # #DCBA6A  — bright enough to hold at 160px
    BONE = (230, 221, 204)      # #E6DDCC
    im = navy_cloth(W, H)
    d = ImageDraw.Draw(im)

    usable = W - 2 * 168
    s1, tr1 = fit_size("PlayfairDisplay-Bold.ttf", TITLE, usable, tracking_em=0.078, hi=210)
    s2 = min(s1 * 1.48, 292)
    tr2 = 0.12 * s2

    f1 = F("PlayfairDisplay-Bold.ttf", s1)
    f2 = F("PlayfairDisplay-Bold.ttf", s2)
    fsub = F("EBGaramond-Italic.ttf", 46)
    fauth = F("LibreFranklin-Medium.ttf", 44)

    y = 360
    y = draw_lt(d, CX, y, TITLE, f1, GOLD, tr1)
    y = draw_lt(d, CX, y + 30, TITLE2, f2, GOLD, tr2)
    y = draw_lt(d, CX, y + 70, SUB, fsub, BONE, 0.8)
    plumb_mark(d, CX, y + 78, GOLD)

    draw_author_foot(d, fauth, BONE, 15)
    print(f"  A sizes STEADFAST={s1:.1f} MEN={s2:.1f}")
    return im


# ---------------------------------------------------------------------------
# B — Cream trade paper, huge stacked navy serif, author at the foot. No objects.
# ---------------------------------------------------------------------------
def cover_b() -> Image.Image:
    NAVY = (24, 36, 64)         # #182440
    im = cream_paper(W, H)
    d = ImageDraw.Draw(im)

    usable = W - 2 * 152
    s1, tr1 = fit_size("PlayfairDisplay-Black.ttf", TITLE, usable, tracking_em=0.028, hi=230)
    s2, tr2 = fit_size("PlayfairDisplay-Black.ttf", TITLE2, usable * 0.96, tracking_em=0.018, hi=430)

    f1 = F("PlayfairDisplay-Black.ttf", s1)
    f2 = F("PlayfairDisplay-Black.ttf", s2)
    fsub = F("EBGaramond-Italic.ttf", 44)
    fauth = F("LibreFranklin-Medium.ttf", 46)

    y = 220
    y = draw_lt(d, CX, y, TITLE, f1, NAVY, tr1)
    y = draw_lt(d, CX, y + 22, TITLE2, f2, NAVY, tr2)

    hrule(d, CX, y + 44, 236, 2, NAVY)
    draw_lt(d, CX, y + 44 + 52, SUB, fsub, NAVY, 0.5)

    draw_author_foot(d, fauth, NAVY, 13)
    print(f"  B sizes STEADFAST={s1:.1f} MEN={s2:.1f}")
    return im


# ---------------------------------------------------------------------------
# C — Charcoal, off-white geometric title, one muted copper accent (subtitle).
# ---------------------------------------------------------------------------
def cover_c() -> Image.Image:
    BONE = (236, 229, 212)      # #ECE5D4
    COPPER = (184, 128, 82)     # #B88052  — the one accent: subtitle color
    im = charcoal_field(W, H)
    d = ImageDraw.Draw(im)

    usable = W - 2 * 156
    s1, tr1 = fit_size("Outfit-SemiBold.ttf", TITLE, usable, tracking_em=0.086, hi=188)
    s2 = min(s1 * 1.34, 252)
    tr2 = 0.16 * s2

    f1 = F("Outfit-SemiBold.ttf", s1)
    f2 = F("Outfit-SemiBold.ttf", s2)
    fsub = F("Outfit-Regular.ttf", 40)
    fauth = F("Outfit-Medium.ttf", 38)

    y = 340
    y = draw_lt(d, CX, y, TITLE, f1, BONE, tr1)
    y = draw_lt(d, CX, y + 28, TITLE2, f2, BONE, tr2)
    draw_lt(d, CX, y + 64, SUB, fsub, COPPER, 2.4)

    draw_author_foot(d, fauth, BONE, 16)
    print(f"  C sizes STEADFAST={s1:.1f} MEN={s2:.1f}")
    return im


# ---------------------------------------------------------------------------
# D — Near-black, bone title owning the top half. High-contrast stacked sans.
# ---------------------------------------------------------------------------
def cover_d() -> Image.Image:
    BONE = (232, 224, 208)      # #E8E0D0
    MUTED = (186, 176, 158)     # #BAB09E
    im = near_black_field(W, H)
    d = ImageDraw.Draw(im)

    usable = W - 2 * 148
    s1, tr1 = fit_size("Oswald-Bold.ttf", TITLE, usable, tracking_em=0.04, hi=300)
    s2, tr2 = fit_size("Oswald-Bold.ttf", TITLE2, usable * 0.98, tracking_em=0.025, hi=780)

    f1 = F("Oswald-Bold.ttf", s1)
    f2 = F("Oswald-Bold.ttf", s2)
    fsub = F("LibreFranklin-Regular.ttf", 36)
    fauth = F("LibreFranklin-Medium.ttf", 44)

    y = 176
    y = draw_lt(d, CX, y, TITLE, f1, BONE, tr1)
    y = draw_lt(d, CX, y + 18, TITLE2, f2, BONE, tr2)
    print(f"  D title bottom y={y:.0f} (half={H//2}) STEADFAST={s1:.1f} MEN={s2:.1f}")

    hrule(d, CX, y + 56, 108, 2, BONE)
    draw_lt(d, CX, y + 56 + 56, SUB, fsub, MUTED, 1.1)

    draw_author_foot(d, fauth, BONE, 14)
    return im


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for name, fn in (
        ("press-a.png", cover_a),
        ("press-b.png", cover_b),
        ("press-c.png", cover_c),
        ("press-d.png", cover_d),
    ):
        im = fn()
        save(im, ROOT / name)
        im.close()


if __name__ == "__main__":
    main()
