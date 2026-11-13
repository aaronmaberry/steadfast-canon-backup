# L12 handoff (session moved because the computer link failed)

These files are the finished L12 prep, so a new session doesn't redo it:
- `L12-v1.srt` is aligned from the spoken script. It was built on the release audio, which runs on the master's clock (re-align on the master: `align_script.py`).
  - All 419 line ends land on stops.
  - OCR gate vs the release: 22 of 25 within ±0.6 s. The other 3 come from the release showing stack boards early.
- `boards_l12.py` goes in `gfx/`; `spec.py` and `cues.py` go in `edit/`. Rebuild `boards.py`.
- `layout.py` showed zero PROBLEMs on the provisional timing.
- `etags.txt` holds the HeyGen ETags and sizes. `pieces.txt` lists the 10 MiB pieces `L12-<key>-NNN.bin`. All 273 pieces are already in ~/Downloads on Aaron's computer.
- B-roll is downloaded to ~/Downloads as `L12-m2847.mp4` (calendar marked), `L12-m3804.mp4` (sauce in pan) and `L12-m10479.mp4` (watering can).
  - Run B1: view a 6-frame strip of each file before use.
  - The release's other 7 clips were dropped as not literal or commercial; those lines stay on Wes.
- Leave "Watch whether he tells on himself" (L344) as is. Aaron approved it on Nov 13. It is not on any board.
- Look: camel crewneck. The release notes report PANEL chin jut on v1. Check every P shot in the contact sheet.
- Steps left:
  - new_lesson.sh 12; copy these files in
  - stage, join, verify
  - AUDIO_END/TOTAL from the master
  - narr_raw.wav; re-align; srt2cues; words
  - skin check; scan; jump scan; align_wides; verified.json; widescan; quality; layout
  - prog_audio; captions; render at CRF 19 (1406 s)
  - finish; postcheck; qc_v6; bandcheck; P-shot check; send
