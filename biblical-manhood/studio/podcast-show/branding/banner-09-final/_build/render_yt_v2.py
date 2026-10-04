"""YouTube v2: photo scaled so both figures fit the 2560x423 desktop band; sky/field extended by edge-median fill."""
import sys, math, json
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
import bannerlib as BL
from bannerlib import lockup, small, ACCENT, BG
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import numpy as np

OUT = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/youtube-v2/'
SRC = Image.open('/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/_build/walk-esrgan-x4.png').convert('RGB')
W, H = 2560, 1440
BAND = (0, 508, 2560, 931); SAFE = (507, 508, 2053, 931)
P = dict(head=548, feet=902, fig_cx=730, cx=1710, cy=720, width=600, feather=380, rdark=0.82)
for a in sys.argv[1:]:
    k, v = a.split('='); P[k] = float(v)

# figures in original 1168 coords: x 342-508, y 339-645
s = (P['feet'] - P['head']) / (645 - 339)
pw, ph = round(1168 * s), round(784 * s)
X0 = round(P['fig_cx'] - 425 * s); Y0 = round(P['head'] - 339 * s)
photo = SRC.resize((pw, ph), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.0, 35, 2))
photo = ImageEnhance.Color(ImageEnhance.Contrast(photo).enhance(1.05)).enhance(0.9)
pa = np.asarray(photo, np.float32)

def smooth1d(v, r):
    if r < 1: return v
    k = np.exp(-0.5 * (np.arange(-3 * r, 3 * r + 1) / r) ** 2); k /= k.sum()
    pad = np.pad(v, ((3 * r, 3 * r), (0, 0)), mode='edge')
    return np.stack([np.convolve(pad[:, c], k, mode='valid') for c in range(v.shape[1])], 1)

