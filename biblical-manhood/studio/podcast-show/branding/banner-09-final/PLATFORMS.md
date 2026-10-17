> **SUPERSEDED 2026-10-16.** Social banners are now locked to banner 09 "The walk" (logo-fixed): `aaronmaberry/steadfast` → `brand/social-banners-LOCKED/` (see `LOCKED.md`; source `studio/podcast-show/branding/banner-09-final/logo-fix/`). Older banner/cover/header references below are historical. No changes without Aaron sign-off.

# Banner-09 "The walk": platform files

Aaron locked banner-09 on 2026-10-03. Every file here is cut from one sharp master. Nothing has been uploaded.

## Status and files

| Platform | Profile | Status (per `digital/social/LIVE-LINKS.md` and the platform notes) | Banner slot | File to upload |
|---|---|---|---|---|
| YouTube | https://youtube.com/@steadfastwalk | Live since 2026-09-21. The current banner is the book, mug and lamp art. | Yes | `master-2560x1440.png` |
| X | https://x.com/steadfastwalk | Live since 2026-09-21. The current header is the book, mug and lamp crop. | Yes (header) | `x-header-1500x500.png` |
| Facebook Page | https://facebook.com/steadfastwalk | Live since 2026-09-21. The current cover is the book, mug and lamp crop. | Yes (cover) | `facebook-cover-1702x630.png` |
| LinkedIn company page | https://linkedin.com/company/steadfastwalk | Page is live (2026-09-22), but the banner is parked: LinkedIn showed "Cover image upload failed" (`linkedin/shot-banner-fail.png`). | Yes (cover) | `linkedin-cover-1512x256.png` |
| Reddit | https://reddit.com/user/steadfastwalk | Profile is live (2026-09-22), but the avatar and banner are parked: Reddit returned server errors on branded uploads (`reddit/PROFILE.md`). | Yes (profile banner) | `reddit-banner-1920x384.png` |
| Instagram | https://instagram.com/steadfastwalk | Live | No banner | none |
| TikTok | https://tiktok.com/@steadfastwalk | Bio is live. The avatar was set through the app. | No banner | none |

## Sizes and sources

- **YouTube: 2560x1440.** The safe area is 1546x423 in the center, and the file must be 6 MB or less. Source: YouTube Help, "Manage your channel branding" (support.google.com/youtube/answer/2972003). The master is 3.9 MB.
- **X: 1500x500.** Source: X Help, profile customization (help.x.com). X warns that about 60 px may be cropped at the top and bottom, and the round profile photo covers the bottom-left corner. All text sits between y 174 and 326, and the man and boy start at x 439, right of the avatar zone (x 0-420).
- **Facebook Page cover: 1702x630.** That is 2x the 851x315 size Facebook Help recommends. Source: Facebook Help, "Facebook Page profile picture and cover photo dimensions" (facebook.com/help/125379114252045). Facebook says the profile picture covers the left side, that the cover may be cropped and resized for different screens, and that PNG is better for covers with text. Meta publishes no pixel safe zone, so the text is kept in the middle (x 871-1349), clear of the bottom-left avatar and the bottom-center mobile avatar. Facebook's help page also describes left-aligned 16:9 (computer) and 2.4:1 (mobile) display frames, so check the cover in Facebook's drag-to-reposition preview on both views before saving.
- **LinkedIn company cover: 1512x256,** PNG or JPEG, 3 MB or less. Source: LinkedIn Help, "Image specifications for your LinkedIn Pages and Career Pages" (linkedin.com/help/linkedin/answer/a563309). That page lists 1512x256 as both the minimum and the recommended size as of 2026. The older 1128x191 figure is a display size, falls below the current minimum, and is no longer listed. LinkedIn says to keep key details away from the edges, especially the lower-right corner. The logo overlaps the lower-left. Text sits at x 862-1158.
- **Reddit profile banner: 1920x384.** Reddit's Help Center gives no official size for profile banners. 1920x384 (5:1, 10 MB or less) is the size most guides agree on, and it is also Reddit's large size for community banners. The mobile app crops the sides, so all text sits in the center half (x 955-1425).

## Notes

- **Cropping.** The man and boy stay in every cut, and nothing is flipped or recolored. At LinkedIn's 6:1 and Reddit's 5:1 shapes, the full photo width only gives enough height to show them from the head to about the waist. That is a limit of those strip shapes.
- **Checks.** Before saving each file, the script confirms that the text sits inside the safe zone and that neither the text nor the figures touch an avatar or logo zone. The results are in `_build/cuts.json`.
- **File sizes.** Every file is under its platform's size limit.
- **Rebuild.** Run `python3 _build/render_final.py`, then `_build/proof.py` and `_build/sharpness.py`.

## Master and sharpness

- **Source.** The largest copy of the photo anywhere on the box, or on the live site, is 1168x784 (`steadfast-fourmarks/img/walk.jpg`, plus identical copies). It is not in the Grok downloads or /workspace/dl.
- **Upscale.** Real-ESRGAN x4plus ran on the CPU using the official weights (`/workspace/tools/esrgan/`), producing 4672x3136. That was scaled down to each size with a light unsharp mask. The framing is the same as banner-09. The text was redrawn sharp at each final size from the Geist font.
- **Laplacian variance, old banner-09 → new master:**
  - Full frame: 98 → 323 (3.3x)
  - Man, boy and trunk at 100%: 19 → 311
  - Oak crown at 100%: 41 → 494
  - Fence and field at 100%: 6.7 → 19.3
- **Side-by-side check.** `sharpness-compare-100pct.png` shows 100% crops of both versions.
- **Trade-off.** Real-ESRGAN clears the JPEG blocks and sharpens the edges, but it smooths the grass and gravel a little. The Tenengrad gradient score in the field area dropped from 17 to 12, because the old JPEG noise is gone.
