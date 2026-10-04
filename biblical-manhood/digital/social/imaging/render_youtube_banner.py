#!/usr/bin/env python3
"""YouTube banner 2560×1440 — Merc remaster 2026-09-15 (Holt bar).

Left-weighted Cloth Store navy jacket ~55–65% frame width.
Title stack STEADFAST → Wes Hart typeset inside center safe ~1546×423.
Quiet wood field. Bone page edge. No site lockup.

Photoreal full-cover at 55–65% cannot fit the whole stack in 423px height;
this editorial soft-plate is the geometry-honest path.
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont

COVER = Path("/workspace/biblical-manhood/book/art/press/cloth-store/cover-front-walksteadfast-locked-2026-09-14.png")
OUT = Path("/workspace/biblical-manhood/digital/social/imaging/youtube-banner.png")
W, H = 2560, 1440
SAFE = (507, 509, 2053, 932)
NAVY = (11, 31, 56)
GOLD = (227, 197, 114)
BONE = (230, 221, 204)
SANS = "/usr/share/fonts/truetype/sand-box/google/Montserrat/Montserrat-VariableFont_wght.ttf"
SERIF_I = "/usr/share/fonts/truetype/sand-box/google/Playfair Display/PlayfairDisplay-Italic-VariableFont_wght.ttf"
SERIF = "/usr/share/fonts/truetype/sand-box/google/Playfair Display/PlayfairDisplay-VariableFont_wght.ttf"


def make_font(path, size, weight=700):
    f = ImageFont.truetype(path, size)
    try:
        f.set_variation_by_axes([float(weight)])
    except Exception:
        pass
    return f


def render_text(text, font, fill=GOLD):
    bbox = font.getbbox(text)
    im = Image.new("RGBA", (bbox[2] - bbox[0] + 12, bbox[3] - bbox[1] + 12), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((-bbox[0] + 6, -bbox[1] + 6), text, font=font, fill=fill + (255,))
    return im


def fit_width(text, path, target_w, start, weight=700):
    size = start
    while size >= 10:
        im = render_text(text, make_font(path, size, weight))
        if im.size[0] <= target_w:
            return im
        size -= 2
    return render_text(text, make_font(path, 10, weight))


def main():
    cover = Image.open(COVER).convert("RGB")
    cw, ch = cover.size
    book = cover.crop((184, 266, 983, 1419))
    jacket_w, jacket_h = int(0.62 * W), int(0.88 * H)
    patch = book.crop((20, 400, 120, 700))
    lum = np.array(patch).mean(axis=2)
    tex = Image.fromarray(np.stack([lum, lum, lum], 2).astype(np.uint8)).resize((jacket_w, jacket_h), Image.Resampling.LANCZOS)
    ta = np.array(tex).astype(np.float32) / 255.0
    ta = (ta - ta.mean()) / (ta.std() + 1e-6)
    base = np.zeros((jacket_h, jacket_w, 3), dtype=np.float32)
    base[:] = NAVY
    base = (base + ta * 9.0) * (0.94 + 0.10 * (1 - np.linspace(0, 1, jacket_h)[:, None, None]))
    jacket = Image.fromarray(base.clip(0, 255).astype(np.uint8))
    page = Image.fromarray(
        (np.array(Image.new("RGB", (34, jacket_h), BONE)).astype(np.float32) * np.linspace(0.85, 1.0, 34)[None, :, None]).clip(0, 255).astype(np.uint8)
    )
    wood = cover.crop((0, int(ch * 0.88), int(cw * 0.25), ch)).resize((W, H), Image.Resampling.LANCZOS)
    wood = ImageEnhance.Brightness(wood).enhance(0.55).filter(ImageFilter.GaussianBlur(8))
    fa = np.array(wood).astype(np.float32)
    fa = fa * 0.15 + np.array([34.0, 24.0, 16.0]) * 0.85
    fa = (fa + np.random.default_rng(5).normal(0, 2.2, fa.shape)).clip(0, 255)
    field = Image.fromarray(fa.astype(np.uint8))
    x_j, y_j = 90, (H - jacket_h) // 2
    stack_pad = 52
    y0, y1 = SAFE[1] + stack_pad, SAFE[3] - stack_pad
    budget = y1 - y0
    jack_l, jack_r = max(x_j, SAFE[0]), min(x_j + jacket_w, SAFE[2])
    cx = (jack_l + jack_r) // 2
    max_w = int((jack_r - jack_l) * 0.86)
    parts = [
        fit_width("STEΛDFΛST", SANS, max_w, 108, 750),
        Image.new("RGBA", (int(max_w * 0.32), 3), GOLD + (255,)),
        fit_width("M   E   N", SANS, int(max_w * 0.48), 46, 550),
        fit_width("The way of Godly Men", SERIF_I, int(max_w * 0.58), 30, 500),
    ]
    plumb = Image.new("RGBA", (10, 30), (0, 0, 0, 0))
    d = ImageDraw.Draw(plumb)
    d.rectangle([4, 0, 5, 22], fill=GOLD + (255,))
    d.ellipse([2, 22, 7, 27], fill=GOLD + (255,))
    parts += [plumb, fit_width("Wes Hart", SERIF, int(max_w * 0.36), 28, 500)]
    gaps = [14, 12, 16, 12, 18]
    total = sum(p.size[1] for p in parts) + sum(gaps)
    if total > budget:
        s = (budget - sum(gaps)) / sum(p.size[1] for p in parts)
        parts = [p.resize((max(2, int(p.size[0] * s)), max(2, int(p.size[1] * s))), Image.Resampling.LANCZOS) for p in parts]
        total = sum(p.size[1] for p in parts) + sum(gaps)
    canvas = field.convert("RGBA")
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rectangle([x_j + 20, y_j + 30, x_j + jacket_w + 48, y_j + jacket_h + 44], fill=(0, 0, 0, 150))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(44)))
    jfull = Image.new("RGBA", (jacket_w + 34, jacket_h))
    jfull.paste(jacket.convert("RGBA"), (0, 0))
    jfull.paste(page.convert("RGBA"), (jacket_w, 0))
    canvas.paste(jfull, (x_j, y_j), jfull)
    y = y0 + (budget - total) // 2
    for i, p in enumerate(parts):
        canvas.alpha_composite(p, (cx - p.size[0] // 2, y))
        y += p.size[1] + (gaps[i] if i < len(gaps) else 0)
    canvas.convert("RGB").save(OUT, "PNG", optimize=True)
    print(OUT, jacket_w, jacket_h)


if __name__ == "__main__":
    main()
