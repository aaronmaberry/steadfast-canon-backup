# Scripture house rule

Bible for Steadfast Men pages: **NIV** (New International Version).

Updated 2026-10-04 for the B-A-A layout Aaron approved. The old margin-block rule is retired (see the changelog at the bottom; the old file is backed up).

## What goes on the page

1. **One anchor verse per chapter, word for word.** It opens the chapter as an epigraph, right under the title. It is the only word-for-word NIV quotation in the chapter. Pick it from verified NIV text and copy it exactly, including the NIV's own capitals and end punctuation (a verse that starts lowercase or ends on a colon stays that way).
2. **Every other passage is narrated in plain words**, in Wes Hart's voice, inside the story. Tell what happened or what was said. Do not put a translation's wording in quote marks. Short, well-known spoken lines (for example "It is finished") may appear in a carry line or a Your Turn prompt only when the chapter can't say its point without them.
3. **Cite in the back, not in the prose.** No "(Genesis 2:15)" in body text. Every narrated passage gets an entry in the chapter's Scripture notes, keyed by a phrase that appears on the page.
4. The body may refer to the anchor ("the line at the top of this chapter") without quoting it again.

## Manuscript marks

Epigraph, right after the `# N. Title` line:

```
:::epigraph
Be on your guard; stand firm in the faith; be courageous; be strong.
1 Corinthians 16:13
:::
```

Line 1 is the NIV text. Line 2 is the reference (no "NIV" on the page; the notes say it). The binder sets it verbatim, italic, with no dash or quote changes.

Scripture notes (back of book, `39-scripture-notes.md`), one section per chapter:

```
## 3. The Four Marks

Opening verse: 1 Corinthians 16:13 (NIV).

"a phrase copied from the page": Book chapter:verse.
```

The phrase must appear on the page exactly as typed (inner double quotes become single quotes in the key).

## Do not

- Invent wording
- Quote a different English Bible and label it NIV (if a note mentions another translation's wording, name that translation in the note)
- Put more than one word-for-word NIV quotation in a chapter
- Dump a verse salad
- Leave a narrated passage out of the notes

## Publish later

NIV is Biblica copyright. The copyright page carries the standard NIV permission notice. The Scripture notes intro points to it. Do not spend on a license until Aaron says.

## Changelog

- 2026-10-04 (Aaron approved the B-A-A structure, 7:32 AM CT). Replaced the margin-block rule (NIV word for word in a `:::margin` block beside every cited verse) with one epigraph anchor per chapter, plain-words narration for every other passage, and back-of-book Scripture notes keyed by phrase. New `:::epigraph` mark. `:::margin` is retired for chapter text. Backup: `/workspace/backups/baa-rules-2026-10-04/SCRIPTURE.md.pre-baa`.
