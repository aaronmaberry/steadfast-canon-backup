"""Re-render banner-09 with the LOCKED live-site logo (steadfast/img/logo-lockup.jpg, md5 5a305f06...) composited in place of the redrawn WALK STEADFAST wordmark.
Photo pipeline is the unchanged render_final.py / render_yt_v2.py; only lockup() is swapped. Logo: crop + scale (Lanczos on premultiplied) + black-bg keyed to alpha. No redraw/recolor."""
import sys, re
from PIL import Image
import numpy as np
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
import bannerlib as BL
LOGO = '/workspace/steadfast/img/logo-lockup.jpg'
A = np.asarray(Image.open(LOGO).convert('RGB'), np.float32)[58:348, 190:966]   # crop (pixels untouched)
BGV = np.median(np.asarray(Image.open(LOGO).convert('RGB'), np.float32)[:40, :40].reshape(-1, 3), 0)
m = A.max(2); a = np.clip((m - BGV.max() - 6) / (255 - BGV.max() - 6), 0, 1)
PRE = np.dstack([np.clip(A - BGV * (1 - a[..., None]), 0, 255), a * 255])    # premultiplied RGB + alpha (bg removal)
H0, W0 = a.shape
orig_tracked = BL.tracked
LOGW = 0.92  # logo width as a fraction of the old STEADFAST width

def lockup(im, cx, top, width, fg=None, rule=None, sub=None, sub_fill=BL.MUTED, layout='stack', walk_fill=None, rule_w=None):
    w = round(width * LOGW); h = round(H0 * w / W0)
    pre = np.dstack([np.asarray(Image.fromarray(PRE[..., c].astype(np.float32), 'F').resize((w, h), Image.LANCZOS)) for c in range(4)])
    al = np.clip(pre[..., 3] / 255, 0, 1)[..., None]
    x0, y0 = round(cx - w / 2), round(top)
    if True:
        reg = np.asarray(im.crop((x0, y0, x0 + w, y0 + h)), np.float32)
        out = np.clip(pre[..., :3], 0, 255) + reg * (1 - al)
        im.paste(Image.fromarray(out.clip(0, 255).astype(np.uint8)), (x0, y0))
    BL.TEXT_BOXES.append((x0, y0, x0 + w, y0 + h))
    y = y0 + h + h * 0.10
    if sub:
        size = int(width * 0.15552)   # same STEADFAST size the old lockup derived -> same subtitle size
        fs = BL.font(max(34, int(size * 0.24)), 400)
        from PIL import ImageDraw
        b = orig_tracked(ImageDraw.Draw(im), (cx, y), sub, fs, sub_fill, fs.size * 0.04, 'c')
        y = b[3]
    return y
BL.lockup = lockup

SRCDIR = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-09-final/'
NEW = SRCDIR + 'logo-fix/'
for script, newout in [('render_final.py', NEW), ('render_yt_v2.py', NEW + 'youtube-v2/')]:
    code = open(SRCDIR + '_build/' + script).read()
    code = re.sub(r"^OUT = .*$", f"OUT = {newout!r}", code, count=1, flags=re.M)
    code = code.replace("OUT + '_build/walk-esrgan-x4.png'", repr(SRCDIR + '_build/walk-esrgan-x4.png'))
    code = code.replace("OUT + '_build/cuts.json'", repr(NEW + '_build/cuts.json'))
    sys.argv = [script]
    exec(compile(code, script, 'exec'), {'__name__': '__main__'})
