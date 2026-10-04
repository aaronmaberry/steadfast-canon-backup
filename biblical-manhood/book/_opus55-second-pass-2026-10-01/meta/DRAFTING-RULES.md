# Drafting rules: Opus 5.5 IP rewrite, 2026-10-01

Working rules given to every chapter writer on this pass. Kept as part of the drafting history (brief §3.14). Source of authority: `OPUS55-REWRITE-BRIEF.md` (2026-10-01) plus the 2026-10-01 CANON, persona and TOC.

## Paths

- Base (read only): `biblical-manhood/book/_grok47-panel-rev-2026-09-25/book/NN-*.md`
- Output (write only here): `biblical-manhood/book/_opus55-ip-rewrite-2026-10-01/book/NN-*.md`, same file name.
- Persona (2026-10-01, wins over repo copies): `/workspace/uploads/STEADFAST-AUTHOR-PERSONA_3d24.md`
- Canon (2026-10-01): `/workspace/uploads/CANON_05ef.md`
- Chapter cards (chapter job only; ignore any card line that carries the old creed or says "four marks unchanged"): `biblical-manhood/book/NN-card.md`
- Checks: `python3 biblical-manhood/book/_opus55-ip-rewrite-2026-10-01/meta/tools/checks.py sweep|sim|ngram FILE.md`
- Do **not** open `biblical-manhood/transcripts/`, `briefs/`, `notes/`, `PHD-MASTERY.md`, `FRAMEWORK.md`, or anything under `studio/`, `training/`, the 9/23 Opus wave files in `book/` root, `_grok47-unslop-2026-09-21/`, or `style/UNSLOP.md`. The transcripts are reference only, and this pass does not need them. Not reading them is part of the independent-creation record.
- No git operations. No edits outside the output folder.

## What "rewrite" means here

Write the chapter fresh, in the starred persona's voice, from the base chapter. Keep:
- the H1 line exactly (`# N. Title`, title unchanged);
- the chapter's job (its card's "One job");
- the people already on the page (Roy, Tomás, Kenny, Micah, Eli, Owen, Anthony, Walt, Dale, Cole, Hollis, Mr. Pruitt, Ray, Cal, etc.), their facts, and the scenes and pictures that are Steadfast's own;
- the short panel-protected lines listed for your chapter below (verbatim);
- the panel-rev fixes listed for your chapter below;
- the Scripture margin blocks (same references), converted to the locked format;
- the closer shape and its season branches;
- the `## Before you turn the page` section with its closing blessing (fresh words).

Change: every sentence of prose. New sentences, new rhythm, the persona's warmth. Section `##` heads may be renamed. Reorder within the chapter if it reads better. Scripture and the protected lines should be the only verbatim carryover. Self-check with `checks.py sim`; aim for a similarity at or under about 0.30.

