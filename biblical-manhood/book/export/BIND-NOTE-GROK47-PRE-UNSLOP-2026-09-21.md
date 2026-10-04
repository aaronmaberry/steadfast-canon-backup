# Bind note — Grok 4.7 PRE-UNSLOP + locked walksteadfast cover

**Date:** 2026-09-21 (America/Chicago)
**Intent:** Aaron OVERRIDE — do NOT use Unslop. Revert to PRE-UNSLOP Grok 4.7 manuscript and bind with locked walksteadfast cover.

## Source

- **Manuscript source:** `_grok47-ms/` (specifically `_grok47-ms/book/`)
- **Unslop:** NOT used. Entire `_grok47-unslop-2026-09-21/` ignored; Unslop prose and rules not applied.
- **Live restore step:** First restored binder live `.md` from `export/pre-unslop-bind-backup-2026-09-21-live-md.tar.gz` into `book/` root (overwrote Unslop-copied live files).
- **Then:** Overwrote those same binder files with PRE-UNSLOP content from `_grok47-ms/book/`.

## Files bound (from `_grok47-ms/book/`)

### Front matter
- `00-half-title.md`
- `00-title-page.md`
- `00-copyright.md`
- `00-dedication.md`
- `00-contents.md`
- `00-introduction.md`

### Chapters (binder `CHAPTER_FILES`)
- `01-a-quiet-tuesday.md` … `35-these-men-are-my-brothers.md` (35 files; names match 1:1)

### Binder closers (also from MS; binder references them)
- `36-about-the-author.md`
- `37-condensed-training.md`

## Filename mapping

**No mismatches.** Every binder `CHAPTER_FILES` entry and every `00-*` front-matter name exists under `_grok47-ms/book/` with the same filename. Closers `36`/`37` likewise matched. No remapping required.

## Cover

- **Locked cover (already in binder):** `book/art/press/cloth-store/cover-front-walksteadfast-locked-2026-09-14.png`
- Binder path: `PRESS / "cloth-store" / "cover-front-walksteadfast-locked-2026-09-14.png"`
- Cover front: yes (binder report `cover_front: true`)

## Output

- **PDF path:** `/workspace/biblical-manhood/book/export/Steadfast-Men-GROK47-PRE-UNSLOP-LOCKED-COVER-2026-09-21.pdf`
- **Also written as:** `export/steadfast-men-ebook.pdf` (binder default)
- **Bytes:** 2613239
- **Pages (pdfinfo physical):** 240
- **Folio end (binder report):** 235
- **Run dir:** `export/_build/run-c3f5a62063/`

## Binder

```
cd /workspace/biblical-manhood/book && python3 tools/make_ebook_pdf.py
```

## Not done (per OVERRIDE)

- No Google Drive upload
- Unslop dir not touched
- Unslop rules not applied
