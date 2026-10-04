# Apple Podcasts spec for Walk Steadfast

Checked against Apple's own pages on 2026-10-03. Each section links the page it comes from. Nothing has been uploaded or submitted.

## Apple's AI content rule (read first)

Apple's content guidelines, section 1.11, cover creators who use AI to generate audio or video, and they name synthetic voices and AI-generated hosts. Those creators "must prominently disclose this to audiences in the content and metadata for each episode and show." Section 1.12 bans using AI to mislead about real events.

Apple says it may label or remove content, or suspend the account, when a show does not meet these guidelines.

The show bible (section 13) records Aaron's locked disclosure of 2026-10-03: "Produced with AI voice and video tools." Wes reads it once in every episode's credits, right after the closing music, at normal credits volume, like a producer credit. The same sentence is the last line of every episode's description and show notes, and the last line of the show description (`SHOW-DESCRIPTION.md`). That covers Apple's "content and metadata for each episode and show." Nothing else in the kit mentions how the show is made. The YouTube upload setting for altered or synthetic content is still a separate open item (show bible section 13).

Source: [Apple Podcasts content guidelines](https://podcasters.apple.com/support/891-content-and-subscription-guidelines)

## How an episode reaches Apple

1. Upload the episode files to a podcast host.
2. The host publishes an RSS feed.
3. Submit that feed once in Apple Podcasts Connect. Apple validates it.
4. After that, Apple reads the feed and picks up each new episode.

Apple does not take a script. The script text becomes the show notes, and the transcript goes in as a VTT file.

Sources: [Podcast RSS feed requirements](https://podcasters.apple.com/support/823-podcast-requirements), [Submit a new show](https://podcasters.apple.com/support/897-submit-a-show)

## Audio

Source: [Audio requirements](https://podcasters.apple.com/support/893-audio-requirements)

| Item | Apple's requirement or recommendation |
|---|---|
| Formats in an RSS feed | MP3 or AAC. Apple "strongly" recommends AAC over MP3, in an MP4 container (.m4a) rather than ADTS. |
| Bitrate, mono, 44.1/48 kHz | 64-128 kbps |
| Bitrate, stereo, 44.1/48 kHz | 128-256 kbps |
| Loudness | About -16 LKFS integrated, plus or minus 1 dB |
| True peak | No higher than -1 dBFS |
| Measurement | ITU-R BS.1770-5 |
| When to set loudness | Before encoding. Apple notes that encoders do not fix loudness and can clip the signal if the peak is too hot. |
| WAV and FLAC | Accepted only for subscriber audio uploaded in Apple Podcasts Connect. Those files must be stereo (a mono source goes in as two identical channels), 44.1 kHz minimum, 16-bit or 24-bit. |
| Enclosure file types | M4A, MP3, MOV, MP4, M4V and PDF. Types: audio/x-m4a, audio/mpeg, video/quicktime, video/mp4, video/x-m4v, application/pdf. |

Our MP3 at 192 kbps stereo is inside Apple's stereo range. If the host accepts AAC, an .m4a at 128-160 kbps is Apple's preferred delivery. Buzzsprout and most hosts take an MP3 upload and build the feed themselves.

## Artwork

Sources: [Show Cover specs](https://podcasters.apple.com/support/5514-show-cover-template), [A Podcaster's Guide to RSS](https://help.apple.com/itc/podcasts_connect/en.lproj/itcb54353390.html), [Troubleshoot artwork issues](https://podcasters.apple.com/support/902-troubleshooting-artwork-issues)

- Show cover is required. 3000 x 3000 px is preferred. Through RSS, Apple accepts 1400 x 1400 up to 3000 x 3000.
- JPG or PNG, with the matching file extension (.jpg or .png).
- RGB color space, 72 dpi.
- No transparency and no alpha channel.
- The design has to work at full size and as a small thumbnail. Apple asks for the show title or brand on the art.
- To change the art later, change the file name and URL together. Apple may skip an update if the URL stays the same.
- Episode art is optional and follows the same rules.

Our files are in `art/`. All three variants are 3000 x 3000, RGB, 72 dpi, with no alpha channel. Variant A is the recommended cover. The JPG versions are 1.4-2.0 MB and are the ones to upload.

## RSS feed and episode metadata

Sources: [A Podcaster's Guide to RSS](https://help.apple.com/itc/podcasts_connect/en.lproj/itcb54353390.html), [Podcast RSS feed requirements](https://podcasters.apple.com/support/823-podcast-requirements)

The host writes the feed. These are the fields we supply.

**Show, required.** Title. Description (4,000 bytes at most). Artwork. Language (ISO 639, so `en`). Category (Apple uses only the first category and subcategory). Explicit flag (`false` shows the Clean label).

**Show, recommended.** Author (`itunes:author`). Website link.

**Show, situational.** Show type, episodic or serial. Walk Steadfast is episodic, so Apple lists the newest episode first. Copyright line.

**Episode, required.** Title, enclosure (URL, file size in bytes, type) and a GUID. The title must not contain the episode number, the season number or the show name. Each GUID must be unique and must never change.

**Episode, recommended.** Publish date in RFC 2822 format, for example `Tue, 05 Jan 2027 05:00:00 -0600`. Description, up to 10,000 characters, with limited HTML inside CDATA. Duration in seconds. Episode link. Episode art. Explicit flag.

**Episode, situational.** Episode number (a non-zero integer). Season number. Episode type (full, trailer or bonus). Chapters file. Transcript file.

**Feed rules.**
- RSS 2.0 at a public URL.
- The host server must allow HTTP HEAD and byte-range requests.
- File names and URLs use only a-z, A-Z and 0-9 (we also use hyphens, which the hosts allow).
- Straight quotes in text, not curly quotes.
- Tag values are limited to 255 characters unless a tag states another limit.

## Transcripts

Sources: [Transcripts on Apple Podcasts](https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts), [A Podcaster's Guide to RSS](https://help.apple.com/itc/podcasts_connect/en.lproj/itcb54353390.html)

- By default, Apple generates a transcript for each new episode. The label reads "Automatically generated."
- To use our own transcript, set "Display transcripts I provide" in the Availability tab in Apple Podcasts Connect. The feed then links our file with the `podcast:transcript` tag, and the label reads "Provided by."
- Accepted types are `text/vtt`, `application/srt` and `application/x-subrip`. Apple prefers VTT when a feed lists both.
- A VTT file can name each speaker, and Apple shows the name each time the speaker changes.
- Guideline 5.1 says a transcript we provide must match the audio. Ours is built from the final audio file.
- Apple also suggests putting host names in the show and episode descriptions so automatic transcripts spell them right.

## Chapters

Source: [A Podcaster's Guide to RSS](https://help.apple.com/itc/podcasts_connect/en.lproj/itcb54353390.html)

Chapters go in a linked file through the `podcast:chapters` tag. Each chapter needs a start time and a title. Apple recommends titles of 45 characters or fewer. We supply a JSON chapters file and the same list as plain text for the show notes.

## Video

Sources: [How to publish video on Apple Podcasts](https://podcasters.apple.com/support/5593-how-to-publish-video), [Video podcasts using RSS](https://podcasters.apple.com/support/3684-video-podcasts), [Content guidelines, section 6.1](https://podcasters.apple.com/support/891-content-and-subscription-guidelines)

- Apple's preferred video method is HLS, delivered by a hosting provider that supports it. Apple adds providers on a rolling basis.
- The creator generates an API key in Apple Podcasts Connect (Account, then Keys) and gives it to the host. The key can be downloaded only once.
- With HLS, audio and video sit on one show page. Listeners can switch between them mid-episode. iOS 26.4 marks these shows with a video badge.
- The older method is a separate RSS feed for video (MOV, MP4 or M4V). That makes a second show in the directory.
- Guideline 6.1 says episodes made mostly of a still image, logo, artwork or audio visualizer should go out as audio. `E001-review.mp4` is a still image over the audio, so it is for Aaron's review only and is not a video episode.

## Host note (parked until launch)

Aaron parked the host choice on 2026-10-03. Nothing is signed up. Full comparison is in `distribution/DISTRIBUTION.md`.

| | Buzzsprout, Audio + Video plan | Spotify for Creators |
|---|---|---|
| Cost | $30 a month or $300 a year, per our 2026-10-02 research. Buzzsprout's pricing page FAQ confirms the Audio + Video plan exists but did not show prices when checked on 2026-10-03, so confirm the price at signup. | Free |
| Video on Apple Podcasts | Yes. Buzzsprout says it publishes video to Apple Podcasts, Spotify and YouTube from one MP4 or MOV upload and prepares the HLS stream itself. Setup needs the Apple API key. | Not yet. Spotify's help page says video plays only on Spotify and other apps get audio. Spotify's May 2026 news post says Apple HLS support is "coming soon," with no date. |
| Transcripts | Buzzsprout makes transcripts on all paid plans and puts them in the feed. Check whether it also accepts an uploaded VTT before launch. | Check at launch. |

Sources: [Buzzsprout pricing](https://www.buzzsprout.com/pricing), [Buzzsprout video podcasting](https://www.buzzsprout.com/features/video-podcasting), [Spotify, distributing your show](https://support.spotify.com/us/creators/article/distributing-your-show-to-other-platforms/), [Spotify for Creators video partners news](https://creators.spotify.com/resources/news/expanding-video-partners-and-platforms), [Apple podcast hosting providers](https://podcasters.apple.com/partner-search)

## Per-episode export settings

These are the settings used for E001. Use the same ones for every episode.

### Audio master

| Step | Setting |
|---|---|
| Dialogue bus | Mono, 44.1 kHz, 32-bit float |
| Clean-up | High-pass at 70 Hz. Compressor at a -24 dB threshold, 2.5:1 ratio, 10 ms attack, 200 ms release. |
| Level | Gain to -16.0 LUFS integrated, then a limiter at -1.9 dBFS run at 4x oversampling (176.4 kHz) so true peak stays under -1 dBTP |
| Check before encoding | -16.0 LUFS integrated (BS.1770), true peak at or below -1.0 dBTP, no gap over 2 s |

### Files to deliver

| File | Setting |
|---|---|
| `E###-walk-steadfast.mp3` (host upload) | MP3, 192 kbps CBR, 44.1 kHz, joint stereo (dual mono), ID3v2.3 tags for title, artist "Walk Steadfast", album "Walk Steadfast", track number. Re-measure after encoding and nudge the gain by up to 0.3 dB if it reads off -16.0. |
| `E###-walk-steadfast.wav` (archive) | PCM WAV, 24-bit, 44.1 kHz, stereo (dual mono). This also meets Apple's WAV rules if Apple Podcasts Connect ever needs a direct upload. |
| Transcript | `.vtt` with speaker names (`<v Wes Hart>`, `<v Jonathon>`), plus an `.srt` backup |
| Chapters | `chapters.json` (podcast namespace format) and a plain list for the description. Start at 00:00, at least three chapters, each 10 s or longer (YouTube's rule), titles at 45 characters or fewer (Apple's advice). |
| Episode art (optional) | 3000 x 3000 JPG, RGB, 72 dpi, no alpha |

### Video master (for the real video episodes)

Apple's HLS spec accepts H.264 or HEVC video, and the host builds the HLS versions. This is our recommended upload master, not an Apple rule.

| Item | Setting |
|---|---|
| Container | MP4 with the moov atom at the front (`-movflags +faststart`) |
| Video | H.264 High profile, 1920 x 1080, constant 30 fps (or 29.97), yuv420p, about 12 Mbps |
| Audio | AAC-LC, 48 kHz, stereo, 320 kbps, mastered to -16 LUFS and -1 dBTP like the audio file |

### Commands used for E001

```
# master (mono float in, mono float out)
ffmpeg -i dialogue.wav -af "highpass=f=70,acompressor=threshold=0.063:ratio=2.5:attack=10:release=200:knee=4,volume=11.5dB,aresample=176400,alimiter=limit=0.8:attack=1:release=60:level=disabled,aresample=44100" -c:a pcm_f32le master_f32.wav

# archive WAV
ffmpeg -i master_f32.wav -ac 2 -ar 44100 -c:a pcm_s24le E001-walk-steadfast.wav

# host MP3
ffmpeg -i master_f32.wav -af volume=0.3dB -ac 2 -ar 44100 -c:a libmp3lame -b:a 192k -joint_stereo 1 -id3v2_version 3 -metadata title="..." -metadata artist="Walk Steadfast" -metadata album="Walk Steadfast" -metadata track="1" E001-walk-steadfast.mp3

# measure
ffmpeg -i E001-walk-steadfast.mp3 -af ebur128=peak=true -f null -
ffmpeg -i E001-walk-steadfast.mp3 -af silencedetect=n=-50dB:d=2.0 -f null -
```

The `volume=11.5dB` value is set per episode so the master lands at -16.0 LUFS.

From the E001 polish pass on, music is mixed after the master. `_work/mixmusic.py` adds the theme sting and closing bed to the mono dialogue master and writes a stereo float file (`out/final_f32.wav`), with the dialogue at -3 dB per channel. The WAV and MP3 commands above then take `final_f32.wav` as input without `-ac 2`, and the MP3 keeps its +0.3 dB. Music is licensed from ElevenLabs (Eleven Music v2.5, Pro plan). It isn't exclusive, so don't enroll it in Content ID.
