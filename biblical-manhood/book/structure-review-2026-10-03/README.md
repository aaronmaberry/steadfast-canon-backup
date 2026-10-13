# Structure review, 2026-10-03

This is Aaron's Part Two note on scripture load, breaks, titles and bold, and the "Before you turn the page" ending. Nothing here changes the manuscript, the 03d print or Drive.

- `STRUCTURE-PROPOSAL.md` / `.pdf` has the options and the recommendation.
- `AUDIT.md` / `.pdf` has the per-chapter numbers. `audit.json` is the raw data, and `tools/audit.py` re-runs it.
- `Steadfast Men - ch10 current vs sample - 2026-10-03.pdf` shows the 03d pages next to the sample pages.
- `sample/` has the ch10 sample text, the back-of-book Your Turn mock-up and the Scripture notes mock-up.
- `build/` has the typeset sample PDFs, and `tools/` has the render and side-by-side scripts.

## 2026-10-04 additions

- `CHAPTER-MAP.md` / `CHAPTER-MAP.pdf`: every chapter with topic, word counts, W session, course topic and overlaps, plus options A (35), B (28, recommended) and C (25), and how the sessions map under each.
- Sample spacing fix: `tools/render_sample.py` (v1 kept as `tools/render_sample.v1-2026-10-03.py`). Side-by-side re-rendered as v2 at the same path. The v1 PDF is at `build/...v1-before-spacing-fix.pdf`.
- `tools/build_map_table.py` builds the chapter table from `audit.json`.
