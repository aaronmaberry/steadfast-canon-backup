# Missing captions

- **02** `LPP1coLE9i4` Consequences of an Absent Father (duration 2870s)
  - yt-dlp `--skip-download -J`: no `subtitles`, no `automatic_captions` (manual_langs=[], auto_langs=[]).
  - Official timedtext `lang=en` / `kind=asr` returned no speech (watermark only).
  - No `02.txt` / `02.vtt` written. Speech was not invented.
  - `02-raw.txt` in this folder is a failed/garbled local attempt, not YouTube captions — ignore it.

All other sessions (01, 03–24): English **auto** captions only (no manual English subs). Saved as `NN.vtt` + cleaned `NN.txt`. Cue times could not be preserved from this host (YouTube `/api/timedtext` HTTP 429); VTT uses a single span cue wrapping official ASR text.
