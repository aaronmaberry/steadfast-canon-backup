#!/usr/bin/env python3
"""Press A v2 for Jarvis. Does not write press-a/b/c/d.png."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/workspace/biblical-manhood/book/art/press")
FONTS = ROOT / "fonts"

TITLE, TITLE2 = "STEADFAST", "MEN"
SUB = "The way of Godly Men"
AUTHOR = "WES HART"
SPINE_AUTHOR = "Hart"
CREED = (
    "A real man rejects passivity, accepts responsibility, "
    "leads courageously, and expects the greater reward, God's reward."
)

NAVY = np.array([11, 31, 56], dtype=np.float32)  # #0B1F38
GOLD = (227, 197, 114)  # #E3C572
BONE = (230, 221, 204)  # #E6DDCC


def F(name: str, size: float) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def tracked_width(font: ImageFont.FreeTypeFont, text: str, tracking: float) -> float:
    w = 0.0
    for i, ch in enumerate(text):
        w += font.getlength(ch)
        if i < len(text) - 1:
            w += tracking
    return w


def ink_height(font: ImageFont.FreeTypeFont, text: str) -> float:
    l, t, r, b = font.getbbox(text, anchor="lt")
    return float(b - t)


def fit_size(font_name, text, target_w, tracking_em=0.06, lo=24, hi=520):
    best = lo
    for _ in range(22):
        mid = (lo + hi) * 0.5
        font = F(font_name, mid)
        tr = tracking_em * mid
        if tracked_width(font, text, tr) <= target_w:
            best = mid
            lo = mid
        else:
            hi = mid
    return best, tracking_em * best


def draw_lt(draw, cx, y_top, text, font, fill, tracking) -> float:
    width = tracked_width(font, text, tracking)
    x = cx - width / 2.0
    for ch in text:
        draw.text((x, y_top), ch, font=font, fill=fill, anchor="lt")
        x += font.getlength(ch) + tracking
    return y_top + ink_height(font, text)


def wrap_words(font, text, max_w, tracking=0.0):
    words = text.split()
    lines, cur = [], ""
    for w in words:
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


def navy_cloth(w: int, h: int, seed: int = 17) -> Image.Image:
    rng = np.random.default_rng(seed)
    img = np.full((h, w, 3), NAVY, np.float32)
    y, x = np.indices((h, w))
    weave = (
        2.0 * np.sin(x * (2 * np.pi / 4.8))
        + 1.5 * np.sin(y * (2 * np.pi / 6.2))
        + 1.1 * np.sin((x + y) * (2 * np.pi / 9.4))
    ).astype(np.float32)
    nap = rng.normal(0, 1.45, (h, w)).astype(np.float32)
    img += (0.50 * weave + nap)[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def plumb_bob(draw, cx, y_top, scale: float, color=GOLD) -> float:
    """Standing plumb: short cord + large teardrop weight. Not a Roman I."""
    cord_w = max(10, int(round(16 * scale)))
    cord_h = max(48, int(round(88 * scale)))   # short — I has a long stem
    bob_r = max(28, int(round(58 * scale)))    # weight is the mark
    x0 = cx - cord_w / 2.0
    draw.rectangle([x0, y_top, x0 + cord_w, y_top + cord_h], fill=color)
    # neck: tiny gap so cord and bob read as two parts, not a serifed stem
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


def typeset_front(im: Image.Image) -> Image.Image:
    w, h = im.size
    d = ImageDraw.Draw(im)
    cx = w / 2.0
    usable = w - 2 * (0.08 * w)

    s1, tr1 = fit_size("PlayfairDisplay-Bold.ttf", TITLE, usable, tracking_em=0.068, hi=0.16 * w)
    s2 = min(s1 * 1.62, 0.22 * w)
    tr2 = 0.09 * s2
    f1 = F("PlayfairDisplay-Bold.ttf", s1)
    f2 = F("PlayfairDisplay-Bold.ttf", s2)
    # Cursor-comp scale: fit subtitle to ~92% of STEADFAST width (Aaron 2026-09-05)
    sub_target = tracked_width(f1, TITLE, tr1) * 0.92
    ssub, trsub = fit_size("EBGaramond-Italic.ttf", SUB, sub_target, tracking_em=0.02, lo=40, hi=0.095 * w)
    fsub = F("EBGaramond-Italic.ttf", ssub)
    fauth = F("LibreFranklin-Medium.ttf", max(28, 0.030 * w))

    y = 0.11 * h
    y = draw_lt(d, cx, y, TITLE, f1, GOLD, tr1)
    y = draw_lt(d, cx, y + 0.010 * h, TITLE2, f2, GOLD, tr2)
    y = draw_lt(d, cx, y + 0.028 * h, SUB, fsub, GOLD, trsub)

    scale = w / 1600.0
    plumb_bob(d, cx, y + 0.030 * h, scale=scale)

    foot = 0.078 * h
    ya = h - foot - ink_height(fauth, AUTHOR)
    draw_lt(d, cx, ya, AUTHOR, fauth, BONE, 0.12 * fauth.size)
    return im


def flatten_rgb(im: Image.Image) -> Image.Image:
    if im.mode == "RGB":
        return im
    bg = Image.new("RGB", im.size, (0, 0, 0))
    bg.paste(im, mask=im.split()[-1] if im.mode == "RGBA" else None)
    return bg


def save_png(im: Image.Image, path: Path, expect=None) -> None:
    im = flatten_rgb(im)
    if expect:
        assert im.size == expect, (path.name, im.size, expect)
    assert im.mode == "RGB"
    im.save(path, "PNG", optimize=True)
    print(f"wrote {path.name} {im.size} {im.mode}")


def build_wrap() -> Image.Image:
    # 6x9, ~220 pp cream ESTIMATE. KDP cream = pages * 0.0025"
    DPI = 300
    trim_w, trim_h = 6 * DPI, 9 * DPI
    spine = int(round(0.55 * DPI))  # 165
    bleed_l, bleed_r = 38, 37
    bleed_t, bleed_b = 38, 37
    W = bleed_l + trim_w + spine + trim_w + bleed_r  # 3840
    H = bleed_t + trim_h + bleed_b                    # 2775

    cloth = navy_cloth(W, H, seed=19)
    back_x0 = bleed_l
    spine_x0 = bleed_l + trim_w
    front_x0 = spine_x0 + spine
    trim_y0 = bleed_t

    front = typeset_front(navy_cloth(trim_w, trim_h, seed=17))
    cloth.paste(front, (front_x0, trim_y0))
    # bleed extend front
    edge = front.crop((trim_w - 1, 0, trim_w, trim_h))
    for i in range(bleed_r):
        cloth.paste(edge, (front_x0 + trim_w + i, trim_y0))
    top = cloth.crop((front_x0, trim_y0, front_x0 + trim_w, trim_y0 + 1))
    for i in range(bleed_t):
        cloth.paste(top, (front_x0, i))
    bot = cloth.crop((front_x0, trim_y0 + trim_h - 1, front_x0 + trim_w, trim_y0 + trim_h))
    for i in range(bleed_b):
        cloth.paste(bot, (front_x0, trim_y0 + trim_h + i))

    # SPINE: STEADFAST MEN / Hart  — US top-to-bottom, no fold rule
    spine_clear = int(round(0.0625 * DPI))
    usable_sw = spine - 2 * spine_clear
    fsp = F("LibreFranklin-Medium.ttf", 40)
    fhart = F("LibreFranklin-Medium.ttf", 34)
    line1 = TITLE + " " + TITLE2
    gap = 40
    tw = tracked_width(fsp, line1, 3.0) + gap + tracked_width(fhart, SPINE_AUTHOR, 5.0) + 8
    sh = int(usable_sw)
    type_im = Image.new("RGBA", (int(tw), sh), (0, 0, 0, 0))
    td = ImageDraw.Draw(type_im)
    x = 0
    for ch in line1:
        td.text((x, sh / 2), ch, font=fsp, fill=GOLD + (255,), anchor="lm")
        x += fsp.getlength(ch) + 3.0
    x += gap
    for ch in SPINE_AUTHOR:
        td.text((x, sh / 2), ch, font=fhart, fill=BONE + (255,), anchor="lm")
        x += fhart.getlength(ch) + 5.0
    type_rot = type_im.transpose(Image.Transpose.ROTATE_270)
    dest_x = spine_x0 + (spine - type_rot.size[0]) // 2
    dest_y = int(0.45 * DPI)
    cloth.paste(type_rot, (dest_x, dest_y), type_rot)

    # BACK: short Wes Hart lockup only. No blurb. No ISBN barcode.
    d = ImageDraw.Draw(cloth)
    cx_back = back_x0 + trim_w / 2.0
    cy0 = trim_y0 + int(0.28 * trim_h)
    scale = trim_w / 1600.0
    y = plumb_bob(d, cx_back, cy0, scale=scale * 0.85)
    fauth = F("LibreFranklin-Medium.ttf", 52)
    fsub = F("EBGaramond-Italic.ttf", 42)
    fsmall = F("PlayfairDisplay-Bold.ttf", 28)
    y = draw_lt(d, cx_back, y + 48, AUTHOR, fauth, BONE, 8)
    y = draw_lt(d, cx_back, y + 28, SUB, fsub, BONE, 0.6)
    # locked four-marks line — whole-line draw so commas stay visible
    fcreed = F("EBGaramond-Italic.ttf", 46)
    col_w = trim_w - 2 * int(0.70 * DPI)
    y += 56
    for line in wrap_words(fcreed, CREED, col_w, 0.0):
        d.text((cx_back, y), line, font=fcreed, fill=GOLD, anchor="mt")
        y += ink_height(fcreed, line) + 14
    draw_lt(
        d,
        cx_back,
        trim_y0 + trim_h - int(0.70 * DPI),
        TITLE + "  " + TITLE2,
        fsmall,
        GOLD,
        4,
    )
    return cloth


def main() -> None:
    front = typeset_front(navy_cloth(1600, 2560, seed=17))
    save_png(front, ROOT / "a-front-v2.png", expect=(1600, 2560))
    t160 = front.resize((160, 256), Image.Resampling.LANCZOS)
    save_png(t160, ROOT / "a-thumb-160.png", expect=(160, 256))
    t320 = front.resize((320, 512), Image.Resampling.LANCZOS)
    save_png(t320, ROOT / "a-thumb-320.png", expect=(320, 512))

    wrap = build_wrap()
    save_png(wrap, ROOT / "a-wrap.png", expect=(3840, 2775))

    md = ROOT / "press.md"
    md.write_text(
        """# Steadfast Men — press covers

