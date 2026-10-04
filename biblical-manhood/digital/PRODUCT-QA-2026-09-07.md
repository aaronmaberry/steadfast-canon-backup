# Product QA — 2026-09-07

Holt · Website HOT · Origin `bc-05c19cb9` · No spend · No publish · No Aaron dump

Evidence: locked Image 2.0 typesets (truth), INNER-DESTINATIONS.md, Origin last assistant reports (#88–#119) including two visual QA passes (`bc-3309e541`, `bc-0d8469ca`). Live site not reachable from this box (`127.0.0.1:43173` down here; no public host).

## Overall verdict: PASS on letter · BLOCKED on public host

| # | Item | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Home/funnel vs Cloth Store locked typesets | **PASS** | Navy/bone; three golds $79/$14/$89; quiet line two lines; Four Marks wrap; MEDIA YouTube+Podcast; Downloads/Devotionals/Shop plain; Shop empty; socials unclickable. Origin #112/#117/#119 + typeset PNGs. Phone quiet lines under golds on navy = locked mobile typeset, not a defect. |
| 2 | `/downloads` one line only | **PASS** | Origin #92/#117: “Purchased training and ebook files live in Account.” No packets/sample cards/worksheets. |
| 3 | Devotionals → `/daily` one day; no fourth Daily tab | **PASS** | Origin #92/#117: one sit-down (Micah 6:8). App tabs stay Home/Training/Store. |
| 4 | App Training chrome | **PASS** | Locked `app-chrome-typeset.png` + Origin #88/#112: Introduction, Week 1 of 24, gold Get the training; tabs Home/Training/Store. |
| 5 | No 01–24 list; Stripe unarmed; legal DRAFT | **PASS** | Origin #92/#117/#119: Training short letter; Stripe unarmed; legal/`/refunds` DRAFT under `[LEGAL ENTITY TO CONFIRM]`; wallet-card 404. |
| 6 | Mobile-first / iOS Safari | **PASS** | Origin #94–#106: mobile-first stated; Safari hardening (safe-area, 44px taps, no 100vw/mix-blend grain). Locked mobile + app typesets. Not re-verified on a physical device this pass. |
| 7 | Public preview hostname | **BLOCKED** | None. Only agent-local `http://127.0.0.1:43173` (not public). No Vercel/`*.vercel.app`/Origin preview host. Porkbun park stays. Do not point DNS. |

## Out of scope / open
- Lane Image 2.0 photoreal stills (hanging/standing plumb, navy cloth, bone paper): flagged, empty slots not rendered. No cheaper gen.
- Aaron page sign before full publish. Auth/Stripe/DNS wait.

## Pace status line (names only)
**Cloth Store letter PASS · public host BLOCKED · Porkbun park · Stripe unarmed · Lane stills open**
