import json, sys
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
from bannerlib import font
from PIL import Image, ImageDraw
OUT = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/'
cuts = json.load(open(OUT + '_build/cuts.json'))
labels = {
 'master-2560x1440.png': 'YouTube banner 2560x1440 (upload this master). Green = 1546x423 safe area on all devices. Yellow = desktop band. No avatar overlap on YouTube.',
 'x-header-1500x500.png': 'X header 1500x500. Red = avatar overlap (bottom-left). Grey bars = ~60 px top/bottom crop X warns about.',
 'facebook-cover-1702x630.png': 'Facebook Page cover 1702x630 (2x of 851x315). Red = desktop avatar (bottom-left) and mobile avatar. Green = mobile-visible center.',
 'linkedin-cover-1512x256.png': 'LinkedIn company cover 1512x256. Red = logo overlap (bottom-left) and the lower-right area LinkedIn says to keep clear.',
 'reddit-banner-1920x384.png': 'Reddit profile banner 1920x384. Red = mobile avatar. Green = center half (mobile crops the sides).',
}
TW = 1600; M = 40
blocks = []
for name, c in cuts.items():
    im = Image.open(OUT + name).convert('RGB'); s = TW / im.width
    im = im.resize((TW, round(im.height * s)), Image.LANCZOS); d = ImageDraw.Draw(im)
    S = lambda b: [v * s for v in b]
    if name.startswith('master'):
        d.rectangle(S((0, 508, 2560, 931)), outline=(255, 200, 0), width=2)
    if name.startswith('x-header'):
        d.rectangle(S((0, 0, 1500, 60)), fill=None, outline=(150, 150, 150), width=2); d.rectangle(S((0, 440, 1500, 500)), outline=(150, 150, 150), width=2)
    d.rectangle(S(c['safe']), outline=(60, 220, 120), width=3)
    for k, z in c['avoid'].items():
        zz = S(z)
        if 'avatar' in k or k == 'logo':
            if k == 'logo':
                d.rectangle(zz, outline=(255, 70, 70), width=3)
            else:
                cx, cy = (zz[0] + zz[2]) / 2, (zz[1] + zz[3]) / 2
                r = min(zz[2] - zz[0], zz[3] - zz[1]) / 2
                d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(255, 70, 70), width=3)
                d.rectangle(zz, outline=(255, 70, 70), width=1)
        else:
            d.rectangle(zz, outline=(255, 70, 70), width=2)
        d.text((zz[0] + 6, zz[1] + 4), k, font=font(18, 500), fill=(255, 110, 110))
    d.rectangle(S(c['text_box']), outline=(139, 156, 255), width=1)
    blocks.append((name, labels[name], im))
H = 120 + sum(b[2].height + 90 for b in blocks)
sheet = Image.new('RGB', (TW + 2 * M, H), (24, 24, 28)); d = ImageDraw.Draw(sheet)
d.text((M, 30), 'Walk Steadfast  |  banner-09 "The walk"  |  platform cuts proof  |  2026-10-03', font=font(40, 500), fill=(244, 244, 245))
d.text((M, 80), 'Green = safe zone. Red = avatar/logo overlap or keep-clear area. Blue = text bounds. All text checked inside safe, clear of red, by script.', font=font(22, 400), fill=(161, 161, 170))
y = 120
for name, lab, im in blocks:
    d.text((M, y + 10), name, font=font(28, 560), fill=(139, 156, 255))
    d.text((M, y + 48), lab, font=font(20, 400), fill=(210, 210, 215))
    sheet.paste(im, (M, y + 82)); y += im.height + 90 + 0
sheet.save(OUT + 'proof-sheet.png', optimize=True); print(sheet.size)
