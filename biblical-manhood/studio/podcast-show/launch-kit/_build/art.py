"""Walk Steadfast show art, 3000x3000. Local PIL only. Photo = banner-09 ESRGAN master."""
import sys, json
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
import bannerlib as BL
from bannerlib import font, tracked, _track_width, ACCENT, BG, TEXT, MUTED
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import numpy as np

OUT = '/workspace/biblical-manhood/studio/podcast-show/launch-kit/art/'
SRC = Image.open('/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/_build/walk-esrgan-x4.png').convert('RGB')
S = 3000

def lock(im, cx, top, width, walk_ratio=0.34, sub=None, sub_ratio=0.24, fg=TEXT, rule=ACCENT, sub_fill=(222, 222, 230), rule_frac=0.86):
    d = ImageDraw.Draw(im)
    size = 200; f = font(size, 420); tr = size * 0.10
    size = int(size * width / _track_width('STEADFAST', f, tr)); f = font(size, 420); tr = size * 0.10
    capH = f.getbbox('H')[3] - f.getbbox('H')[1]
    fw = font(int(size * walk_ratio), 520); trw = size * walk_ratio * 0.9
    capw = fw.getbbox('H')[3] - fw.getbbox('H')[1]
    tracked(d, (cx, top), 'WALK', fw, fg, trw, 'c')
    y = top + capw + capH * 0.42
    b = tracked(d, (cx, y), 'STEADFAST', f, fg, tr, 'c', tri_a=True)
    y = b[3] + capH * 0.34
    rw = width * rule_frac; th = max(6, size // 36)
    d.rectangle((cx - rw / 2, y, cx + rw / 2, y + th), fill=rule)
    y += th + capH * 0.30
    if sub:
        fs = font(int(size * sub_ratio), 400)
        b = tracked(d, (cx, y), sub, fs, sub_fill, fs.size * 0.04, 'c'); y = b[3]
    return y

def grain(im, amt=10, seed=7):
    rng = np.random.default_rng(seed)
    g = rng.normal(0, 1, (S // 2, S // 2)).astype(np.float32)
    g = np.asarray(Image.fromarray(((g * amt) + 128).clip(0, 255).astype(np.uint8)).resize((S, S), Image.BILINEAR), np.float32) - 128
    a = np.asarray(im, np.float32) + g[..., None] * 0.5
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))

def vfade(im, y0, y1, a0, a1, color=BG):
    """vertical fade toward color: alpha a0 at y0 -> a1 at y1 (clamped outside)."""
    ys = np.arange(S, dtype=np.float32)
    t = np.clip((ys - y0) / (y1 - y0), 0, 1); t = t * t * (3 - 2 * t)
    a = (a0 + (a1 - a0) * t)[:, None, None]
    arr = np.asarray(im, np.float32); c = np.array(color, np.float32)
    return Image.fromarray((arr * (1 - a) + c * a).clip(0, 255).astype(np.uint8))

def photo_square(x0, size, scale_to):
    # crop square region from 4672x3136 source; size<=3136
    c = SRC.crop((x0, 3136 - size, x0 + size, 3136)) if size <= 3136 else None
    return c.resize((scale_to, scale_to), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 40, 2))

# ---------- A: full-bleed photo, wordmark in the sky
def variant_a():
    im = photo_square(260, 3136, S)
    im = ImageEnhance.Brightness(im).enhance(1.05)
    im = vfade(im, 0, 1500, 0.80, 0.0)
    im = vfade(im, 2300, 3000, 0.0, 0.70)
    lock(im, S // 2, 330, 2440, walk_ratio=0.40, sub=None)
    return grain(im)

# ---------- B: typographic, near-black with the road as a thin periwinkle line
def variant_b():
    im = Image.new('RGB', (S, S), BG)
    # faint dusk glow at the horizon
    ys, xs = np.mgrid[0:S, 0:S].astype(np.float32)
    glow = np.exp(-(((ys - 2050) / 520) ** 2)) * np.exp(-(((xs - S / 2) / 1500) ** 2))
    arr = np.asarray(im, np.float32) + glow[..., None] * np.array([28, 34, 70], np.float32)
    im = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    # road: soft tapered path from bottom center to the horizon, fading out as it recedes
    hz = 2050
    m = Image.new('L', (S, S), 0); md = ImageDraw.Draw(m)
    md.polygon([(S / 2 - 420, S), (S / 2 + 420, S), (S / 2 + 10, hz), (S / 2 - 10, hz)], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(6))
    fade = np.clip((np.arange(S, dtype=np.float32) - hz) / (S - hz), 0, 1) ** 0.7
    ma = np.asarray(m, np.float32) / 255 * fade[:, None] * 0.55
    arr = np.asarray(im, np.float32); c = np.array([70, 78, 130], np.float32)
    im = Image.fromarray((arr * (1 - ma[..., None]) + c * ma[..., None]).clip(0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    hl = np.exp(-(((np.arange(S) - S / 2) / 900) ** 2))
    for x in range(150, S - 150, 6):
        a = hl[x]; col = tuple(int(BG[i] + (ACCENT[i] - BG[i]) * a * 0.6) for i in range(3))
        d.line([(x, hz), (x + 6, hz)], fill=col, width=4)
    y = lock(im, S // 2, 760, 2500, walk_ratio=0.40, sub='A podcast for men who stay', sub_ratio=0.19, sub_fill=MUTED)
    return grain(im, 8)

# ---------- C: photo bottom, wordmark on dark top panel (closest to the YouTube banner)
def variant_c():
    im = Image.new('RGB', (S, S), BG)
    ph = photo_square(560, 2700, S)   # tighter on man, boy and oak
    ph = ImageEnhance.Brightness(ph).enhance(1.08)
    im.paste(ph, (0, 0))
    im = vfade(im, 0, 1350, 0.97, 0.0)
    im = vfade(im, 2500, 3000, 0.0, 0.55)
    y = lock(im, S // 2, 300, 2300, walk_ratio=0.40, sub='A podcast for men who stay', sub_ratio=0.17)
    return grain(im)

res = {}
SEL = sys.argv[1:] or ['A','B','C']
for k, fn in dict(A=variant_a, B=variant_b, C=variant_c).items():
    if k not in SEL: continue
    BL.TEXT_BOXES.clear()
    im = fn().convert('RGB')
    boxes = [tuple(round(v) for v in b) for b in BL.TEXT_BOXES]
    im.save(OUT + f'walk-steadfast-art-{k}-3000.png', optimize=True)
    im.save(OUT + f'walk-steadfast-art-{k}-3000.jpg', quality=92, subsampling=0, dpi=(72, 72))
    res[k] = dict(text_boxes=boxes)
import os
old = json.load(open(OUT + '../_build/art.json')) if os.path.exists(OUT + '../_build/art.json') else {}
old.update(res); json.dump(old, open(OUT + '../_build/art.json', 'w'), indent=1)
print(res)
