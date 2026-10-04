# FORMAT FIX LOG — 2026-09-14

Shelf-quality binder pass for Steadfast Men ebook PDF. No spend. No publish. Cover stays walksteadfast locked (Wes Hart).

## Root causes

1. **`##` leak:** `parse_md` treated `##` / `###` lines as ordinary paragraph text, so hashes printed raw in the PDF.
2. **CHAPTER 0:** `parse_md` only took `N` from `# N. Title`. After UNSLOP, chapters 16–23 and 32–35 lost the `N.` prefix, so `num=0` and the opener printed `CHAPTER 0` (e.g. Write the Next Move).
3. **Empty notes inventing lines:** empty `:::notes` fell back to `"_" * 47`, drawing blank write-in rails / large closer voids.

## Binder fixes (`tools/make_ebook_pdf.py`)

- Filename fallback: `NN-*.md` → chapter `N` when H1 lacks `N.`
- Parse `##` / `###` as `h2` / `h3` blocks (hashes stripped); `## Your Turn` still opens closer
- Render h2 ~11.5pt Libre-Bold NAVY; h3 ~10.5pt; never print `#`
- `clean_inline_md`: strip leading hashes and `**` / `__` from paragraph text
- Empty `:::notes`: skip block (body + closer); do not invent underscore lines
- Intro / back-matter / chapter render all handle h2/h3

## Live H1 normalize (CHAPTER_FILES only)

Restored `# N. Title` on: 16–23, 32–35. Binder fallback remains mandatory.

## Build

- Binder: `python make_ebook_pdf.py` via `/workspace/.venv-ebook`
- Output: `export/steadfast-men-ebook.pdf` (binder) + `export/Steadfast-Men-FULL-FORMAT-2026-09-14.pdf` (gs `/ebook`)
- Cover: `cover-front-walksteadfast-locked-2026-09-14.png` unchanged
- Backup: `make_ebook_pdf.py.pre-format-fix-20260914`, `steadfast-men-ebook.pre-format-fix-20260914.pdf`

## Verification (pdftotext)

- `##` / `###` in body: **0**
- `CHAPTER 0`: **0**
- CHAPTER 16 / 34 present; 16–23 and 32–35 numbered correctly
- Spot subheads (e.g. "The shapes it takes", "Steadiness", "Make it plain") as plain heading text
- `**` raw: **0**

## Drive

- Folder: `1WSLXOjfooaw74sYwFmKaM0DaZMfXaLiB`
- File: `Steadfast-Men-FULL-FORMAT-2026-09-14.pdf` (`1BsU76bJ6T9htV1rO45cB7HQHjqhjrwvQ`)
- View: https://drive.google.com/file/d/1BsU76bJ6T9htV1rO45cB7HQHjqhjrwvQ/view?usp=drivesdk
- Size on Drive: 1,873,518 bytes (gs `/ebook` compress of binder output)

## Remaining known issues

- No two-Adams figure for ch 19 (not on disk) — pre-existing
- Closer-box art only for CLOSER_ART set; others typeset Your Turn — pre-existing
- Write-in underscore lines that exist in source `:::notes` still draw (intentional)
