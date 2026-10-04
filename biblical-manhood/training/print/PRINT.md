# Week 1 print (Binder)

Cloth Store on paper. Navy strip, bone sheet. Gold only on Do this week.

## Files

- `/workspace/biblical-manhood/training/print/week-01-leader.html`
- `/workspace/biblical-manhood/training/print/week-01-leader.pdf` (letter, 2 pages)
- `/workspace/biblical-manhood/training/print/week-01-participant.html`
- `/workspace/biblical-manhood/training/print/week-01-participant.pdf` (letter, 1 page)
- `/workspace/biblical-manhood/training/print/proofs/week-01-leader-p1.png`
- `/workspace/biblical-manhood/training/print/proofs/week-01-leader-p2.png`
- `/workspace/biblical-manhood/training/print/proofs/week-01-participant-p1.png`
- `/workspace/biblical-manhood/training/print/proofs/week-01-leader-p1-gray.png`
- `/workspace/biblical-manhood/training/print/proofs/week-01-leader-p2-gray.png`
- `/workspace/biblical-manhood/training/print/proofs/week-01-participant-p1-gray.png`

## Fonts

Owned files. Not downloaded. The press TTFs internally all name themselves Regular/Thin, so print copies under `print/fonts/` were retagged (name table only, glyphs unchanged) so Chrome can embed Bold, Medium, and Regular as separate faces.

Source glyphs:

`/workspace/biblical-manhood/book/art/press/fonts/`

@font-face files (what the HTML actually loads):

- `/workspace/biblical-manhood/training/print/fonts/PlayfairDisplay-Bold.ttf`
- `/workspace/biblical-manhood/training/print/fonts/PlayfairDisplay-Regular.ttf`
- `/workspace/biblical-manhood/training/print/fonts/PlayfairDisplay-Italic.ttf`
- `/workspace/biblical-manhood/training/print/fonts/EBGaramond-Regular.ttf`
- `/workspace/biblical-manhood/training/print/fonts/EBGaramond-Italic.ttf`
- `/workspace/biblical-manhood/training/print/fonts/EBGaramond-Bold.ttf`
- `/workspace/biblical-manhood/training/print/fonts/LibreFranklin-Medium.ttf`
- `/workspace/biblical-manhood/training/print/fonts/LibreFranklin-Regular.ttf`

## Reprint

```
google-chrome --headless --disable-gpu --no-pdf-header-footer --allow-file-access-from-files --print-to-pdf=/workspace/biblical-manhood/training/print/week-01-leader.pdf file:///workspace/biblical-manhood/training/print/week-01-leader.html

google-chrome --headless --disable-gpu --no-pdf-header-footer --allow-file-access-from-files --print-to-pdf=/workspace/biblical-manhood/training/print/week-01-participant.pdf file:///workspace/biblical-manhood/training/print/week-01-participant.html
```

Print CSS: `@page { size: letter; margin: 0; }`. Layout owns the 0.78in margins.

## Gold

Gold `#E3C572` is only on Do this week: navy type on a gold fill. Nowhere else. Not on the title lockup, not on the four marks, not on scripture, not on the plumb (bone on navy). In grayscale the bar goes light gray and the navy type stays dark.


## Week 1 — Fable refresh reprint (2026-09-05 CDT)

- Replaced `week-01-leader.html` / `.pdf` (letter, 2 pages) and `week-01-participant.html` / `.pdf` (letter, 1 page).
- H1: Introduction + A quiet Tuesday (dual-title dual-verse).
- Scriptures: 1 Corinthians 16:13-14 NIV; 1 Corinthians 13:11 NIV (word-for-word from refresh `leader.md`).
- CSS cloned from week-18 dual stack (`scripture-stack` / `scripture-row.two.with-well`, smaller `.weektitles`).
- Cloth Store: navy `#0B1F38`, gold `#E3C572` only on Do this week, bone `#E6DDCC`.
- Stills reused only: `image-2.0/crops/week-02-mast-plumb.png`, `image-2.0/week-04-well.png`. No GenerateImage. No new stills.
- Footer: Steadfast Men | Week 1 of 24 | Leader guide / Participant worksheet.
- Proofs regenerated: `proofs/week-01-leader-p{1,2}.png` (+ gray), `proofs/week-01-participant-p1.png` (+ gray) at 150dpi.
- Weeks 2–27 HTML/PDF mtimes frozen (untouched).

