# Structure audit, Steadfast Men, 2026-10-03

Source: the manuscript behind Review Print 2026-10-03d, `book/_opus55-second-pass-2026-10-01/book/` (intro plus chapters 1-35). This audit only read files. Nothing in the manuscript, the print or Drive was changed. Script: `tools/audit.py` (re-run it any time). Raw numbers: `audit.json`.

## Headline numbers (chapters 1-35)

| What | Count | Notes |
|---|---|---|
| NIV verse boxes (`:::margin`) | **158** | 4.5 per chapter. Range 1 (ch2) to 12 (ch19). Part Two has 37 across 10 chapters. |
| Boxes announced by a set-up sentence | **about 100 of 158** | The sentence before the box points at it, e.g. "Paul says it in eight words.", "Jesus said it like this.", "Look where the father is." This is the "trying too hard" rhythm Aaron feels. |
| Scripture quoted inside the prose | 2 | Almost every word-for-word quote sits in a box. |
| Prose sentences naming a Bible person or book | 308 | A heuristic count, and it includes phrases like "in Christ". Most are retellings, which is the style Aaron asked for. |
| In-chapter subheads | **228** | 6.5 per chapter, or one every ~230 words. Range 4 (ch27) to 11 (ch24). |
| End headings | 34 "Before you turn the page" + 35 "Your Turn" | Ch19 has no "Before you turn the page". Ch35 uses "Before you close the book". |
| Bold inside prose | 9 | The creed line (intro, ch3, ch7, ch34, ch35) and the four closer labels taught in the intro. |
| Bold the reader sees on the page | 228 subheads + 158 verse labels + 140 Your Turn labels | The bold Aaron is seeing comes from headings and labels, not the prose. |
| Body paragraphs | 1,046 | Average 50 words. Part Two averages 52.8. |
| Short paragraphs (25 words or fewer) | 218 (21%) | 82 are one sentence long. |
| Paragraphs in list-like runs | 39 | Three or more paragraphs in a row that open the same way ("Some of you...", "If the seat...", "Use the name. / Take Him... / Let Him..."). |
| "Before you turn the page" | 34 sections, 2,232 words | 33 of the 34 are built on a "May the..." blessing. |
| Your Turn | 35 pages (15% of the 238-page print), 5,552 words, 105 write-in blocks | Every chapter ends on the same form page. |
| Interruptions | 7.3 per 1,000 words | Boxes plus subheads. A 1,500-word chapter breaks about 11 times. |

How the counts were made: verse boxes, subheads and bold were counted exactly. "Set-up sentence" and "list-like run" are pattern matches. I spot-checked them against the text, but read them as close, not exact. Paragraphs only count body prose, without headings, boxes or the end sections.

## Where Part Two sits

Part Two (ch8-17) is close to the book average. It has 37 boxes, 62 subheads, 295 paragraphs averaging 52.8 words, ten "Before you turn the page" sections and ten Your Turn pages. The heaviest chapters for Scripture are ch17 (6 boxes) and ch16 (5). The heaviest for subheads is ch13 (8). The heaviest anywhere in the book are Part Three's ch18 and ch19 (11 and 12 boxes, 14.3 and 12.2 interruptions per 1,000 words).

## Per chapter

