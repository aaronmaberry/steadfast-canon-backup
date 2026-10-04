#!/usr/bin/env python3
"""Typeset Cloth Store chrome over Jarvis Image 2.0 mobile still. No second plumb."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_cloth_store import (  # noqa: E402
    BONE_T,
    CREED,
    F,
    GOLD_CTAS,
    GOLD_T,
    HAIR,
    HUB,
    NAVY_T,
    QUIET_LINE,
    SOCIAL,
    draw_bone_shelf,
    gold_rect_cta,
    ink_height,
    wrap_words,
)

STILL = Path("/workspace/biblical-manhood/digital/cloth-store/image-2.0/mobile-home.png")
OUT = Path("/workspace/biblical-manhood/digital/cloth-store/image-2.0/mobile-home-typeset.png")


def main() -> None:
    im = Image.open(STILL).convert("RGB")
    assert im.size == (1170, 2532)
    d = ImageDraw.Draw(im)
    x0 = 72
    type_w = 560  # keep Four Marks off the plumb
    split = 680

    f_time = F("LibreFranklin-Medium.ttf", 28)
    f_st = F("PlayfairDisplay-Bold.ttf", 56)
    f_men = F("PlayfairDisplay-Bold.ttf", 92)
    f_sub = F("PlayfairDisplay-Italic.ttf", 28)
    f_sub_r = F("PlayfairDisplay-Regular.ttf", 28)
    f_auth = F("LibreFranklin-Medium.ttf", 20)
    f_line = F("EBGaramond-Italic.ttf", 30)
    f_cta = F("LibreFranklin-Medium.ttf", 28)
    f_quiet = F("LibreFranklin-Regular.ttf", 22)
    f_kicker = F("LibreFranklin-Medium.ttf", 16)
    f_creed = F("EBGaramond-Regular.ttf", 28)
    f_slot = F("LibreFranklin-Regular.ttf", 24)
    f_shop = F("LibreFranklin-Regular.ttf", 20)
    f_soc = F("LibreFranklin-Regular.ttf", 18)
    f_url = F("LibreFranklin-Medium.ttf", 18)

    d.text((72, 48), "9:41", font=f_time, fill=BONE_T, anchor="lt")

    y = 120
    d.text((x0, y), "STEADFAST", font=f_st, fill=GOLD_T, anchor="lt")
    y += ink_height(f_st, "STEADFAST") + 6
    d.text((x0, y), "MEN", font=f_men, fill=GOLD_T, anchor="lt")
    y += ink_height(f_men, "MEN") + 16

    left, word, right = "The way of ", "Godly", " Men"
    ascent = f_sub.getmetrics()[0]
    yb = y + ascent
    d.text((x0, yb), left, font=f_sub, fill=BONE_T, anchor="ls")
    x = x0 + f_sub.getlength(left)
    d.text((x, yb), word, font=f_sub_r, fill=BONE_T, anchor="ls")
    x += f_sub_r.getlength(word)
    d.text((x, yb), right, font=f_sub, fill=BONE_T, anchor="ls")
    y += ink_height(f_sub, "The way of Godly Men") + 14

    d.text((x0, y), "WES HART", font=f_auth, fill=BONE_T, anchor="lt")
    y += 28
    for line in wrap_words(f_line, "You picked this up for a reason. Sit down.", type_w, 0.3):
        d.text((x0, y), line, font=f_line, fill=BONE_T, anchor="lt")
        y += ink_height(f_line, line) + 6
    y += 16

    cta_w, cta_h = 620, 68
    for label, price in GOLD_CTAS:
        gold_rect_cta(d, (x0, y, x0 + cta_w, y + cta_h), label, f_cta, price=price)
        y += cta_h + 10

    for line in wrap_words(f_quiet, QUIET_LINE, 560, 0.0):
        d.text((x0, y), line, font=f_quiet, fill=BONE_T, anchor="lt")
        y += ink_height(f_quiet, line) + 3

    y = split + 36
    d.text((x0, y), "THE FOUR MARKS", font=f_kicker, fill=NAVY_T, anchor="lt")
    y += 28
    for line in wrap_words(f_creed, CREED, type_w, 0.0):
        d.text((x0, y), line, font=f_creed, fill=NAVY_T, anchor="lt")
        y += ink_height(f_creed, line) + 8

    y += 24
    y = draw_bone_shelf(d, x0, y, 620, 68, 10, f_slot, f_kicker, f_shop)

    # footer sits after Shop, not below a long empty cream
    y += 28
    d.text((x0, y), HUB, font=f_url, fill=HAIR, anchor="lt")
    y += 32
    d.text((x0, y), "   ·   ".join(SOCIAL), font=f_soc, fill=HAIR, anchor="lt")

    im.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {im.size}")


if __name__ == "__main__":
    main()
