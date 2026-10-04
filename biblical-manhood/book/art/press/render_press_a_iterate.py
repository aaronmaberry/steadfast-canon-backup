#!/usr/bin/env python3
"""Iterate locked Press A. Does NOT write press-a.png / b / c / d."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/workspace/biblical-manhood/book/art/press")
FONTS = ROOT / "fonts"

TITLE, TITLE2 = "STEADFAST", "MEN"
SUB = "The way of Godly Men"
AUTHOR = "WES HART"

# Locked palette, gold nudged one step brighter so it holds at 160px
NAVY = np.array([11, 31, 56], dtype=np.float32)  # #0B1F38
GOLD = (227, 197, 114)  # #E3C572
BONE = (230, 221, 204)  # #E6DDCC
BONE_DIM = (196, 186, 168)
CREED = (
    "A real man rejects passivity, accepts responsibility, "
    "leads courageously, and expects the greater reward, God's reward."
)
HOOK = "You picked this up for a reason. I won't pretend I know which one."
HOOK2 = (
    "God isn't confused about you. He made you on purpose. "
    "He isn't embarrassed by manhood and He isn't impressed by the knockoffs."
)
# From 00-introduction.md (locked)


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


def fit_size(font_name: str, text: str, target_w: float, tracking_em: float = 0.06,
             lo: float = 24, hi: float = 520) -> tuple[float, float]:
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
    for i, ch in enumerate(text):
        draw.text((x, y_top), ch, font=font, fill=fill, anchor="lt")
        x += font.getlength(ch) + tracking
    return y_top + ink_height(font, text)


def draw_lt_left(draw, x0, y_top, text, font, fill, tracking) -> float:
    x = x0
    for i, ch in enumerate(text):
        draw.text((x, y_top), ch, font=font, fill=fill, anchor="lt")
        x += font.getlength(ch) + tracking
    return y_top + ink_height(font, text)


def wrap_words(font, text, max_w, tracking=0.0) -> list[str]:
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


def plumb_mark(draw, cx, y_top, color, bar_h, bar_w, base_w, base_h) -> float:
    x0 = cx - bar_w / 2.0
    draw.rectangle([x0, y_top, x0 + bar_w, y_top + bar_h], fill=color)
    bx0 = cx - base_w / 2.0
    yb = y_top + bar_h
    draw.rectangle([bx0, yb, bx0 + base_w, yb + base_h], fill=color)
    return y_top + bar_h + base_h


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


def typeset_front(im: Image.Image) -> Image.Image:
    """A lockup scaled to whatever front size is on `im`."""
    w, h = im.size
    d = ImageDraw.Draw(im)
    cx = w / 2.0
    usable = w - 2 * (0.09 * w)

    s1, tr1 = fit_size("PlayfairDisplay-Bold.ttf", TITLE, usable, tracking_em=0.07, hi=0.145 * w)
    s2 = min(s1 * 1.58, 0.195 * w)
    tr2 = 0.10 * s2
    f1 = F("PlayfairDisplay-Bold.ttf", s1)
    f2 = F("PlayfairDisplay-Bold.ttf", s2)
    fsub = F("EBGaramond-Italic.ttf", max(28, 0.032 * w))
    fauth = F("LibreFranklin-Medium.ttf", max(26, 0.028 * w))

    y = 0.125 * h
    y = draw_lt(d, cx, y, TITLE, f1, GOLD, tr1)
    y = draw_lt(d, cx, y + 0.012 * h, TITLE2, f2, GOLD, tr2)
    y = draw_lt(d, cx, y + 0.028 * h, SUB, fsub, BONE, 0.8)

    bar_h = 0.085 * h
    bar_w = max(12, 0.014 * w)
    base_w = 0.062 * w
    base_h = max(6, 0.0055 * h)
    plumb_mark(d, cx, y + 0.032 * h, GOLD, bar_h, bar_w, base_w, base_h)

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
    print(f"wrote {path} {im.size} {im.mode}")


def build_ebook_front() -> Image.Image:
    w, h = 1600, 2560
    return typeset_front(navy_cloth(w, h, seed=17))


def build_print_front(w=1800, h=2700) -> Image.Image:
    return typeset_front(navy_cloth(w, h, seed=17))


def build_wrap() -> Image.Image:
    # 6x9, 220 pp cream, KDP G201953020. 300 DPI.
    DPI = 300
    bleed = int(round(0.125 * DPI))          # 38
    trim_w = 6 * DPI                         # 1800
    trim_h = 9 * DPI                         # 2700
    spine = int(round(0.55 * DPI))           # 165
    W = bleed + trim_w + spine + trim_w + bleed   # 3841 if bleed=38
    H = bleed + trim_h + bleed
    # Snap to documented 3840 x 2775 by using bleed 37.5 → 38 left/right would be odd.
    # Use exact: bleed 38, spine 165 → width 38+1800+165+1800+38 = 3841.
    # Prefer even 3840: bleed 37, spine 166 (0.553") — document in md.
    # Official: 0.125*300=37.5. We'll use 38/37 split to hit 3840:
    bleed_l, bleed_r = 38, 37
    bleed_t, bleed_b = 38, 37
    spine = 165
    W = bleed_l + trim_w + spine + trim_w + bleed_r  # 3840
    H = bleed_t + trim_h + bleed_b                    # 2775

    cloth = navy_cloth(W, H, seed=19)
    d = ImageDraw.Draw(cloth)

    back_x0 = bleed_l
    spine_x0 = bleed_l + trim_w
    front_x0 = spine_x0 + spine
    trim_y0 = bleed_t

    # --- FRONT panel (trim box) ---
    front = build_print_front(trim_w, trim_h)
    cloth.paste(front, (front_x0, trim_y0))
    # bleed: extend navy already in cloth; clone front edge into outer bleed
    if bleed_r:
        edge = front.crop((trim_w - 1, 0, trim_w, trim_h))
        for i in range(bleed_r):
            cloth.paste(edge, (front_x0 + trim_w + i, trim_y0))
    if bleed_t:
        top = cloth.crop((front_x0, trim_y0, front_x0 + trim_w, trim_y0 + 1))
        for i in range(bleed_t):
            cloth.paste(top, (front_x0, i))
    if bleed_b:
        bot = cloth.crop((front_x0, trim_y0 + trim_h - 1, front_x0 + trim_w, trim_y0 + trim_h))
        for i in range(bleed_b):
            cloth.paste(bot, (front_x0, trim_y0 + trim_h + i))

    # --- SPINE (no vertical rule on the fold) ---
    spine_clear = int(round(0.0625 * DPI))  # 19px
    usable_sw = spine - 2 * spine_clear
    fspine = F("LibreFranklin-Medium.ttf", 42)
    fhart = F("LibreFranklin-Medium.ttf", 36)
    # Draw horizontal then rotate 90° clockwise (US top-to-bottom)
    gap = 48
    tw1 = tracked_width(fspine, TITLE + " " + TITLE2, 3.2)
    tw2 = tracked_width(fhart, AUTHOR, 6)
    strip_w = int(tw1 + gap + tw2 + 8)
    strip_h = int(usable_sw)
    strip = Image.new("RGB", (strip_w, strip_h), tuple(int(c) for c in NAVY))
    # match cloth under spine by cropping
    spine_panel = cloth.crop((spine_x0, 0, spine_x0 + spine, H))
    sd = ImageDraw.Draw(strip)
    # We'll assemble on a tall spine canvas instead, rotating type
    spine_img = spine_panel.copy()
    # Make a long type image
    type_im = Image.new("RGBA", (strip_w, strip_h), (0, 0, 0, 0))
    td = ImageDraw.Draw(type_im)
    x = 0
    for i, ch in enumerate(TITLE + " " + TITLE2):
        td.text((x, strip_h / 2), ch, font=fspine, fill=GOLD + (255,), anchor="lm")
        x += fspine.getlength(ch) + 3.2
    x += gap
    for i, ch in enumerate(AUTHOR):
        td.text((x, strip_h / 2), ch, font=fhart, fill=BONE + (255,), anchor="lm")
        x += fhart.getlength(ch) + 6
    type_rot = type_im.transpose(Image.Transpose.ROTATE_270)  # 90° clockwise
    # Center in spine, top-to-bottom, with vertical inset 0.45"
    inset_y = int(0.45 * DPI)
    dest_x = (spine - type_rot.size[0]) // 2
    dest_y = inset_y
    # If type is shorter than spine minus insets, that's good — sits in the upper-middle
    max_h = H - 2 * inset_y
    if type_rot.size[1] > max_h:
        type_rot = type_rot.resize((type_rot.size[0], max_h), Image.Resampling.LANCZOS)
    spine_img.paste(type_rot, (dest_x, dest_y), type_rot)
    cloth.paste(spine_img, (spine_x0, 0))

    # --- BACK ---
    d = ImageDraw.Draw(cloth)
    inset = int(0.70 * DPI)  # 0.70" from back trim
    bx0 = back_x0 + inset
    by0 = trim_y0 + inset
    bx1 = back_x0 + trim_w - inset
    col_w = bx1 - bx0
    cx_back = (bx0 + bx1) / 2.0

    fhook = F("EBGaramond-Regular.ttf", 48)   # ~11.5pt
    fhook2 = F("EBGaramond-Regular.ttf", 46)
    fcreed = F("EBGaramond-Italic.ttf", 44)
    fcat = F("LibreFranklin-Medium.ttf", 28)
    ftitle = F("PlayfairDisplay-Bold.ttf", 36)

    y = by0
    # small plumb
    y = plumb_mark(d, cx_back, y, GOLD, bar_h=70, bar_w=12, base_w=56, base_h=6)
    y += 54

    def block(text, font, fill, leading, tracking=0.4):
        nonlocal y
        for line in wrap_words(font, text, col_w, tracking):
            draw_lt_left(d, bx0, y, line, font, fill, tracking)
            y += ink_height(font, line) + leading
        return y

    block(HOOK, fhook, BONE, leading=14, tracking=0.3)
    y += 28
    block(HOOK2, fhook2, BONE, leading=14, tracking=0.3)
    y += 40
    # thin gold rule
    rw = 120
    d.rectangle([cx_back - rw / 2, y, cx_back + rw / 2, y + 3], fill=GOLD)
    y += 36
    block(CREED, fcreed, GOLD, leading=12, tracking=0.2)

    # category bottom-left of back (above barcode row)
    cat = "CHRISTIAN LIVING  /  MEN"
    cat_y = trim_y0 + trim_h - int(0.55 * DPI) - ink_height(fcat, cat)
    draw_lt_left(d, bx0, cat_y, cat, fcat, BONE_DIM, 2.4)

    # KDP barcode box: bottom-right of BACK, 2.0" x 1.2"
    bw, bh = int(2.0 * DPI), int(1.2 * DPI)
    box_r = back_x0 + trim_w - int(0.30 * DPI)
    box_b = trim_y0 + trim_h - int(0.30 * DPI)
    box_l = box_r - bw
    box_t = box_b - bh
    d.rectangle([box_l, box_t, box_r, box_b], fill=(245, 245, 245))
    d.rectangle([box_l, box_t, box_r, box_b], outline=(180, 180, 180), width=2)

    return cloth, (front_x0, trim_y0, front_x0 + trim_w, trim_y0 + trim_h)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    front = build_ebook_front()
    save_png(front, ROOT / "press-a-iterate.png", expect=(1600, 2560))
    thumb = front.resize((160, 256), Image.Resampling.LANCZOS)
    save_png(thumb, ROOT / "press-a-iterate-thumb.png", expect=(160, 256))
    thumb80 = front.resize((80, 128), Image.Resampling.LANCZOS)
    save_png(thumb80, ROOT / "press-a-iterate-thumb-80.png", expect=(80, 128))

    wrap, front_box = build_wrap()
    save_png(wrap, ROOT / "press-a-wrap.png", expect=(3840, 2775))
    fx0, fy0, fx1, fy1 = front_box
    wrap_front = wrap.crop((fx0, fy0, fx1, fy1))
    save_png(wrap_front, ROOT / "press-a-wrap-front.png", expect=(1800, 2700))

    md = ROOT / "press-a-iterate.md"
    md.write_text(
        """# Press A iterate — locked navy cloth