| Ch | Part | Body words | Verse boxes (NIV) | Set-up lines before a box | Inline quoted verse words | "X said/wrote" Scripture sentences | Sentences naming a Bible person/book | Subheads | Bold in prose | Bold verse labels | Bold closer labels | Paragraphs | Avg para (words) | Median para | Paras ≤25 words | One-sentence paras | Paras in list-like runs (3+) | "Notice" in prose | "Before you turn" words | Your Turn words | Write-in blocks | Boxes+subheads per 1k words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Intro | Front | 1476 | 0 | 0 | 0 | 0 | 2 | 6 | 5 | 0 | 0 | 25 | 59.0 | 51 | 4 | 1 | 0 | 1 | 0 | 0 | 0 | 4.1 |
| 1 | One | 1633 | 2 | 2 | 0 | 2 | 5 | 6 | 0 | 2 | 4 | 30 | 54.4 | 57.0 | 3 | 0 | 0 | 1 | 101 | 120 | 3 | 4.9 |
| 2 | One | 1533 | 1 | 0 | 0 | 0 | 0 | 5 | 0 | 1 | 4 | 30 | 51.1 | 48.0 | 6 | 2 | 0 | 0 | 85 | 143 | 3 | 3.9 |
| 3 | One | 1433 | 5 | 5 | 0 | 4 | 9 | 6 | 1 | 5 | 4 | 27 | 53.1 | 48 | 9 | 6 | 0 | 1 | 85 | 127 | 3 | 7.7 |
| 4 | One | 1517 | 5 | 3 | 0 | 0 | 4 | 6 | 0 | 5 | 4 | 33 | 46.0 | 38 | 8 | 2 | 4 | 0 | 68 | 124 | 3 | 7.3 |
| 5 | One | 1591 | 6 | 6 | 0 | 5 | 8 | 7 | 0 | 6 | 4 | 28 | 56.8 | 44.5 | 8 | 4 | 0 | 1 | 82 | 131 | 3 | 8.2 |
| 6 | One | 1355 | 7 | 7 | 1 | 3 | 11 | 6 | 0 | 7 | 4 | 31 | 43.7 | 44 | 7 | 2 | 0 | 0 | 55 | 116 | 3 | 9.6 |
| 7 | One | 1363 | 7 | 3 | 0 | 2 | 7 | 7 | 1 | 7 | 4 | 29 | 47.0 | 39 | 10 | 3 | 0 | 0 | 63 | 143 | 3 | 10.3 |
| 8 | Two | 1687 | 2 | 2 | 0 | 1 | 6 | 6 | 0 | 2 | 4 | 34 | 49.6 | 44.5 | 7 | 1 | 4 | 0 | 37 | 127 | 3 | 4.7 |
| 9 | Two | 1685 | 3 | 3 | 0 | 1 | 6 | 7 | 0 | 3 | 4 | 32 | 52.7 | 47.5 | 4 | 1 | 0 | 0 | 43 | 134 | 3 | 5.9 |
| 10 | Two | 1581 | 4 | 4 | 1 | 8 | 12 | 6 | 0 | 4 | 4 | 28 | 56.5 | 49.0 | 4 | 1 | 4 | 1 | 48 | 135 | 3 | 6.3 |
| 11 | Two | 1499 | 3 | 3 | 0 | 3 | 16 | 7 | 0 | 3 | 4 | 27 | 55.5 | 60 | 3 | 1 | 0 | 0 | 58 | 177 | 3 | 6.7 |
| 12 | Two | 1462 | 4 | 3 | 0 | 1 | 3 | 5 | 0 | 4 | 4 | 25 | 58.5 | 56 | 4 | 2 | 0 | 1 | 58 | 152 | 3 | 6.2 |
| 13 | Two | 1629 | 4 | 1 | 0 | 2 | 7 | 8 | 0 | 4 | 4 | 28 | 58.2 | 53.0 | 6 | 2 | 0 | 0 | 61 | 143 | 3 | 7.4 |
| 14 | Two | 1564 | 2 | 2 | 0 | 2 | 7 | 7 | 0 | 2 | 4 | 28 | 55.9 | 55.5 | 5 | 0 | 0 | 0 | 89 | 173 | 3 | 5.8 |
| 15 | Two | 1518 | 4 | 2 | 0 | 5 | 11 | 5 | 0 | 4 | 4 | 29 | 52.3 | 49 | 4 | 1 | 0 | 1 | 70 | 189 | 3 | 5.9 |
| 16 | Two | 1502 | 5 | 4 | 0 | 2 | 24 | 5 | 0 | 5 | 4 | 32 | 46.9 | 38.0 | 6 | 2 | 0 | 0 | 52 | 136 | 3 | 6.7 |
| 17 | Two | 1455 | 6 | 3 | 0 | 2 | 12 | 6 | 0 | 6 | 4 | 32 | 45.5 | 36.5 | 7 | 4 | 3 | 0 | 48 | 146 | 3 | 8.2 |
| 18 | Three | 1327 | 11 | 5 | 0 | 1 | 8 | 8 | 0 | 11 | 4 | 36 | 36.9 | 31.0 | 14 | 7 | 0 | 0 | 48 | 146 | 3 | 14.3 |
| 19 | Three | 1396 | 12 | 3 | 0 | 7 | 24 | 5 | 0 | 12 | 4 | 36 | 38.8 | 40.5 | 9 | 1 | 0 | 0 | 0 | 166 | 3 | 12.2 |
| 20 | Three | 1487 | 5 | 3 | 0 | 7 | 20 | 5 | 0 | 5 | 4 | 27 | 55.1 | 43 | 5 | 3 | 0 | 0 | 61 | 147 | 3 | 6.7 |
| 21 | Four | 1519 | 3 | 0 | 0 | 3 | 12 | 8 | 0 | 3 | 4 | 41 | 37.0 | 34 | 11 | 5 | 0 | 0 | 92 | 169 | 3 | 7.2 |
| 22 | Four | 1507 | 4 | 3 | 0 | 2 | 4 | 6 | 0 | 4 | 4 | 37 | 40.7 | 40 | 9 | 4 | 0 | 0 | 45 | 227 | 3 | 6.6 |
| 23 | Four | 1569 | 3 | 1 | 0 | 3 | 6 | 6 | 0 | 3 | 4 | 33 | 47.5 | 49 | 7 | 3 | 7 | 1 | 53 | 161 | 3 | 5.7 |
| 24 | Four | 1485 | 3 | 2 | 0 | 2 | 5 | 11 | 0 | 3 | 4 | 27 | 55.0 | 53 | 1 | 1 | 0 | 0 | 53 | 205 | 3 | 9.4 |
| 25 | Four | 1566 | 4 | 3 | 0 | 4 | 8 | 7 | 0 | 4 | 4 | 29 | 54.0 | 50 | 6 | 3 | 0 | 0 | 70 | 177 | 3 | 7.0 |
| 26 | Four | 1529 | 3 | 2 | 0 | 1 | 4 | 6 | 0 | 3 | 4 | 22 | 69.5 | 70.0 | 3 | 0 | 11 | 0 | 72 | 242 | 3 | 5.9 |
| 27 | Four | 1365 | 3 | 3 | 0 | 2 | 4 | 4 | 0 | 3 | 4 | 24 | 56.9 | 50.0 | 4 | 2 | 0 | 0 | 84 | 166 | 3 | 5.1 |
| 28 | Four | 1477 | 4 | 2 | 0 | 2 | 5 | 6 | 0 | 4 | 4 | 31 | 47.6 | 41 | 6 | 2 | 0 | 0 | 96 | 178 | 3 | 6.8 |
| 29 | Four | 1236 | 2 | 2 | 0 | 1 | 3 | 7 | 0 | 2 | 4 | 18 | 68.7 | 66.5 | 2 | 0 | 0 | 0 | 65 | 268 | 3 | 7.3 |
| 30 | Five | 1327 | 6 | 5 | 0 | 3 | 8 | 7 | 0 | 6 | 4 | 26 | 51.0 | 45.0 | 4 | 3 | 0 | 1 | 65 | 197 | 3 | 9.8 |
| 31 | Five | 1545 | 4 | 2 | 0 | 2 | 13 | 6 | 0 | 4 | 4 | 30 | 51.5 | 44.0 | 8 | 3 | 0 | 1 | 64 | 126 | 3 | 6.5 |
| 32 | Five | 1550 | 5 | 3 | 0 | 2 | 10 | 10 | 0 | 5 | 4 | 27 | 57.4 | 53 | 3 | 2 | 0 | 0 | 54 | 119 | 3 | 9.7 |
| 33 | Five | 1460 | 5 | 3 | 0 | 3 | 11 | 7 | 0 | 5 | 4 | 27 | 54.1 | 55 | 8 | 2 | 0 | 0 | 55 | 138 | 3 | 8.2 |
| 34 | Five | 1524 | 6 | 4 | 0 | 0 | 6 | 7 | 1 | 6 | 4 | 45 | 33.9 | 30 | 15 | 5 | 6 | 0 | 82 | 152 | 3 | 8.5 |
| 35 | Five | 1380 | 5 | 1 | 0 | 1 | 7 | 7 | 1 | 5 | 4 | 27 | 51.1 | 49 | 2 | 1 | 0 | 0 | 70 | 152 | 3 | 8.7 |
| **Whole book** | | 53732 | 158 | 100 | 2 | 89 | 308 | 234 | 9 | 158 | 140 | 1071 | 50.2 |  | 222 | 82 | 39 | 10 | 2232 | 5552 | 105 | 7.3 |
| **Part One** | | 10425 | 33 | 26 | 1 | 16 | 44 | 43 | 2 | 33 | 28 | 208 | 50.1 |  | 51 | 19 | 4 | 3 | 539 | 904 | 21 | 7.3 |
| **Part Two** | | 15582 | 37 | 27 | 1 | 27 | 104 | 62 | 0 | 37 | 40 | 295 | 52.8 |  | 50 | 15 | 11 | 3 | 564 | 1512 | 30 | 6.4 |
| **Part Three** | | 4210 | 28 | 11 | 0 | 15 | 52 | 18 | 0 | 28 | 12 | 99 | 42.5 |  | 28 | 11 | 0 | 0 | 109 | 459 | 9 | 10.9 |
| **Part Four** | | 13253 | 29 | 18 | 0 | 20 | 51 | 61 | 0 | 29 | 36 | 262 | 50.6 |  | 49 | 20 | 18 | 1 | 630 | 1793 | 27 | 6.8 |
| **Part Five** | | 8786 | 31 | 18 | 0 | 11 | 55 | 44 | 2 | 31 | 24 | 182 | 48.3 |  | 40 | 16 | 6 | 2 | 390 | 884 | 18 | 8.5 |
