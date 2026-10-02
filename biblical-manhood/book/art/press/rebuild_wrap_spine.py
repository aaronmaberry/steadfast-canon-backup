#!/usr/bin/env python3
"""Resize the a-wrap.png spine for the final page count. Back and front panels are copied
pixel-for-pixel from the current wrap; only the spine strip is rebuilt (same cloth, same type,
same placement as render_a_v2.build_wrap), re-centered on the new spine width.

Spine math (KDP paperback, cream paper, as assumed in every earlier wrap build):
  spine_in = pages * 0.0025 in
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import render_a_v2 as r  # noqa: E402  (fonts, colors, tracked_width; does not write files on import)

DPI = 300
TRIM_W, TRIM_H = 6 * DPI, 9 * DPI
BLEED_L, BLEED_R, BLEED_T, BLEED_B = 38, 37, 38, 37
CREAM_IN_PER_PAGE = 0.0025


def spine_strip(spine: int, h: int, x_offset: int, seed: int = 19) -> Image.Image:
    rng = np.random.default_rng(seed)
    img = np.full((h, spine, 3), r.NAVY, np.float32)
    y, x = np.indices((h, spine))
    x = x + x_offset  # keep the weave phase continuous with the back panel
    weave = (2.0 * np.sin(x * (2 * np.pi / 4.8)) + 1.5 * np.sin(y * (2 * np.pi / 6.2))
             + 1.1 * np.sin((x + y) * (2 * np.pi / 9.4))).astype(np.float32)
    nap = rng.normal(0, 1.45, (h, spine)).astype(np.float32)
    img += (0.50 * weave + nap)[..., None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def spine_type(spine: int) -> Image.Image:
    clear = int(round(0.0625 * DPI))
    sh = int(spine - 2 * clear)
    fsp = r.F("LibreFranklin-Medium.ttf", 40)
    fhart = r.F("LibreFranklin-Medium.ttf", 34)
    line1 = r.TITLE + " " + r.TITLE2
    gap = 40
    tw = r.tracked_width(fsp, line1, 3.0) + gap + r.tracked_width(fhart, r.SPINE_AUTHOR, 5.0) + 8
    im = Image.new("RGBA", (int(tw), sh), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = 0.0
    for ch in line1:
        d.text((x, sh / 2), ch, font=fsp, fill=r.GOLD + (255,), anchor="lm")
        x += fsp.getlength(ch) + 3.0
    x += gap
    for ch in r.SPINE_AUTHOR:
        d.text((x, sh / 2), ch, font=fhart, fill=r.BONE + (255,), anchor="lm")
        x += fhart.getlength(ch) + 5.0
    return im.transpose(Image.Transpose.ROTATE_270)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, required=True)
    ap.add_argument("--wrap", default=str(ROOT / "a-wrap.png"))
    ap.add_argument("--old-spine", type=int, default=None, help="current spine px (default: derived from width)")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    src = Image.open(a.wrap).convert("RGB")
    W0, H = src.size
    assert H == BLEED_T + TRIM_H + BLEED_B, H
    old_spine = a.old_spine or (W0 - BLEED_L - BLEED_R - 2 * TRIM_W)
    spine_in = a.pages * CREAM_IN_PER_PAGE
    spine = int(round(spine_in * DPI + 1e-9))
    # Python rounds .5 to even; KDP min is the computed width, so round half up.
    if spine < spine_in * DPI:
        spine += 1
    W = BLEED_L + TRIM_W + spine + TRIM_W + BLEED_R

    back = src.crop((0, 0, BLEED_L + TRIM_W, H))
    front = src.crop((BLEED_L + TRIM_W + old_spine, 0, W0, H))
    out = Image.new("RGB", (W, H))
    out.paste(back, (0, 0))
    strip = spine_strip(spine, H, x_offset=BLEED_L + TRIM_W)
    t = spine_type(spine)
    strip.paste(t, ((spine - t.size[0]) // 2, int(0.45 * DPI)), t)
    out.paste(strip, (BLEED_L + TRIM_W, 0))
    out.paste(front, (BLEED_L + TRIM_W + spine, 0))

    dst = Path(a.out or a.wrap)
    out.save(dst, "PNG", optimize=True, dpi=(DPI, DPI))
    print(f"pages={a.pages} spine={spine_in:.4f}in -> {spine}px ({spine / DPI:.4f}in); "
          f"old spine {old_spine}px; wrap {W0}x{H} -> {W}x{H} ({W / DPI:.4f}x{H / DPI:.4f}in); "
          f"type {t.size[0]}x{t.size[1]}px, side clearance {(spine - t.size[0]) / 2 / DPI:.3f}in -> {dst}")


if __name__ == "__main__":
    main()
