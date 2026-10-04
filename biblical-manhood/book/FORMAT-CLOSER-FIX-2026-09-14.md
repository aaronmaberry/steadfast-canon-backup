# FORMAT CLOSER FIX — 2026-09-14

Aaron: Your Turn / Name it inconsistent across chapters. Fix every closer to match Ch1 gold-standard box. No message to Aaron.

## Root cause

`CLOSER_ART = {1, 2, 3, 13, 14, 15, 33, 34, 35}` embedded PNG closer boxes for nine chapters while all other chapters used thin `closer_text` (L-rail, empty-looking voids, inconsistent labels). Two looks in one book.

## Fix (`tools/make_ebook_pdf.py`)

- `CLOSER_ART = set()` — never call PNG `closer_art` in the live render path
- New shared **`closer_box(num, lines)`** typeset for every chapter:
  - Light bone panel, dark left rail + ticks, header `NN · YOUR TURN`
  - Sections: NAME IT / DO THIS WEEK / TELL A BROTHER / CARRY THIS
  - Libre-Bold rust labels; EBGaramond body; thin section rules
  - Write-in rules from `:::notes` (1–2 max); none under CARRY THIS
  - CARRY THIS shaded `CARRY_BAND` + larger italic carry line
- `parse_closer_sections`: labels with/without `**`; body until next label/`:::notes`; strip `##`/`**`/`---`; empty notes skipped; ch35 **Be a brother** → BE A BROTHER
- Figures ch3/ch34 unchanged (before closer)

Backup: `make_ebook_pdf.py.pre-closer-fix-20260914`

## Build

- Binder: `/workspace/.venv-ebook/bin/python make_ebook_pdf.py`
- `export/steadfast-men-ebook.pdf` (binder, ~2.6 MB, 246 pages)
- gs `/ebook` → `export/Steadfast-Men-FULL-CLOSER-2026-09-14.pdf` (~1.25 MB)
- Also refreshed `export/Steadfast-Men-FULL-FORMAT-2026-09-14.pdf` to same bytes

## Verification (pdftotext)

| Check | Result |
|-------|--------|
| `##` / `###` | 0 |
| `CHAPTER 0` | 0 |
| raw `**` | 0 |
| `YOUR TURN` | 35 |
| `NAME IT` | 35 |
| `DO THIS WEEK` | 35 |
| `TELL A BROTHER` | 34 |
| `BE A BROTHER` | 1 (ch35 intentional) |
| `CARRY THIS` | 35 |

Spot-check ch 1, 7, 8, 10, 16, 25, 34: all four labels + carry italic. pdftoppm samples pages 20 / 64 / 112: panel + rail + ticks + 2 write-ins + carry band; no empty L-void pages.

## Drive

- Folder: `1WSLXOjfooaw74sYwFmKaM0DaZMfXaLiB`
- File: `Steadfast-Men-FULL-CLOSER-2026-09-14.pdf` (`1LPsTnHm0XixQ2dqaK_ONiEslNXXFYZmm`)
- View: https://drive.google.com/file/d/1LPsTnHm0XixQ2dqaK_ONiEslNXXFYZmm/view?usp=drivesdk
- Size on Drive: 1,251,824 bytes (gs `/ebook` of binder output)
- Upload: Chrome CDP file-chooser (same path as prior FULL dumps); MCP create_file OIDC returned 401 for large PDF

## Remaining

- No two-Adams figure for ch 19 (not on disk) — pre-existing
- Ch35 uses BE A BROTHER instead of TELL A BROTHER (source copy)
