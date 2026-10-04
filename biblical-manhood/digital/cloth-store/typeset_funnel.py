#!/usr/bin/env python3
"""Typeset Cloth Store funnel over Jarvis Image 2.0 still. No second plumb."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_cloth_store import (  # noqa: E402
    BONE_T,
    F,
    GOLD_CTAS,
    GOLD_T,
    HUB,
    QUIET_LINE,
    gold_rect_cta,
    ink_height,
)

STILL = Path("/workspace/biblical-manhood/digital/cloth-store/image-2.0/funnel.png")
OUT = Path("/workspace/biblical-manhood/digital/cloth-store/image-2.0/funnel-typeset.png")


def main() -> None:
    im = Image.open(STILL).convert("RGB")
    assert im.size == (1080, 1920)
    d = ImageDraw.Draw(im)
    x0 = 72
    cta_w, cta_h = 700, 88

    f_st = F("PlayfairDisplay-Bold.ttf", 56)
    f_men = F("PlayfairDisplay-Bold.ttf", 108)
    f_sub = F("PlayfairDisplay-Italic.ttf", 28)
    f_sub_r = F("PlayfairDisplay-Regular.ttf", 28)
    f_line = F("EBGaramond-Italic.ttf", 32)
    f_cta = F("LibreFranklin-Medium.ttf", 30)
    f_quiet = F("LibreFranklin-Regular.ttf", 24)
    f_url = F("LibreFranklin-Medium.ttf", 24)

    y = 120
    d.text((x0, y), "STEADFAST", font=f_st, fill=GOLD_T, anchor="lt")
    y += ink_height(f_st, "STEADFAST") + 4
    d.text((x0, y), "MEN", font=f_men, fill=GOLD_T, anchor="lt")
    y += ink_height(f_men, "MEN") + 18

    left, word, right = "The way of ", "Godly", " Men"
    ascent = f_sub.getmetrics()[0]
    yb = y + ascent
    d.text((x0, yb), left, font=f_sub, fill=BONE_T, anchor="ls")
    x = x0 + f_sub.getlength(left)
    d.text((x, yb), word, font=f_sub_r, fill=BONE_T, anchor="ls")
    x += f_sub_r.getlength(word)
    d.text((x, yb), right, font=f_sub, fill=BONE_T, anchor="ls")
    y += ink_height(f_sub, "The way of Godly Men") + 28

    d.text((x0, y), "You picked this up for a reason.", font=f_line, fill=BONE_T, anchor="lt")
    y += ink_height(f_line, "You picked this up for a reason.") + 36

    for label, price in GOLD_CTAS:
        gold_rect_cta(d, (x0, y, x0 + cta_w, y + cta_h), label, f_cta, price=price)
        y += cta_h + 14

    qy = y + 12
    d.text((x0, qy), "Training is the 24 weeks.", font=f_quiet, fill=BONE_T, anchor="lt")
    qy += ink_height(f_quiet, "Training is the 24 weeks.") + 6
    d.text((x0, qy), "Bundle adds the ebook for $10 more.", font=f_quiet, fill=BONE_T, anchor="lt")
    d.text((x0, 1808), HUB, font=f_url, fill=BONE_T, anchor="lt")

    im.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {im.size} last_cta_bottom={y}")


if __name__ == "__main__":
    main()
