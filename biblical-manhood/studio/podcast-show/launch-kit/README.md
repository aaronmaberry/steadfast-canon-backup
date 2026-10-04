# Walk Steadfast launch kit

Built 2026-10-03. Nothing here has been uploaded, submitted or published.

| Path | What it is |
|---|---|
| `SPEC.md` | Apple Podcasts requirements, checked on Apple's pages with links. Covers audio, loudness, artwork, RSS and episode fields, transcripts, chapters and video. Also has the host note (parked) and the export settings used for every episode. Read the AI-rule section at the top first. |
| `SHOW-DESCRIPTION.md` | The show description for Apple, Spotify, YouTube and the feed, ending with the locked disclosure line (show bible section 13) |
| `EPISODE-TEMPLATE.md` | Fill-in template for each episode's metadata, description, show notes, chapters and links |
| `art/walk-steadfast-art-A-3000.jpg` / `.png` | **Recommended show cover.** The banner-09 ranch-road photo, full bleed, with the wordmark in the sky. |
| `art/walk-steadfast-art-B-3000.jpg` / `.png` | Type only. Wordmark and tagline on near-black, with a road line to the horizon. |
| `art/walk-steadfast-art-C-3000.jpg` / `.png` | The photo cropped closer on the man, boy and oak, with a dark top and the tagline |
| `art/contact-sheet.jpg` / `.png` | All three variants, plus 150, 90 and 60 px thumbnails on dark and light backgrounds |
| `E001/` | E001 package: metadata, description, show notes, chapters (JSON and text) and transcripts (VTT and SRT) built from the final audio |
| `_build/` | Scripts that rebuild the art and contact sheet |

## Why art A

- Of the three, A reads best at 60 px. STEADFAST stays legible on both dark and light backgrounds.
- It's the same photo, wordmark, Geist type and periwinkle rule as the live YouTube banner, so the show looks the same everywhere.
- The figures are seen from behind at dusk, so no face is shown.
- B is the cleanest at full size but has no picture to set it apart in a grid. C's tagline gets too small to read below about 150 px.

All art files are 3000 x 3000, RGB, 72 dpi, with no alpha channel, which meets Apple's spec. Upload the JPG.
