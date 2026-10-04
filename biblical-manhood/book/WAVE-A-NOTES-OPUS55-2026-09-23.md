# Wave A notes (Opus 5.5 max, UNSLOP), 2026-09-23

Wave A covers the front matter (00-*) and chapters 01 through 08. Each file was rewritten in place in `book/`. Commit `2e9833d` holds the untouched Grok 4.7 source, so `git diff 2e9833d -- book/<file>` shows every change. Chapters 09 through 37 in `book/` are still the untouched source, waiting for Waves B through D.

## Files written

| File | Words (wc -w) | Source | Notes |
| --- | ---: | ---: | --- |
| 00-half-title.md | 6 | 6 | No prose. Unchanged. |
| 00-title-page.md | 24 | 24 | No prose. Unchanged. Wes Hart byline. |
| 00-copyright.md | 300 | 317 | Four-marks note and disclaimer rewritten. Legal text untouched. |
| 00-dedication.md | 110 | 111 | One confusing clause fixed. |
| 00-contents.md | 217 | 217 | Unchanged. Titles and PART order kept. |
| 00-introduction.md | 1,390 | 1,377 | Full rewrite. |
| 01-a-quiet-tuesday.md | 2,031 | 1,997 | Full rewrite. |
| 02-you-are-not-crazy.md | 1,840 | 1,695 | Full rewrite. |
| 03-the-four-marks.md | 1,757 | 1,664 | Full rewrite. |
| 04-stop-waiting.md | 1,946 | 1,885 | Full rewrite. |
| 05-pick-up-the-weight.md | 2,053 | 1,878 | Full rewrite. |
| 06-go-first.md | 2,076 | 1,777 | Full rewrite. |
| 07-live-for-a-reward-that-lasts.md | 1,968 | 1,721 | Full rewrite. |
| 08-the-empty-chair.md | 2,081 | 1,907 | Full rewrite. |

Chapter prose bodies (without headings, Scripture blocks, or closers) run 1,486 to 1,813 words. The Empty Chair is 13 words over the lean guide of about 1,800. I left it long because the persona gives father-wound chapters room.

## Craft changes, every file

- Plain speech with contractions. The source avoided contractions and compressed ideas into noun stacks and inversions ("Sellers were happy to supply pieces," "Door number two came next"). Those are now whole sentences with named actors.
- Antithesis ("It isn't X. It's Y.") cut to about one per chapter. Tidy three-beat buttons broken up. Repeated sentence frames, such as six paragraphs in a row opening with "It borrows," varied.
- Personified and decorative lines restated plainly unless they carried the chapter's one image. One earned joke kept (by dark the couch has hired a lawyer).
- One word held per idea. Weight in Pick Up the Weight, with pack and crushing weight only for Galatians 6. Step over for the stair.
- Chants retired. "Pile" is gone. "The maps' account" is gone. Tuesday now appears only in the introduction and A Quiet Tuesday.
- Chapter titles referenced in prose now sit in straight quotes instead of bold. Closer labels stay bold.
- Lint is clean for em and en dashes, curly quotes, mid-sentence colons, semicolons, the UNSLOP word list, and the persona's never-import list.
- Kept exactly as written. All 29 NIV Scripture blocks match the source byte for byte. The four marks sentence is verbatim everywhere it appears. Every chapter keeps the ch1 closer box, with Because leads and notes lines of 2, 2, 2, and 1.

## Craft changes, by file

- Introduction. Removed "I am not writing against them" and the "wild places" nod, per the 2026-09-14 notes. The list of named men now matches who actually shows up later. Kenny is out and Dale is in.
- A Quiet Tuesday. The Carry this line now reads "The big days only show what the ordinary ones built." The old line said big days "mark" things, which fought the book's own meaning of a mark.
- You Are Not Crazy. The diner scene is now told as a scene. The tailgate moved out so The Four Marks owns that picture.
- The Four Marks. Robert Lewis is no longer named here. The chapter points back to the introduction, per the once-in-the-intro rule. The composite-names paragraph was cut because the introduction and copyright page already cover it. Genesis 3 corrected (Adam stood by, then ate). "Stock tank" changed to a pond so the picture carries no region.
- Pick Up the Weight. In the list of five things, "soul" became "your walk with God," so it no longer contradicts the list of weights that aren't yours.
- Go First. Nehemiah inspected the wall with a few men (Nehemiah 2:12), not alone. Moses did tell Joshua to be strong and courageous (Deuteronomy 31:7) before giving the reason. The eight seconds stay, because Ask the Man calls them back.
- Live for a Reward That Lasts. Mr. Pruitt is now introduced as a widower who planted forty pecan trees past seventy, which sets up his thread in the last chapters. "Parking lot" removed (persona never-import list).
- The Empty Chair. Jesus is no longer described as "marked" by the chair. The unmailed-letter closer no longer promises a callback that no later chapter delivers.

## Flags for Aaron

1. Reopened locks. The intro and ch1 were locked at LISTEN-2 (2026-09-08), and intro through ch3 by the 2026-09-14 notes. This pass rewrote them because the 2026-09-23 brief says to. Their voice, pictures, structure, and closers stay closest to the approved versions. No lock or status files in the repo were edited.
2. Byline and toolchain. Repo docs (AGENTS.md, LOCKS-REGISTER, the 02-voice-style persona) still say "Byline Max" and name Grok 4.6 for copy. The pack persona and this brief say Wes Hart and Opus 5.5. Wave A follows the brief.
3. Kenny. The old intro named him, but he appears in no chapter from 01 to 37. If you want him back, Wave C could give him the divorced father's weekly call in Your Daughter Is Watching or Give Your Son a Name, and he returns to the intro list.
4. The unmailed father letter has no callback yet. Wave B could bring it back in The Father Who Does Not Leave or Leave Without Slamming the Door. If it does, add a forward pointer back into The Empty Chair.
5. For Wave D. About the Author still says "a Texan" and "live in Texas," which breaks the 2026-09-14 rule against Texas as identity.
6. Before any publication, check the NIV permission line against the current required Zondervan and Biblica wording. Also consider adding a crisis line to the disclaimer.
