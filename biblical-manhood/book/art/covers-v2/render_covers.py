#!/usr/bin/env python3
"""Five named Steadfast Men cover comps. Front only. 1600x2560.
A Mesquite Type, B Limestone Field, C Cedar Brand, D Night Lamp, E Work Ledger.
No portrait. No icon. No distress. No cliff/sword/lion/camo.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import random
import math

OUT = Path("/workspace/biblical-manhood/book/art/covers")
W, H = 1600, 2560

BONE = (244, 239, 228)
INK = (36, 30, 24)
MESQUITE = (74, 42, 26)
NIGHT = (10, 9, 8)
NAVY = (24, 36, 62)
LEDGER_CREAM = (246, 240, 224)
LEDGER_RED = (158, 48, 44)
GRAY_BORDER = (150, 148, 144)

FONT_TITLE = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_CROMAN = "/usr/share/fonts/opentype/urw-base35/C059-Roman.otf"
FONT_ITAL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"
FONT_ROMAN = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"

TEX_STONE = OUT / "limestone-texture.png"
TEX_CEDAR = OUT / "cedar-grain.png"

TITLE = "STEADFAST"
TITLE2 = "MEN"
SUB_SC = "THE WAY OF GODLY MEN"
SUB = "The way of Godly Men"
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


def hairline_border(img, px=4, color=GRAY_BORDER):
    d = ImageDraw.Draw(img)
    for i in range(px):
        d.rectangle([i, i, W - 1 - i, H - 1 - i], outline=color)
    return img


def stack(draw, left, top, f_title, f_sub, fill_title, fill_sub, fill_rule, track, rule_h=3):
    y = top
    draw_tracked(draw, TITLE, (left, y), f_title, fill_title, track)
    y += int(text_h(f_title) * 0.96)
    draw_tracked(draw, TITLE2, (left, y), f_title, fill_title, track + 6)
    y += int(text_h(f_title) * 1.04)
    tw = tracked_width(draw, TITLE, f_title, track)
    draw.rectangle([left, y, left + tw, y + rule_h], fill=fill_rule)
    y += 34
    draw_tracked(draw, SUB_SC, (left, y), f_sub, fill_sub, 3.2)
    return y + text_h(f_sub)


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", dpi=(266, 266), optimize=True)
    thumb = img.resize((200, int(200 * H / W)), Image.Resampling.LANCZOS)
    tpath = OUT / name.replace(".png", "-thumb.png")
    thumb.save(tpath, "PNG", optimize=True)
    print(path, img.size)
    return path


def cover_a():
    """Mesquite Type. Default. Dark brown field, bone serif, no icon, no distress."""
    img = Image.new("RGB", (W, H), MESQUITE)
    img = grain(img, amount=9, seed=2)
    d = ImageDraw.Draw(img)
    f_title = font(FONT_TITLE, 128)
    f_sub = font(FONT_CROMAN, 26)
    f_by = font(FONT_CROMAN, 32)
    left = 140
    top = 780
    stack(d, left, top, f_title, f_sub, BONE, BONE, BONE, track=8, rule_h=3)
    d.text((left, H - 210), BY, font=f_by, fill=BONE)
    return img


def cover_b():
    """Limestone Field. Pale stone, carved dark type. Kindle gray hairline."""
    src = Image.open(TEX_STONE).convert("RGB")
    img = fit_cover(src, crop="center")
    img = grain(img, amount=4, seed=5)
    # slight light wash so type carves
    wash = Image.new("RGB", (W, H), (238, 230, 214))
    img = Image.blend(img, wash, 0.12)
    d = ImageDraw.Draw(img)
    f_title = font(FONT_TITLE, 118)
    f_sub = font(FONT_CROMAN, 24)
    f_by = font(FONT_CROMAN, 30)
    left = 130
    top = 760
    stack(d, left, top, f_title, f_sub, INK, INK, INK, track=5, rule_h=3)
    d.text((left, H - 210), BY, font=f_by, fill=INK)
    return hairline_border(img)


def cover_c():
    """Cedar Brand. Close-crop grain, letterpress stamp, no forest, no man."""
    src = Image.open(TEX_CEDAR).convert("RGB")
    img = fit_cover(src, crop="center")
    img = grain(img, amount=3, seed=7)
    d = ImageDraw.Draw(img)
    stamp = (28, 18, 12)
    f_title = font(FONT_TITLE, 112)
    f_sub = font(FONT_CROMAN, 24)
    f_by = font(FONT_CROMAN, 30)
    left = 120
    top = 720
    # slight impression: 1px offset darker, then stamp
    stack(d, left + 2, top + 2, f_title, f_sub, (12, 8, 6), (12, 8, 6), (12, 8, 6), track=4, rule_h=3)
    stack(d, left, top, f_title, f_sub, stamp, stamp, stamp, track=4, rule_h=3)
    d.text((left + 2, H - 208), BY, font=f_by, fill=(12, 8, 6))
    d.text((left, H - 210), BY, font=f_by, fill=stamp)
    return img


def cover_d():
    """Night Lamp. Near-black, one warm light pool, type in the light. Not a photo of a lamp."""
    img = Image.new("RGB", (W, H), NIGHT)
    px = img.load()
    cx, cy = int(W * 0.42), int(H * 0.30)
    rx, ry = 720, 640
    warm = (236, 188, 118)
    for y in range(H):
        for x in range(0, W, 1):
            nx = (x - cx) / rx
            ny = (y - cy) / ry
            r2 = nx * nx + ny * ny
            t = math.exp(-r2 * 1.55)
            if t < 0.01:
                continue
            r = int(NIGHT[0] + (warm[0] - NIGHT[0]) * t)
            g = int(NIGHT[1] + (warm[1] - NIGHT[1]) * t)
            b = int(NIGHT[2] + (warm[2] - NIGHT[2]) * t)
            px[x, y] = (r, g, b)
    img = grain(img, amount=7, seed=19)
    d = ImageDraw.Draw(img)
    f_title = font(FONT_TITLE, 118)
    f_sub = font(FONT_CROMAN, 24)
    f_by = font(FONT_CROMAN, 30)
    left = 150
    top = 220
    # title in the light
    y = top
    track = 6
    draw_tracked(d, TITLE, (left, y), f_title, BONE, track)
    y += int(text_h(f_title) * 0.96)
    draw_tracked(d, TITLE2, (left, y), f_title, BONE, track + 6)
    y += int(text_h(f_title) * 1.04)
    tw = tracked_width(d, TITLE, f_title, track)
    d.rectangle([left, y, left + tw, y + 3], fill=BONE)
    # subtitle and author wait in the dark below
    dim = (168, 158, 142)
    f_sub = font(FONT_CROMAN, 24)
    d.text((left, int(H * 0.62)), SUB, font=font(FONT_ITAL, 34), fill=dim)
    d.text((left, H - 210), BY, font=f_by, fill=dim)
    return img


def cover_e():
    """Work Ledger. Cream invoice, navy type, one thin red rule. Not torn newspaper."""
    img = Image.new("RGB", (W, H), LEDGER_CREAM)
    img = grain(img, amount=6, seed=4)
    d = ImageDraw.Draw(img)
    f_title = font(FONT_TITLE, 118)
    f_sub = font(FONT_CROMAN, 24)
    f_by = font(FONT_CROMAN, 28)
    left = 140
    top = 820
    y = top
    track = 6
    draw_tracked(d, TITLE, (left, y), f_title, NAVY, track)
    y += int(text_h(f_title) * 0.96)
    draw_tracked(d, TITLE2, (left, y), f_title, NAVY, track + 6)
    y += int(text_h(f_title) * 1.02)
    tw = tracked_width(d, TITLE, f_title, track)
    d.rectangle([left, y, left + tw, y + 4], fill=LEDGER_RED)
    y += 36
    draw_tracked(d, SUB_SC, (left, y), f_sub, NAVY, 3.4)
    # prepared-by line
    prep = font(FONT_CROMAN, 16)
    d.text((left, H - 250), "WES HART", font=f_by, fill=NAVY)
    d.text((left, H - 208), "BY", font=prep, fill=NAVY)
    return hairline_border(img)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    save(cover_a(), "cover-a.png")
    save(cover_b(), "cover-b.png")
    save(cover_c(), "cover-c.png")
    save(cover_d(), "cover-d.png")
    save(cover_e(), "cover-e.png")


if __name__ == "__main__":
    main()
