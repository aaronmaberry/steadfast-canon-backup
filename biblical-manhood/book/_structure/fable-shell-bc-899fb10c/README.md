# Steadfast Men
**The way of Godly Men**
by Max

Manuscript repository for the *Steadfast Men* ebook and paperback. The book is a commercial self-help and faith trade title built around a single sentence:

> A real man rejects passivity, accepts responsibility, leads courageously, and expects the greater reward, God's reward.

The book stands alone. It is also the companion to the 24-week Steadfast Men training, which is a separate purchase at [walksteadfast.com](https://walksteadfast.com).

## Repository layout

```
book/
  00-half-title.md          Front matter
  00-title-page.md
  00-copyright.md
  00-dedication.md
  00-contents.md
  00-introduction.md
  01-*.md ... 35-*.md       Body chapters (not yet in this repo)
  36-about-the-author.md    Back matter
  37-condensed-training.md  24-week map and full-class CTA
  SHELL-PASS-NOTES.md       What changed in the shell pass and what is still open
README.md
```

Every manuscript file is plain Markdown so it can be diffed, reviewed, and built into EPUB, PDF, or DOCX with standard tools.

## Reading order

Front matter, then chapters 1 through 35 in order, then About the Author, then the Condensed Training. The introduction asks readers to go start to finish, and the build should preserve that order.

## Building

Nothing in this repository requires a build to read. To assemble a single manuscript, any Markdown concatenation tool works. Example with [pandoc](https://pandoc.org):

```bash
pandoc \
  book/00-half-title.md \
  book/00-title-page.md \
  book/00-copyright.md \
  book/00-dedication.md \
  book/00-contents.md \
  book/00-introduction.md \
  book/[0-3][0-9]-*.md \
  --from markdown --to epub3 \
  --metadata title="Steadfast Men" \
  --metadata subtitle="The way of Godly Men" \
  --metadata author="Max" \
  -o steadfast-men.epub
```

Adjust the glob once the body chapters are added so the front matter is not included twice. The `SHELL-PASS-NOTES.md` file is internal and should be excluded from any build.

## Style rules

- No em dashes or en dashes anywhere in the manuscript. Use commas, periods, colons, or the word "through" for ranges.
- Byline is **Max**, one name. No other author names.
- The four marks sentence is never altered.
- Robert Lewis is credited only as the origin of the sentence shape. No third-party curriculum material is reprinted.
- Plain, direct prose. Concrete detail over abstraction.
- Do not cut for length.

## Status

Shell pass complete: front matter, TOC, introduction, back matter. Body chapters are pending. See `book/SHELL-PASS-NOTES.md` for the full change log and the open-items checklist.

## Contact

[walksteadfast.com](https://walksteadfast.com)
