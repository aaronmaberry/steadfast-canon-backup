#!/usr/bin/env python3
"""Round 2 comps. FULLER covers. Writes ONLY to covers-v2/.
Do not touch book/art/covers/cover-a.png through cover-d.png.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

OUT = Path("/workspace/biblical-manhood/book/art/covers-v2")
TEX_PASTURE = Path("/workspace/biblical-manhood/book/art/covers/cover-b-texture.png")

W, H = 1600, 2560

BONE = (244, 239, 228)
INK = (44, 41, 36)
INK_SOFT = (90, 84, 76)
RUST = (122, 74, 50)
NIGHT = (22, 20, 18)
NAVY = (24, 36, 62)
LEDGER_CREAM = (246, 240, 224)
LEDGER_RED = (158, 48, 44)
LEDGER_LINE = (214, 204, 186)
GRAY_BORDER = (150, 148, 144)

FONT_TITLE = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_CROMAN = "/usr/share/fonts/opentype/urw-base35/C059-Roman.otf"
FONT_ITAL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"
FONT_ROMAN = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"

TITLE = "STEADFAST"
TITLE2 = "MEN"
SUB = "The way of Godly Men"
SUB_SC = "THE WAY OF GODLY MEN"
BY = "Wes Hart"


def font(path, px):
    return ImageFont.truetype(path, px)


def tracked_width(draw, text, fnt, tracking):
    w = 0
    for i, ch in enumerate(text):
        w += draw.textlength(ch, font=fnt)
        if i < len(text) - 1:
            w += tracking
    return w


def draw_tracked(draw, text, xy, fnt, fill, tracking):
    x, y = xy
    for i, ch in enumerate(text):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


def text_h(fnt):
    a, d = fnt.getmetrics()
    return a + d


def grain(img, amount=8, seed=11):
    rng = random.Random(seed)
    noise = Image.new("L", img.size, 0)
    px = noise.load()
    w, h = img.size
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            v = 128 + rng.randint(-amount, amount)
            px[x, y] = v
            if x + 1 < w:
                px[x + 1, y] = v
            if y + 1 < h:
                px[x, y + 1] = v
                if x + 1 < w:
                    px[x + 1, y + 1] = v
    noise = noise.filter(ImageFilter.GaussianBlur(0.55))
    noise_rgb = Image.merge("RGB", (noise, noise, noise))
    return Image.blend(img, noise_rgb, 0.04)


def hairline_border(img, px=4, color=GRAY_BORDER):
    d = ImageDraw.Draw(img)
    for i in range(px):
        d.rectangle([i, i, W - 1 - i, H - 1 - i], outline=color)
    return img


def fit_cover(src, crop="center"):
    src = src.convert("RGB")
    scale = H / src.height
    nw, nh = int(src.width * scale), H
    src = src.resize((nw, nh), Image.Resampling.LANCZOS)
    if nw >= W:
        if crop == "left":
            left = 0
        elif crop == "right":
            left = nw - W
        else:
            left = (nw - W) // 2
        return src.crop((left, 0, left + W, H))
    canvas = Image.new("RGB", (W, H), src.getpixel((0, 0)))
    canvas.paste(src, ((W - nw) // 2, 0))
    return canvas


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", dpi=(266, 266), optimize=True)
    thumb = img.resize((200, int(200 * H / W)), Image.Resampling.LANCZOS)
    thumb.save(OUT / name.replace(".png", "-thumb.png"), "PNG", optimize=True)
    print("WROTE", path, img.size)
    return path


def cover_a():
    """Big type on bone. Title owns the board."""
    img = Image.new("RGB", (W, H), BONE)
    img = grain(img, amount=7, seed=3)
    d = ImageDraw.Draw(img)
    f_st = font(FONT_TITLE, 176)
    f_men = font(FONT_TITLE, 268)
    f_sub = font(FONT_ITAL, 46)
    f_by = font(FONT_ROMAN, 40)
    left = 56
    y = 64
    track_st = 2
    draw_tracked(d, TITLE, (left, y), f_st, INK, track_st)
    y += int(text_h(f_st) * 0.88)
    draw_tracked(d, TITLE2, (left, y), f_men, INK, 10)
    y += int(text_h(f_men) * 0.92)
    d.rectangle([left, y, W - 56, y + 10], fill=RUST)
    y += 52
    d.text((left, y), SUB, font=f_sub, fill=INK_SOFT)
    d.rectangle([40, 48, 54, H - 140], fill=RUST)
    d.text((left, H - 180), BY, font=f_by, fill=INK_SOFT)
    return hairline_border(img)


def cover_b():
    """Type + large object. Iron post fills most of the frame; type sits in it."""
    img = Image.new("RGB", (W, H), BONE)
    img = grain(img, amount=6, seed=9)
    d = ImageDraw.Draw(img)
    post_x = 48
    post_w = 240
    d.rectangle([post_x, 40, post_x + post_w, H - 40], fill=RUST)
    tick_w = 980
    tick_h = 64
    inner_top, inner_bot = 90, H - 90
    for i in range(4):
        cy = inner_top + int((i + 0.5) * (inner_bot - inner_top) / 4)
        d.rectangle(
            [post_x, cy - tick_h // 2, post_x + tick_w, cy + tick_h // 2],
            fill=RUST,
        )
    f_title = font(FONT_TITLE, 118)
    f_sub = font(FONT_ITAL, 34)
    f_by = font(FONT_ROMAN, 32)
    left = 340
    y = 500
    track = 2
    draw_tracked(d, TITLE, (left, y), f_title, INK, track)
    y += int(text_h(f_title) * 0.94)
    draw_tracked(d, TITLE2, (left, y), f_title, INK, track + 6)
    y += int(text_h(f_title) * 1.00)
    tw = tracked_width(d, TITLE, f_title, track)
    rule_w = min(tw, W - left - 48)
    d.rectangle([left, y, left + rule_w, y + 6], fill=INK)
    y += 36
    d.text((left, y), SUB, font=f_sub, fill=INK)
    d.text((left, H - 180), BY, font=f_by, fill=INK)
    return img


def cover_c():
    """Fuller photograph. Quiet Texas pasture filling the wrap. Large type."""
    src = Image.open(TEX_PASTURE).convert("RGB")
    img = fit_cover(src, crop="left")
    img = grain(img, amount=5, seed=8)
    scrim = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(scrim)
    for i in range(1100):
        sd.rectangle([0, i, W, i + 1], fill=int(120 * (1 - i / 1100) ** 1.05))
    for i in range(380):
        y = H - 380 + i
        sd.rectangle([0, y, W, y + 1], fill=int(90 * (i / 380)))
    dark = Image.new("RGB", (W, H), (28, 24, 20))
    img = Image.composite(dark, img, scrim)
    d = ImageDraw.Draw(img)
    f_title = font(FONT_TITLE, 164)
    f_sub = font(FONT_ITAL, 42)
    f_by = font(FONT_ROMAN, 36)
    left = 64
    y = 96
    track = 2
    draw_tracked(d, TITLE, (left, y), f_title, BONE, track)
    y += int(text_h(f_title) * 0.90)
    draw_tracked(d, TITLE2, (left, y), f_title, BONE, track + 6)
    y += int(text_h(f_title) * 0.96)
    tw = tracked_width(d, TITLE, f_title, track)
    d.rectangle([left, y, left + min(tw, 1100), y + 8], fill=RUST)
    y += 44
    d.text((left, y), SUB, font=f_sub, fill=BONE)
    d.text((left, H - 170), BY, font=f_by, fill=BONE)
    return img


def cover_d():
    """Night field filled. Type and mark take real estate."""
    img = Image.new("RGB", (W, H), NIGHT)
    overlay = Image.new("RGB", (W, H), (38, 34, 30))
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([-180, 200, W + 180, H - 80], fill=90)
    mask = mask.filter(ImageFilter.GaussianBlur(160))
    img = Image.composite(overlay, img, mask)
    img = grain(img, amount=9, seed=21)
    d = ImageDraw.Draw(img)
    d.rectangle([48, 80, 88, H - 80], fill=RUST)
    tick_w = 420
    tick_h = 36
    for i in range(4):
        cy = 160 + int((i + 0.5) * (H - 320) / 4)
        d.rectangle([48, cy - tick_h // 2, 48 + tick_w, cy + tick_h // 2], fill=RUST)
    f_st = font(FONT_TITLE, 176)
    f_men = font(FONT_TITLE, 220)
    f_sub = font(FONT_ITAL, 42)
    f_by = font(FONT_ROMAN, 36)
    left = 120
    y = 200
    track = 2
    draw_tracked(d, TITLE, (left, y), f_st, BONE, track)
    y += int(text_h(f_st) * 0.88)
    draw_tracked(d, TITLE2, (left, y), f_men, BONE, 8)
    y += int(text_h(f_men) * 0.92)
    d.rectangle([left, y, W - 64, y + 10], fill=RUST)
    y += 48
    d.text((left, y), SUB, font=f_sub, fill=(200, 192, 178))
    d.text((left, H - 180), BY, font=f_by, fill=(200, 192, 178))
    return img


def cover_e():
    """Work Ledger filled. Cream invoice, navy type, one thin red rule. Used, not sparse."""
    img = Image.new("RGB", (W, H), LEDGER_CREAM)
    img = grain(img, amount=6, seed=4)
    d = ImageDraw.Draw(img)
    yline = 160
    while yline < H - 64:
        d.line([(72, yline), (W - 56, yline)], fill=LEDGER_LINE, width=2)
        yline += 48
    d.rectangle([0, 0, 56, H], fill=(236, 226, 206))
    for cy in range(72, H - 40, 64):
        d.ellipse([18, cy, 38, cy + 20], outline=(196, 184, 168), width=2)
    f_st = font(FONT_TITLE, 168)
    f_men = font(FONT_TITLE, 232)
    f_sub = font(FONT_CROMAN, 30)
    f_by = font(FONT_CROMAN, 38)
    left = 84
    y = 200
    track = 2
    draw_tracked(d, TITLE, (left, y), f_st, NAVY, track)
    y += int(text_h(f_st) * 0.88)
    draw_tracked(d, TITLE2, (left, y), f_men, NAVY, 8)
    y += int(text_h(f_men) * 0.92)
    d.rectangle([left, y, W - 64, y + 8], fill=LEDGER_RED)
    y += 48
    draw_tracked(d, SUB_SC, (left, y), f_sub, NAVY, 5)
    prep = font(FONT_CROMAN, 18)
    d.text((left, H - 260), "PREPARED BY", font=prep, fill=NAVY)
    d.text((left, H - 210), BY, font=f_by, fill=NAVY)
    return hairline_border(img)


def main():
    assert str(OUT).endswith("covers-v2")
    OUT.mkdir(parents=True, exist_ok=True)
    save(cover_a(), "cover-v2-a.png")
    save(cover_b(), "cover-v2-b.png")
    save(cover_c(), "cover-v2-c.png")
    save(cover_d(), "cover-v2-d.png")
    save(cover_e(), "cover-v2-e.png")


if __name__ == "__main__":
    main()
