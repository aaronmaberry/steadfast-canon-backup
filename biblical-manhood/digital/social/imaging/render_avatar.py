#!/usr/bin/env python3
"""OPTIONAL single-rule TRY plate only. Never overwrite locked avatar.png."""
from pathlib import Path
from PIL import Image
import numpy as np

OUT = Path(__file__).resolve().parent
SRC = OUT / "logo-lockup-site.png"
SIZE = 1024
NAVY = (11, 31, 56)
BLACK = (0, 0, 0)
DEST = OUT / "avatar-single-rule-TRY-2026-09-15.png"


def main() -> None:
    src = Image.open(SRC).convert("RGBA")
    arr = np.array(src)
    white = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 180) & (arr[:, :, 2] > 180) & (arr[:, :, 3] > 200)
    navy_mask = (
        (arr[:, :, 2] > arr[:, :, 0] + 20)
        & (arr[:, :, 0] < 80)
        & (arr[:, :, 2] < 120)
        & (arr[:, :, 3] > 200)
    )
    navy_rows = np.where(navy_mask.any(axis=1))[0]
    above = white.copy(); above[navy_rows.min() :, :] = False
    below = white.copy(); below[: navy_rows.max() + 1, :] = False
    ya, xa = np.where(above)
    yb, xb = np.where(below)
    stead = src.crop((int(xa.min()), int(ya.min()), int(xa.max()) + 1, int(ya.max()) + 1))
    men = src.crop((int(xb.min()), int(yb.min()), int(xb.max()) + 1, int(yb.max()) + 1))
    pad = 56
    max_w = SIZE - 2 * pad
    sw, sh = stead.size
    s_scale = max_w / sw
    stead_r = stead.resize((int(sw * s_scale), int(sh * s_scale)), Image.Resampling.LANCZOS)
    mw, mh = men.size
    target_h = max(int(stead_r.size[1] * 0.58), int(SIZE * 0.09))
    m_scale = target_h / mh
    if mw * m_scale > stead_r.size[0]:
        m_scale = stead_r.size[0] / mw
    men_r = men.resize((int(mw * m_scale), int(mh * m_scale)), Image.Resampling.LANCZOS)
    rule = Image.new("RGBA", (stead_r.size[0], 7), (*NAVY, 255))
    gap1, gap2 = 18, 24
    stack_h = stead_r.size[1] + gap1 + 7 + gap2 + men_r.size[1]

    def paste_rgba(base, overlay, xy):
        overlay = overlay.convert("RGBA")
        layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        layer.paste(overlay, xy, overlay)
        return Image.alpha_composite(base, layer)

    canvas = Image.new("RGBA", (SIZE, SIZE), (*BLACK, 255))
    y = (SIZE - stack_h) // 2
    canvas = paste_rgba(canvas, stead_r, ((SIZE - stead_r.size[0]) // 2, y))
    y2 = y + stead_r.size[1] + gap1
    canvas = paste_rgba(canvas, rule, ((SIZE - rule.size[0]) // 2, y2))
    y3 = y2 + 7 + gap2
    canvas = paste_rgba(canvas, men_r, ((SIZE - men_r.size[0]) // 2, y3))
    canvas.convert("RGB").save(DEST, "PNG", optimize=True)
    print("wrote", DEST, "(locked avatar.png untouched)")


if __name__ == "__main__":
    main()