Voice (persona): warm first, then one clean hit, stay with it, then a next move a man can do this week. Every season in the room (19, single, married, divorced, widowed, older, high performer). Contractions. Short and long sentences mixed. Concrete nouns. A little mess. He tells on himself first, but **do not invent new Wes Hart biography** (no new facts about his father, wife, kids' names, hometown, job, past career). Keep first-person anecdotes at the level the base already has. No stacked "Maybe / Maybe / Maybe." No tidy three-beat buttons. No "If that sounds heavy, good." No "Let's dive in." Lists are scaffolding, not personality. Humor only where the cluster allows (almost none in father wound, depravity, crisis sexuality). Never wife-as-dummy, mom-as-villain, young-man-as-joke, older-man-as-mascot.

Never import (persona fences): Ted Cunningham bits (parking lot, Andes, mint leaf, Macchiato, GM of the universe, "show up naked", crockpot candle, "for a good time, call home", unlimited data, Chip Gaines), Red Rocks lines ("make heaven more crowded", "imperfect people / perfect God", "free me from me", "kill the control freak", "flip the FOMO", "scripture before smartphone", jet ski, Scuba Steve, jam study, MURPH vest, "wild man"), any Tim Hawks family story, Mead, Keillor, Newsweek, Levinson, Wild at Heart material.

## The four marks (locked 2026-10-01)

| # | Mark | Verse | One line |
|---|---|---|---|
| 1 | **Stop Waiting** | James 4:17 | When it's yours to do, start now, before you feel like it. |
| 2 | **Pick Up the Weight** | Galatians 6:5 | Carry what's yours, even when somebody else dropped it. |
| 3 | **Go First** | John 10:4 | Step out ahead of your people, scared or not. |
| 4 | **Work for God's Pay** | Colossians 3:23-24 | Do it for the Lord's reward, not the room's applause. |

Creed: "A steadfast man stops waiting, picks up the weight, goes first, and works for God's pay, not the room's."

- **The full creed may appear only in:** intro (1), ch3 (at most 2), ch7 (1), ch34 (1, top line of the plan), ch35 (1), back cover (1). **Nowhere else.** Ch27 and ch32 used to carry it: take it out and say the point in fresh words.
- Don't recite all four mark names as a stock tagline. If a chapter leans on one mark, name it by its title plainly, in Title Case, e.g. "That's Stop Waiting, in a marriage." Bold is optional on a first mention. Don't start a line with it in bold if it could be mistaken for a closer label (it can't, but don't start any prose line with a bold closer label).
- Keep the label "four marks" where useful. "No fifth" is ours and may stay where the base had it.
- The opener is "A steadfast man...", never "A real man...".
- Never use "Go First" (or "Four Marks") as the name of a product, course, podcast, workbook, or series.
- **God's pay = inheritance (required wherever pay or reward carries weight).** The pay is the inheritance the Lord gives his children (Col 3:24, "an inheritance from the Lord as a reward"). It is grace-given. It is never wages that earn salvation (Eph 2:8-10; Rom 6:23; Rom 8:17). The picture is a son's inheritance and the Father's "well done" (Matt 25:21), not a paycheck you bargain for. There must be **no** sentence a reader could take as "work hard and God will save you." Write one plain anchor sentence in any chapter where pay/reward carries weight (ch30, 32, 33, 35 at minimum), e.g. "Nobody earns an inheritance. You get one because you're in the family, and in Christ you are." If you cite a verse reference (book chapter:verse) in prose, it needs a margin block right after it; a plain-words anchor or a callback to chapter 7 is fine without one.

## Banned wording (zero tolerance; `checks.py sweep` must show 0 SWEEP hits and 0 extra hits)

The sweep regex is case-insensitive and catches substrings, so these words are out even in innocent use:
- `rejects passivity`, `accepts responsibility`, `leads courageously`, `greater reward`, `God's reward`, `invests eternally` (any tense), and the imperatives "Reject passivity. Accept responsibility. Lead courageously. Expect God's reward."
- `real man` (anywhere, including "a real man's", "the real man"). Use "a steadfast man", "a grown man", "a godly man", "the man".
- `Better Man` (so no "be a better man", "a better man"). Say "a man who's further along", "the man you want to be".
- `knight` (so **no "weeknight"/"weeknights"**: say "a school night", "on a Tuesday night", "any night of the week"), `squire`.
- `Lewis` (no C. S. Lewis either), `Little Rock`, `Men's Fraternity`, `Authentic Manhood` (and "authentic man"), `Fellowship Bible`, `Modern-Day Knight`.
- Synonym rebuilds of Lewis's four: no "refuses inaction", "embraces duty", "owns responsibility", "leads with courage", "courageous leadership", "expects a reward", "invest in eternity". No noun rail of the four (PASSIVITY / RESPONSIBILITY / COURAGE / REWARD) presented together as the marks. Ordinary words like "passive", "passivity", "courage", "responsible" are fine one at a time when describing the sin or the virtue; just never rebuild his four phrases or pair them up as the marks.
- Course sub-points: no "three things every son needs from his father"; no conventional-vs-authentic manhood contrast list; no "bearers of destiny" / "nurturers of life"; no "a will to obey, a work to do, a woman to love"; no "direction, protection, provision" triad under leading (don't list those three together); no age-banded life-stage map (spring/summer/fall/winter, 0-22, 17-45), no Hebrew stage names (adam/zakar/gibbor/enosh/ish/zaken) on this pass; no "manhood ceremony"; no knight/page/squire/stage language; no "code" / "cause" triad in the son chapters (the words "code" and "cause" should not appear at all in ch27-29; "because" is fine).
- "Gave it to us" style handoff phrasing: never.
- **No em dashes or en dashes.** Use commas, periods, colons, parentheses.

## Locked format (the binder parses this)

- Line 1: `# N. Title` exactly as the base. Sections use `##`. No `###` unless the base had it.
- Scripture block, immediately after the sentence that cites it, in exactly this form (bold ref line with `NIV`, no parentheses, no wrapping quotation marks around the verse; inner quotation marks that are part of the NIV text stay as double quotes, nested ones as single):

```
:::margin
**James 4:17 NIV**
If anyone, then, knows the good they ought to do and doesn't do it, it is sin for them.
:::
```

- Keep the NIV text exactly as the base has it (only strip the outer wrapping quotes and fix the ref line). Do not paraphrase inside a margin block. Do not add new verses unless your chapter notes say so; if you think one is needed, add it and list it in your report. The parent agent verifies every block against the NIV 2011.
- Closer, at the end, exactly:

```
## Your Turn

---

**Name it**

Because ... (one or two sentences, then the ask; season branches where the base had them)

:::notes
_______________________________________________
_______________________________________________
:::


**Do this week**

Because ...

:::notes
_______________________________________________
_______________________________________________
:::


**Tell a brother**

Because ...

:::notes
_______________________________________________
_______________________________________________
:::


**Carry this**

One screenshot-able sentence (two short ones at most).
```

  Ch35 uses `**Be a brother**` in place of `**Tell a brother**`. `Carry this` gets **no** `:::notes` block. The first three each open with "Because". Fresh wording for every closer line; keep its job and its season branches (single, divorced, no son/daughter, etc.).
- Never start a non-closer prose line with `**Name it`, `**Do this week`, `**Tell a brother`, `**Be a brother`, `**Carry this` (bold or not). The binder will treat it as a closer.
- No images, no HTML, no tables, no bullet lists in chapter prose (the binder joins lines; keep to paragraphs).
- Length: keep each chapter within about ±5% of its base word count (`checks.py sim` prints before/after). Numbered chapters stay under about 2,050 words total including the closer.

## Report back (per chapter)

1. File written, before/after words, similarity.
2. One or two lines: what changed.
3. Which mark(s) the chapter names, and how many times.
4. Every sentence where pay/reward carries weight, and the anchor sentence that makes it inheritance/grace (quote it, with line number).
5. Margin blocks: list refs; any added or removed and why.
6. Anything unsure (a line you are not sure is original enough, a panel fix you had to bend).
7. Output of `checks.py sweep FILE` (must be clean).

> **Override, 2026-10-03 (Aaron):** "I actually hate how every chapter ending ... starts with 'because.'" The closer sections no longer open with "Because". Name it, Do this week, Tell/Be a brother each open with a plain statement of the reason, worded differently each time. Do not reintroduce a "Because" opener, or any single replacement word (Since, That's why, etc.), as a pattern. This supersedes the "Because ..." template lines above.
