#!/usr/bin/env python3
"""Cornerstone covers. Writes ONLY to covers-v3/. Do not touch covers/ or covers-v2/."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageEnhance, ImageFilter

OUT = Path("/workspace/biblical-manhood/book/art/covers-v3")
TEX = OUT / "tex"
W, H = 1600, 2560

FONT_TITLE = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_ITAL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"
FONT_ROMAN = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"

TITLE = "STEADFAST"
TITLE2 = "MEN"
SUB = "The way of Godly Men"
BY = "Wes Hart"

BONE = (244, 239, 228)
INK = (62, 52, 42)


def font(path, px):
    return ImageFont.truetype(path, px)


def text_h(fnt):
    a, d = fnt.getmetrics()
    return a + d


def draw_tracked(draw, text, xy, fnt, fill, tracking):
    x, y = xy
    for i, ch in enumerate(text):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


def glyph_mask(size, lines):
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    for text, xy, fnt, tracking in lines:
        draw_tracked(d, text, xy, fnt, 255, tracking)
    return mask


def fill_cover(src, box=None):
    src = src.convert("RGB")
    if box:
        w, h = src.size
        src = src.crop(
            (
                int(box[0] * w),
                int(box[1] * h),
                int(box[2] * w),
                int(box[3] * h),
            )
        )
    scale = max(W / src.width, H / src.height)
    nw, nh = max(W, int(round(src.width * scale))), max(H, int(round(src.height * scale)))
    src = src.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - W) // 2
    top = (nh - H) // 2
    return src.crop((left, top, left + W, top + H))


def vcut(base, mask, light=(3, 3), mode="carve", depth=5):
    """True V: floor inset, highlight/shadow only on the walls."""
    sx, sy = light
    out = base.copy()
    floor = mask.filter(ImageFilter.MinFilter(depth))

    if mode == "bone":
        floor_col = Image.new("RGB", base.size, BONE)
        wall_dark = Image.new("RGB", base.size, (40, 32, 24))
    else:
        floor_col = ImageEnhance.Brightness(base).enhance(0.55)
        floor_col = ImageEnhance.Color(floor_col).enhance(0.75)
        wall_dark = Image.new("RGB", base.size, (42, 32, 24))

    walls = ImageChops.subtract(mask, floor)
    out = Image.composite(wall_dark, out, walls)
    out = Image.composite(floor_col, out, floor)

    shadow_src = Image.new("L", base.size, 0)
    shadow_src.paste(mask, (sx, sy))
    rim_sh = ImageChops.multiply(ImageChops.subtract(shadow_src, mask), walls)
    rim_sh = rim_sh.filter(ImageFilter.GaussianBlur(0.4))
    out = Image.composite(Image.new("RGB", base.size, (28, 22, 16)), out, rim_sh)

    hi_src = Image.new("L", base.size, 0)
    hi_src.paste(mask, (-sx, -sy))
    rim_hi = ImageChops.multiply(ImageChops.subtract(hi_src, mask), walls)
    rim_hi = rim_hi.filter(ImageFilter.GaussianBlur(0.35))
    hi = (252, 244, 220) if mode != "bone" else (255, 252, 240)
    out = Image.composite(Image.new("RGB", base.size, hi), out, rim_hi)
    return out


def small_carve(base, mask):
    """Small type: recessed, no highlight blowout."""
    out = base.copy()
    dark = ImageEnhance.Brightness(base).enhance(0.42)
    out = Image.composite(dark, out, mask)
    sh = Image.new("L", base.size, 0)
    sh.paste(mask, (1, 1))
    rim = ImageChops.subtract(sh, mask)
    out = Image.composite(Image.new("RGB", base.size, (36, 28, 20)), out, rim)
    return out


def title_stack(left, y, f_st, f_men, track=1):
    y2 = y + int(text_h(f_st) * 0.88)
    return [
        (TITLE, (left, y), f_st, track),
        (TITLE2, (left, y2), f_men, track + 6),
    ], y2 + int(text_h(f_men) * 0.92)


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", dpi=(266, 266), optimize=True)
    thumb = img.resize((200, int(200 * H / W)), Image.Resampling.LANCZOS)
    thumb.save(OUT / name.replace(".png", "-thumb.png"), "PNG", optimize=True)
    print("WROTE", path, img.size)
    return path


def compose(base, title_lines, small_lines, light, mode="carve", depth=5):
    img = vcut(base, glyph_mask(base.size, title_lines), light=light, mode=mode, depth=depth)
    if small_lines:
        img = small_carve(img, glyph_mask(img.size, small_lines))
    return img


def cover_a():
    base = fill_cover(Image.open(TEX / "face.png"))
    f_st, f_men = font(FONT_TITLE, 168), font(FONT_TITLE, 252)
    titles, y3 = title_stack(64, 140, f_st, f_men)
    small = [
        (SUB, (64, y3 + 36), font(FONT_ITAL, 40), 1),
        (BY, (64, H - 200), font(FONT_ROMAN, 36), 1),
    ]
    return compose(base, titles, small, light=(4, 4), mode="carve", depth=7)


def cover_b():
    base = fill_cover(Image.open(TEX / "corner.png"), box=(0.18, 0.0, 0.82, 1.0))
    f_st, f_men = font(FONT_TITLE, 128), font(FONT_TITLE, 188)
    titles, y3 = title_stack(500, 260, f_st, f_men)
    small = [
        (SUB, (500, y3 + 32), font(FONT_ITAL, 34), 1),
        (BY, (500, H - 220), font(FONT_ROMAN, 32), 1),
    ]
    return compose(base, titles, small, light=(-4, 3), mode="carve", depth=7)


def cover_c():
    base = fill_cover(Image.open(TEX / "evening.png"), box=(0.0, 0.0, 0.70, 1.0))
    base = ImageEnhance.Brightness(base).enhance(0.72)
    base = ImageEnhance.Color(base).enhance(0.85)
    f_st, f_men = font(FONT_TITLE, 156), font(FONT_TITLE, 228)
    titles, y3 = title_stack(90, 180, f_st, f_men)
    small = [
        (SUB, (90, y3 + 36), font(FONT_ITAL, 36), 1),
        (BY, (90, H - 200), font(FONT_ROMAN, 34), 1),
    ]
    return compose(base, titles, small, light=(4, 2), mode="bone", depth=7)


def cover_d():
    base = fill_cover(Image.open(TEX / "wall.png"), box=(0.0, 0.28, 0.58, 1.0))
    f_st, f_men = font(FONT_TITLE, 112), font(FONT_TITLE, 164)
    titles, y3 = title_stack(70, 1500, f_st, f_men)
    small = [
        (SUB, (70, y3 + 24), font(FONT_ITAL, 30), 1),
        (BY, (70, y3 + 78), font(FONT_ROMAN, 28), 1),
    ]
    return compose(base, titles, small, light=(4, 4), mode="carve", depth=5)


def cover_e():
    base = fill_cover(Image.open(TEX / "bleed.png"), box=(0.08, 0.0, 0.92, 1.0))
    f_st, f_men = font(FONT_TITLE, 172), font(FONT_TITLE, 248)
    titles, y3 = title_stack(56, 160, f_st, f_men)
    small = [
        (SUB, (56, y3 + 36), font(FONT_ITAL, 40), 1),
        (BY, (56, H - 200), font(FONT_ROMAN, 36), 1),
    ]
    return compose(base, titles, small, light=(3, 4), mode="carve", depth=7)


def main():
    assert str(OUT).endswith("covers-v3")
    OUT.mkdir(parents=True, exist_ok=True)
    save(cover_a(), "cover-v3-a.png")
    save(cover_b(), "cover-v3-b.png")
    save(cover_c(), "cover-v3-c.png")
    save(cover_d(), "cover-v3-d.png")
    save(cover_e(), "cover-v3-e.png")


if __name__ == "__main__":
    main()
