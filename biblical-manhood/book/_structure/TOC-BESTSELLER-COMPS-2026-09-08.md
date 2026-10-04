# TOC bestseller comps — Steadfast Men

Date: 2026-09-08  
Sources: public TOC samples / chapter lists for Atomic Habits, Extreme Ownership, Dare to Lead, Deep Work, Wild at Heart; trade design notes on print TOC hierarchy. No spend. Internal structure brief.

Canonical chapter order: `BOOK-TOC.md` (decided 2026-08-27) and live `book/00-contents.md` (A Quiet Tuesday → These Men Are My Brothers, plus About + Condensed Training).

---

## 1. How bestsellers group chapters

Bestsellers treat the TOC as a map, not a decoration. Grouping is visual and typographic — never markdown hashtags, emoji, or ornamental # symbols.

### Pattern: labeled PART / SECTION bands

| Book | Grouping device | Typical band size |
| --- | --- | --- |
| Atomic Habits (Clear) | Six PART labels (Fundamentals; four Laws; Advanced Tactics) | 3–4 chapters per part |
| Extreme Ownership (Willink / Babin) | Three PART / SECTION labels (Winning the War Within; Laws of Combat; Sustaining Victory) | 4 chapters per part |
| Dare to Lead (Brown) | Four PART labels; Part One further split into named Sections | Uneven (Part One dominates) |
| Deep Work (Newport) | Two PART labels (The Idea; The Rules) | 3 chapters, then 4 “Rules” |
| Wild at Heart (Eldredge) | Printed Contents is a flat CHAPTER list (no PART heads on the TOC page itself); narrative arc still moves in three movements | 12 chapters + epilogue / appendix |

**Takeaway for Steadfast Men:** Prefer Extreme Ownership / Atomic Habits style — short PART labels above clusters of chapter titles. Christian men’s trade often uses either Eldredge’s flat numbered list *or* Willink-style PART bands; with 35 body chapters, PART bands are required for scanability.

### How the grouping is set (print conventions)

- **PART labels** sit above their chapter cluster. Trade books commonly set them in **small caps** (or short all-caps with modest tracking), often lighter weight or a slightly smaller size than chapter titles — or the reverse: PART slightly larger / letterspaced, chapters regular. Either works if hierarchy is consistent.
- **Blank space** does the heavy lifting: extra leading *before* each PART label (and sometimes a thin hairline or nothing at all). Space between chapters inside a part stays tighter than space between parts.
- **No hashtags.** “PART ONE” or “Part I · The Man You Were Built to Be” — never `# Part 1` and never decorative hash ornaments.
- **Title of the page** is usually **Contents** (not “Table of Contents”).
- **Chapter lines** are title case (or sentence case for long titles), optionally preceded by arabic chapter numbers. Page numbers right-aligned with leaders when typeset for print.
- **Front / back matter** (Introduction, About, appendix-style training) sit outside PART numbering — same pattern as Atomic Habits intro/conclusion and Wild at Heart About / Appendix.

### Visual hierarchy that reads fast

1. Page title: Contents  
2. Front matter entries (Dedication, Introduction) — unnumbered or roman  
3. PART label (small caps) + blank line  
4. Chapter titles (regular or semibold) with optional numbers  
5. Extra blank band → next PART  
6. Back matter (About the Author, Condensed Training) — not PART VI

That blank-band rhythm is what Extreme Ownership and Atomic Habits share: the eye lands on PART, then skims titles.

---

## 2. What to avoid

- **Markdown / web leftovers in print TOC:** `#`, `##`, emoji bullets, checkbox glyphs, “---” as decoration.
- **Gold `#E3C572` on bone `#E6DDCC` for PART labels or chapter type.** Measured contrast ≈ **1.25:1** — fails WCAG AA (4.5:1) and AAA (7:1). Matches existing FLOW rule: gold only on navy, never gold-on-bone body/accent type.
- **One flat 35-line dump** with no PART labels and no extra inter-part leading — hard to scan; unlike Wild at Heart’s 12-chapter list.
- **Too many TOC levels** (PART → Section → Chapter → subsection). Dare to Lead can carry nested sections because Part One is the book; Steadfast Men should stop at PART + chapter.
- **Long all-caps chapter titles** — slows reading; reserve small caps / tracked caps for short PART labels only.
- **Course / brand clutter in the TOC** (program names, cohort labels, “Hawks,” Lewis reprints, marketing CTAs). Keep Contents literary; put training map in Condensed Training.
- **Crowded leading** — single-spaced chapter stacks with no breath between parts look amateur next to Clear / Willink / Newport.
- **Inconsistent numbering** — either number every body chapter 1–35 or omit numbers everywhere; do not mix.

---

## 3. Concrete TOC grouping for Steadfast Men

Use the decided five PART titles from `BOOK-TOC.md`. Set PART labels in small caps (or short tracked caps). Use **extra blank space before each PART** — not hashtags. Keep Dedication / Introduction above Part 1; About + Condensed Training below Part 5.

### Recommended Contents layout (typesetting brief)

