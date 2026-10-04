# Steadfast merch — POD vendor memo

Internal. Holt, 2026-09-01. Research only. No signup, no spend, no publish.

Brand: **Steadfast Men** / *The way of Godly Men*. Site: `walksteadfast.com`. Look: Cloth Store (navy `#0B1F38` · gold `#E3C572` · bone `#E6DDCC`). Stack: Next.js on Vercel, Stripe later. Shop on the site is a placeholder (`/shop`). Training + ebook are the live money path; merch is not.

Need: t-shirts, coffee mugs, later challenge coins / “man coins”. No inventory. Order prints and ships to the buyer.

---

## 1. Recommendation (shirts + mugs)

**Primary vendor: Printful.** One partner for both tees and mugs.

Why this brand, not the cheap-catalog default:

| Need | Printful |
| --- | --- |
| Quality | In-house plants, not a marketplace of random printers. Bella + Canvas 3001 (Navy is in the 2026 color run) is adult cloth, not Gildan youth-group. |
| White-label | Packing slip and carton carry **no Printful mark**. Logo + custom message on the slip are free. Inside-neck labels exist (~$0.99–$2.49). Partner/backup plants skip custom slips — keep US routing on owned facilities. |
| US ship | US plants. Observed 2026: first tee ~$4.69, extra ~$2.20; first 11 oz mug ~$6.49, extra ~$3.50. Fulfillment typically 2–5 business days then carrier. Mixed tee+mug can split shipments. |
| Fees | Free plan: $0/mo, pay per order. Optional Growth $24.99/mo (discounts; waived after ~$12k trailing Printful sales). No listing fee. Stripe (later) is 2.9% + $0.30 — that is ours, not Printful’s. |
| API | Mature Orders + Catalog + Mockup + Shipping-rate APIs. Private token. Draft orders, then confirm after Stripe webhook. Packing-slip fields overridable per order. This is the path that fits Next.js on Vercel. |
| Colors | Navy 3001 for the jacket field. Bone-adjacent blanks (Natural / Cream / Heather Dust — pick at mockup time, do not invent a hex match). Mug: white glossy 11/15 oz, or white with color-inside (navy handle if the 2026 catalog still lists it). Gold lives in the **print**, not the blank. |
| Policy | Printful Acceptable Content (updated 2024, still posted 2026) bans hate *against* religion, illegal content, and IP theft. Original Steadfast Men art is fine. Do not print Hawks / One Mission / other ministries as product. Do not use other orgs’ marks. |

**Do not pick these as primary**

- **Printify** — cheapest bases, real API, but quality is the print *provider*, not Printify. Branding (inserts, neck labels, packing identity) is provider-gated. Fine as a backup printer later; wrong as the face of a quality-first men’s brand.
- **Gelato** — white-label cartons, no invoice in the box, strong local-print network. Packing-slip branding is thin vs Printful. Best if we ever ship a lot of EU. US quality/consistency is partner-dependent. Inserts/labels are Gelato+ API extras, not the default.
- **Fourthwall** — creator store + POD in one. $0/mo, no platform fee on physical, 2.9% + $0.30 cards. Checkout is **theirs** (they are merchant of record). 5% platform fee on digital on the free plan — that would tax training + ebook if we ever merged catalogs. Official Next.js/Vercel template exists, but it redirects to Fourthwall checkout. Fights “the website is the store” and the locked Stripe-later path. Park it.
- **Shopify + Printful/SPOD/CustomCat** — Shopify Basic is ~$29/mo annual / ~$39 monthly (2026). Second storefront, second checkout, extra platform tax. SPOD is fast and cheap (48-hour production) with weaker branding and more volume look. CustomCat is US DIGISOFT, white-label carton, **no** custom slips/inserts/hang tags. All of these assume we pay for Shopify. We do not.
- **Printful Quick Stores / Printify Pop-Up** — vendor-hosted shops. Off-brand. Ignore.

**Blank to mock later (not live):** Bella + Canvas 3001, Navy, front print only. Small gold plumb + STEADFAST MEN lockup. No swords, lions, camo, neon, “Jesus is my homeboy” type. Mug: 11 oz white glossy or navy-inside, same lockup, bone field.

---

## 2. Honest coin path

**Challenge coins are not print-on-demand.** There is no Printful/Printify/Gelato equivalent where a paid web order mints one coin and drops it to the buyer the same week with an API.

What the named shops actually are (2026):

| Shop | What they are | Dropship? |
| --- | --- | --- |
| **GS-JJ** | China factory. No MOQ (1 pc). Mold fee on true die-struck; 2-year mold storage. Proof in ~12 hours. Production 3–30 days, rush 24-hour *printed* coins. Ships US. Quoting site, not a fulfillment API. | Manual. You place the order; they ship to an address you give. Not “buyer pays → coin appears.” |
| **PinProsPlus** | US-facing pin/coin shop since 2008. Free design, US shipping marketed as free. ~15 business days. Reviews note China production on some lots. Quote → proof → batch. | Manual. |
| **ChallengeCoinKing** and peers | Same class: custom manufacturer, quote-driven. | Manual. |
| **Signature Coins** (US) | Closest to “order one.” Texture-*printed* stock coins, no MOQ, made in USA, 2–3 weeks. Traditional fully-custom die-struck still has a ~50 min. This is a printed token, not a heavy enamel challenge coin. | Still a custom order, not an API. |
| **The Medal Foundry** | US-made, no min, claims blind dropship + your packing slip. Quote program, not POD software. | Closest *process* to dropship. Still not an order-creates-item API. |

