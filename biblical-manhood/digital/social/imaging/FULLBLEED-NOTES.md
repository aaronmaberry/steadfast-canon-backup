> **SUPERSEDED 2026-10-16.** Social banners are now locked to banner 09 "The walk" (logo-fixed): `aaronmaberry/steadfast` → `brand/social-banners-LOCKED/` (see `LOCKED.md`; source `studio/podcast-show/branding/banner-09-final/logo-fix/`). Older banner/cover/header references below are historical. No changes without Aaron sign-off.

# Full-bleed LOCAL composites — Steadfast Men YouTube

Jarvis Imagine → `youtube-banner-fullbleed-vN.png`. **Locals (no API):** `youtube-banner-fullbleed-local-vN.png`.

- **Source:** `youtube-banner-grok-locked-NEW.jpg` (1168×784 locked)
- **Canon hold:** did not overwrite `youtube-banner.png` or `avatar.png`
- **Target:** exact 2560×1440 RGB PNG, full-bleed (no postage-stamp / letterbox bars)
- **Safe zone:** ≈1546×423 at x≈507–2053, y≈509–932
- **Geometry:** Full book height > safe 423px — key STEADFAST/MEN targeted into safe; full stack legible on desktop/TV.
- **Extend method:** wood + void atmosphere fills from source patches (blurred/grained). **No mirrored lamp tiles.**

## local-v1
- **File:** `youtube-banner-fullbleed-local-v1.png` / `youtube-banner-fullbleed-local-v1-safe-proof.png`
- **Method:** LANCZOS×2.05; focus STEADFAST→safe (~1180,600); wood/void atmosphere fill (no lamp mirror); book+mug+lamp large full-bleed
- **Meta:** `{'note': 'unchanged from prior pass scale=2.05 target=(1180,600)'}`
- **Title in safe:** key=YES; stack mid=YES — `bbox=(766, 423, 1554, 1007) cx=1160 cy=715 steadfast_cy=514 key_in=True mid_in=True`
- **Edge means:** `{'top': 3.61, 'bot': 9.12, 'left': 6.09, 'right': 6.99}`

## local-v2
- **File:** `youtube-banner-fullbleed-local-v2.png` / `youtube-banner-fullbleed-local-v2-safe-proof.png`
- **Method:** LANCZOS×2.20; STEADFAST→safe (~1200,580); atmosphere wood/void fill no lamp-mirror; punchier crop
- **Meta:** `{'scale': 2.2, 'paste_x': -837, 'paste_y': 349, 'dst': (0, 349, 1733, 1440), 'hero': (2570, 1725), 'focus_src': (926.0, 105.0), 'target': (1200, 580)}`
- **Title in safe:** key=YES; stack mid=YES — `bbox=(754, 390, 1603, 980) cx=1178 cy=685 steadfast_cy=482 key_in=True mid_in=True`
- **Edge means:** `{'top': 3.55, 'bot': 11.31, 'left': 5.77, 'right': 6.99}`

## local-v3
- **File:** `youtube-banner-fullbleed-local-v3.png` / `youtube-banner-fullbleed-local-v3-safe-proof.png`
- **Method:** LANCZOS×2.00; STEADFAST→safe (~1160,560); atmosphere fill; balanced scale between v1 and v2
- **Meta:** `{'scale': 2.0, 'paste_x': -692, 'paste_y': 350, 'dst': (0, 350, 1644, 1440), 'hero': (2336, 1568), 'focus_src': (926.0, 105.0), 'target': (1160, 560)}`
- **Title in safe:** key=YES; stack mid=YES — `bbox=(760, 388, 1525, 977) cx=1142 cy=682 steadfast_cy=480 key_in=True mid_in=True`
- **Edge means:** `{'top': 3.64, 'bot': 8.26, 'left': 5.98, 'right': 6.99}`

## Recommendation (Holt gate)
**Prefer `youtube-banner-fullbleed-local-v1.png`.** Best balance: STEADFAST/MEN keyed into mobile safe, mug+lamp still in frame, full-bleed wood/atmosphere without letterbox or lamp-mirror artifacts. Use **local-v2** for punchier larger crop; **local-v3** for a middle scale.
