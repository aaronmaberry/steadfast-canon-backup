import numpy as np
from PIL import Image, ImageDraw
import sys
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
from bannerlib import font
OLD = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/banner-09.png'
NEW = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/master-2560x1440.png'
def lapvar(im):
    a = np.asarray(im.convert('L'), np.float64)
    l = -4 * a[1:-1, 1:-1] + a[:-2, 1:-1] + a[2:, 1:-1] + a[1:-1, :-2] + a[1:-1, 2:]
    return l.var()
def tenengrad(im):
    a = np.asarray(im.convert('L'), np.float64)
    gx = a[1:-1, 2:] - a[1:-1, :-2]; gy = a[2:, 1:-1] - a[:-2, 1:-1]
    return (gx ** 2 + gy ** 2).mean()
old, new = Image.open(OLD), Image.open(NEW)
regions = {'full frame': (0, 0, 2560, 1440), 'figures + trunk (100%)': (560, 600, 1260, 1300), 'oak crown vs sky (100%)': (300, 60, 1200, 560), 'fence + field, right (100%)': (1700, 950, 2500, 1400)}
rows = []
for k, b in regions.items():
    o, n = old.crop(b), new.crop(b)
    rows.append((k, lapvar(o), lapvar(n), tenengrad(o), tenengrad(n)))
for r in rows:
    print(f'{r[0]:30s} LapVar old {r[1]:8.1f} new {r[2]:8.1f} ({r[2]/r[1]:.2f}x)  Tenengrad old {r[3]:7.1f} new {r[4]:7.1f}')
# side-by-side 100% crops
b = regions['figures + trunk (100%)']; b2 = regions['oak crown vs sky (100%)']
o1, n1 = old.crop(b), new.crop(b); o2, n2 = old.crop(b2), new.crop(b2)
W = o1.width * 2 + 30; H = 90 + o1.height + 70 + o2.height
sheet = Image.new('RGB', (max(W, o2.width * 2 + 30), H), (24, 24, 28)); d = ImageDraw.Draw(sheet)
f = font(30, 500)
d.text((10, 20), f'OLD banner-09 (Lanczos 2.2x)  LapVar {rows[1][1]:.0f}', font=f, fill=(230, 230, 235))
d.text((o1.width + 30, 20), f'NEW master (Real-ESRGAN x4)  LapVar {rows[1][2]:.0f}', font=f, fill=(139, 156, 255))
sheet.paste(o1, (0, 70)); sheet.paste(n1, (o1.width + 30, 70))
y = 70 + o1.height + 20
d.text((10, y), f'100% crop: oak crown.  LapVar old {rows[2][1]:.0f} / new {rows[2][2]:.0f}', font=f, fill=(230, 230, 235))
sheet.paste(o2, (0, y + 45)); sheet.paste(n2, (o2.width + 30, y + 45))
sheet.save('/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/sharpness-compare-100pct.png')
import json; json.dump(rows, open('/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/_build/sharpness.json', 'w'), indent=1)
