# Steadfast Men — press covers

**Title lock:** STEADFAST MEN / The way of Godly Men / Wes Hart

Not sent to Aaron. Jarvis presents.

`book/art/covers/`, `covers-v2/`, and `covers-v3/` were not touched.

## Locked pick — A
Navy cloth, gold Playfair, plumb. Do not average with B/C/D.

Locked original (do not overwrite until told): `press-a.png` (1600×2560 RGB).

### A v2 — PARKED until the book is finished
Official set. Do not overwrite. STOP cover iterates. When the wrap reopens: real copy and real endorsements only; recalc spine after last chapter.

- `a-front-v2.png` — 1600×2560 RGB. Larger gold lockup. Plumb is a standing cord + teardrop bob (not a Roman I, not a cross, not a compass).
- `a-thumb-160.png` — 160×256 Amazon thumb
- `a-thumb-320.png` — 320×512
- `a-wrap.png` — 6×9 KDP wrap, 3840×2775 px @ 300 DPI (back | spine | front)

Palette: navy `#0B1F38` · gold `#E3C572` · bone `#E6DDCC`  
Type: Playfair Display Bold, EB Garamond Italic, Libre Franklin Medium.

**Wrap math (estimate):** cream B&W, **~220 pages** (manuscript still in progress; recalc at bind). KDP cream spine = pages × 0.0025" → 0.55" (165 px). Width 12.80", height 9.25". Spine type: STEADFAST MEN / Hart. No fold rule. Back: Wes Hart lockup + locked four-marks line (commas): A real man rejects passivity, accepts responsibility, leads courageously, and expects the greater reward, God's reward. No fake blurbs. No ISBN barcode yet.

## Unused roads (frozen)
- B cream stacked navy — `press-b.png`
- C charcoal geometric — `press-c.png`
- D near-black bone — `press-d.png`

## Wrap back (Reed-signed 2026-09-05)
Applied to `a-wrap.png` back panel only. Front `a-front-v2.png` not overwritten.
Blocks: hook / four marks / CHRISTIAN LIVING / MEN / walksteadfast.com / Wes Hart.
No fake blurbs. No ISBN. Source: `wrap-back-copy.md`.

## Cloth Store recolor (2026-09-05)
Pace/Jarvis reopen. Palette navy `#0B1F38` · gold `#E3C572` · bone `#E6DDCC`.
- `a-front-v2.png` restored to 1600×2560 from pre-cloth-store backup (rejected a bad 1536×1024 landscape drop).
- `cover-cloth-store-navy-gold.png` — same portrait jacket for digital/PALETTE.md.
- `cloth-store/` pack + `export/_build/cloth-store-20260905/` bind art.
- `covers-v3/` not overwritten (limestone rejected; not revived).
- Wrap-back Reed-signed blocks unchanged.

**2026-09-05:** Circular patch locked. Subtitle *The way of Godly Men* enlarged to Cursor-comp scale (gold).

## Subtitle enlarge (Aaron 2026-09-05)
*The way of Godly Men* set gold italic at Cursor-comp scale (~92% of STEADFAST width) on `cover-cloth-store-navy-gold.png` and synced `a-front-v2.png` / wrap front / thumbs / bind art. Wrap-back Reed-signed blocks preserved. No spend. No publish.

## Cursor-layout lock (Aaron 2026-09-05 via Jarvis)
Live jacket: `cover-cloth-store-navy-gold.png` (= `a-front-v2.png`).
STEADFAST MEN one line · large gold italic *The way of Godly Men* · full-height vertical gold plumb on the right · Cloth Store navy/gold.
Landscape twin: `cover-cloth-store-cursor-layout-landscape.png`.
Prior stacked plumb-bob kept as `.pre-cursor-layout-20260905.png`. Circular patch keeper. Shop empty. Not sent to Aaron.

## Wrap back re-applied 2026-10-01 (box print-build prep)
Creed swapped to the Steadfast creed (locked 2026-10-01): A steadfast man stops waiting, picks up the weight, goes first, and works for God's pay, not the room's.
Inheritance line added under it: God's pay is a Father's inheritance, not wages.
Hook unchanged (Reed-signed 2026-09-05). Back panel only; front and spine untouched.

## Spine recalculated for final page count (2026-10-01 10:45 CT)
- Final interior: 242 pages, 6x9, KDP paperback, cream paper (0.0025 in/page, as in every earlier wrap build).
- Spine = 242 x 0.0025 = 0.605 in = 181.5 px @ 300 DPI -> 182 px (0.6067 in). Was 165 px (220-page estimate).
- a-wrap.png 3840x2775 -> 3857x2775 px (12.857 x 9.25 in). Back and front panels byte-identical; spine strip rebuilt
  with `rebuild_wrap_spine.py --pages 242` (same type, size and top offset, re-centered: 76 px clear each side).
- Pre-change backup: /workspace/backups/pre-spine-242-2026-10-01/

## Wrap back: Sample D locked (Aaron 2026-10-01 11:14 CT)
Back panel replaced with Sample D (question opener + INSIDE bullets + creed + inheritance line),
with the third bullet changed to "Help for every season of a man's life" (no "counsel" on the back;
reworded from "Straight talk for every season" at Aaron's OK, 11:19 CT; prior state in
/workspace/backups/back-cover-pre-D-2026-10-01/straight-talk-version-2026-10-01-1120/).
Wrap palette #0B1F38 / #E3C572; footer CHRISTIAN LIVING / MEN, walksteadfast.com, WES HART bottom left;
blank white barcode block 2.0 x 1.2 in, bottom right, 0.25 in from trim. Copy: `wrap-back-copy.md`.
Back panel only; spine (182 px, 242 pages) and front byte-identical. Not uploaded.
Pre-D backup: /workspace/backups/back-cover-pre-D-2026-10-01/
