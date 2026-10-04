# Shell Pass Notes

Pass: ebook shell rewrite for *Steadfast Men: The way of Godly Men* by Max.
Scope: front matter, back matter, TOC, introduction, repo README. Body chapters were out of scope for this pass.

## State of the repo before this pass

The repository contained only a seeded README. The `book/` directory did not exist, and none of the 35 body chapter files were present on any branch. Everything under `book/` was created in this pass.

Consequences of that:

- **No "Wes Hart" byline changes were made** because there was no chapter text to search. When the chapter files land, run a search for `Wes Hart` and `Hawks` across `book/` and correct any author self-reference to Max without rewriting the chapter. See the checklist at the bottom.
- **The TOC uses provisional chapter titles.** They follow the problem-to-framework-to-action arc described in the brief and are flagged with an HTML comment at the top of `00-contents.md`. Replace them with the actual chapter titles before typesetting. Nothing else in the shell depends on those exact titles.
- **The condensed training references chapter numbers, not titles.** The week-to-chapter mapping assumes roughly chapters 1 to 8 name the problem, 9 to 22 build the frame, and 23 to 35 apply it. Adjust the *Read* lines once the real chapter breakpoints are known.

## Files created

| File | Purpose |
| --- | --- |
| `book/00-half-title.md` | Title only. |
| `book/00-title-page.md` | Steadfast Men / The way of Godly Men / Max, with imprint line and walksteadfast.com. |
| `book/00-copyright.md` | © 2026 Max / Steadfast Men, walksteadfast.com, ISBN TBD, Scripture notice placeholder, Robert Lewis sentence-shape acknowledgment, standard disclaimer. |
| `book/00-dedication.md` | Wife, two children, the men who kept a chair. Generic, no locations. |
| `book/00-contents.md` | Spaced TOC, bold titles, no Part-number scaffolding. |
| `book/00-introduction.md` | Full introduction written to the Aaron locks. |
| `book/36-about-the-author.md` | Max bio with masked background and CTA line. |
| `book/37-condensed-training.md` | How-to-use section, 24-week map (Read / Anchor / Ask / Do), finish note, full-class CTA. |
| `book/SHELL-PASS-NOTES.md` | This file. |
| `README.md` | Replaced seeded README with project overview, structure, build notes, style rules. |

## Aaron locks and where each is satisfied

1. **TOC breathing room, bold titles, no dense Part scaffolding.** `00-contents.md` puts a blank spacer between every entry, bolds every chapter title, and uses a double spacer instead of Part headings to mark the three movements. No Part numbers appear.
2. **Intro "Who I'm writing to" uses seasons, lands fast, fewer ages.** The section names seven seasons (newly married, thick of it with young kids, raising teenagers, kids grown, single, starting over, and a catch-all) in one short paragraph each. One age reference remains in the opening story ("in his thirties") because it describes a specific man, not the reader.
3. **Intro does not outline chapter numbers.** No chapter numbers appear anywhere in the introduction. Chapter names were not used either, so the intro survives title reconciliation without edits.
4. **Intro "How the book is built" is start-to-finish narrative, no Part labels.** The section walks the reader through the opening, middle, and close as one continuous argument. The words "Part 1," "Part 2," and "Part 3" do not appear.
5. **"One more thing before you start" is honest about the training.** States plainly that Steadfast Men is also a 24-week training, that the book grew out of it, that the condensed version is in the back, that the full class guide is at walksteadfast.com, and that the book stands alone and requires no further purchase.
6. **Word count not cut for length.** Nothing was trimmed to hit a target. The introduction runs long by design.
7. **Book is buyable standalone; training is a separate purchase path.** Stated in the introduction, restated in the closing CTA of `37-condensed-training.md` ("It is a separate purchase, and it is not required"), and echoed in `36-about-the-author.md`.

## Product constraints

- **Byline:** Max, one name, everywhere. No Wes Hart. No Tim Hawks.
- **Bio:** husband, dad of two, Texas, technology and leadership by day, teaches men. No employer, city, or church named.
- **Four marks:** unchanged. "A real man rejects passivity, accepts responsibility, leads courageously, and expects the greater reward, God's reward."
- **Robert Lewis:** credited only as origin of the sentence shape, once in the introduction and once on the copyright page. No Hawks or One Mission material reprinted or referenced.
- **No em dashes:** verified by search across `book/` and `README.md`. En dashes also avoided. Scripture ranges use "through" instead of a dash.
- **No AI sheen:** plain sentences, concrete detail, no filler transitions.
- **Original only:** all stories, teaching, and training material written fresh for this pass. No spend, no publish.

## Ordering decision

The brief's shell structure lists back matter as Condensed Training, then About the Author, then CTA. The deliverable filenames were `36-about-the-author.md` and `37-condensed-training.md`. This pass followed the filenames. Result: About the Author comes first, then the Condensed Training, which ends with the full-class CTA so the reader closes the book on the invitation. If the other order is preferred, swap the two file numbers and the two TOC lines. No content changes are needed.

No separate conclusion file was created. Chapter 35 is expected to close the body.

## Open items for the next pass

- [ ] Drop the 35 body chapter files into `book/` as `01-*.md` through `35-*.md`.
- [ ] Search chapter text for `Wes Hart` and `Hawks`. Change author self-references to Max. Do not rewrite chapters.
- [ ] Replace provisional TOC titles with real chapter titles.
- [ ] Confirm the chapter breakpoints and adjust *Read* lines in the condensed training.
- [ ] Fill in the Scripture translation on the copyright page and confirm the permission notice wording for that translation.
- [ ] Add ISBNs when assigned.
- [ ] Cover and interior design credits.
- [ ] Decide whether the front-matter files should be renumbered (00a, 00b, and so on) for the build tool, or whether the build script should list them explicitly in order.