So: a live `/shop` coin SKU would either (a) lie about ship time, (b) require us to hold a small batch (inventory — forbidden), or (c) take 2–4 weeks with a human forwarding each Stripe order to a factory. None of that is v1.

**Later path, when Aaron wants coins:**

1. Lane locks a plumb + four-marks die. Gold field, navy enamel, bone lettering. Not a cross, not a lion.
2. Order **one proof** from a US shop (Signature printed, or Medal Foundry / a US die-struck house). Judge weight in hand.
3. If it is a gift/insert, buy a small batch and warehouse it (Printful warehouse products exist — that *is* inventory; call it that).
4. If it must sell one-at-a-time with no stock, sign a **blind-ship** quote with Medal Foundry or GS-JJ, disclose 3–4 week production on the product page, and fulfill by hand or a thin admin script. Do not pretend it is Printful.

Until then: `/shop` may *name* a Man Coin as a hairline placeholder. No mockup-as-product, no “add to cart,” no invented price.

---

## 3. How it attaches to walksteadfast.com later

`/shop` stays a Cloth Store hairline card. No products, no dollars, no fake reviews. IA already says this.

When Aaron says merch is real (art approved, Stripe open, legal entity confirmed):

```
walksteadfast.com /shop
        │
        ├─ Next.js product pages (Cloth Store chrome)
        ├─ Stripe Checkout (same register as training + ebook)
        └─ Vercel serverless: checkout.session.completed
                 → POST Printful /orders (confirm after payment)
                 → Printful ships to buyer
                 → Printful webhook → tracking on /account
```

**That is the fit.** Printful never takes the card. Stripe never prints the shirt. We already planned Stripe for digital; merch rides the same webhook with `metadata.type = merch` vs `training`.

Three architectures compared (do not build any of them yet):

| Path | Verdict |
| --- | --- |
| **Next.js + Stripe Checkout + Printful API** | Primary. Matches STACK.md. One domain, one member account, one refunds page. Env: `PRINTFUL_API_KEY` (server-only), `STRIPE_*`. Draft orders until webhook verifies payment. |
| **Shopify store + Printful app** | Reject for now. $29+/mo, second checkout, merch lives off-site. Only revisit if Aaron wants a full retail ops stack. |
| **Fourthwall (hosted or headless)** | Reject for now. Fast merch, they are MoR, checkout leaves our Stripe, 5% on digital if we mix catalogs. Official Vercel template is a merch site, not Cloth Store. |

Printify API is a real fallback (custom shop + `POST /v1/shops/{id}/orders.json`) if Printful ever fails us on price. Same webhook shape. Do not dual-run.

Operational notes for later (not now): sample one Navy 3001 and one mug before listing; set return address away from Printful default; packing slip store name **Steadfast Men**, support `orders@walksteadfast.com`; never print our cost on the slip (`retail_price` on the order). CA Prop 65 sticker can appear on some inks — expect it.

---

## 4. What we do NOT do yet

- No Printful / Printify / Gelato / Fourthwall / Shopify / SPOD / CustomCat **signup**.
- No Stripe account (already locked).
- No live SKUs, no cart, no “from $24,” no mockup galleries on the public site.
- No fake products, no invented merch photography, no fake reviews.
- No coin order, no mold fee, no sample spend.
- No publishing designs. Art is Lane, after Aaron. Plumb only — not a cross, not a compass, not a Roman I.
- No reprint of sermon graphics, Hawks language, One Mission, or other ministries.
- No street address on packing copy (Counsel drafts later, Texas, entity TBD).
- No merch checkout in the apps. Store tab stays “Open the store.”

`/shop` copy, if it needs a sentence: *Shirts and a mug later. Nothing for sale here yet.*

---

## 5. First four placeholder SKUs

Names only. Not live. No prices. Do not put these on the site as products. If art is approved later, these are the first four to mock — not to sell.

| Code | Name | Notes |
| --- | --- | --- |
| `SM-TEE-NAVY` | **Steadfast Men Tee** | Navy 3001. Gold plumb + STEADFAST MEN. Front only. |
| `SM-TEE-BONE` | **The way of Godly Men Tee** | Bone/natural blank. Navy lockup, italic subtitle. Quieter shirt. |
| `SM-MUG` | **Steadfast Mug** | 11 oz ceramic. Navy/gold/bone print. Coffee, not novelty. |
| `SM-COIN` | **Man Coin** | Four marks / plumb. **Not POD.** Placeholder until a proof exists. |

Do not add a fifth. Do not name colors as SKUs until a sample is in hand. Do not sell the four marks as an icon set on a shirt (LOOK-DIRECTIONS: four marks stay words).

---

## Sources (fetched 2026-09-01)

Printful: content guidelines; packing-slip / white-label help; developers.printful.com Orders + packing_slip; 2026 catalog/shipping writeups (Bella 3001, mug bases). Printify: developers.printify.com, branding/inserts, ToS hate clause. Gelato: white-label help, branded-insert API (Gelato+). Fourthwall: transaction-fees, storefront API / Vercel template. Shopify Basic 2026 plan pages. SPOD / CustomCat app listings. Coins: GS-JJ FAQs (no MOQ, mold fee), PinProsPlus, Signature Coins no-min printed US, Medal Foundry blind dropship page. Numbers move; re-quote at signup. No accounts were created.