**Title lock:** STEADFAST MEN / The way of Godly Men / Wes Hart

Not sent to Aaron. Jarvis presents.

`book/art/covers/`, `covers-v2/`, and `covers-v3/` were not touched.

## Locked pick — A
Navy cloth, gold Playfair, plumb. Do not average with B/C/D.

Locked original (do not overwrite until told): `press-a.png` (1600×2560 RGB).

### A v2 (iterate)
- `a-front-v2.png` — 1600×2560 RGB. Larger gold lockup. Plumb is a standing cord + teardrop bob (not a Roman I, not a cross, not a compass).
- `a-thumb-160.png` — 160×256 Amazon thumb
- `a-thumb-320.png` — 320×512
- `a-wrap.png` — 6×9 KDP wrap, 3840×2775 px @ 300 DPI (back | spine | front)

Palette: navy `#0B1F38` · gold `#E3C572` · bone `#E6DDCC`  
Type: Playfair Display Bold, EB Garamond Italic, Libre Franklin Medium.

**Wrap math (estimate):** cream B&W, **~220 pages** (manuscript still in progress; recalc at bind). KDP cream spine = pages × 0.0025" → 0.55" (165 px). Width 12.80", height 9.25". Spine type: STEADFAST MEN / Hart. No fold rule. Back: Wes Hart lockup + locked four-marks line (commas): A real man rejects passivity, accepts responsibility, leads courageously, and expects the greater reward, God's reward. No fake blurbs. No ISBN barcode yet.

## Unused roads (frozen)
- B cream stacked navy — `press-b.png`
- C charcoal geometric — `press-c.png`
- D near-black bone — `press-d.png`
""",
        encoding="utf-8",
    )
    print("wrote press.md")


if __name__ == "__main__":
    main()
