# Steadfast Men: The Way of Godly Men

**Byline:** Wes Hart
**Status:** Internal rewrite repository. Not for publication. Not for distribution.

This repo holds the revised manuscript produced from the buyer-panel bounce, the Wes Hart persona brief, and the research pack. It is a working repo for the editorial team only. Nothing in it is release-ready, and nothing in it should be pushed to a printer, a retailer, a newsletter, or a jacket designer without a separate, explicit sign-off.

## What this repo is for

- Hold the full revised manuscript, chapter by chapter, as markdown.
- Track every change against the panel's digs in `book/CHANGELOG.md`.
- Keep proposals for the Aaron-locked files separate from the manuscript so nothing locked is silently overwritten.

## What this repo is not for

- No publishing. No PR to a production pipeline. No spend on design, printing, or promotion.
- No jacket copy. The buyer-panel verdicts (Caleb, Marcus, Drew, James, Earl) are internal context only and must never appear as blurbs, pull quotes, or marketing lines.
- No reprints of other authors' material. Every chapter here is original prose built on our own structure. The four marks sentence is the one locked sentence; everything around it is original.

## Layout

```
book/
  00-dedication.md        LOCKED stub (Aaron-locked; proposals only)
  00-contents.md          LOCKED stub (Aaron-locked; proposals only)
  00-introduction.md      LOCKED stub (Aaron-locked; proposals only)
  01-a-quiet-tuesday.md   LOCKED stub (Aaron-locked; proposals only)
  02-you-are-not-crazy.md LOCKED stub (Aaron-locked; proposals only)
  03-...  through  35-... Full revised original chapters (33 chapters, about 95,900 words)
  CHANGELOG.md            Every change mapped to the bounce digs, extras, scripture handling,
                          production flags, verification, open decisions for Aaron
  proposals/              Proposed edits for the five locked files (never applied to book/)
```

## The five locked files

`00-dedication`, `00-contents`, `00-introduction`, `01-a-quiet-tuesday`, and `02-you-are-not-crazy` are Aaron-locked. The files in `book/` for those five are short stubs that say so. All suggested changes live in `book/proposals/` and are summarized in `book/CHANGELOG.md` section 6. Do not paste proposal text into the locked files. That decision belongs to Aaron.

## Manuscript conventions

**Four marks (locked sentence).** A real man rejects passivity, accepts responsibility, leads courageously, and expects the greater reward, God's reward. This sentence appears verbatim (chapters 3, 19, 29, 35) and is never paraphrased into a competitor's phrasing.

**Parts.**

- Part 1 (1-7): The man you were built to be
- Part 2 (8-17): What you inherited, and what is yours
- Part 3 (18-20): The story that names you
- Part 4 (21-29): The house
- Part 5 (30-35): The long road

**Chapter file shape.** Line 1 is `# N. Title`. Line 3 is the italic part line. Body follows. The closer sits after a horizontal rule at the end of the file.

**Scripture.** NIV only. Full quotations sit in margin blocks, exactly three lines between the fences:

```
:::margin
Genesis 2:15 (NIV)
"The LORD God took the man and put him in the Garden of Eden to work it and take care of it."
:::
```

Short phrases may be quoted inline with the reference in prose. 191 blocks, 240 verses. The production copyright page must carry the standard NIV permission notice (Biblica). Verses were chosen so that no margin quotation contains an em dash; where the NIV text uses one, the quotation is cut before it or a neighboring verse is used.

**Closers.** Every chapter ends with the four-line product: **Name it. / Do this week. / Tell a brother. / Carry this.** Five chapters vary one label on purpose and say so in the closer: 13 "Find a brother," 14 "Ask the man," 29 "Do this year," 32 "Do this season," 35 "Be a brother." Closers run 100 to 160 words so production can render the boxes at an even height.

**Tuesday spine.** Chapter 1 sets the spine: a man's life is decided mostly on ordinary days. Every chapter from 3 on lands at least once on a Tuesday-shaped picture, and the "Do this week" line is always something a man can do before next Tuesday.

**Seasons.** The book speaks to men in every season (single, newly married, under a newborn, divorced, empty nest, retired, widowed, ill) without stamping an age tour into every chapter. Chapter 3 signposts the approach once. Seasons are addressed inside the prose where they change the counsel and gathered deliberately in chapter 32.

**Punctuation.** No em dashes and no en dashes anywhere in the manuscript. Use commas, periods, colons, or parentheses. Verse ranges use a hyphen.

**People in the chapters.** The men named in the chapters are composites with changed names and mixed details: Roy, Tomás, Kenny, Micah, Walt, Anthony, Cole, Hollis, Mr. Pruitt, Mr. Alvarez, Dale, Buck, Ed, the wastewater operator, the young man with four jobs. None is a portrait of a living person, and none borrows another author's biography. Chapter 3 says so in the text. Ages and timelines are harmonized across chapters (see CHANGELOG section 4).

**Author's first-person details.** Kept modest and generic (a grandfather's hands, an old Ford, a rancher outside Post, a man named Buck) so they cannot collide with the Aaron-locked introduction. No wife's name, children's names, hometown, or employer appear.

**Cover direction.** Navy, gold, plumb line. The plumb line runs through chapters 17, 29, 33, and 35 as the book's controlling image. Prose and CHANGELOG reference only. No art lives in this repo.

## Checking the manuscript

Run these from the repo root before any hand-off (bash):

```
# no em or en dashes (should print nothing)
rg -n $'[\u2014\u2013]' book/

# no review-draft or process language in chapters (should print nothing)
rg -n -i "review draft|review copy|working draft|v0\.|lorem|the panel|bounce|manuscript" book/[0-9]*.md | rg -v "AARON-LOCKED|placeholder"

# no borrowed-shelf phrasing (should print nothing)
rg -n -i "battle to fight|adventure to live|beauty to rescue|wild at heart|have what it takes|will to obey|woman to love|modern-day knight" book/[0-9]*.md

# closer labels: four per chapter, 03 through 35
for f in book/[0-3][0-9]-*.md; do printf "%s " "$f"; rg -c '^\*\*(Name it|Do this week|Do this year|Do this season|Tell a brother|Find a brother|Ask the man|Be a brother|Carry this)\.\*\*' "$f"; done

# margin fences balanced
for f in book/[0-9]*.md; do o=$(rg -c '^:::margin' "$f"); c=$(rg -c '^:::$' "$f"); [ "$o" != "$c" ] && echo "UNBALANCED $f"; done
```

## Ownership

Editorial owns `book/`. Aaron owns the five locked files. Production owns footers, closer-box rendering, page padding, small caps, the copyright page, and the crisis-line check; their open items are in `book/CHANGELOG.md` section 7.
