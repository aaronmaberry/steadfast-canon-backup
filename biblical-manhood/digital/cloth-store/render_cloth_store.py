#!/usr/bin/env python3
"""Cloth Store frames for Lane. Does not touch press cover PNGs."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw

PRESS = Path("/workspace/biblical-manhood/book/art/press")
sys.path.insert(0, str(PRESS))

from render_a_v2 import (  # noqa: E402
    BONE,
    F,
    GOLD,
    draw_lt,
    ink_height,
    navy_cloth,
    plumb_bob,
    tracked_width,
    wrap_words,
)

OUT = Path("/workspace/biblical-manhood/digital/cloth-store")

NAVY_T = (11, 31, 56)
GOLD_T = GOLD
BONE_T = BONE
DIM_BONE = (168, 164, 154)
HAIR = (72, 78, 70)

MOBILE = (1170, 2532)
STORY = (1080, 1920)

CREED = (
    "A real man rejects passivity, accepts responsibility, "
    "leads courageously, and expects the greater reward, God's reward."
)
HERO = "You picked this up for a reason. Sit down."
FUNNEL_LINE = "You picked this up for a reason."
# Bone shelf split: books, media, files. Shop last, quieter, empty — not next to the $79 path.
SHELF_BOOKS = ("Paperback", "Audiobook")
SHELF_MEDIA = ("YouTube", "Podcast")
SHELF_FILES = ("Downloads", "Devotionals")
SHOP_SLOT = "Shop"
SLOTS = SHELF_BOOKS + SHELF_MEDIA + SHELF_FILES + (SHOP_SLOT,)
SOCIAL = ("YouTube", "Instagram", "X", "Facebook", "TikTok", "Reddit", "LinkedIn")
HUB = "walksteadfast.com"
QUIET_LINE = "Training is the 24 weeks. Bundle adds the ebook for $10 more."
# Parked. Unclickable until Aaron signs each profile. Do not draw @handles.
PARKED_SOCIAL = {
    "YouTube": "youtube.com/@steadfastwalk",
    "Instagram": "instagram.com/steadfastwalk",
    "X": "x.com/steadfastwalk",
    "Facebook": "facebook.com/steadfastwalk",
    "TikTok": "tiktok.com/@steadfastwalk",
    "Reddit": "reddit.com/user/steadfastwalk",
    "LinkedIn": "linkedin.com/company/steadfastwalk",
}
GOLD_CTAS = (
    ("Start the training", "$79"),
    ("Get the ebook", "$14"),
    ("Get the bundle", "$89"),
)
SESSIONS = (
    ("01", "Introduction"),
    ("02", "You are not crazy"),
    ("03", "The four marks"),
)


def flatten_rgb(im: Image.Image) -> Image.Image:
    if im.mode == "RGB":
        return im
    bg = Image.new("RGB", im.size, NAVY_T)
    bg.paste(im, mask=im.split()[-1] if im.mode == "RGBA" else None)
    return bg


def save_png(im: Image.Image, path: Path, expect) -> None:
    im = flatten_rgb(im)
    assert im.size == expect, (path.name, im.size, expect)
    assert im.mode == "RGB"
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)
    print(f"wrote {path} {im.size} {im.mode}")


def draw_tracked(draw, x, y_top, text, font, fill, tracking) -> float:
    for ch in text:
        draw.text((x, y_top), ch, font=font, fill=fill, anchor="lt")
        x += font.getlength(ch) + tracking
    return y_top + ink_height(font, text)



def draw_godly_line(draw, cx, y_top, italic, roman, fill) -> float:
    """Godly is upright so the o cannot read as a degree. Rest of the line stays italic."""
    left, word, right = "The way of ", "Godly", " Men"
    # shared baseline
    ascent = italic.getmetrics()[0]
    yb = y_top + ascent
    total = italic.getlength(left) + roman.getlength(word) + italic.getlength(right)
    x = cx - total / 2.0
    draw.text((x, yb), left, font=italic, fill=fill, anchor="ls")
    x += italic.getlength(left)
    draw.text((x, yb), word, font=roman, fill=fill, anchor="ls")
    x += roman.getlength(word)
    draw.text((x, yb), right, font=italic, fill=fill, anchor="ls")
    return y_top + max(ink_height(italic, left + right), ink_height(roman, word))


def draw_social_row(draw, cx, y, font, fill) -> None:
    """Hairline names. No handles. No icon farm. One plumb lives in the header."""
    sep = "   ·   "
    line = sep.join(SOCIAL)
    draw.text((cx, y), line, font=font, fill=fill, anchor="mt")

def gold_rect_cta(draw, box, label, font, price=None) -> None:
    x0, y0, x1, y1 = box
    draw.rectangle([x0, y0, x1, y1], fill=GOLD_T)
    cx = (x0 + x1) / 2.0
    cy = (y0 + y1) / 2.0 + 2
    if price:
        text = f"{label}  ·  {price}"
    else:
        text = label
    draw.text((cx, cy), text, font=font, fill=NAVY_T, anchor="mm")


def draw_bone_shelf(draw, x0, y, col_w, row_h, gap, f_slot, f_kicker, f_shop) -> float:
    """Books, MEDIA (YouTube + Podcast), files, then Shop last and quieter."""
    def card(label, font, fill, outline, width=1):
        nonlocal y
        draw.rectangle([x0, y, x0 + col_w, y + row_h], outline=outline, width=width)
        draw.text((x0 + 16, y + row_h / 2 + 1), label, font=font, fill=fill, anchor="lm")
        y += row_h + gap

    for name in SHELF_BOOKS:
        card(name, f_slot, NAVY_T, HAIR)
    y += 4
    draw.text((x0, y), "MEDIA", font=f_kicker, fill=HAIR, anchor="lt")
    y += ink_height(f_kicker, "MEDIA") + 8
    for name in SHELF_MEDIA:
        card(name, f_slot, NAVY_T, HAIR)
    y += 12  # files are not media — plain words, like Shop
    for name in SHELF_FILES:
        draw.text((x0, y), name, font=f_shop, fill=HAIR, anchor="lt")
        y += ink_height(f_shop, name) + gap + 6
    y += 10
    # Shop last, quieter, still empty — word only, no box, not next to the golds
    draw.text((x0, y), SHOP_SLOT, font=f_shop, fill=HAIR, anchor="lt")
    y += ink_height(f_shop, SHOP_SLOT) + gap
    return y


def status_bar(draw, w, y=54) -> None:
    fill = BONE_T
    f = F("LibreFranklin-Medium.ttf", 42)
    draw.text((78, y), "9:41", font=f, fill=fill, anchor="lt")
    bx = w - 78
    draw.rectangle([bx - 66, y + 8, bx, y + 36], outline=fill, width=3)
    draw.rectangle([bx - 8, y + 16, bx + 4, y + 28], fill=fill)
    draw.rectangle([bx - 60, y + 13, bx - 18, y + 31], fill=fill)
    x = bx - 96
    draw.rectangle([x, y + 28, x + 8, y + 36], fill=fill)
    draw.rectangle([x + 14, y + 20, x + 22, y + 36], fill=fill)
    draw.rectangle([x + 28, y + 12, x + 36, y + 36], fill=fill)
    draw.rectangle([x + 42, y + 4, x + 50, y + 36], fill=fill)


def home_indicator(draw, w, h, fill=BONE_T) -> None:
    pw, ph = 402, 15
    x0 = (w - pw) / 2.0
    y0 = h - 42
    draw.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=8, fill=fill)


def hairline_card(draw, box, label, font) -> None:
    x0, y0, x1, y1 = box
    draw.rectangle([x0, y0, x1, y1], outline=HAIR, width=2)
    draw.text((x0 + 36, (y0 + y1) / 2.0 + 1), label, font=font, fill=NAVY_T, anchor="lm")


def render_home() -> Image.Image:
    w, h = MOBILE
    im = navy_cloth(w, h, seed=17)
    d = ImageDraw.Draw(im)
    cx = w / 2.0
    pad = 90
    usable = w - 2 * pad

    status_bar(d, w)

    f_st = F("PlayfairDisplay-Bold.ttf", 88)
    f_men = F("PlayfairDisplay-Bold.ttf", 140)
    f_sub = F("EBGaramond-Italic.ttf", 42)
    f_auth = F("LibreFranklin-Medium.ttf", 26)
    f_line = F("EBGaramond-Italic.ttf", 44)
    f_cta = F("LibreFranklin-Medium.ttf", 40)
    f_creed = F("EBGaramond-Regular.ttf", 38)
    f_slot = F("LibreFranklin-Regular.ttf", 34)
    f_kicker = F("LibreFranklin-Medium.ttf", 22)

    y = 176
    y = draw_lt(d, cx, y, "STEADFAST", f_st, GOLD_T, 6.2)
    y = draw_lt(d, cx, y + 8, "MEN", f_men, GOLD_T, 11.2)
    f_sub_roman = F("PlayfairDisplay-Regular.ttf", f_sub.size)
    y = draw_godly_line(d, cx, y + 24, f_sub, f_sub_roman, BONE_T)
    y = draw_lt(d, cx, y + 20, "WES HART", f_auth, BONE_T, 6.8)

    y = plumb_bob(d, cx, y + 32, scale=0.28, color=GOLD_T) + 36
    for line in wrap_words(f_line, HERO, usable, 0.4):
        d.text((cx, y), line, font=f_line, fill=BONE_T, anchor="mt")
        y += ink_height(f_line, line) + 8

    y += 28
    cta_h = 96
    for label, price in GOLD_CTAS:
        gold_rect_cta(d, (pad, y, w - pad, y + cta_h), label, f_cta, price=price)
        y += cta_h + 16
    y += 16

    d.rectangle([0, y, w, h], fill=BONE_T)
    inner_top = y + 52
    inner_bot = h - 108
    kicker = "THE FOUR MARKS"
    draw_tracked(d, pad, inner_top, kicker, f_kicker, NAVY_T, 3.2)
    sy = inner_top + 40
    creed_lines = wrap_words(f_creed, CREED, usable, 0.0)
    for line in creed_lines:
        d.text((pad, sy), line, font=f_creed, fill=NAVY_T, anchor="lt")
        sy += ink_height(f_creed, line) + 10

    sy += 28
    n = len(SLOTS)
    remain = inner_bot - sy
    gap = 18
    row_h = int((remain - gap * (n - 1)) / n)
    row_h = max(96, min(row_h, 168))
    for name in SLOTS:
        hairline_card(d, (pad, sy, w - pad, sy + row_h), name, f_slot)
        sy += row_h + gap

    f_soc = F("LibreFranklin-Regular.ttf", 22)
    draw_social_row(d, cx, h - 72, f_soc, HAIR)
    return im


def render_app() -> Image.Image:
    w, h = MOBILE
    im = navy_cloth(w, h, seed=21)
    d = ImageDraw.Draw(im)
    pad = 90
    cx = w / 2.0

    status_bar(d, w)

    f_mark = F("LibreFranklin-Medium.ttf", 22)
    f_title = F("PlayfairDisplay-Bold.ttf", 64)
    f_sub = F("EBGaramond-Italic.ttf", 34)
    f_num = F("LibreFranklin-Medium.ttf", 32)
    f_item = F("EBGaramond-Regular.ttf", 44)
    f_cta = F("LibreFranklin-Medium.ttf", 40)
    f_tab = F("LibreFranklin-Regular.ttf", 28)
    f_tab_on = F("LibreFranklin-Medium.ttf", 28)

    y = plumb_bob(d, cx, 150, scale=0.16, color=BONE_T) + 28
    draw_tracked(d, pad, y, "STEADFAST MEN", f_mark, BONE_T, 4.0)
    y += 42
    d.text((pad, y), "Training", font=f_title, fill=BONE_T, anchor="lt")
    y += ink_height(f_title, "Training") + 12
    d.text((pad, y), "Three sessions. Sit down.", font=f_sub, fill=BONE_T, anchor="lt")
    y += 52

    tab_h = 168
    btn_h = 112
    ind_room = 52
    soc_h = 48
    tab_top = h - tab_h - ind_room
    # bone sheet runs to the tab bar so the social hairline sits on paper, not on gold
    d.rectangle([0, y, w, tab_top], fill=BONE_T)

    soc_y = tab_top - 36
    btn_y = soc_y - 20 - btn_h
    sheet_bottom = btn_y - 24

    n = len(SESSIONS)
    block = sheet_bottom - y
    row_h = int(block / n)
    for i, (num, title) in enumerate(SESSIONS):
        ly = y + i * row_h
        cy = ly + row_h / 2.0
        d.text((pad, cy), num, font=f_num, fill=NAVY_T, anchor="lm")
        d.text((pad + 110, cy), title, font=f_item, fill=NAVY_T, anchor="lm")
        if i < n - 1:
            hy = ly + row_h
            d.rectangle([pad, hy - 1, w - pad, hy + 1], fill=HAIR)

    gold_rect_cta(d, (pad, btn_y, w - pad, btn_y + btn_h), "Open the store", f_cta)
    f_soc = F("LibreFranklin-Regular.ttf", 20)
    draw_social_row(d, cx, soc_y, f_soc, HAIR)

    d.rectangle([0, tab_top, w, h], fill=NAVY_T)
    labels = ("Home", "Training", "Store")
    tw = w / 3.0
    cy_tab = tab_top + 58
    for i, lab in enumerate(labels):
        tx = tw * i + tw / 2.0
        on = lab == "Training"
        font = f_tab_on if on else f_tab
        fill = BONE_T if on else DIM_BONE
        d.text((tx, cy_tab), lab, font=font, fill=fill, anchor="mm")
        if on:
            uw = 72
            d.rectangle([tx - uw / 2, cy_tab + 28, tx + uw / 2, cy_tab + 31], fill=BONE_T)

    home_indicator(d, w, h, fill=BONE_T)
    return im


def render_funnel() -> Image.Image:
    w, h = STORY
    im = navy_cloth(w, h, seed=19)
    d = ImageDraw.Draw(im)
    cx = w / 2.0
    pad = 86
    usable = w - 2 * pad

    f_st = F("PlayfairDisplay-Bold.ttf", 86)
    f_men = F("PlayfairDisplay-Bold.ttf", 150)
    f_sub = F("PlayfairDisplay-Italic.ttf", 36)
    f_line = F("EBGaramond-Italic.ttf", 42)
    f_cta = F("LibreFranklin-Medium.ttf", 38)
    f_url = F("LibreFranklin-Medium.ttf", 30)
    f_note = F("LibreFranklin-Regular.ttf", 22)

    y = 148
    y = draw_lt(d, cx, y, "STEADFAST", f_st, GOLD_T, 5.8)
    y = draw_lt(d, cx, y + 6, "MEN", f_men, GOLD_T, 10.4)
    f_sub_roman = F("PlayfairDisplay-Regular.ttf", f_sub.size)
    y = draw_godly_line(d, cx, y + 22, f_sub, f_sub_roman, BONE_T)

    y = plumb_bob(d, cx, y + 30, scale=0.26, color=GOLD_T) + 40
    d.text((cx, y), FUNNEL_LINE, font=f_line, fill=BONE_T, anchor="mt")
    y += ink_height(f_line, FUNNEL_LINE) + 44

    cta_h = 96
    for label, price in GOLD_CTAS:
        gold_rect_cta(d, (pad, y, w - pad, y + cta_h), label, f_cta, price=price)
        y += cta_h + 14

    url = "walksteadfast.com"
    url_y = h - 110
    draw_lt(d, cx, url_y, url, f_url, BONE_T, 1.6)
    return im


def write_notes() -> None:
    text = """# Cloth Store frames — Lane for Holt

