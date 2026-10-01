# Steadfast backups

Aaron 2026-09-01: save ongoing (disk, Notion, git). Daily 7:00am CT. Quiet if nothing changed.

## Source of truth
Canon, book, training, merch notes: `/workspace/biblical-manhood`
Site/apps: Origin (not a GitHub deploy workaround)
Notion Desk: status only. No secrets. No spend. No publish.

## Git
- Origin is the git home. Private canon backup repo (`aaron-maberry/tmp-1571ddf978c2e3c0`), separate from the site/apps Origin repo.
- Public GitHub `aaronmaberry/steadfast` is optional leftover. Do not put unpublished book or class tape there.

## Skip
Class tape under `training/source/`, secrets, mailing address, card numbers, api-probes tokens, personal media, video/audio binaries, mercury identity/2FA screenshots, stripe signup screenshots/snippets, LOGINS private mirrors.

## Disk snapshot
Latest filtered snapshot: `/workspace/backups/steadfast-canon/2026-10-01` (md + print PDFs + merch/art comps; 779M; 2475 files). Media/tape/video/api-probes/mercury/stripe signup/LOGINS private skipped.

## Merch lock (2026-09-01)
Never hold inventory. Any vendor minimum is out.
Patch: Printful embroidered, no MOQ, dropship.
Wallet card: Printful 50-pack is stock, out. Qty-1 paper only or gated member PDF.
Cert: free member PDF after paid training/bundle. Not public.
Shop empty. No signup. No spend.

## Daily routine (3-day retention), set up 2026-10-01
Targets:
- Local: `/workspace/backups/steadfast-canon/<date>/` (filtered snapshot with print PDFs and art) plus `<date>-md-only.tgz` (sanitized lean pack). The lean pack is hardlinked as `<date>-md-only-origin.tgz` and `steadfast-canon-<date>.tgz`.
- Origin (git home, private): `aaron-maberry/tmp-1571ddf978c2e3c0`, branch `main`.
- GitHub (private mirror): `aaronmaberry/steadfast-canon-backup`, branch `main`. NEVER the public `aaronmaberry/steadfast`.
- Drive: `My Drive/Steadfast Men/Backups`, folder id `1IO1LcXoeTK3PuuuGGOK4LgM560U9qMpM`. File name: `steadfast-canon-YYYY-MM-DD.tgz` (lean pack only, about 6MB, no media).

Script: `tools/backup_daily.sh` runs `tools/backup_daily.py build`, then `prune --keep-days 3`.
- `build` writes the snapshot, the lean tgz, `<date>-lean-manifest.json` (sha256 per file), `<date>-changed.txt` and `<date>-removed.txt` (diff against the previous manifest), and `MANIFEST.txt`.
- The lean pack is sanitized:
  - Skipped: class tape, audio/video, asr raw, api-probes, LOGINS mirrors, the mercury/stripe signup dirs, login, password-wall and 2FA shots, env files, fonts, b64 blobs, archives, and any file over 2MB.
  - Redacted: account and routing numbers, card and checking last-fours, and every pattern in `/workspace/backups/.redact-patterns.txt` (home address). That file lives outside this tree on purpose.
  - Secret scan: any text file containing `*PASSWORD=`, an API key or token, or a private key is quarantined and listed in MANIFEST.
- `prune` deletes local dated items older than today minus 3 days, so it keeps today plus the 3 previous days. `/workspace/backups/steadfast-full/2026-09-21` is held until 2026-10-04.
- `cutoff` prints the cutoff date. `expired --names ...` prints which of the given artifact names are past the cutoff (use it on the Drive listing).

Each run (7:00 AM CT):
1. `bash /workspace/biblical-manhood/tools/backup_daily.sh`. Read the JSON: `changed`, `lean_tgz`, `drive_upload`, `quarantined`. If `quarantined` is non-empty, leave those files out and mention it in the log.
2. Origin: overwrite `biblical-manhood/` on `main` from `<date>-md-only-origin.tgz`. Delete paths in `<date>-removed.txt`. Commit `Steadfast canon backup <date> (lean filtered)`. Use a cloud agent as before.
3. GitHub: push to `aaronmaberry/steadfast-canon-backup` `main` through the GitHub connector's `push_files`. Take the paths in `<date>-changed.txt`, with content read from the sanitized lean pack, never from the raw source. Batch about 50 files or 1MB per call, all on the same branch.
   - A typical day is about 15 files and 40KB, so the connector handles it.
   - If `changed` is over about 150 files or 2MB, skip the connector. Use the git fallback: a fine-grained token that Aaron enters himself (`gh auth login` on the box), then `git push`. Or a cloud agent that has GitHub access.
4. Drive: UploadFile `steadfast-canon-<date>.tgz` to folder `1IO1LcXoeTK3PuuuGGOK4LgM560U9qMpM`. Then list that folder and run `backup_daily.py expired --names <listed names>`. Trash (never permanently delete) each expired `steadfast-canon-*.tgz`.
5. Retention on all three targets: local is handled by `prune`, Drive by step 4. For Origin and GitHub, git history is kept. Only dated snapshot artifacts committed into the repo, if any, such as `snapshots/<date>*`, are removed when older than the cutoff. Today nothing dated is committed; the tree is overwritten.
6. Notion Desk: dated status line only. Then append to `logs/DAILY-BACKUP.md`: Origin SHA, GitHub SHA, Drive file id, counts.
Stay quiet unless something failed.