## Week 2

- `week-02-leader.pdf` — letter, 2 pages
- `week-02-participant.pdf` — letter, 1 page
- Image 2.0 prompts: `image-2.0/week-02-prompts.md` (Jarvis, grok.com/imagine Quality Mode)

Week 1 files above stay. Do not reprint them.

## Week 2 — Fable refresh reprint (2026-09-05 CDT)

- Replaced `week-02-leader.html` / `.pdf` (letter, 2 pages) and `week-02-participant.html` / `.pdf` (letter, 1 page).
- H1: You are not crazy (single title).
- Scripture: Genesis 1:27 NIV (word-for-word from refresh `leader.md`, line breaks preserved).
- CSS cloned from week-17 single verse (`scripture-row.one.with-well`).
- Cloth Store: navy `#0B1F38`, gold `#E3C572` only on Do this week, bone `#E6DDCC`.
- Stills reused only: `image-2.0/crops/week-02-mast-plumb.png`, `image-2.0/week-04-well.png`. No GenerateImage. No new stills.
- Footer: Steadfast Men | Week 2 of 24 | Leader guide / Participant worksheet.
- Proofs regenerated: `proofs/week-02-leader-{1,2}.png` (+ gray), `proofs/week-02-participant-1.png` (+ gray) at 150dpi.
- Week 1 and weeks 3–27 HTML/PDF mtimes frozen. Hold week 3.

## Week 3

- `week-03-leader.pdf` — letter, 2 pages
- `week-03-participant.pdf` — letter, 1 page

Week 1 and 2 files stay. Do not reprint them.

## Week 3 — Fable refresh reprint (2026-09-05 CDT)

- Replaced `week-03-leader.html` / `.pdf` (letter, 2 pages) and `week-03-participant.html` / `.pdf` (letter, 1 page).
- H1: The four marks (single title).
- Scripture: Genesis 3:6 NIV (word-for-word from refresh `leader.md`).
- CSS cloned from week-02 / week-10 single verse (`scripture-row.one.with-well`).
- Cloth Store: navy `#0B1F38`, gold `#E3C572` only on Do this week, bone `#E6DDCC`.
- Stills reused only: `image-2.0/crops/week-02-mast-plumb.png`, `image-2.0/week-04-well.png`. No GenerateImage. No new stills.
- Footer: Steadfast Men | Week 3 of 24 | Leader guide / Participant worksheet.
- Proofs regenerated: `proofs/week-03-leader-{1,2}.png` (+ gray), `proofs/week-03-participant-1.png` (+ gray) at 150dpi.
- Weeks 1–2 and weeks 4–27 HTML/PDF mtimes frozen. Hold week 4.


## Week 4

- `week-04-leader.pdf` — letter, 2 pages
- `week-04-participant.pdf` — letter, 1 page
- Image 2.0 well prompt: `image-2.0/week-04-prompts.md`

Weeks 1-3 stay. Do not reprint them.

## Week 5

- `week-05-leader.pdf` — letter, 2 pages
- `week-05-participant.pdf` — letter, 1 page
- Mast: week-2 Image 2.0. Well: week-4 Image 2.0. No new still.

Weeks 1-4 stay. Do not reprint them.

## Week 5 — Fable refresh reprint (2026-09-05 CDT)