Pick is **Cloth Store** (direction 1). Bone Page and Quiet Gold stay parked — not drawn.

Gold is fill on three rectangles only: Start the training, Get the ebook, Open the store. Title lockup STEADFAST / MEN is gold Playfair like the jacket. Placeholders are bone hairline cards, never gold, no prices, no “coming soon,” no stars.

Funnel URL: walksteadfast.com (purchased Porkbun 2026-09-01 to 2027-09-01). Host live. No working-name caption. Do not buy steadfastmen.com. No extra spend.

Files: home-mobile.png (1170×2532), app-chrome.png (1170×2532), funnel-frame.png (1080×1920). Re-run: python3 render_cloth_store.py. Press covers under book/art/press/*.png were not touched.

Navy cloth + plumb geometry imported from book/art/press/render_a_v2.py. Long copy sits on a bone sheet over navy chrome. Four marks stay words. Apps free: no IAP, ads, streaks, or badges.
"""
    path = OUT / "NOTES.md"
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path}")


def main() -> None:
    save_png(render_home(), OUT / "home-mobile.png", expect=MOBILE)
    save_png(render_app(), OUT / "app-chrome.png", expect=MOBILE)
    save_png(render_funnel(), OUT / "funnel-frame.png", expect=STORY)
    write_notes()


if __name__ == "__main__":
    main()
