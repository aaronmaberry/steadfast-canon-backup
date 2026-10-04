# Grok Build job — Steadfast website + apps full cleanup pass
**Date:** 2026-09-21  
**From:** Jarvis / Aaron Maberry  
**Authority:** Aaron ordered: pull design rules, clean site + apps, max fixes, push Origin, republish Vercel.

---

## Goal
Run the **entire** Steadfast digital surface (marketing website + companion Expo apps) through one disciplined cleanup and fix pass. Ship Fortune 500 quality. Push to the existing **Origin** repo. Redeploy on the existing **Vercel** project for `walksteadfast.com`. Do **not** invent a second stack.

## Source of truth (read first)
Canon / rules on the shared box (and mirrored in Origin when present):
- `/workspace/biblical-manhood/CANON.md`
- `/workspace/biblical-manhood/digital/STACK.md`
- `/workspace/biblical-manhood/style/GRAPHICS.md`
- `/workspace/biblical-manhood/style/UNSLOP.md` (global — all prose)
- `/workspace/biblical-manhood/digital/LOOK-DIRECTIONS.md` (Cloth Store is the locked digital look)
- `/workspace/biblical-manhood/digital/social/BIO.md` + `ABOUT.md` + `LIVE-LINKS.md`
- House mark: `/workspace/biblical-manhood/digital/social/imaging/avatar.png` (site top-left logo-lockup on black — STEADFAST / MEN). Prefer also `logo-lockup-LIVE.jpg` from walksteadfast.com.
- Coffee-cup / book banner (where a banner exists): `imaging/youtube-banner-fullbleed-LOCKED.png`

Live hub: **https://walksteadfast.com**  
Handle / brand: **Steadfast Men** · **steadfastwalk** · author line **Wes Hart**

Origin: prefer the Steadfast digital / Cloth Store Origin repo already wired to Vercel (historical cloud agent `bc-05c19cb9`; canon KB also at Origin `aaron-maberry/tmp-0400534119012e43` / steadfast-canon). **Find the repo that actually deploys walksteadfast.com on Vercel and work only there.** Do not create a parallel site.

Local scratch if needed for comparison only: `/workspace/steadfast-digital` — Origin remains source of truth.

---

## Hard locks (never break)
1. **No spend.** No new paid SaaS, no paid fonts, no stock, no ads, no Stripe arming, no App Store / Play submit.
2. **No posts** on social. This job is website + apps only.
3. **Stripe stays unarmed.** Checkout may exist as UI, but do not enable live charges.
4. **Original only.** No church templates, no ministry find-replace, no stock men, no Hawks / One Mission / Lewis art.
5. **UNSLOP** on every string you touch (no em dashes, no AI vocab, plain speech).
6. **Cloth Store palette:** navy `#0B1F38` · gold `#E3C572` · bone `#E6DDCC` (also seen as `#0B1F38` / `#E3C572` / `#E6DDCC`). Gold is earned, not decoration everywhere.
7. **Mobile-first.** Must work on iOS Safari + major desktop browsers.
8. **Apps are free companions.** Expo iOS/Android (one codebase). No IAP. Paid CTAs open walksteadfast.com.
iOS app lane was paused earlier — **fix and harden the existing Expo code; do not submit to App Store / Play.**
9. **No home street address** in UI, footers, legal, or checkout.
10. Domain collision: never buy or brand as steadfastmen.com (Burnett). Ours is walksteadfast.com.

---

## Design bar
Fortune 500 craft (Apple / Aesop / Stripe / Linear / Shinola as study — then beat them at being Steadfast). If a screen could be any men's ministry site with a find-replace, kill it.

- Restraint. Cut until it hurts.
- Real type scale. Playfair / Playfair Display for titles; one clean sans for UI; generous leading.
- Image 2.9 Quality / Cloth Store stills only for any new art. Prefer existing locked assets over generating.
- Motion responds; it does not perform.
- Fast. Slow is cheap.
- Same chrome language across desktop, mobile web, iOS, Android.

---

## What to do (in order)
1. **Inventory** the Origin repo that powers walksteadfast.com: routes, components, app (Expo) tree, env, Vercel project link.
2. **Audit** against STACK + GRAPHICS + LOOK (Cloth Store) + UNSLOP + BIO/ABOUT. List concrete defects (layout, type, spacing, broken links, wrong mark, church-template residue, a11y, perf, SEO basics, mobile Safari bugs).
3. **Fix max priority issues** end-to-end:
   - Wrong / outdated logo → site lockup house mark (`imaging/avatar.png` / LIVE logo-lockup).
   - Hero / OG / banners → prefer coffee-cup / book full-bleed locked art where a banner belongs; never SAFEZONE postage stamps.
   - Copy → BIO short/full and ABOUT; strip slop.
   - Navigation / CTAs → hub first; social links from LIVE-LINKS only for profiles that are LIVE.
   - Dead links, 404s, placeholder junk that looks shipped.
   - Mobile Safari layout bugs, overflow, tap targets.
   - Accessibility: contrast, focus, alt text on marks.
   - Perf: images sized, no obvious bloat.
4. **Apps:** align Expo chrome to Cloth Store; deep-link paid actions to walksteadfast.com; no IAP; no store metadata submit.
5. **Tests / build:** `lint` + production build must pass. Fix what you break.
6. **Commit** on a clear branch (e.g. `fix/site-apps-fortune500-2026-09-21`) with honest messages.
7. **Open / update PR on Origin** (or push main only if that is already how this Vercel project deploys — prefer PR if the repo uses PRs).
8. **Vercel:** trigger / confirm production deploy for walksteadfast.com from that commit. Do not change billing plan. Do not add paid add-ons.
9. **Report back to Jarvis** with: repo URL, branch/PR, Vercel deploy URL, before/after notes, remaining risks, anything that still needs Aaron (DNS, Apple, Stripe).

---

## Out of scope
- Social posting, ads, merch inventory, Stripe live keys, App Store / Play submission, SOS/LLC filings, Options trading, book PDF rewrite.
- Renaming the company away from Steadfast Men / walksteadfast.com.
- Buying domains or fonts.

## Done means
- Origin has the cleaned code.
- Vercel production for walksteadfast.com reflects the pass.
- Site + apps meet Cloth Store + Fortune 500 bar on a hard look (mobile + desktop).
- Written report to Jarvis with links and residual risks.
- Zero spend. Stripe still unarmed. No store submit. No social posts.
