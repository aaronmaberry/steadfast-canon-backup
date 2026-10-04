#!/usr/bin/env python3
"""Chapter 34 man-plan worksheet. Cloth Store.
Contrast lock 2026-09-07: gold accent on navy ONLY. No gold-on-bone.
Body high contrast. Writes ONLY under book/art/.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("/workspace/biblical-manhood/book/art")
MAST = Path("/workspace/biblical-manhood/training/print/image-2.0/week-02-mast.png")
FONTS = Path("/workspace/biblical-manhood/training/print/fonts")

PPI = 300
W = 6 * PPI
H = 9 * PPI

NAVY = (11, 31, 56)       # #0B1F38
GOLD = (227, 197, 114)    # #E3C572
BONE = (230, 221, 204)    # #E6DDCC
RULE = (90, 82, 70)       # darker write lines on bone
RULE_ON_NAVY = (180, 168, 148)


def pt(n):
    return int(round(n * PPI / 72))


def font(name, size_pt):
    return ImageFont.truetype(str(FONTS / name), pt(size_pt))


def text_h(fnt):
    a, d = fnt.getmetrics()
    return a + d


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def hairline(d, y, x0, x1, color=RULE, width=2):
    d.line([(x0, y), (x1, y)], fill=color, width=width)


def main():
    img = Image.new("RGB", (W, H), BONE)
    d = ImageDraw.Draw(img)

    mast = Image.open(MAST).convert("RGB")
    band_h = int(1.28 * PPI)
    scale = W / mast.width
    mw, mh = W, int(mast.height * scale)
    mast = mast.resize((mw, mh), Image.Resampling.LANCZOS)
    top = max(0, int(mh * 0.42))
    if top + band_h > mh:
        top = mh - band_h
    band = mast.crop((0, top, W, top + band_h))
    img.paste(band, (0, 0))

    playfair_b = font("PlayfairDisplay-Bold.ttf", 22)
    playfair_i = font("PlayfairDisplay-Italic.ttf", 13)
    playfair_t = font("PlayfairDisplay-Bold.ttf", 28)
    garamond = font("EBGaramond-Regular.ttf", 12)
    garamond_i = font("EBGaramond-Italic.ttf", 11)
    franklin = font("LibreFranklin-Medium.ttf", 8)

    m = pt(50)
    x0, x1 = m, W - m

    d.text((m, pt(22)), "34", font=playfair_b, fill=BONE)

    y = band_h + pt(28)
    d.text((m, y), "Write the next move", font=playfair_t, fill=NAVY)
    y += text_h(playfair_t) + pt(6)
    d.text((m, y), "Ink, not the windshield.", font=playfair_i, fill=NAVY)
    y += text_h(playfair_i) + pt(22)

    d.text((m, y), "THE COURSE THAT SITS STILL", font=franklin, fill=NAVY)
    y += text_h(franklin) + pt(8)
    hint = "One sentence you would still own if a brother read it out loud."
    for line in wrap(d, hint, garamond_i, x1 - x0):
        d.text((m, y), line, font=garamond_i, fill=NAVY)
        y += int(text_h(garamond_i) * 1.2)
    y += pt(16)
    for _ in range(4):
        y += pt(26)
        hairline(d, y, x0, x1, RULE, 2)

    y += pt(28)

    # THIS WEEK — navy field, gold accent only (no gold-on-bone)
    panel_top = y
    panel_h = pt(150)
    d.rectangle([m - pt(10), panel_top, W - m + pt(10), panel_top + panel_h], fill=NAVY)
    # gold accent rule under label
    gy = panel_top + pt(16)
    d.text((m, gy), "THIS WEEK", font=franklin, fill=GOLD)
    gy += text_h(franklin) + pt(6)
    d.rectangle([m, gy, m + pt(72), gy + 4], fill=GOLD)
    gy += pt(14)
    d.text((m, gy), "The step, with a day on it.", font=garamond, fill=BONE)
    gy += text_h(garamond) + pt(18)
    hairline(d, gy, x0, x1, RULE_ON_NAVY, 2)
    gy += pt(24)
    hairline(d, gy, x0, x1, RULE_ON_NAVY, 2)
    y = panel_top + panel_h + pt(22)

    d.text((m, y), "The day:", font=garamond_i, fill=NAVY)
    dw = d.textlength("The day:", font=garamond_i)
    hairline(d, y + text_h(garamond_i) - 4, m + dw + pt(8), m + pt(220), RULE, 2)

    foot = "Steadfast Men, The way of Godly Men"
    fw = d.textlength(foot, font=garamond_i)
    fy = H - m
    hairline(d, fy - pt(14), x0, x1, RULE, 2)
    d.text(((W - fw) / 2, fy), foot, font=garamond_i, fill=NAVY)

    png = OUT / "34-man-plan.png"
    img.save(png, "PNG", dpi=(PPI, PPI), optimize=True)
    preview = img.resize((W // 3, H // 3), Image.Resampling.LANCZOS)
    prev = OUT / "34-man-plan-preview.png"
    preview.save(prev, "PNG", dpi=(100, 100), optimize=True)
    (OUT / "34-man-plan.md").write_text(
        "\n".join(
            [
                "# 34 man-plan worksheet",
                "",
                "Original book page for chapter 34. Not a training packet. Not a Lewis past/present/future form.",
                "One course that sits still, then one step this week with a day on it.",
                "",
                "- `34-man-plan.png` — 6x9, 300 ppi, Cloth Store",
                "- `34-man-plan-preview.png` — third-size look",
                "",
                "Contrast lock 2026-09-07: THIS WEEK is navy with gold accent only. No gold-on-bone.",
                "Navy cloth mast is the locked Image 2.0 still (`training/print/image-2.0/week-02-mast.png`).",
                "Body navy on bone. Write lines darkened. Footer one quiet brand line.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print("PNG", png, img.size)


if __name__ == "__main__":
    main()
