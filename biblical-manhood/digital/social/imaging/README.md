# Steadfast social stills — INTERNAL

Parked 2026-09-01. Reach sends these to Jarvis. **Not public until Aaron signs.** Do not upload. Do not publish. No spend.

Cloth Store stills: navy cloth field, gold Playfair lockup, bone subtitle, locked patch plumb. Original RGB PNGs. No GenerateImage. No Aaron face. No home address. No Hawks / One Mission / Lewis art. No swords, seals, gym-bro, church-slide, or stock. No four-mark list on the banners. No fake reviews.

Source patch (do not redraw): `/workspace/biblical-manhood/digital/merch/art/patch-circle-cloth-store-navy-gold.png` (Aaron lock; rectangle is not the lock)  
Type/cloth: `book/art/press/render_a_v2.py` + `digital/cloth-store/render_cloth_store.py`  
Re-run: `python3 /workspace/biblical-manhood/digital/social/imaging/render_stills.py`

## Files

| File | Pixels | Use |
| --- | --- | --- |
| `avatar.png` | 1024×1024 RGB | Every platform avatar. Site logo-lockup, square-optimized (reads small). |
| `avatar-1024.png` | 1024×1024 RGB | Same pixels as `avatar.png`. |
| `youtube-banner.png` | 2560×1440 RGB | YouTube channel art. |
| `x-banner.png` | 1500×500 RGB | X header. |
| `linkedin-banner.png` | 1128×191 RGB | LinkedIn Company Page. Compact strip (URL · WES HART on one line). |
| `facebook-cover.png` | 1640×624 RGB | Facebook Page cover. |
| `reddit-banner.png` | 1920×384 RGB | Reddit community banner. |

Instagram and TikTok have no banner. Skip those.

Lockup on every banner: small locked patch + gold STEADFAST MEN + italic *The way of Godly Men* (Godly upright) + walksteadfast.com + Wes Hart small.

## Layout notes for Jarvis

- **YouTube safe zone.** Official center ~1546×423 inside 2560×1440 (x 507–2053, y 508.5–931.5). Lockup sits fully inside that box (~1264×236, ~141 px left/right and ~94 px top/bottom remaining). Desktop and mobile crop to the center 423-tall band; TV sees the full 2560×1440, which is quiet navy above and below. No type in the left/right TV/mobile crop. No yellow arrows.
- **Facebook Page.** Profile circle covers the bottom-left of the cover. Lockup is centered; patch bottom is ~y 432 of 624, so it should clear the usual desktop overlap. Mobile crops tighter — do not shift the lockup left.
- **LinkedIn Company** is 191 px tall. Type is compact so STEADFAST MEN stays readable. No creed stack.
- **X** and **Reddit** use the same lockup, scaled. Reddit has extra side navy on purpose.

Wes Hart is the author line. Four marks stay words in About files, not on these stills.

## LOCK 2026-09-15 (Aaron via Jarvis)

**Avatar / profile mark:** top-left logo from walksteadfast.com (`img/logo-lockup.jpg`).
Local: `logo-lockup-site.jpg`, square avatars `avatar.png` / `avatar-1024.png` (site lockup on navy).
Previous patch-plumb avatars saved as `*-patch-plumb-PREV.png`.
All seats: use site lockup for avatars. Banners/covers = book cover files (see Banner lock below). Old Cloth Store banners are *-PREV.

## LOCK 2026-09-15b (Aaron via Jarvis)

**Wallpapers / banners / covers:** locked Steadfast Men book cover
`book/art/press/cloth-store/cover-front-walksteadfast-locked-2026-09-14.png`
→ `youtube-banner.png`, `x-banner.png`, `facebook-cover.png`, `linkedin-banner.png`, `reddit-banner.png`, `wallpaper-book-cover.png`.
Old Cloth Store stills backed as `*-PREV.png`.

**Avatars:** site top-left lockup (`logo-lockup-site.jpg` → `avatar.png`).

## LOCK 2026-09-15c (Aaron via Jarvis — Loom)

**Avatar must read small.** Not a tiny unreadible crop of the wide site lockup.
Shipped: `avatar.png` / `avatar-1024.png` — site glyphs from `logo-lockup-site.png`, black field, STEADFAST + navy rule + MEN width-filled for 1024².
Pre-optimized: `avatar-pre-optimized-2026-09-15.png`.
Prompts / banner layout notes: `AVATAR-AND-BANNER-PROMPTS.md`.
**Banners:** Merc owns creative soft-crop render pass (not center-crop). Book cover hero only. No posts. No spend.

## Imagine pack 2026-09-15d (Loom → Merc → Holt → Jarvis)

Image 2.9 Quality prompts (YouTube first): `prompts/README.md`
- `prompts/01-avatar-1024.md`
- `prompts/02-youtube-banner-2560x1440.md`
- Layout boards in `prompts/layout-board-*.png`
Other platforms HOLD in `prompts/03-HOLD-other-platforms.md`.

## Aaron lock 2026-09-15 evening
Grok Imagine plate is the socials banner (youtube-banner-grok-locked.jpg → youtube-banner.png). Soft-crop PASS superseded; backup at youtube-banner-softcrop-BACKUP.png.
