#!/usr/bin/env python3
"""Internal parked social stills for Steadfast Men. Cloth Store lockup. Not public."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw

PRESS = Path("/workspace/biblical-manhood/book/art/press")
CLOTH = Path("/workspace/biblical-manhood/digital/cloth-store")
sys.path.insert(0, str(PRESS))
sys.path.insert(0, str(CLOTH))

from render_a_v2 import (  # noqa: E402
    BONE,
    F,
    GOLD,
    ink_height,
    navy_cloth,
    tracked_width,
)

OUT = Path("/workspace/biblical-manhood/digital/social/imaging")
PATCH_PATH = Path("/workspace/biblical-manhood/digital/merch/art/patch-circle-cloth-store-navy-gold.png")  # Aaron lock

NAVY_T = (11, 31, 56)
GOLD_T = GOLD
BONE_T = BONE
DIM_BONE = (168, 164, 154)


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


def load_patch() -> Image.Image:
    """Locked patch plate, rounded to merrow. Do not redraw."""
    raw = Image.open(PATCH_PATH).convert("RGBA")
    w, h = raw.size
    m = 10
    raw = raw.crop((m, m, w - m, h - m))
    w, h = raw.size
    radius = int(round(0.088 * w))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    raw.putalpha(mask)
    return raw


PATCH = None


def patch_rgba() -> Image.Image:
    global PATCH
    if PATCH is None:
        PATCH = load_patch()
    return PATCH


def scaled_patch(target_h: int) -> Image.Image:
    src = patch_rgba()
    tw = max(1, int(round(target_h * (src.size[0] / src.size[1]))))
    th = max(1, int(target_h))
    return src.resize((tw, th), Image.Resampling.LANCZOS)


def paste_patch(im: Image.Image, patch: Image.Image, x: float, y: float) -> None:
    px, py = int(round(x)), int(round(y))
    im.paste(patch, (px, py), patch)


def draw_left_tracked(draw, x, y_top, text, font, fill, tracking) -> float:
    xx = x
    for ch in text:
        draw.text((xx, y_top), ch, font=font, fill=fill, anchor="lt")
        xx += font.getlength(ch) + tracking
    return y_top + ink_height(font, text)


def draw_godly_left(draw, x, y_top, italic, roman, fill) -> float:
    """Godly upright so the o cannot read as a degree. Matches cloth-store."""
    left, word, right = "The way of ", "Godly", " Men"
    ascent = italic.getmetrics()[0]
    yb = y_top + ascent
    xx = x
    draw.text((xx, yb), left, font=italic, fill=fill, anchor="ls")
    xx += italic.getlength(left)
    draw.text((xx, yb), word, font=roman, fill=fill, anchor="ls")
    xx += roman.getlength(word)
    draw.text((xx, yb), right, font=italic, fill=fill, anchor="ls")
    return y_top + max(ink_height(italic, left + right), ink_height(roman, word))


def godly_width(italic, roman) -> float:
    left, word, right = "The way of ", "Godly", " Men"
    return italic.getlength(left) + roman.getlength(word) + italic.getlength(right)


def lockup_fonts(title_size: float, sub_size: float, url_size: float, auth_size: float):
    f_title = F("PlayfairDisplay-Bold.ttf", title_size)
    f_sub = F("EBGaramond-Italic.ttf", sub_size)
    f_sub_roman = F("PlayfairDisplay-Regular.ttf", sub_size)
    f_url = F("LibreFranklin-Medium.ttf", url_size)
    f_auth = F("LibreFranklin-Medium.ttf", auth_size)
    return f_title, f_sub, f_sub_roman, f_url, f_auth


def footer_width(f_url, f_auth, compact: bool) -> float:
    uw = f_url.getlength("walksteadfast.com")
    aw = tracked_width(f_auth, "WES HART", 0.12 * f_auth.size)
    if compact:
        dot = f_url.getlength("  ·  ")
        return uw + dot + aw
    return max(uw, aw)


def type_column_size(
    f_title, f_sub, f_sub_roman, f_url, f_auth, title_tr, gap_ts, gap_su, gap_ua, compact
):
    title = "STEADFAST MEN"
    tw = tracked_width(f_title, title, title_tr)
    th = ink_height(f_title, title)
    sw = godly_width(f_sub, f_sub_roman)
    sh = max(ink_height(f_sub, "The way of  Men"), ink_height(f_sub_roman, "Godly"))
    fw = footer_width(f_url, f_auth, compact)
    if compact:
        fh = max(
            ink_height(f_url, "walksteadfast.com"),
            ink_height(f_auth, "WES HART"),
        )
        height = th + gap_ts + sh + gap_su + fh
    else:
        uh = ink_height(f_url, "walksteadfast.com")
        ah = ink_height(f_auth, "WES HART")
        height = th + gap_ts + sh + gap_su + uh + gap_ua + ah
    width = max(tw, sw, fw)
    return width, height


def draw_type_column(
    draw,
    x,
    y,
    f_title,
    f_sub,
    f_sub_roman,
    f_url,
    f_auth,
    title_tr,
    gap_ts,
    gap_su,
    gap_ua,
    compact,
):
    y = draw_left_tracked(draw, x, y, "STEADFAST MEN", f_title, GOLD_T, title_tr)
    y = draw_godly_left(draw, x, y + gap_ts, f_sub, f_sub_roman, BONE_T)
    y = y + gap_su
    if compact:
        draw.text((x, y), "walksteadfast.com", font=f_url, fill=BONE_T, anchor="lt")
        xx = x + f_url.getlength("walksteadfast.com")
        draw.text((xx, y), "  ·  ", font=f_url, fill=DIM_BONE, anchor="lt")
        xx += f_url.getlength("  ·  ")
        draw_left_tracked(draw, xx, y, "WES HART", f_auth, DIM_BONE, 0.12 * f_auth.size)
    else:
        draw.text((x, y), "walksteadfast.com", font=f_url, fill=BONE_T, anchor="lt")
        y = y + ink_height(f_url, "walksteadfast.com") + gap_ua
        draw_left_tracked(draw, x, y, "WES HART", f_auth, DIM_BONE, 0.12 * f_auth.size)


def compose_banner(
    w: int,
    h: int,
    *,
    seed: int,
    patch_h: int,
    title_size: float,
    sub_size: float,
    url_size: float,
    auth_size: float,
    gap_patch: int,
    gap_ts: int,
    gap_su: int,
    gap_ua: int,
    pad: int,
    safe=None,
    compact=False,
) -> Image.Image:
    im = navy_cloth(w, h, seed=seed)
    d = ImageDraw.Draw(im)

    patch = scaled_patch(patch_h)
    pw, ph = patch.size
    f_title, f_sub, f_sub_roman, f_url, f_auth = lockup_fonts(
        title_size, sub_size, url_size, auth_size
    )
    title_tr = 0.055 * title_size
    col_w, col_h = type_column_size(
        f_title,
        f_sub,
        f_sub_roman,
        f_url,
        f_auth,
        title_tr,
        gap_ts,
        gap_su,
        gap_ua,
        compact,
    )

    group_w = pw + gap_patch + col_w
    group_h = max(ph, col_h)

    if safe is not None:
        sx, sy, sw, sh = safe
        gx = sx + (sw - group_w) / 2.0
        gy = sy + (sh - group_h) / 2.0
        gx = max(sx + pad, min(gx, sx + sw - pad - group_w))
        gy = max(sy + pad, min(gy, sy + sh - pad - group_h))
        assert gx >= sx - 0.5 and gy >= sy - 0.5
        assert gx + group_w <= sx + sw + 0.5
        assert gy + group_h <= sy + sh + 0.5
        print(
            f"  youtube safe margins L={gx - sx:.0f} R={sx + sw - (gx + group_w):.0f} "
            f"T={gy - sy:.0f} B={sy + sh - (gy + group_h):.0f}"
        )
    else:
        gx = (w - group_w) / 2.0
        gy = (h - group_h) / 2.0
        gx = max(pad, min(gx, w - pad - group_w))
        gy = max(pad, min(gy, h - pad - group_h))

    px = gx
    py = gy + (group_h - ph) / 2.0
    tx = gx + pw + gap_patch
    ty = gy + (group_h - col_h) / 2.0

    paste_patch(im, patch, px, py)
    draw_type_column(
        d,
        tx,
        ty,
        f_title,
        f_sub,
        f_sub_roman,
        f_url,
        f_auth,
        title_tr,
        gap_ts,
        gap_su,
        gap_ua,
        compact,
    )

    print(f"  lockup {int(group_w)}x{int(group_h)} at ({int(gx)},{int(gy)}) on {w}x{h}")
    return im


def render_avatar(size: int = 1024) -> Image.Image:
    im = navy_cloth(size, size, seed=17)
    target_w = int(round(size * 0.74))
    src = patch_rgba()
    target_h = int(round(target_w * (src.size[1] / src.size[0])))
    patch = src.resize((target_w, target_h), Image.Resampling.LANCZOS)
    x = (size - target_w) / 2.0
    y = (size - target_h) / 2.0
    paste_patch(im, patch, x, y)
    return im


def youtube_safe():
    # Official YouTube channel-art safe zone ~1546x423, centered in 2560x1440.
    W, H = 2560, 1440
    sw, sh = 1546, 423
    sx = (W - sw) / 2.0
    sy = (H - sh) / 2.0
    return (W, H), (sx, sy, sw, sh)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    avatar = render_avatar(1024)
    save_png(avatar, OUT / "avatar.png", expect=(1024, 1024))
    save_png(avatar.copy(), OUT / "avatar-1024.png", expect=(1024, 1024))

    (yw, yh), safe = youtube_safe()
    yt = compose_banner(
        yw,
        yh,
        seed=19,
        patch_h=236,
        title_size=94,
        sub_size=36,
        url_size=22,
        auth_size=16,
        gap_patch=48,
        gap_ts=12,
        gap_su=14,
        gap_ua=8,
        pad=20,
        safe=safe,
    )
    save_png(yt, OUT / "youtube-banner.png", expect=(2560, 1440))

    xban = compose_banner(
        1500,
        500,
        seed=21,
        patch_h=210,
        title_size=84,
        sub_size=32,
        url_size=20,
        auth_size=15,
        gap_patch=44,
        gap_ts=10,
        gap_su=14,
        gap_ua=8,
        pad=36,
    )
    save_png(xban, OUT / "x-banner.png", expect=(1500, 500))

    li = compose_banner(
        1128,
        191,
        seed=23,
        patch_h=148,
        title_size=52,
        sub_size=22,
        url_size=14,
        auth_size=13,
        gap_patch=28,
        gap_ts=5,
        gap_su=7,
        gap_ua=4,
        pad=10,
        compact=True,
    )
    save_png(li, OUT / "linkedin-banner.png", expect=(1128, 191))

    fb = compose_banner(
        1640,
        624,
        seed=25,
        patch_h=240,
        title_size=96,
        sub_size=36,
        url_size=22,
        auth_size=16,
        gap_patch=48,
        gap_ts=12,
        gap_su=16,
        gap_ua=8,
        pad=40,
    )
    save_png(fb, OUT / "facebook-cover.png", expect=(1640, 624))

    rd = compose_banner(
        1920,
        384,
        seed=27,
        patch_h=196,
        title_size=78,
        sub_size=30,
        url_size=18,
        auth_size=14,
        gap_patch=40,
        gap_ts=8,
        gap_su=12,
        gap_ua=6,
        pad=28,
    )
    save_png(rd, OUT / "reddit-banner.png", expect=(1920, 384))


if __name__ == "__main__":
    main()
