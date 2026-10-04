#!/usr/bin/env python3
"""Restore the locked first set: Iron Rail, Fence at last light, Four ticks, Night charcoal."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import random

OUT = Path("/workspace/biblical-manhood/book/art/covers")
SRC = Path("/workspace/biblical-manhood/book/art/covers")
W, H = 1600, 2560

BONE = (244, 239, 228)
INK = (44, 41, 36)
INK_SOFT = (90, 84, 76)
RUST = (122, 74, 50)
RULE = (196, 184, 168)
NIGHT = (28, 26, 23)
NIGHT_LIFT = (38, 35, 31)

FONT_TITLE = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_ITAL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"
FONT_ROMAN = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"

TEX_B = SRC / "cover-b-texture.png"
TEX_C = SRC / "cover-c-texture.png"

TITLE = "STEADFAST"
TITLE2 = "MEN"
SUB = "The way of Godly Men"
BY = "Wes Hart"


def font(path, px):
    return ImageFont.truetype(path, px)


def tracked_width(draw, text, fnt, tracking):
    if not text:
        return 0
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
    noise = noise.filter(ImageFilter.GaussianBlur(0.6))
    noise_rgb = Image.merge("RGB", (noise, noise, noise))
    return Image.blend(img, noise_rgb, 0.045)


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


def rail(draw, x, y0, y1, ticks=4, rail_w=7, tick_w=42, tick_h=7):
    draw.rectangle([x, y0, x + rail_w, y1], fill=RUST)
    inner = y1 - y0
    for i in range(ticks):
        cy = y0 + int((i + 0.5) * inner / ticks)
        draw.rectangle(
            [x, cy - tick_h // 2, x + tick_w, cy + tick_h // 2 + 1],
            fill=RUST,
        )


def stack_title(draw, f_title, f_sub, f_by, fill_title, fill_sub, fill_by, left, top, tracking_title, tracking_sub=1.2):
    y = top
    draw_tracked(draw, TITLE, (left, y), f_title, fill_title, tracking_title)
    y += int(text_h(f_title) * 0.96)
    draw_tracked(draw, TITLE2, (left, y), f_title, fill_title, tracking_title + 4)
    y += int(text_h(f_title) * 1.02)
    tw = tracked_width(draw, TITLE, f_title, tracking_title)
    draw.rectangle([left, y, left + min(tw, 420), y + 3], fill=RUST)
    y += 28
    draw.text((left, y), SUB, font=f_sub, fill=fill_sub)
    return y + text_h(f_sub)


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", dpi=(266, 266), optimize=True)
    print(path, img.size)
    return path


def cover_a():
    img = Image.new("RGB", (W, H), BONE)
    img = grain(img, amount=7, seed=3)
    d = ImageDraw.Draw(img)
    rail(d, 78, 180, H - 180, rail_w=8, tick_w=48, tick_h=8)
    f_title = font(FONT_TITLE, 118)
    f_sub = font(FONT_ITAL, 38)
    f_by = font(FONT_ROMAN, 30)
    left = 210
    top = 820
    stack_title(d, f_title, f_sub, f_by, INK, INK_SOFT, INK_SOFT, left, top, tracking_title=6)
    d.text((left, H - 220), BY, font=f_by, fill=INK_SOFT)
    return img


def cover_b():
    land = Image.open(TEX_B).convert("RGB")
    canvas = fit_cover(land, crop="left")
    canvas = grain(canvas, amount=6, seed=8)
    scrim = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(scrim)
    for i in range(780):
        sd.rectangle([0, i, W, i + 1], fill=int(95 * (1 - i / 780) ** 1.15))
    dark = Image.new("RGB", (W, H), (32, 28, 24))
    canvas = Image.composite(dark, canvas, scrim)
    d = ImageDraw.Draw(canvas)
    f_title = font(FONT_TITLE, 108)
    f_sub = font(FONT_ITAL, 36)
    f_by = font(FONT_ROMAN, 28)
    left = 120
    top = 160
    stack_title(d, f_title, f_sub, f_by, BONE, (226, 218, 206), (226, 218, 206), left, top, tracking_title=5)
    d.text((left, H - 160), BY, font=f_by, fill=BONE)
    return canvas


def cover_c():
    src = Image.open(TEX_C).convert("RGB")
    img = fit_cover(src, crop="center")
    img = grain(img, amount=5, seed=14)
    overlay = Image.new("RGB", (W, H), (236, 228, 212))
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    for i in range(420):
        md.rectangle([0, i, W, i + 1], fill=int(55 * (1 - i / 420)))
    for i in range(280):
        y = H - 280 + i
        md.rectangle([0, y, W, y + 1], fill=int(40 * (i / 280)))
    img = Image.composite(overlay, img, mask)
    d = ImageDraw.Draw(img)
    f_title = font(FONT_TITLE, 96)
    f_sub = font(FONT_ITAL, 34)
    f_by = font(FONT_ROMAN, 28)
    left = 130
    top = 120
    stack_title(d, f_title, f_sub, f_by, INK, INK_SOFT, INK_SOFT, left, top, tracking_title=5)
    d.text((left, H - 190), BY, font=f_by, fill=INK)
    return img


def cover_d():
    img = Image.new("RGB", (W, H), NIGHT)
    overlay = Image.new("RGB", (W, H), NIGHT_LIFT)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([-200, 400, W + 200, H - 200], fill=70)
    mask = mask.filter(ImageFilter.GaussianBlur(180))
    img = Image.composite(overlay, img, mask)
    img = grain(img, amount=10, seed=21)
    d = ImageDraw.Draw(img)
    rail(d, 90, 240, 720, rail_w=6, tick_w=36, tick_h=6)
    f_title = font(FONT_TITLE, 118)
    f_sub = font(FONT_ITAL, 38)
    f_by = font(FONT_ROMAN, 30)
    left = 200
    top = 900
    stack_title(d, f_title, f_sub, f_by, BONE, RULE, RULE, left, top, tracking_title=6)
    d.text((left, H - 220), BY, font=f_by, fill=RULE)
    return img


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    save(cover_a(), "cover-a.png")
    save(cover_b(), "cover-b.png")
    save(cover_c(), "cover-c.png")
    save(cover_d(), "cover-d.png")


if __name__ == "__main__":
    main()