Aaron locked Press A. This folder keeps `press-a.png` untouched.

**Title lock:** STEADFAST MEN / The way of Godly Men / Wes Hart

Not sent to Aaron. Cole holds files; Jarvis presents.

## Files
- `press-a.png` — locked pick (do not overwrite)
- `press-a-iterate.png` — 1600×2560 RGB, stronger thumb
- `press-a-iterate-thumb.png` — 160×256
- `press-a-iterate-thumb-80.png` — 80×128 search size
- `press-a-wrap.png` — KDP 6×9 wrap, 3840×2775 px @ 300 DPI (back | spine | front)
- `press-a-wrap-front.png` — wrap front trim crop, 1800×2700 (6×9 @ 300)

B/C/D unused. `covers/`, `covers-v2/`, `covers-v3/` not touched.

## What changed vs locked A
Same road: navy cloth `#0B1F38`, gold Playfair, bone italic subtitle, gold plumb, Wes Hart at the foot.
- Title lockup larger (MEN ~1.58× STEADFAST, wider usable)
- Gold `#E3C572` (one step brighter foil, still cloth-and-gold)
- Plumb scaled to ~8.5% of cover height so it reads as a tick at 160px
- Typeset as fractions so the 6×9 front matches the ebook front

## Wrap math (KDP G201953020)
Cream interior, **220 pages assumed** (manuscript in progress; recalc after last chapter).
- Spine = 220 × 0.0025" = **0.55"** (165 px @ 300)
- Width = 0.125 + 6 + 0.55 + 6 + 0.125 = 12.80" → **3840 px** (bleed 38/37 to land even)
- Height = 0.125 + 9 + 0.125 = 9.25" → **2775 px**
- No vertical rule on the spine fold. Spine type: STEADFAST MEN + WES HART, US top-to-bottom, ≥0.0625" side clearance.
- Back hook from `book/00-introduction.md`. Barcode box empty (KDP fills). Category: CHRISTIAN LIVING / MEN.
- Matte. No portrait. No fake imprint.

## Palette
Navy `#0B1F38` · Gold `#E3C572` · Bone `#E6DDCC`
Playfair Display Bold, EB Garamond Italic/Regular, Libre Franklin Medium.
""",
        encoding="utf-8",
    )
    print(f"wrote {md}")


if __name__ == "__main__":
    main()
