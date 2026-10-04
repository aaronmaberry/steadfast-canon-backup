# Walk Steadfast YouTube banner concepts

Made 2026-10-03. Ten 2560x1440 mockups for @steadfastwalk. Nothing is uploaded and nothing on YouTube was changed. The live banner is still `digital/social/youtube/youtube-banner.png`.

Every banner uses the same wordmark: a small tracked WALK over STEADFAST, with the open-triangle A from the walksteadfast.com house mark, set in Geist (the site font), with the site accent color #8b9cff for the rule and the small lines. All type sits inside the 1546x423 safe area. The render script fails if any text box falls outside it. `contact-sheet.png` shows all ten, with the safe area (red) and the desktop band (yellow) marked.

| # | File | Concept |
|---|------|---------|
| 01 | banner-01.png | The table. The empty studio from the site (dark acoustic wall, two boom mics, two mugs, a wood table, two empty chairs), with the wordmark between the mics. "Pull up a chair." and "New episodes Tuesday and Friday". |
| 02 | banner-02.png | Type only. A near-black field with one large faint house-mark triangle behind a big wordmark. "A podcast for men who stay" and walksteadfast.com / @steadfastwalk. |
| 03 | banner-03.png | Hill Country oak at dusk, with a fence line and hills. The wordmark sits in the sky to the right of the tree. "A podcast for men who stay" and "From the Texas Hill Country". |
| 04 | banner-04.png | Bible and coffee in line art. An open Bible between two steaming mugs, drawn in the accent color on black, with the wordmark to the right. "Coffee and Scripture" and "Tuesday and Friday". |
| 05 | banner-05.png | The road. A two-lane country road running into a sunset, with WALK STEADFAST on one line across the sky. "New episodes Tuesday and Friday" and @steadfastwalk. |
| 06 | banner-06.png | Dark studio. A close shot of a single boom mic against an acoustic wall, with the wordmark on the left. "A video podcast", "With Wes Hart and Jonathon" and a small TUE / FRI. |
| 07 | banner-07.png | Brand-color field. Solid site periwinkle with faint nested triangles, with the wordmark and rule in near-black. "A podcast for men who stay" and walksteadfast.com. |
| 08 | banner-08.png | Schedule strip. The wordmark on the left. On the right are two schedule cards: Tuesday for the main episode, Friday for Field Notes. |
| 09 | banner-09.png | The walk. A man and a boy, seen from behind as dark shapes, walking a gravel ranch road under a live oak at dusk. "A podcast for men who stay" and "Tuesday and Friday". |
| 10 | banner-10.png | Continuity. The live book, mug and lamp art (full-bleed v1), with the new wordmark in the dark left side. "Now a video podcast" and "Tuesday and Friday". |

## Notes

- No real people. Only banner 09 shows people, as two unlit figures from behind. No faces of Wes or Jonathon are used (the site's hero-studio photo was left out on purpose).
- Banners 01, 03, 05, 06 and 09 use photos from the walksteadfast.com image folder (`steadfast-fourmarks/img/`), which are only 1168 px wide. They were scaled up about 2.2x, so they look soft at full size. Once Aaron picks, re-render the chosen one from a larger source image before upload. Banners 02, 04, 07 and 08 are drawn entirely in code and are sharp at any size. Banner 10 uses the 2560 px live art.
- No paid image generation was used. Everything was put together locally with PIL.
- Taglines checked against the unslop rules (no em dashes, no rule-of-three lines, plain words).
- Rebuild: `python3 _build/render.py [numbers]`, then `python3 _build/contact.py`.
