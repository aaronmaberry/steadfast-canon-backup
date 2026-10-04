"""Shared helpers for Walk Steadfast banner concepts. Local PIL only, no paid generation."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps
import math

W, H = 2560, 1440
SAFE = (507, 508, 2053, 931)   # 1546 x 423 centered
TV_DESK = (0, 508, 2560, 931)  # desktop shows full width of the middle band
BG = (7, 7, 10)
ACCENT = (139, 156, 255)       # site --accent #8b9cff
TEXT = (244, 244, 245)
MUTED = (161, 161, 170)
IMG = '/workspace/steadfast-fourmarks/img/'
GEIST = '/usr/share/fonts/truetype/sand-box/google/Geist/Geist-VariableFont_wght.ttf'
GEISTMONO = '/usr/share/fonts/truetype/sand-box/google/Geist Mono/GeistMono-VariableFont_wght.ttf'

TEXT_BOXES = []

def font(size, wght=400, mono=False):
    f = ImageFont.truetype(GEISTMONO if mono else GEIST, size)
    try:
        f.set_variation_by_axes([wght])
    except Exception:
        pass
    return f

def cover(path, ox=0.5, oy=0.5, scale=1.0, flip=False):
    im = Image.open(path).convert('RGB')
    if flip:
        im = ImageOps.mirror(im)
    s = max(W / im.width, H / im.height) * scale
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    x = round((im.width - W) * ox); y = round((im.height - H) * oy)
    return im.crop((x, y, x + W, y + H))

def grade(im, bright=1.0, contrast=1.0, color=1.0):
    im = ImageEnhance.Brightness(im).enhance(bright)
    im = ImageEnhance.Contrast(im).enhance(contrast)
    return ImageEnhance.Color(im).enhance(color)

def vignette(im, strength=0.6, power=2.2):
    m = Image.new('L', (W // 8, H // 8))
    px = m.load()
    for y in range(m.height):
        for x in range(m.width):
            dx = (x / m.width - 0.5) * 2; dy = (y / m.height - 0.5) * 2
            d = min(1, math.sqrt(dx * dx * 0.8 + dy * dy) / 1.25)
            px[x, y] = int(255 * strength * d ** power)
    m = m.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(20))
    dark = Image.new('RGB', (W, H), BG)
    return Image.composite(dark, im, m)

def shade(im, box, alpha=0.55, blur=120):
    """Soft dark pad behind type for legibility."""
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).rounded_rectangle(box, radius=80, fill=int(255 * alpha))
    m = m.filter(ImageFilter.GaussianBlur(blur))
    return Image.composite(Image.new('RGB', (W, H), BG), im, m)

def gradient(im, side='left', start=0.0, end=0.55, alpha=0.9):
    m = Image.new('L', (W, 1))
    for x in range(W):
        t = x / W if side == 'left' else 1 - x / W
        v = 1 - min(1, max(0, (t - start) / (end - start)))
        m.putpixel((x, 0), int(255 * alpha * v))
    m = m.resize((W, H))
    return Image.composite(Image.new('RGB', (W, H), BG), im, m)

def _track_width(text, f, track):
    w = 0
    for i, ch in enumerate(text):
        w += f.getlength(ch) + (track if i < len(text) - 1 else 0)
    return w

def _hollow_tri(d, bl, top, br, stem, fill):
    img = d._image
    m = Image.new('L', img.size, 0); md = ImageDraw.Draw(m)
    md.polygon([bl, top, br], fill=255)
    # inner triangle: offset each edge inward by stem (incenter scaling)
    ax, ay = top; bx, by = bl; cx_, cy_ = br
    a = math.dist(bl, br); b = math.dist(top, br); c = math.dist(top, bl)
    ix = (a * ax + b * bx + c * cx_) / (a + b + c); iy = (a * ay + b * by + c * cy_) / (a + b + c)
    area = abs((bx - ax) * (cy_ - ay) - (cx_ - ax) * (by - ay)) / 2
    r = 2 * area / (a + b + c)
    k = max(0.0, (r - stem) / r)
    inner = [(ix + (px - ix) * k, iy + (py - iy) * k) for px, py in (bl, top, br)]
    md.polygon(inner, fill=0)
    img.paste(Image.new(img.mode, img.size, fill), (0, 0), m)

def tracked(d, xy, text, f, fill, track=0, anchor='l', tri_a=False, stroke=None, tri_pos=None):
    """Draw tracked text. anchor l/c/r on x, y is the cap top. tri_a draws the house-mark open triangle for A."""
    x, y = xy
    w = _track_width(text, f, track)
    if anchor == 'c': x -= w / 2
    elif anchor == 'r': x -= w
    cap = f.getbbox('H')  # (l, t, r, b) relative to origin
    capt, capb = cap[1], cap[3]
    _mb = f.getmask('I').getbbox()
    stem = stroke or max(2, round((_mb[2] - _mb[0]) * 1.05))
    tri_done = False
    x0 = x
    for i, ch in enumerate(text):
        cw = f.getlength(ch)
        if tri_a and ch == 'A' and not tri_done and (tri_pos is None or i == tri_pos):
            tri_done = True
            top = (x + cw / 2, y)
            bl = (x + cw * 0.04, y + (capb - capt))
            br = (x + cw * 0.96, y + (capb - capt))
            _hollow_tri(d, bl, top, br, stem, fill)
        else:
            d.text((x, y - capt), ch, font=f, fill=fill)
        x += cw + track
    box = (x0, y, x0 + w, y + (capb - capt))
    TEXT_BOXES.append(box)
    return box

def lockup(im, cx, top, width, fg=TEXT, rule=ACCENT, sub=None, sub_fill=MUTED, layout='stack', walk_fill=None, rule_w=None):
    """Walk Steadfast wordmark. stack: WALK small over STEADFAST, accent rule under. line: WALK STEADFAST on one line."""
    d = ImageDraw.Draw(im)
    if layout == 'stack':
        # size STEADFAST to width
        size = 200
        f = font(size, 420); tr = size * 0.10
        w = _track_width('STEADFAST', f, tr)
        size = int(size * width / w); f = font(size, 420); tr = size * 0.10
        capH = f.getbbox('H')[3] - f.getbbox('H')[1]
        fw = font(int(size * 0.34), 520); trw = size * 0.34 * 0.9
        capw = fw.getbbox('H')[3] - fw.getbbox('H')[1]
        tracked(d, (cx, top), 'WALK', fw, walk_fill or fg, trw, 'c')
        y = top + capw + capH * 0.42
        b = tracked(d, (cx, y), 'STEADFAST', f, fg, tr, 'c', tri_a=True)
        y = b[3] + capH * 0.34
        rw = rule_w or width * 0.86
        d.rectangle((cx - rw / 2, y, cx + rw / 2, y + max(4, size // 40)), fill=rule)
        y += capH * 0.30
    else:
        size = 200
        f = font(size, 420); tr = size * 0.10
        w = _track_width('WALK STEADFAST', f, tr)
        size = int(size * width / w); f = font(size, 420); tr = size * 0.10
        capH = f.getbbox('H')[3] - f.getbbox('H')[1]
        b = tracked(d, (cx, top), 'WALK STEADFAST', f, fg, tr, 'c', tri_a=True, tri_pos=8)
        y = b[3] + capH * 0.38
        rw = rule_w or width * 0.5
        d.rectangle((cx - rw / 2, y, cx + rw / 2, y + max(4, size // 40)), fill=rule)
        y += capH * 0.32
    if sub:
        fs = font(max(34, int(size * 0.24)), 400)
        b = tracked(d, (cx, y), sub, fs, sub_fill, fs.size * 0.04, 'c')
        y = b[3]
    return y

def small(im, xy, text, size=34, fill=MUTED, anchor='l', track=0.12, wght=450, mono=False):
    d = ImageDraw.Draw(im)
    f = font(size, wght, mono)
    return tracked(d, xy, text, f, fill, size * track, anchor)

def check_safe(name):
    bad = [b for b in TEXT_BOXES if b[0] < SAFE[0] - 1 or b[1] < SAFE[1] - 1 or b[2] > SAFE[2] + 1 or b[3] > SAFE[3] + 1]
    TEXT_BOXES.clear()
    if bad:
        raise SystemExit(f'{name}: text outside safe area {bad}')