```
Contents


Dedication

Introduction


PART ONE
The Man You Were Built to Be

  1.  A Quiet Tuesday
  2.  You Are Not Crazy
  3.  The Four Marks
  4.  Stop Waiting
  5.  Pick Up the Weight
  6.  Go First
  7.  Live for a Reward That Lasts


PART TWO
What You Inherited, and What Is Yours

  8.  The Empty Chair
  9.  Anger, the Itch, and the Drift
 10.  The Father Who Does Not Leave
 11.  When Home Never Handed You Off
 12.  Leave Without Slamming the Door
 13.  A Man With No Brothers
 14.  Ask the Man
 15.  The Problem Inside
 16.  How That Looks on a Man
 17.  No North Star


PART THREE
The Story That Names You

 18.  Before the Fall
 19.  Two Men, Two Ways
 20.  Destiny Is Not a Vibe


PART FOUR
The House

 21.  If There Is No Wife Yet
 22.  Know Her
 23.  Lay It Down
 24.  What She Actually Needs
 25.  The Bed Is a Covenant
 26.  Your Daughter Is Watching
 27.  Give Your Son a Name
 28.  Give Your Son a Hill
 29.  Give Your Son a Day He Will Not Forget


PART FIVE
The Long Road

 30.  You Were Made for a Work
 31.  Feelings Are the Dash, Not the Wheel
 32.  Every Season Still Counts
 33.  What You Are Building When Nobody Claps
 34.  Write the Next Move
 35.  These Men Are My Brothers


About the Author

Condensed Training
```

### Why this grouping

| Part | Chs | Comp parallel | Job for the reader |
| --- | --- | --- | --- |
| One | 1–7 | Atomic Habits “Fundamentals” / Extreme Ownership “Winning the War Within” | Wake-up + framework (four marks) |
| Two | 8–17 | Extreme Ownership “Laws” density; Wild at Heart wound / father arc | Inheritance, wound, brothers, drift |
| Three | 18–20 | Deep Work short “Idea” band | Gospel naming — short, weighty |
| Four | 21–29 | Dare to Lead skill-cluster length | House: wife, bed, daughter, son |
| Five | 30–35 | Extreme Ownership “Sustaining Victory” | Long obedience + brotherhood close |

**Band sizes (7 / 10 / 3 / 9 / 6)** match bestseller practice: uneven is fine when thematic. Do not force equal chapter counts.

**Markdown manuscript note:** In `00-contents.md`, represent PART heads as plain text or emphasis — never `#`. Extra blank lines between parts already match live Contents; add the PART labels themselves so the print TOC and manuscript TOC agree.

**Optional print polish:** PART label in small caps + charcoal or navy ink; chapter titles in body ink; right-aligned page numbers with leaders once pagination is locked.

---

## 4. Colorblind-safe accent hex alternatives to gold on bone

Background: bone `#E6DDCC`  
Rejected for type/accent *on bone:* gold `#E3C572` (≈ **1.25:1** — fails AA/AAA).  
Keep gold for **gold-on-navy** only (≈ **9.86:1**, AAA) — covers, man-plan panels, cloth-store chrome.

### Recommended accents on bone

| Role | Hex | Contrast on `#E6DDCC` | Rationale |
| --- | --- | --- | --- |
| Primary accent / PART labels | Navy `#0B1F38` | ≈ **12.3:1** (AAA) | Already cloth-store canonical; strong luminance split survives deuteranopia / protanopia / tritanopia because separation is value, not hue. |
| Secondary / cooler accent | Deep teal `#134E4A` | ≈ **7.0:1** (AAA) | Distinct from navy by hue *and* still AAA luminance; teal stays separable under common red-green CVD when lightness differs this much from bone. |
| Neutral accent / hairlines / numbers | Charcoal `#2C2C2C` | ≈ **10.4:1** (AAA) | Hue-independent; safest for CVD and low-vision; use for leaders, chapter numbers, quiet rules. |

### Usage rules (align with FLOW contrast pass)

- **On bone:** navy, deep teal, or charcoal for PART labels, rules, and any accent type — never gold.
- **On navy:** gold `#E3C572` or bone `#E6DDCC` remain the warm accents.
- Do not encode meaning by color alone (e.g. “gold = this week”); pair with weight, small caps, or position.
- Verify any new tint with a contrast check before typesetting; target ≥ 7:1 for PART labels (large / short text) and ≥ 4.5:1 for any smaller TOC type.

### Quick pick for Steadfast Men TOC

- PART labels: **navy `#0B1F38`** small caps on bone  
- Chapter titles: body ink / charcoal `#2C2C2C`  
- Optional cool accent (e.g. part-opener ornament or training callout): **deep teal `#134E4A`**  
- Gold: cover and navy panels only

---

## Sources consulted (public)

- Atomic Habits chapter/part lists (Clear; multiple public summaries matching 6 parts / 20 chapters)
- Extreme Ownership part/chapter lists (Willink & Babin; 3 parts / 12 chapters)
- Dare to Lead part/section structure (Brown; 4 parts)
- Deep Work Contents sample (Newport; Part 1 The Idea / Part 2 The Rules)
- Wild at Heart Contents sample PDF (Eldredge / Thomas Nelson; CHAPTER n — Title flat list + About / Appendix)
- Trade TOC design notes: hierarchy, spacing, Contents titling, avoid all-caps long titles
- WCAG relative-luminance contrast math on listed hex pairs (computed 2026-09-08)

