import sys, math, random
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
from bannerlib import *
OUT = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/'
CUR = '/workspace/biblical-manhood/digital/social/imaging/youtube-banner.png'

def grain(im, amt=6, seed=1):
    random.seed(seed)
    n = Image.effect_noise((W // 2, H // 2), 40).resize((W, H)).convert('RGB')
    return Image.blend(im, n, amt / 255 * 2)

def save(im, n):
    check_safe(f'banner-{n:02d}')
    im.save(OUT + f'banner-{n:02d}.png', optimize=True)
    print('saved', n)

def b01():
    im = cover(IMG + 'table-empty.jpg', oy=0.60)
    # second mug: copy the right mug, place mirrored on the left of the table
    mug = im.crop((1972, 832, 2078, 940))
    mk = Image.new('L', mug.size, 0); ImageDraw.Draw(mk).rounded_rectangle((6, 6, mug.width - 6, mug.height - 3), 10, fill=255)
    mk = mk.filter(ImageFilter.GaussianBlur(4))
    im.paste(ImageOps.mirror(mug), (2560 - 2078, 832), ImageOps.mirror(mk))
    im = grade(im, 0.92, 1.05, 0.9)
    im = vignette(im, 0.55)
    im = shade(im, (900, 515, 1660, 860), 0.5, 90)
    y = lockup(im, 1280, 530, 640, sub='Pull up a chair.')
    small(im, (1280, y + 44), 'NEW EPISODES TUESDAY AND FRIDAY', 26, ACCENT, 'c', 0.22, 500)
    save(im, 1)

def b02():
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    # giant faint house-mark triangle
    lay = Image.new('RGB', (W, H), BG); ld = ImageDraw.Draw(lay)
    ld.line([(1280 - 760, 1440 + 40), (1280, -120), (1280 + 760, 1440 + 40), (1280 - 760, 1440 + 40)], fill=(30, 33, 58), width=26, joint='curve')
    im = Image.blend(im, lay, 1.0)
    im = grain(im, 4)
    y = lockup(im, 1280, 540, 1040, sub='A podcast for men who stay')
    small(im, (1280, y + 40), 'WALKSTEADFAST.COM   /   @STEADFASTWALK', 26, (113, 113, 122), 'c', 0.2, 500)
    save(im, 2)

def b03():
    im = cover(IMG + 'landscape.jpg', oy=0.55, scale=1.0)
    im = grade(im, 0.85, 1.08, 0.85)
    im = gradient(im, 'right', 0.0, 0.62, 0.85)
    im = vignette(im, 0.45)
    im = shade(im, (1240, 530, 2040, 910), 0.6, 100)
    y = lockup(im, 1640, 566, 700, sub='A podcast for men who stay', sub_fill=(220, 220, 228))
    small(im, (1640, y + 40), 'FROM THE TEXAS HILL COUNTRY', 26, ACCENT, 'c', 0.26, 550)
    save(im, 3)

def mug_art(d, x, y, s, col, w):
    # simple mug outline with handle and steam
    d.rounded_rectangle((x, y, x + s, y + s * 1.05), radius=int(s * 0.12), outline=col, width=w)
    d.arc((x + s - s * 0.18, y + s * 0.22, x + s + s * 0.38, y + s * 0.75), -90, 90, fill=col, width=w)
    for k in range(2):
        sx = x + s * (0.33 + 0.34 * k)
        pts = [(sx + math.sin(t / 7) * s * 0.06, y - s * 0.12 - t * s * 0.012) for t in range(0, 30)]
        d.line(pts, fill=col, width=max(2, w - 2))

def bible_art(d, cx, y, w, col, lw):
    """Open Bible, line art. y is the spine top."""
    h = w * 0.50
    dip = h * 0.10
    for side in (-1, 1):
        # top edge: from spine (low) curving up to the outer corner
        top = [(cx + side * t / 40 * w / 2, y + dip * (1 - math.sin(t / 40 * math.pi / 2)) ** 1.5) for t in range(41)]
        bot = [(cx + side * t / 40 * w / 2, y + h + dip * (1 - math.sin(t / 40 * math.pi / 2)) ** 1.5 - dip * 0.3) for t in range(41)]
        d.line(top, fill=col, width=lw, joint='curve')
        d.line(bot, fill=col, width=lw, joint='curve')
        d.line([top[-1], bot[-1]], fill=col, width=lw)
        # page stack under the outer edge
        d.line([(cx + side * w / 2, bot[-1][1]), (cx + side * w * 0.52, bot[-1][1] + h * 0.05), (cx, y + h + h * 0.08)], fill=(90, 100, 170), width=max(2, lw - 2))
        # text lines
        for r in range(7):
            f = 0.22 + r * 0.095
            x1 = cx + side * w * 0.06; x2 = cx + side * w * (0.42 if r not in (3, 6) else 0.28)
            yy = y + h * f + dip * 0.4
            d.line([(x1, yy), (x2, yy)], fill=(80, 90, 150), width=max(2, lw // 2))
    d.line([(cx, y + dip), (cx, y + h + dip * 0.7)], fill=col, width=lw)
    # ribbon marker
    d.line([(cx + w * 0.04, y + h + dip * 0.6), (cx + w * 0.05, y + h * 1.16)], fill=ACCENT, width=lw)

def b04():
    im = Image.new('RGB', (W, H), BG); im = grain(im, 3)
    d = ImageDraw.Draw(im)
    bible_art(d, 880, 600, 520, ACCENT, 6)
    mug_art(d, 455, 780, 100, ACCENT, 6)
    mug_art(d, 1190, 780, 100, ACCENT, 6)
    d.line([(380, 900), (1340, 900)], fill=(50, 56, 95), width=4)  # table line
    y = lockup(im, 1700, 575, 620, sub='Coffee and Scripture')
    small(im, (1700, y + 40), 'TUESDAY AND FRIDAY', 26, ACCENT, 'c', 0.3, 500)
    save(im, 4)

def b05():
    im = cover(IMG + 'road.jpg', oy=0.0, scale=1.0)
    im = grade(im, 0.95, 1.05, 0.95)
    im = vignette(im, 0.5)
    im = shade(im, (620, 520, 1940, 900), 0.35, 120)
    y = lockup(im, 1280, 560, 1240, layout='line', sub='New episodes Tuesday and Friday')
    small(im, (1280, y + 40), '@STEADFASTWALK', 26, ACCENT, 'c', 0.3, 500)
    save(im, 5)

def b06():
    im = cover(IMG + 'mic.jpg', ox=0.0, oy=0.40)
    im = grade(im, 0.75, 1.15, 0.6)
    im = gradient(im, 'left', 0.0, 0.42, 0.92)
    im = vignette(im, 0.6)
    y = lockup(im, 790, 560, 520, sub='A video podcast', rule_w=440)
    small(im, (790, y + 36), 'WITH WES HART AND JONATHON', 24, ACCENT, 'c', 0.22, 500)
    small(im, (2030, 900 - 24), 'TUE / FRI', 24, (180, 180, 190), 'r', 0.3, 500, mono=True)
    save(im, 6)

def b07():
    im = Image.new('RGB', (W, H), ACCENT)
    lay = Image.new('RGB', (W, H), ACCENT); ld = ImageDraw.Draw(lay)
    for i, s in enumerate([1500, 1150, 800]):
        ld.line([(1280 - s, 1440 + 60), (1280, 1440 + 60 - 2 * s * 0.98), (1280 + s, 1440 + 60), (1280 - s, 1440 + 60)], fill=(124, 140, 240), width=14, joint='curve')
    im = lay
    # soft radial lift
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).ellipse((380, 160, 2180, 1280), fill=90)
    im = Image.composite(Image.new('RGB', (W, H), (160, 174, 255)), im, m.filter(ImageFilter.GaussianBlur(260)))
    y = lockup(im, 1280, 565, 1000, fg=BG, rule=BG, sub='A podcast for men who stay', sub_fill=(30, 32, 52))
    small(im, (1280, y + 40), 'WALKSTEADFAST.COM', 26, (30, 32, 52), 'c', 0.3, 550)
    save(im, 7)

def b08():
    im = Image.new('RGB', (W, H), BG); im = grain(im, 3)
    d = ImageDraw.Draw(im)
    lockup(im, 880, 590, 640, sub='A podcast for men who stay', rule_w=560)
    d.rectangle((1262, 560, 1266, 880), fill=(50, 56, 95))
    small(im, (1340, 568), 'NEW EPISODES', 26, MUTED, 'l', 0.3, 500, mono=True)
    rows = [('TUESDAY', 'The main episode'), ('FRIDAY', 'Field Notes')]
    for i, (day, what) in enumerate(rows):
        yy = 650 + i * 120
        d.rounded_rectangle((1340, yy, 2030, yy + 96), radius=14, outline=(60, 68, 120), width=3)
        d.rectangle((1340, yy, 1352, yy + 96), fill=ACCENT)
        small(im, (1384, yy + 30), day, 40, TEXT, 'l', 0.18, 560)
        small(im, (2000, yy + 34), what, 34, ACCENT, 'r', 0.02, 420)
    save(im, 8)

def b09():
    im = cover(IMG + 'walk.jpg', oy=0.18, scale=1.0)
    im = grade(im, 1.0, 1.05, 0.9)
    im = vignette(im, 0.45)
    im = shade(im, (1260, 520, 2020, 900), 0.30, 110)
    y = lockup(im, 1640, 566, 660, sub='A podcast for men who stay')
    small(im, (1640, y + 40), 'TUESDAY AND FRIDAY', 26, ACCENT, 'c', 0.3, 500)
    save(im, 9)

def b10():
    im = Image.open(CUR).convert('RGB')
    im = gradient(im, 'left', 0.0, 0.40, 0.6)
    y = lockup(im, 820, 572, 560, sub='Now a video podcast', rule_w=480)
    small(im, (820, y + 40), 'TUESDAY AND FRIDAY', 26, ACCENT, 'c', 0.3, 500)
    save(im, 10)

which = [int(a) for a in sys.argv[1:]] or range(1, 11)
for n in which:
    globals()[f'b{n:02d}']()