# ---- backdrop: mirror-extend the photo to the full canvas, then blur hard (soft depth-of-field fill, no streaks)
padL, padT = max(0, X0), max(0, Y0)
padR, padB = max(0, W - (X0 + pw)), max(0, H - (Y0 + ph))
ext = np.pad(pa, ((padT, padB), (padL, padR), (0, 0)), mode='symmetric')[:H, :W]
small_ = Image.fromarray(ext.clip(0, 255).astype(np.uint8)).resize((W // 8, H // 8), Image.BILINEAR)
small_ = small_.filter(ImageFilter.GaussianBlur(P.get('blur', 9)))
canvas = np.asarray(small_.resize((W, H), Image.BICUBIC), np.float32).copy()
xs = np.arange(W)[None, :, None]
r0 = X0 + pw * P.get('r0', 0.62); r1 = P.get('r1', 2350)
dR = np.clip((xs - r0) / (r1 - r0), 0, 1); dR = dR * dR * (3 - 2 * dR)
dL = np.clip((X0 + pw * 0.05 - xs) / max(1, X0 + pw * 0.05), 0, 1)
canvas *= (1 - P['rdark'] * dR) * (1 - 0.75 * dL ** 0.8)
# ---- paste photo with feathered left/right edges and top/bottom edges
mask = np.ones((ph, pw), np.float32)
f = int(P['feather']);
ramp = np.clip(np.arange(pw) / f, 0, 1); ramp = np.minimum(ramp, np.clip((pw - 1 - np.arange(pw)) / f, 0, 1))
mask *= (0.5 - 0.5 * np.cos(np.pi * ramp))[None, :]
fv = int(f * 0.6); rv = np.clip(np.arange(ph) / fv, 0, 1); rv = np.minimum(rv, np.clip((ph - 1 - np.arange(ph)) / fv, 0, 1))
mask *= (0.5 - 0.5 * np.cos(np.pi * rv))[:, None]
# keep the left edge mostly hard where photo already sits near canvas edge
x0c, y0c = max(0, X0), max(0, Y0); x1c, y1c = min(W, X0 + pw), min(H, Y0 + ph)
m = mask[y0c - Y0:y1c - Y0, x0c - X0:x1c - X0, None]
canvas[y0c:y1c, x0c:x1c] = pa[y0c - Y0:y1c - Y0, x0c - X0:x1c - X0] * m + canvas[y0c:y1c, x0c:x1c] * (1 - m)
# ---- top and bottom: fade to deep dusk navy / near black (letterbox feel)
ys = np.arange(H)[:, None, None]
top_t = np.clip((P['head'] - 330 - ys) / 300, 0, 1)       # above the photo's upper sky
bot_t = np.clip((ys - (P['feet'] + 120)) / 380, 0, 1)
NIGHT = np.array([12, 16, 30], np.float32); FLOOR = np.array([6, 7, 10], np.float32)
canvas = canvas * (1 - 0.85 * top_t ** 1.3) + NIGHT * 0.85 * top_t ** 1.3
canvas = canvas * (1 - 0.9 * bot_t) + FLOOR * 0.9 * bot_t
# ---- film grain so the fill matches photo texture, then gentle global vignette
rng = np.random.default_rng(7)
g = rng.normal(0, 1, (H // 2, W // 2)).astype(np.float32)
g = np.asarray(Image.fromarray(((g * 18) + 128).clip(0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR), np.float32) - 128
canvas += g[:, :, None] * 0.10
im = Image.fromarray(canvas.clip(0, 255).astype(np.uint8))
# vignette weighted to edges (TV frame), lighter in the band
vm = Image.new('L', (W // 8, H // 8)); px = vm.load()
for y in range(vm.height):
    for x in range(vm.width):
        dx = (x / vm.width - 0.5) * 2; dy = (y / vm.height - 0.5) * 2
        px[x, y] = int(255 * 0.55 * min(1, math.sqrt(dx * dx * 0.55 + dy * dy * 1.1) / 1.2) ** 2.4)
vm = vm.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(30))
im = Image.composite(Image.new('RGB', (W, H), BG), im, vm)
# ---- type
BL.TEXT_BOXES.clear()
scratch = Image.new('RGB', (4000, 2000))
hgt = lockup(scratch, 2000, 0, P['width'], sub='A podcast for men who stay') + 40 + 26
BL.TEXT_BOXES.clear()
top = P['cy'] - hgt / 2
y = lockup(im, P['cx'], top, P['width'], sub='A podcast for men who stay', sub_fill=(222, 222, 230))
small(im, (P['cx'], y + 40), 'TUESDAY AND FRIDAY', 26, ACCENT, 'c', 0.3, 550)
tb = [min(b[0] for b in BL.TEXT_BOXES), min(b[1] for b in BL.TEXT_BOXES), max(b[2] for b in BL.TEXT_BOXES), max(b[3] for b in BL.TEXT_BOXES)]
BL.TEXT_BOXES.clear()
fb = [X0 + 342 * s, Y0 + 339 * s, X0 + 508 * s, Y0 + 645 * s]
inside = lambda a, b: a[0] >= b[0] and a[1] >= b[1] and a[2] <= b[2] and a[3] <= b[3]
rep = dict(scale_vs_orig=round(s, 3), photo_box=[X0, Y0, X0 + pw, Y0 + ph], figures_box=[round(v) for v in fb], text_box=[round(v) for v in tb],
           figures_in_desktop_band=inside(fb, BAND), figures_in_safe=inside(fb, SAFE), text_in_safe=inside(tb, SAFE),
           gap_figures_to_text_px=round(tb[0] - fb[2]), params=P)
print(json.dumps(rep, indent=1))
im.save(OUT + 'banner-yt-v2.png', optimize=True)
json.dump(rep, open(OUT + 'checks.json', 'w'), indent=1)
# previews
def lab(img, text):
    d = ImageDraw.Draw(img); d.text((20, 14), text, font=BL.font(28, 500), fill=(255, 210, 0)); return img
im.crop(BAND).save(OUT + 'preview-desktop.png')
im.crop(SAFE).save(OUT + 'preview-mobile.png')
tv = im.copy(); d = ImageDraw.Draw(tv)
d.rectangle(BAND, outline=(255, 200, 0), width=4); d.rectangle(SAFE, outline=(60, 220, 120), width=4)
tv.save(OUT + 'preview-tv.png')
