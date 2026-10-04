#!/usr/bin/env python3
"""Typeset Cloth Store app chrome over Jarvis Image 2.0 still. No second plumb."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path("/workspace/biblical-manhood/book/art/press")))
from render_a_v2 import navy_cloth  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_cloth_store import (  # noqa: E402
    BONE_T,
    DIM_BONE,
    F,
    HAIR,
    NAVY_T,
    QUIET_LINE,
    SESSIONS,
    SOCIAL,
    draw_social_row,
    gold_rect_cta,
    home_indicator,
    ink_height,
)

STILL = Path("/workspace/biblical-manhood/digital/cloth-store/image-2.0/app-chrome.png")
OUT = Path("/workspace/biblical-manhood/digital/cloth-store/image-2.0/app-chrome-typeset.png")


def main() -> None:
    im = Image.open(STILL).convert("RGB")
    assert im.size == (1170, 2532)
    w, h = im.size
    d = ImageDraw.Draw(im)
    pad = 72
    cx = w / 2.0
    split = 566

    f_time = F("LibreFranklin-Medium.ttf", 28)
    f_mark = F("LibreFranklin-Medium.ttf", 20)
    f_title = F("PlayfairDisplay-Bold.ttf", 56)
    f_sub = F("EBGaramond-Italic.ttf", 28)
    f_week = F("LibreFranklin-Medium.ttf", 16)
    f_num = F("LibreFranklin-Medium.ttf", 28)
    f_item = F("EBGaramond-Regular.ttf", 40)
    f_cta = F("LibreFranklin-Medium.ttf", 32)
    f_quiet = F("LibreFranklin-Regular.ttf", 22)
    f_tab = F("LibreFranklin-Regular.ttf", 24)
    f_tab_on = F("LibreFranklin-Medium.ttf", 24)
    f_soc = F("LibreFranklin-Regular.ttf", 18)

    d.text((pad, 48), "9:41", font=f_time, fill=BONE_T, anchor="lt")

    y = 130
    x = pad
    for ch in "STEADFAST MEN":
        d.text((x, y), ch, font=f_mark, fill=BONE_T, anchor="lt")
        x += f_mark.getlength(ch) + 3.2
    y += 36
    d.text((pad, y), "Training", font=f_title, fill=BONE_T, anchor="lt")
    y += ink_height(f_title, "Training") + 10
    d.text((pad, y), "24 weeks", font=f_sub, fill=BONE_T, anchor="lt")

    tab_h = 148
    ind_room = 48
    btn_h = 96
    tab_top = h - tab_h - ind_room

    cloth = navy_cloth(w, h - tab_top, seed=21)
    im.paste(cloth, (0, tab_top))
    d = ImageDraw.Draw(im)

    soc_y = tab_top - 40
    btn_y = soc_y - 16 - btn_h
    quiet_h = 36
    sheet_top = split + 40
    sheet_bottom = btn_y - quiet_h - 24

    d.text((pad, sheet_top), "Week 1 of 24", font=f_week, fill=HAIR, anchor="lt")
    # this week only — not 01–03 as one night
    d.text((pad, sheet_top + 48), "Introduction", font=f_item, fill=NAVY_T, anchor="lt")

    y = sheet_top + 48 + ink_height(f_item, "Introduction") + 40
    for line in ("Training is the 24 weeks.", "Bundle adds the ebook for $10 more."):
        d.text((pad, y), line, font=f_quiet, fill=HAIR, anchor="lt")
        y += ink_height(f_quiet, line) + 4
    y += 16
    gold_rect_cta(d, (pad, y, w - pad, y + btn_h), "Get the training", f_cta)
    y += btn_h + 20
    draw_social_row(d, cx, y, f_soc, HAIR)

    labels = ("Home", "Training", "Store")
    tw = w / 3.0
    cy_tab = tab_top + 52
    for i, lab in enumerate(labels):
        tx = tw * i + tw / 2.0
        on = lab == "Training"
        font = f_tab_on if on else f_tab
        fill = BONE_T if on else DIM_BONE
        d.text((tx, cy_tab), lab, font=font, fill=fill, anchor="mm")
        if on:
            uw = 64
            d.rectangle([tx - uw / 2, cy_tab + 24, tx + uw / 2, cy_tab + 27], fill=BONE_T)

    home_indicator(d, w, h, fill=BONE_T)
    im.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {im.size}")


if __name__ == "__main__":
    main()