- Replaced `week-05-leader.html` / `.pdf` (letter, 2 pages) and `week-05-participant.html` / `.pdf` (letter, 1 page).
- H1: Pick up the weight (single title).
- Scripture: Galatians 6:5 NIV (word-for-word from refresh `leader.md`).
- CSS cloned from week-04 Fable single verse (`scripture-row.one.with-well`).
- Cloth Store: navy `#0B1F38`, gold `#E3C572` only on Do this week, bone `#E6DDCC`.
- Stills reused only: `image-2.0/crops/week-02-mast-plumb.png`, `image-2.0/week-04-well.png`. No GenerateImage. No new stills.
- Footer: Steadfast Men | Week 5 of 24 | Leader guide / Participant worksheet.
- Proofs regenerated: `proofs/week-05-leader-{1,2}.png` (+ gray), `proofs/week-05-participant-1.png` (+ gray) at 150dpi.
- Weeks 1–4 and weeks 7–27 HTML/PDF mtimes frozen. Hold week 6 until after this pass.

## Week 6

- `week-06-leader.pdf` — letter, 2 pages
- `week-06-participant.pdf` — letter, 1 page
- Mast: week-2. Well: week-4. No new still.

Weeks 1-5 stay.

## Week 7

- `week-07-leader.pdf` — letter, 2 pages
- `week-07-participant.pdf` — letter, 1 page
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-6 stay. Part 1 print closed until week 8 is signed.

## Week 8

- `week-08-leader.pdf` — letter, 2 pages
- `week-08-participant.pdf` — letter, 1 page
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-7 stay. Hold week 9 until Reed signs.

## Week 9

- `week-09-leader.pdf` — letter, 2 pages
- `week-09-participant.pdf` — letter, 1 page
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-8 stay. Hold week 10 until Reed signs.

## Week 10

- `week-10-leader.pdf` — letter, 2 pages
- `week-10-participant.pdf` — letter, 1 page
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-9 stay. Hold week 11 until Reed signs.

## Week 11

- `week-11-leader.pdf` — letter, 2 pages
- `week-11-participant.pdf` — letter, 1 page
- H1: When home never handed you off + Leave without slamming the door
- Luke 2:49 and Genesis 2:24 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-10 stay. Hold week 12 until Reed signs.

## Week 12

- `week-12-leader.pdf` — letter, 2 pages
- `week-12-participant.pdf` — letter, 1 page
- H1: A man with no brothers + Ask the man
- Ecclesiastes 4:10 and Proverbs 13:20 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-11 stay. Hold week 13 until Reed signs.

## Week 13

- `week-13-leader.pdf` — letter, 2 pages
- `week-13-participant.pdf` — letter, 1 page
- H1: Week 13 | The problem inside
- Read this week: Chapter 15, The problem inside
- Romans 7:18 NIV parked
- Recast off leftover Week 10 Father copy. CSS cloned from week 10 (single verse + well). Cloth Store. Gold only on Do this week.
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-12 stay. Hold week 14 until Reed signs.

## Week 14

- `week-14-leader.pdf` — letter, 2 pages
- `week-14-participant.pdf` — letter, 1 page
- Proverbs 14:12 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-13 stay.

## Week 15

- `week-15-leader.pdf` — letter, 2 pages
- `week-15-participant.pdf` — letter, 1 page
- Proverbs 29:18 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-14 stay. Hold week 16 until Reed signs.

## Week 16

- `week-16-leader.pdf` — letter, 2 pages
- `week-16-participant.pdf` — letter, 1 page
- H1: Before the fall + Two men, two ways
- Genesis 2:15 and 1 Corinthians 15:45 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-15 stay. Hold week 17 until Reed signs.

## Week 17

- `week-17-leader.pdf` — letter, 2 pages
- `week-17-participant.pdf` — letter, 1 page
- 2 Corinthians 5:15 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-16 stay. Hold week 18 until Reed signs.

## Week 18

- `week-18-leader.pdf` — letter, 2 pages
- `week-18-participant.pdf` — letter, 1 page
- H1: If there is no wife yet + Know her
- 1 Corinthians 7:17 and Proverbs 20:5 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-17 stay. Hold week 19 until Reed signs.

## Week 19

- `week-19-leader.pdf` — letter, 2 pages
- `week-19-participant.pdf` — letter, 1 page
- H1: Lay it down + What she actually needs
- Ephesians 5:25 and Philippians 2:4 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-18 stay. Hold week 20 until Reed signs.

