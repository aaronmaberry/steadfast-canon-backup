"""Banner-09 'The walk' final master + platform cuts. Local only: Real-ESRGAN x4 source, PIL type."""
import sys, math, json
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
import bannerlib as BL
from bannerlib import lockup, small, font, ACCENT, BG, TEXT
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

OUT = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/'
SRC = Image.open(OUT + '_build/walk-esrgan-x4.png').convert('RGB')   # 4672x3136, 4x of the 1168x784 site photo
SW, SH = SRC.size
K = SW / 1168  # source px per original px

def bg(w, h, x0, y0, cw):
    """Crop the source: x0,y0,cw in ORIGINAL 1168-px coordinates, aspect from w/h. Lanczos down, light unsharp."""
    ch = cw * h / w
    box = (x0 * K, y0 * K, (x0 + cw) * K, (y0 + ch) * K)
    assert box[2] <= SW + 1 and box[3] <= SH + 1 and box[0] >= 0 and box[1] >= 0, box
    im = SRC.crop(tuple(round(v) for v in box)).resize((w, h), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=35, threshold=2))

def grade(im):
    im = ImageEnhance.Contrast(im).enhance(1.05)
    return ImageEnhance.Color(im).enhance(0.9)

def vignette(im, strength=0.45, power=2.2):
    w, h = im.size
    m = Image.new('L', (max(2, w // 8), max(2, h // 8)))
    px = m.load()
    for y in range(m.height):
        for x in range(m.width):
            dx = (x / m.width - 0.5) * 2; dy = (y / m.height - 0.5) * 2
            d = min(1, math.sqrt(dx * dx * 0.8 + dy * dy) / 1.25)
            px[x, y] = int(255 * strength * d ** power)
    m = m.resize((w, h), Image.BILINEAR).filter(ImageFilter.GaussianBlur(max(2, w // 128)))
    return Image.composite(Image.new('RGB', (w, h), BG), im, m)

def shade(im, box, alpha, blur):
    m = Image.new('L', im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle(box, radius=int(blur * 0.7), fill=int(255 * alpha))
    m = m.filter(ImageFilter.GaussianBlur(blur))
    return Image.composite(Image.new('RGB', im.size, BG), im, m)

def measure(width, sub, layout='stack', rule_w=None, extra=None):
    """Dry-run the lockup on scratch to get its height."""
    scratch = Image.new('RGB', (4000, 2000))
    BL.TEXT_BOXES.clear()
    y = lockup(scratch, 2000, 0, width, sub=sub, layout=layout, rule_w=rule_w)
    if extra:
        y += extra[1] + extra[0]
    BL.TEXT_BOXES.clear()
    return y

def place(im, cx, cy, width, sub=None, extra=None, layout='stack', rule_w=None, sub_fill=(220, 220, 228)):
    """Draw lockup vertically centered at cy. extra=(gap, size, text) small accent line under it."""
    h = measure(width, sub, layout, rule_w, (extra[0], extra[1]) if extra else None)
    top = cy - h / 2
    BL.TEXT_BOXES.clear()
    y = lockup(im, cx, top, width, sub=sub, layout=layout, rule_w=rule_w, sub_fill=sub_fill)
    if extra:
        small(im, (cx, y + extra[0]), extra[2], extra[1], ACCENT, 'c', 0.3, 550)
    boxes = list(BL.TEXT_BOXES); BL.TEXT_BOXES.clear()
    return (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))

def inside(a, b):
    return a[0] >= b[0] - 1 and a[1] >= b[1] - 1 and a[2] <= b[2] + 1 and a[3] <= b[3] + 1

def overlap(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])

def fig_box(x0, y0, cw, w):
    """Man+boy bounding box (original coords 342-508 x, 339-645 y) mapped into the cut."""
    s = w / cw
    return ((342 - x0) * s, (339 - y0) * s, (508 - x0) * s, (645 - y0) * s)

CUTS = {}

def cut(name, w, h, x0, y0, cw, cx, cy, width, sub, extra, safe, avoid, shade_pad=1.0, vig=0.45):
    im = grade(bg(w, h, x0, y0, cw))
    im = vignette(im, vig)
    # legibility pad behind type: size from a measured dry run
    hh = measure(width, sub, 'stack', None, (extra[0], extra[1]) if extra else None)
    pw, ph = width * 0.62 * shade_pad, hh * 0.75 * shade_pad
    im = shade(im, (cx - pw, cy - ph, cx + pw, cy + ph), 0.30, max(8, int(h * 0.08)))
    tb = place(im, cx, cy, width, sub, extra)
    fb = fig_box(x0, y0, cw, w)
    ok_safe = inside(tb, safe)
    hits = [k for k, z in avoid.items() if overlap(tb, z) or overlap(fb, z)]
    CUTS[name] = dict(size=[w, h], text_box=[round(v) for v in tb], figures_box=[round(v) for v in fb],
                      safe=[round(v) for v in safe], avoid={k: [round(v) for v in z] for k, z in avoid.items()},
                      text_in_safe=ok_safe, avoid_hits=hits)
    if not ok_safe or hits:
        print('WARN', name, 'text_in_safe', ok_safe, 'hits', hits, tb, fb)
    im.save(OUT + name, optimize=True)
    print('saved', name, im.size)
    return im

# ---------- master (same framing as banner-09: full width, top offset 22.9) ----------
cut('master-2560x1440.png', 2560, 1440, 0, 22.86, 1168, 1640, 720, 660,
    'A podcast for men who stay', (40, 26, 'TUESDAY AND FRIDAY'),
    safe=(507, 508, 2053, 931), avoid={})

# ---------- YouTube: upload the master ----------
# ---------- X header 1500x500 ----------
# avatar circle overlaps bottom-left; ~60px top/bottom may crop
cut('x-header-1500x500.png', 1500, 500, 0, 270, 1168, 1060, 250, 470,
    'A podcast for men who stay', None,
    safe=(300, 60, 1440, 440), avoid={'avatar': (0, 300, 420, 500)})

# ---------- Facebook page cover 1702x630 (2x of 851x315) ----------
# desktop avatar bottom-left; mobile shows ~center 68% of width; mobile avatar bottom-center
cut('facebook-cover-1702x630.png', 1702, 630, 0, 210, 1168, 1110, 230, 470,
    'A podcast for men who stay', None,
    safe=(272, 40, 1430, 590), avoid={'avatar_desktop': (0, 270, 420, 630), 'avatar_mobile': (761, 450, 941, 630)})

# ---------- LinkedIn company cover 1512x256 ----------
cut('linkedin-cover-1512x256.png', 1512, 256, 0, 316, 1168, 1010, 124, 300,
    None, None,
    safe=(250, 20, 1300, 236), avoid={'logo': (0, 150, 240, 256), 'lower_right': (1300, 160, 1512, 256)})

# ---------- Reddit profile banner 1920x384 ----------
cut('reddit-banner-1920x384.png', 1920, 384, 0, 318, 1168, 1190, 180, 380,
    None, (18, 20, 'A PODCAST FOR MEN WHO STAY'),
    safe=(480, 30, 1440, 354), avoid={'avatar_mobile': (0, 254, 300, 384)})

json.dump(CUTS, open(OUT + '_build/cuts.json', 'w'), indent=1)
