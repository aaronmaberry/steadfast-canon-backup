#!/usr/bin/env python3
"""Week 24 kit comps — Loom. Cloth Store. Original plumb. Iterate, not a lock."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

PRESS = Path("/workspace/biblical-manhood/book/art/press")
sys.path.insert(0, str(PRESS))

from render_a_v2 import (  # noqa: E402
    BONE,
    F,
    GOLD,
    draw_lt,
    fit_size,
    ink_height,
    navy_cloth,
)

OUT = Path("/workspace/biblical-manhood/digital/merch/art")

NAVY_T = (11, 31, 56)
GOLD_T = GOLD
BONE_T = BONE
OLD_GOLD = (166, 120, 67)
TWILL_BLACK = (18, 18, 18)
DIM_BONE = (196, 188, 172)
WRITE_LINE = (90, 100, 92)

MARKS = (
    "Rejects passivity",
    "Accepts responsibility",
    "Leads courageously",
    "Expects God's reward",
)


def plumb(draw, cx, y_top, scale: float, color=GOLD_T) -> float:
    """Standing cord + teardrop bob. Linear scale. Not a Roman I."""
    cord_w = max(2.5, 16 * scale)
    cord_h = max(10.0, 72 * scale)
    bob_r = max(6.0, 58 * scale)
    x0 = cx - cord_w / 2.0
    draw.rectangle([x0, y_top, x0 + cord_w, y_top + cord_h], fill=color)
    cy = y_top + cord_h + bob_r * 0.72
    draw.ellipse([cx - bob_r, cy - bob_r, cx + bob_r, cy + bob_r], fill=color)
    tip = bob_r * 0.70
    draw.polygon(
        [
            (cx - bob_r * 0.62, cy + bob_r * 0.50),
            (cx + bob_r * 0.62, cy + bob_r * 0.50),
            (cx, cy + bob_r + tip),
        ],
        fill=color,
    )
    return cy + bob_r + tip


def plumb_h(scale: float) -> float:
    cord_h = max(10.0, 72 * scale)
    bob_r = max(6.0, 58 * scale)
    return cord_h + bob_r * 0.72 + bob_r + bob_r * 0.70


def draw_left(draw, x, y_top, text, font, fill, tracking) -> float:
    xx = x
    for ch in text:
        draw.text((xx, y_top), ch, font=font, fill=fill, anchor="lt")
        xx += font.getlength(ch) + tracking
    return y_top + ink_height(font, text)


def draw_godly_left(draw, x, y_top, italic, roman, fill) -> float:
    left, word, right = "The way of ", "Godly", " Men"
    ascent = italic.getmetrics()[0]
    yb = y_top + ascent
    xx = x
    draw.text((xx, yb), left, font=italic, fill=fill, anchor="ls")
    xx += italic.getlength(left)
    draw.text((xx, yb), word, font=roman, fill=fill, anchor="ls")
    xx += roman.getlength(word)
    draw.text((xx, yb), right, font=italic, fill=fill, anchor="ls")
    return y_top + max(ink_height(italic, left + right), ink_height(roman, word))


def draw_godly_center(draw, cx, y_top, italic, roman, fill) -> float:
    left, word, right = "The way of ", "Godly", " Men"
    ascent = italic.getmetrics()[0]
    yb = y_top + ascent
    total = italic.getlength(left) + roman.getlength(word) + italic.getlength(right)
    x = cx - total / 2.0
    draw.text((x, yb), left, font=italic, fill=fill, anchor="ls")
    x += italic.getlength(left)
    draw.text((x, yb), word, font=roman, fill=fill, anchor="ls")
    x += roman.getlength(word)
    draw.text((x, yb), right, font=italic, fill=fill, anchor="ls")
    return y_top + max(ink_height(italic, left + right), ink_height(roman, word))


def round_card(im: Image.Image, radius: int, bg=NAVY_T) -> Image.Image:
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    out = Image.new("RGB", (w, h), bg)
    out.paste(im, mask=mask)
    return out


def hairline(draw, x0, y, x1, fill, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def bone_sheet(w: int, h: int, seed: int = 7) -> Image.Image:
    rng = np.random.default_rng(seed)
    base = np.array(BONE, dtype=np.float32)
    img = np.full((h, w, 3), base, np.float32)
    img += rng.normal(0, 0.85, (h, w)).astype(np.float32)[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def card_palette(plate: str):
    if plate == "bone":
        return {
            "title": NAVY_T,
            "body": NAVY_T,
            "muted": WRITE_LINE,
            "rule": GOLD_T,
            "plumb": GOLD_T,
            "frame": NAVY_T,
            "round_bg": BONE_T,
        }
    return {
        "title": GOLD_T,
        "body": BONE_T,
        "muted": DIM_BONE,
        "rule": GOLD_T,
        "plumb": GOLD_T,
        "frame": GOLD_T,
        "round_bg": NAVY_T,
    }


def card_field(w: int, h: int, plate: str) -> Image.Image:
    if plate == "bone":
        return bone_sheet(w, h, seed=11)
    return navy_cloth(w, h, seed=21)


def render_card_front(dpi: int = 600, plate: str = "navy") -> Image.Image:
    """Split: large plumb left, type right. The mark is the graphic."""
    pal = card_palette(plate)
    w, h = int(3.5 * dpi), int(2.0 * dpi)
    im = card_field(w, h, plate)
    d = ImageDraw.Draw(im)
    inset = int(0.07 * dpi)
    rule_w = max(2, dpi // 250)
    d.rounded_rectangle(
        [inset, inset, w - 1 - inset, h - 1 - inset],
        radius=int(0.08 * dpi),
        outline=pal["frame"],
        width=rule_w,
    )

    split = int(0.34 * w)
    d.line([(split, inset + int(0.10 * h)), (split, h - inset - int(0.10 * h))], fill=pal["rule"], width=rule_w)

    scale = 2.55
    ph = plumb_h(scale)
    px = split / 2.0
    py = (h - ph) / 2.0
    plumb(d, px, py, scale=scale, color=pal["plumb"])

    tx = split + int(0.055 * w)
    col_w = w - tx - int(0.10 * w)
    title_size, tr = fit_size(
        "PlayfairDisplay-Bold.ttf", "STEADFAST MEN", col_w, tracking_em=0.048, lo=18, hi=0.078 * w
    )
    f_title = F("PlayfairDisplay-Bold.ttf", title_size)
    f_sub_i = F("EBGaramond-Italic.ttf", 0.038 * w)
    f_sub_r = F("EBGaramond-Regular.ttf", 0.038 * w)
    f_earned = F("PlayfairDisplay-Bold.ttf", 0.042 * w)
    f_mark = F("EBGaramond-Regular.ttf", 0.036 * w)

    gap_sub = 0.012 * h
    gap_rule = 0.028 * h
    gap_earned = 0.022 * h
    gap_mark = 0.008 * h
    block = (
        ink_height(f_title, "STEADFAST MEN")
        + gap_sub
        + ink_height(f_sub_i, "The way of Godly Men")
        + gap_rule
        + rule_w
        + gap_rule
        + ink_height(f_earned, "A STEADFAST MAN")
        + gap_earned
    )
    for line in MARKS:
        block += ink_height(f_mark, line) + gap_mark

    y = (h - block) / 2.0
    y = draw_left(d, tx, y, "STEADFAST MEN", f_title, pal["title"], tr)
    y += gap_sub
    y = draw_godly_left(d, tx, y, f_sub_i, f_sub_r, pal["body"])
    y += gap_rule
    hairline(d, tx, y, tx + 0.28 * w, pal["rule"], rule_w)
    y += gap_rule
    y = draw_left(d, tx, y, "A STEADFAST MAN", f_earned, pal["body"], 0.03 * f_earned.size)
    y += gap_earned
    for line in MARKS:
        d.text((tx, y), line, font=f_mark, fill=pal["body"], anchor="lt")
        y += ink_height(f_mark, line) + gap_mark

    return round_card(im, radius=int(0.125 * dpi), bg=pal["round_bg"])


def render_card_back(dpi: int = 600, plate: str = "navy") -> Image.Image:
    pal = card_palette(plate)
    w, h = int(3.5 * dpi), int(2.0 * dpi)
    im = card_field(w, h, plate if plate == "bone" else "navy")
    if plate == "navy":
        im = navy_cloth(w, h, seed=23)
    d = ImageDraw.Draw(im)
    inset = int(0.07 * dpi)
    rule_w = max(2, dpi // 250)
    d.rounded_rectangle(
        [inset, inset, w - 1 - inset, h - 1 - inset],
        radius=int(0.08 * dpi),
        outline=pal["frame"],
        width=rule_w,
    )

    split = int(0.34 * w)
    d.line([(split, inset + int(0.10 * h)), (split, h - inset - int(0.10 * h))], fill=pal["rule"], width=rule_w)

    scale = 2.55
    ph = plumb_h(scale)
    plumb(d, split / 2.0, (h - ph) / 2.0, scale=scale, color=pal["plumb"])

    tx = split + int(0.055 * w)
    f_line = F("EBGaramond-Italic.ttf", 0.044 * w)
    f_label = F("LibreFranklin-Medium.ttf", 0.020 * w)
    f_url = F("LibreFranklin-Medium.ttf", 0.024 * w)

    y = 0.22 * h
    d.text((tx, y), "You finished the 24.", font=f_line, fill=pal["body"], anchor="lt")
    y += ink_height(f_line, "You finished the 24.") + 0.10 * h
    x1 = w - int(0.12 * w)
    hairline(d, tx, y, x1, pal["rule"], rule_w)
    d.text((tx, y + 0.028 * h), "NAME", font=f_label, fill=pal["muted"], anchor="lt")
    y += 0.20 * h
    hairline(d, tx, y, tx + 0.28 * w, pal["rule"], rule_w)
    d.text((tx, y + 0.028 * h), "YEAR", font=f_label, fill=pal["muted"], anchor="lt")
    d.text((tx, 0.78 * h), "walksteadfast.com", font=f_url, fill=pal["muted"], anchor="lt")
    return round_card(im, radius=int(0.125 * dpi), bg=pal["round_bg"])


def render_certificate(size_in=(8.5, 11.0), dpi: int = 300) -> Image.Image:
    """Cloth Store: navy jacket band, bone page. Not a diploma seal."""
    w, h = int(size_in[0] * dpi), int(size_in[1] * dpi)
    im = bone_sheet(w, h, seed=9)
    band_h = int(0.30 * h)
    band = navy_cloth(w, band_h, seed=17)
    im.paste(band, (0, 0))
    d = ImageDraw.Draw(im)
    cx = w / 2.0
    rule_w = max(3, dpi // 120)

    # gold join where cloth meets paper
    d.rectangle([0, band_h, w, band_h + max(rule_w, dpi // 50)], fill=GOLD_T)

    f_brand = F("PlayfairDisplay-Bold.ttf", 0.052 * w)
    tr_brand = 0.07 * f_brand.size
    f_sub_i = F("EBGaramond-Italic.ttf", 0.024 * w)
    f_sub_r = F("EBGaramond-Regular.ttf", 0.024 * w)
    f_earned = F("PlayfairDisplay-Bold.ttf", 0.048 * w)
    tr_earned = 0.04 * f_earned.size
    f_finish = F("EBGaramond-Italic.ttf", 0.026 * w)
    f_mark = F("EBGaramond-Regular.ttf", 0.032 * w)
    f_label = F("LibreFranklin-Medium.ttf", 0.014 * w)
    f_url = F("LibreFranklin-Medium.ttf", 0.016 * w)

    scale = 1.65
    ph = plumb_h(scale)
    # band stack: plumb, title, subtitle — vertically centered in cloth
    gap1 = 0.018 * h
    gap2 = 0.010 * h
    stack = ph + gap1 + ink_height(f_brand, "STEADFAST MEN") + gap2 + ink_height(f_sub_i, "The way of Godly Men")
    y = (band_h - stack) / 2.0
    y = plumb(d, cx, y, scale=scale, color=GOLD_T)
    y += gap1
    y = draw_lt(d, cx, y, "STEADFAST MEN", f_brand, GOLD_T, tr_brand)
    y += gap2
    draw_godly_center(d, cx, y, f_sub_i, f_sub_r, BONE_T)

    y = band_h + 0.07 * h
    y = draw_lt(d, cx, y, "A STEADFAST MAN", f_earned, NAVY_T, tr_earned)
    y += 0.018 * h
    d.text((cx, y), "You finished the 24-week training.", font=f_finish, fill=NAVY_T, anchor="mt")
    y += ink_height(f_finish, "You finished the 24-week training.") + 0.040 * h
    hairline(d, cx - 0.12 * w, y, cx + 0.12 * w, GOLD_T, rule_w)
    y += 0.042 * h

    gap = 0.016 * h
    for line in MARKS:
        d.text((cx, y), line, font=f_mark, fill=NAVY_T, anchor="mt")
        y += ink_height(f_mark, line) + gap

    y = 0.84 * h
    left0, left1 = 0.16 * w, 0.56 * w
    right0, right1 = 0.62 * w, 0.84 * w
    hairline(d, left0, y, left1, NAVY_T, max(2, dpi // 250))
    hairline(d, right0, y, right1, NAVY_T, max(2, dpi // 250))
    d.text((left0, y + 0.016 * h), "NAME", font=f_label, fill=WRITE_LINE, anchor="lt")
    d.text((right0, y + 0.016 * h), "DATE", font=f_label, fill=WRITE_LINE, anchor="lt")
    d.text((cx, 0.935 * h), "walksteadfast.com", font=f_url, fill=WRITE_LINE, anchor="mt")
    return im


def twill_black(w: int, h: int, seed: int = 31) -> Image.Image:
    rng = np.random.default_rng(seed)
    base = np.array(TWILL_BLACK, dtype=np.float32)
    img = np.full((h, w, 3), base, np.float32)
    yy, xx = np.indices((h, w))
    weave = (1.4 * np.sin(xx * (2 * np.pi / 5.2)) + 1.1 * np.sin(yy * (2 * np.pi / 5.8))).astype(np.float32)
    img += (0.45 * weave + rng.normal(0, 1.1, (h, w)).astype(np.float32))[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def render_patch(dpi: int = 600) -> Image.Image:
    """Held. Do not restyle."""
    w, h = int(3.5 * dpi), int(2.25 * dpi)
    im = twill_black(w, h, seed=31)
    d = ImageDraw.Draw(im)
    cx = w / 2.0
    merrow = int(0.125 * dpi)
    d.rounded_rectangle(
        [merrow // 2, merrow // 2, w - 1 - merrow // 2, h - 1 - merrow // 2],
        radius=int(0.11 * dpi),
        outline=OLD_GOLD,
        width=merrow,
    )
    usable = w - 2 * merrow - 0.16 * dpi
    size, tr = fit_size("PlayfairDisplay-Bold.ttf", "STEADFAST MAN", usable, tracking_em=0.05, lo=24, hi=0.11 * w)
    f_word = F("PlayfairDisplay-Bold.ttf", size)
    scale = 0.48
    gap = 0.045 * h
    group = plumb_h(scale) + gap + ink_height(f_word, "STEADFAST MAN")
    y = (h - group) / 2.0
    y = plumb(d, cx, y, scale=scale, color=OLD_GOLD)
    y += gap
    draw_lt(d, cx, y, "STEADFAST MAN", f_word, OLD_GOLD, tr)
    return im


def contact_sheet(front, back, cert, patch) -> Image.Image:
    def fit_h(im, th):
        r = th / im.size[1]
        return im.resize((max(1, int(im.size[0] * r)), th), Image.Resampling.LANCZOS)

    f = fit_h(front, 400)
    b = fit_h(back, 400)
    p = fit_h(patch, 360)
    c = fit_h(cert, 900)
    pad, gap = 48, 32
    left_w = f.size[0] + b.size[0] + gap + 2 * pad
    W = left_w + c.size[0] + 3 * pad
    H = max(f.size[1] + p.size[1] + 180, c.size[1] + 40) + 150
    board = Image.new("RGB", (W, H), NAVY_T)
    d = ImageDraw.Draw(board)
    fcap = F("LibreFranklin-Medium.ttf", 26)
    fhed = F("PlayfairDisplay-Bold.ttf", 40)
    d.text((pad, 28), "WEEK 24 KIT  ·  ITERATE", font=fhed, fill=GOLD_T, anchor="lt")
    d.text((pad, 78), "Not a lock  ·  patch holds  ·  bone plate waits", font=fcap, fill=DIM_BONE, anchor="lt")
    y0 = 124
    board.paste(f, (pad, y0))
    board.paste(b, (pad + f.size[0] + gap, y0))
    d.text((pad, y0 + f.size[1] + 8), "Navy card  ·  3.5 × 2  ·  front / back", font=fcap, fill=DIM_BONE, anchor="lt")
    y1 = y0 + f.size[1] + 64
    board.paste(p, (pad, y1))
    d.text((pad, y1 + p.size[1] + 8), "Patch  ·  held  ·  black twill / Old Gold", font=fcap, fill=DIM_BONE, anchor="lt")
    cx0 = left_w + pad
    # bone mat so the navy jacket band doesn't vanish on the navy board
    mat = 6
    d.rectangle(
        [cx0 - mat, 124 - mat, cx0 + c.size[0] + mat, 124 + c.size[1] + mat],
        fill=BONE_T,
    )
    board.paste(c, (cx0, 124))
    d.text((cx0, 124 + c.size[1] + 10), "Certificate  ·  US Letter  ·  Cloth Store band", font=fcap, fill=DIM_BONE, anchor="lt")
    return board


def save(im: Image.Image, name: str) -> Path:
    path = OUT / name
    if im.mode != "RGB":
        im = im.convert("RGB")
    im.save(path, "PNG")
    print(f"wrote {path} {im.size}")
    return path


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    front = render_card_front()
    back = render_card_back()
    front_b = render_card_front(plate="bone")
    back_b = render_card_back(plate="bone")
    cert = render_certificate()
    cert_8x10 = render_certificate(size_in=(8.0, 10.0))
    patch = render_patch()
    sheet = contact_sheet(front, back, cert, patch)
    save(front, "wallet-card-front.png")
    save(back, "wallet-card-back.png")
    save(front_b, "wallet-card-front-bone.png")
    save(back_b, "wallet-card-back-bone.png")
    save(cert, "certificate-letter.png")
    save(cert_8x10, "certificate-8x10.png")
    # Image 2.0 plate lives at patch-rectangle.png — do not overwrite with the type-only renderer
    save(patch, "patch-rectangle-type.png")
    save(sheet, "kit-comps.png")


if __name__ == "__main__":
    main()