## Week 20

- `week-20-leader.pdf` — letter, 2 pages
- `week-20-participant.pdf` — letter, 1 page
- Hebrews 13:4 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-19 stay. Hold week 21 until Reed signs.

## Week 21

- `week-21-leader.pdf` — letter, 2 pages
- `week-21-participant.pdf` — letter, 1 page
- Deuteronomy 6:7 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-20 stay. Hold week 22 until Reed signs.

## Week 22

- `week-22-leader.pdf` — letter, 2 pages
- `week-22-participant.pdf` — letter, 1 page
- Isaiah 43:1 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-21 stay. Hold week 23 until Reed signs Give your son a hill.

## Week 23

- `week-23-leader.pdf` — letter, 2 pages
- `week-23-participant.pdf` — letter, 1 page
- 1 Thessalonians 2:11-12 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-22 stay.

## Week 24

- `week-24-leader.pdf` — letter, 2 pages
- `week-24-participant.pdf` — letter, 1 page
- Joshua 4:6-7 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-23 stay.

## Week 25

- `week-25-leader.pdf` — letter, 2 pages
- `week-25-participant.pdf` — letter, 1 page
- H1: You were made for a work + Feelings are the dash, not the wheel
- Ephesians 2:10 and Psalm 42:5 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-24 stay. Hold week 26 until Dean opens.

## Week 26

- `week-26-leader.pdf` — letter, 2 pages
- `week-26-participant.pdf` — letter, 1 page
- H1: Every season still counts + What you are building when nobody claps
- Proverbs 20:29 and Colossians 3:23 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.

Weeks 1-25 stay.

## Week 27

- `week-27-leader.pdf` — letter, 2 pages
- `week-27-participant.pdf` — letter, 1 page
- H1: Write the next move + These men are my brothers
- Proverbs 16:9 and Hebrews 3:13 NIV parked
- Mast: week-2 Imagine 2.0. Well: week-4 Imagine 2.0. No new still. No GenerateImage.
- Last Part 5 packet.

Weeks 1-26 stay.

## Week 26 — Fable 5.1 dig reprint (2026-09-07 CDT)

- Replaced `week-26-leader.html` / `.pdf` (letter, 2 pages) and `week-26-participant.html` / `.pdf` (letter, 1 page).
- H1 dual: Every season still counts + What you are building when nobody claps.
- Scriptures: Proverbs 20:29 NIV; Colossians 3:23 NIV (word-for-word from signed dig).
- Participant dig: Older / empty-nest / not-a-mascot under Name it; Alone line includes Empty nest is not a refund. Not a mascot seat.
- carry-block + density; Carry above footer. Footer Week 26 of 27.
- Brand letter-spacing 0.08em. Gold only on Do this week.
- Stills: `image-2.0/crops/week-02-mast-plumb.png`, `image-2.0/week-04-well.png`.
- Proofs regenerated at 150dpi (+ gray).

## Week 27 — Fable 5.1 dig reprint (2026-09-07 CDT)

- Replaced `week-27-leader.html` / `.pdf` (letter, 2 pages) and `week-27-participant.html` / `.pdf` (letter, 1 page).
- H1 dual: Write the next move + These men are my brothers.
- Scriptures: Proverbs 16:9 NIV; Hebrews 3:13 NIV (word-for-word from signed dig).
- Participant dig: Older / empty-nest / not-a-mascot under Name it; Alone line includes Empty nest still needs two names. Not a mascot seat.
- CRITICAL Carry: body padding-bottom 0.72in, short write-lines, carry-block. pdftotext order: CARRY THIS → carry line → Write it once → then footer Week 27 of 27 (no interleaving).
- Brand letter-spacing 0.08em. Gold only on Do this week.
- Stills: `image-2.0/crops/week-02-mast-plumb.png`, `image-2.0/week-04-well.png`.
- Proofs regenerated at 150dpi (+ gray). Last Part 5 packet.
