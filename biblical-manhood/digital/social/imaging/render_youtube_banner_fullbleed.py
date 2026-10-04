#!/usr/bin/env python3
"""Full-bleed YouTube banner from Grok lock NEW — Merc 2026-09-15.

Cover-scales youtube-banner-grok-locked-NEW.jpg to 2560×1440.
Picks vertical crop maximizing gold title in YT safe ~1546×423.
Atmosphere fills edges (no SAFEZONE letterbox). Avatar untouched.
No spend. No posts. Do not overwrite youtube-banner.png until Holt PASS.
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

SRC = Path(__file__).with_name("youtube-banner-grok-locked-NEW.jpg")
OUT = Path(__file__).with_name("youtube-banner-fullbleed-v1.png")
W, H = 2560, 1440
SAFE = (507, 509, 2053, 932)

def main():
    src = Image.open(SRC).convert("RGB")
    sw, sh = src.size
    S = max(W / sw, H / sh)
    nw, nh = int(sw * S + 0.5), int(sh * S + 0.5)
    scaled = src.resize((nw, nh), Image.Resampling.LANCZOS)
    a = np.array(scaled)
    r, g, b = [a[:, :, i].astype(np.int16) for i in range(3)]
    gold = (r > 155) & (g > 115) & (b < 110) & (r > b + 45) & (g > b + 25)
    best = None
    for y in range(0, nh - H + 1, 2):
        gy, gx = np.where(gold)
        m = (gy >= y + SAFE[1]) & (gy <= y + SAFE[3]) & (gx >= SAFE[0]) & (gx <= SAFE[2])
        score = int(m.sum())
        lum = 0.299 * r[y : y + H] + 0.587 * g[y : y + H] + 0.114 * b[y : y + H]
        lit = float((lum[SAFE[1] : SAFE[3], SAFE[0] : SAFE[2]] > 45).mean())
        total = score + lit * 5000
        if best is None or total > best[0]:
            best = (total, y)
    y = best[1]
    canvas = scaled.crop((0, y, W, y + H))
    canvas = ImageEnhance.Sharpness(canvas).enhance(1.22)
    canvas = ImageEnhance.Contrast(canvas).enhance(1.08)
    canvas.save(OUT, "PNG", optimize=True)
    proof = canvas.copy()
    ImageDraw.Draw(proof).rectangle([SAFE[0], SAFE[1], SAFE[2], SAFE[3]], outline=(227, 197, 114), width=4)
    proof.save(OUT.with_name("youtube-banner-fullbleed-v1-safe-proof.png"))
    canvas.crop(SAFE).save(OUT.with_name("youtube-banner-fullbleed-v1-safe-crop.png"))
    print("wrote", OUT, "y=", y)

if __name__ == "__main__":
    main()
