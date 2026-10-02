#!/usr/bin/env python3
"""Simple four-mark figure for Steadfast Men ch 03. Mark names only. No unpacking.
2026-10-01: Steadfast marks (renamed from the retired Lewis nouns). Labels print in tracked caps."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("/workspace/biblical-manhood/book/art")
PPI = 300
BONE = (244, 239, 228)
INK = (44, 41, 36)
RUST = (122, 74, 50)
RULE = (196, 184, 168)

FONT_WORD = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_SMALL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"

MARKS = ["Stop Waiting", "Pick Up the Weight", "Go First", "Work for God's Pay"]


def label(mark: str) -> str:
    """Display form: tracked caps, typographic apostrophe."""
    return mark.upper().replace("'", "\u2019")


def pt(n):
    return int(round(n * PPI / 72))


def draw_label(draw, text, xy, font, fill, tracking_px):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking_px
    return x


def main():
    word_f = ImageFont.truetype(FONT_WORD, pt(11))
    cap_f = ImageFont.truetype(FONT_SMALL, pt(8.5))
    a, d = word_f.getmetrics()
    word_h = a + d
    track = 4.2

    pad_t = pt(16)
    pad_b = pt(14)
    pad_r = pt(16)
    rail_x = pt(14)
    rail_w = max(2, pt(0.65))
    tick_w = max(8, pt(6))
    inner_l = rail_x + tick_w + pt(10)
    row_h = pt(28)
    gap = pt(10)

    # measure widest word
    tmp = Image.new("RGB", (10, 10), BONE)
    td = ImageDraw.Draw(tmp)
    max_w = 0
    for m in MARKS:
        w = 0
        for ch in label(m):
            w += td.textlength(ch, font=word_f) + track
        max_w = max(max_w, w)

    W = inner_l + int(max_w) + pad_r
    H = pad_t + 4 * row_h + 3 * gap + pad_b

    img = Image.new("RGB", (W, H), BONE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=RULE, width=1)
    d.rectangle([rail_x, pt(10), rail_x + rail_w, H - pt(10)], fill=RUST)

    y = pad_t
    tick_h = max(3, pt(2.4))
    for i, mark in enumerate(MARKS):
        cy = y + word_h // 2
        d.rectangle(
            [rail_x - 1, cy - tick_h // 2, rail_x + tick_w, cy + tick_h // 2 + 1],
            fill=RUST,
        )
        draw_label(d, label(mark), (inner_l, y), word_f, RUST, track)
        y += row_h + gap

    png = OUT / "03-four-marks.png"
    img.save(png, "PNG", dpi=(PPI, PPI))
    preview = img.resize((max(1, W // 2), max(1, H // 2)), Image.Resampling.LANCZOS)
    preview.save(OUT / "03-four-marks-preview.png", "PNG", dpi=(150, 150))
    print(png, img.size)


if __name__ == "__main__":
    main()
