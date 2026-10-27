#!/usr/bin/env python3
"""Steadfast daily backup helper (local side).

Subcommands
  build  [--date YYYY-MM-DD]   filtered snapshot dir + lean (sanitized) tgz + file manifest + changed list
  prune  [--keep-days 3] [--dry-run] [--date D]   delete local dated snapshots older than D-keep_days
  cutoff [--keep-days 3] [--date D]   print the cutoff date (anything dated before it is expired)
  expired --names N1 N2 ...    given Drive/GitHub artifact names, print the ones past the cutoff

The Drive upload, Drive trash, Origin push and GitHub push go through connectors or agents.
See BACKUP.md, section "Daily routine".
"""
import argparse, datetime as dt, fnmatch, hashlib, io, json, os, re, shutil, sys, tarfile

SRC = "/workspace/biblical-manhood"
DEST = "/workspace/backups/steadfast-canon"
FULL = "/workspace/backups/steadfast-full"
# special hold: the one-off full backup whose Drive copy was trashed 2026-10-01
FULL_KEEP_UNTIL = {"2026-09-21": "2026-10-04"}
ORIGIN_REPO = "aaron-maberry/tmp-1571ddf978c2e3c0"
GITHUB_REPO = "aaronmaberry/steadfast-canon-backup"   # PRIVATE. Never aaronmaberry/steadfast (public).
DRIVE_BACKUPS_FOLDER = "1IO1LcXoeTK3PuuuGGOK4LgM560U9qMpM"  # My Drive/Steadfast Men/Backups

# Directory names skipped at any depth
EXCL_DIRS = {"audio", "asr-raw", "_raw", "raw", "video", "api-probes", "_fable-incoming",
             ".venv", "venv", "__pycache__", "node_modules", ".git", "mercury", "stripe", "_bind_tmp"}
# Path prefixes (relative to SRC) skipped
EXCL_PREFIX = ("training/source/", "export/_build/", "book/export/_build/", "book/audio/")
# Filename globs skipped (case-insensitive)
EXCL_GLOBS = ["*.mov", "*.wav", "*.mp4", "*.m4a", "*.mp3", "*.m4b", "*.mkv", "*.webm", "*.flac",
              "*.aac", "*.ogg", "*secret*", "*credential*", "*.pem", "*.key", "*.env", ".env*",
              "*token*", "*logins*", "*login*.png", "*password*.png", "*password-wall*",
              "*2fa*", "*.p12", "*.pfx", "id_rsa*", "id_ed25519*", "*env.sh", ".*env*", "*.env.*", "*cookies*", "*session*.json"]
EXCL_LOG_GLOBS = ["logs/*.out", "logs/*.log"]
MAX_SNAPSHOT_FILE = 100 * 1024 * 1024        # skip >100MB anything (big binaries)
# Lean pack (Origin / GitHub / Drive): text only, no PDFs/images/archives
LEAN_EXCL_GLOBS = ["*.pdf", "*.png", "*.jpg", "*.jpeg", "*.webp", "*.gif", "*.heic", "*.zip",
                   "*.docx", "*.pptx", "*.xlsx", "*.svgz",
                   "*.ttf", "*.otf", "*.woff", "*.woff2", "*.b64", "*.b64.txt", "*.tar.gz", "*.tgz"]
MAX_LEAN_FILE = 2 * 1024 * 1024
TEXT_EXT = {".md", ".txt", ".vtt", ".srt", ".js", ".html", ".css", ".json", ".jsonl", ".py", ".sh",
            ".yml", ".yaml", ".svg", ".csv", ".log", ".out", ".toml", ""}
# Redactions applied to text in the lean pack (home address etc.)
# Redactions applied to text in the lean pack. Personal patterns (home address etc.) live OUTSIDE the
# backed-up tree in REDACT_FILE (one regex per line) so they never get committed themselves.
REDACT_FILE = "/workspace/backups/.redact-patterns.txt"
REDACT = [
    (re.compile(r"\b(acct|account|routing)(\s*(no\.?|number|#))?\s*[:#]?\s*[`'\"*]*\d{6,17}[`'\"*]*", re.I), r"\1 [redacted]"),
    (re.compile(r"\b(checking|savings|account|acct|card)\s+(ending|last[- ]?four|last 4|x+|\*+)\s*(in\s*)?\d{4}\b", re.I), r"\1 \2 [redacted]"),
]
if os.path.exists(REDACT_FILE):
    for line in open(REDACT_FILE, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            REDACT.append((re.compile(line, re.I), "[redacted]"))
# Content safety net: any text file matching these is quarantined (left out of snapshot + lean pack)
SECRET_RX = re.compile(
    r"\b[A-Z0-9_]*(PASSWORD|PASSWD|SECRET|API_KEY|APIKEY|ACCESS_TOKEN|AUTH_TOKEN|PRIVATE_KEY)[A-Z0-9_]*\s*=\s*['\"]?[^\s'\"]{4,}"
    r"|sk_live_[0-9A-Za-z]{10,}|rk_live_[0-9A-Za-z]{10,}|ghp_[0-9A-Za-z]{30,}|github_pat_[0-9A-Za-z_]{30,}"
    r"|AKIA[0-9A-Z]{16}|xox[abp]-[0-9A-Za-z-]{10,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN [A-Z ]*PRIVATE KEY-----")
SCAN_ALLOW = {"tools/backup_daily.py"}  # contains the patterns themselves
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
# Extra source trees (Aaron approved 2026-10-20): locked Steadfast training scripts.
# (source dir, repo/archive path). Text files only; *.bak-* skipped; same exclusions, secret scan and redaction.
EXTRA_SRCS = [("/workspace/training-ep01/locked", "training-ep01/locked"),
              ("/workspace/training-ep01/scripts-v7", "training-ep01/scripts-v7")]
# Single extra files (source path, repo path)
EXTRA_FILES = [("/workspace/training-ep01/rec/S01-v2/W01-script-v-24lessons-LOCKED-2026-10-21b.md",
                "training-ep01/rec/S01-v2/W01-script-v-24lessons-LOCKED-2026-10-21b.md")]  # 2026-10-21 lock (replaces kickoff-2026-10-20)
# Locked lecture audio (Aaron 2026-10-20): copied into the local snapshot despite the audio exclusions,
# hashed into <date>-audio-manifest.json, changes listed in <date>-audio-changed.txt. Text files there
# (README.md etc.) also go in the lean pack. Binaries (mp3/wav) never go in the lean pack: push them to
# GitHub with git (LFS for files >50MB), not push_files.
AUDIO_SRCS = [("/workspace/training-ep01/locked/audio", "training-ep01/locked/audio"),
              ("/workspace/steadfast-main/training-locked/audio", "steadfast-main/training-locked/audio")]  # S01 LOCKED mp3 (+ dated 2026-10-21 copy)
AUDIO_EXT = {".mp3", ".wav"}
EXTRA_EXT = {".md", ".txt", ".py", ".sh", ".log", ".json", ".csv", ".yml", ".yaml", ".toml", ".vtt", ".srt"}


def today_ct():
    return dt.date.today().isoformat()  # box clock is America/Chicago


def excluded(rel, size):
    parts = rel.split("/")
    if any(p in EXCL_DIRS for p in parts[:-1]):
        return True
    if rel.startswith(EXCL_PREFIX):
        return True
    name = parts[-1].lower()
    if any(fnmatch.fnmatch(name, g) for g in EXCL_GLOBS):
        return True
    if any(fnmatch.fnmatch(rel, g) for g in EXCL_LOG_GLOBS):
        return True
    return size > MAX_SNAPSHOT_FILE


def lean_ok(rel, size):
    name = rel.rsplit("/", 1)[-1].lower()
    if any(fnmatch.fnmatch(name, g) for g in LEAN_EXCL_GLOBS):
        return False
    return size <= MAX_LEAN_FILE


def redact_bytes(rel, data):
    ext = os.path.splitext(rel)[1].lower()
    if ext not in TEXT_EXT:
        return data, 0
    try:
        s = data.decode("utf-8")
    except UnicodeDecodeError:
        return data, 0
    n = 0
    for rx, rep in REDACT:
        s, k = rx.subn(rep, s)
        n += k
    return s.encode("utf-8"), n


def build(date):
    global DEST
    if os.environ.get("STEADFAST_BACKUP_DEST"):  # testing only: build into another dir
        DEST = os.environ["STEADFAST_BACKUP_DEST"]
        os.makedirs(DEST, exist_ok=True)
    snap = os.path.join(DEST, date)
    tmp = snap + ".building"
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(os.path.join(tmp, "biblical-manhood"))
    files = skipped = total = extra_files = 0
    lean = []   # archive keys ("biblical-manhood/x", "training-ep01/locked/y")
    srcmap = {}  # archive key -> source path
    quarantined = []
    for root, dirs, fnames in os.walk(SRC):
        relroot = os.path.relpath(root, SRC)
        relroot = "" if relroot == "." else relroot + "/"
        dirs[:] = sorted(d for d in dirs if d not in EXCL_DIRS and not (relroot + d + "/").startswith(EXCL_PREFIX))
        for f in sorted(fnames):
            p = os.path.join(root, f)
            if os.path.islink(p) or not os.path.isfile(p):
                continue
            rel = relroot + f
            size = os.path.getsize(p)
            if excluded(rel, size):
                skipped += 1
                continue
            if rel not in SCAN_ALLOW and os.path.splitext(rel)[1].lower() in TEXT_EXT and size < 5 * 1024 * 1024:
                try:
                    if SECRET_RX.search(open(p, encoding="utf-8", errors="ignore").read()):
                        quarantined.append(rel)
                        continue
                except OSError:
                    pass
            out = os.path.join(tmp, "biblical-manhood", rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            shutil.copy2(p, out)
            files += 1
            total += size
            if lean_ok(rel, size):
                lean.append("biblical-manhood/" + rel)
                srcmap["biblical-manhood/" + rel] = p
    walks = [(s_, d_, os.walk(s_)) for s_, d_ in EXTRA_SRCS if os.path.isdir(s_)]
    walks += [(os.path.dirname(fs_), os.path.dirname(fd_), [(os.path.dirname(fs_), [], [os.path.basename(fs_)])])
              for fs_, fd_ in EXTRA_FILES if os.path.isfile(fs_)]
    for esrc, eprefix, walker in walks:
        for root, dirs, fnames in walker:
            dirs[:] = sorted(d for d in dirs if d not in EXCL_DIRS)
            for f in sorted(fnames):
                p = os.path.join(root, f)
                if os.path.islink(p) or not os.path.isfile(p):
                    continue
                key = eprefix + "/" + os.path.relpath(p, esrc)
                size = os.path.getsize(p)
                if (".bak-" in f.lower() or os.path.splitext(f)[1].lower() not in EXTRA_EXT
                        or excluded(key, size) or not lean_ok(key, size)):
                    skipped += 1
                    continue
                try:
                    if SECRET_RX.search(open(p, encoding="utf-8", errors="ignore").read()):
                        quarantined.append(key)
                        continue
                except OSError:
                    pass
                out = os.path.join(tmp, key)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                shutil.copy2(p, out)
                files += 1; extra_files += 1
                total += size
                lean.append(key)
                srcmap[key] = p
    audio_manifest = {}
    for asrc, aprefix in AUDIO_SRCS:
        for root, dirs, fnames in os.walk(asrc):
            dirs.sort()
            for f in sorted(fnames):
                p = os.path.join(root, f)
                if os.path.islink(p) or not os.path.isfile(p) or ".bak-" in f.lower():
                    continue
                key = aprefix + "/" + os.path.relpath(p, asrc)
                ext = os.path.splitext(f)[1].lower()
                size = os.path.getsize(p)
                if ext in AUDIO_EXT:
                    out = os.path.join(tmp, key)
                    os.makedirs(os.path.dirname(out), exist_ok=True)
                    shutil.copy2(p, out)
                    h = hashlib.sha256()
                    with open(p, "rb") as fh:
                        for chunk in iter(lambda: fh.read(1 << 20), b""):
                            h.update(chunk)
                    audio_manifest[key] = {"sha256": h.hexdigest(), "bytes": size}
                    files += 1; total += size
                elif ext in EXTRA_EXT and lean_ok(key, size):
                    out = os.path.join(tmp, key)
                    os.makedirs(os.path.dirname(out), exist_ok=True)
                    shutil.copy2(p, out)
                    files += 1; extra_files += 1; total += size
                    lean.append(key); srcmap[key] = p
    amf = os.path.join(DEST, f"{date}-audio-manifest.json")
    json.dump(audio_manifest, open(amf, "w"), indent=0, sort_keys=True)
    aprev = sorted(f for f in os.listdir(DEST) if f.endswith("-audio-manifest.json") and f < f"{date}-")
    aold = json.load(open(os.path.join(DEST, aprev[-1]))) if aprev else {}
    audio_changed = [k for k, v in audio_manifest.items() if aold.get(k) != v]
    with open(os.path.join(DEST, f"{date}-audio-changed.txt"), "w") as fh:
        fh.write("\n".join(audio_changed) + ("\n" if audio_changed else ""))
    # lean pack: sanitized
    manifest = {}
    redactions = 0
    lean_tgz = os.path.join(DEST, f"{date}-md-only.tgz")
    with tarfile.open(lean_tgz + ".tmp", "w:gz") as tf:
        for rel in lean:
            p = os.path.join(tmp, rel)
            data = open(p, "rb").read()
            data, n = redact_bytes(rel, data)
            redactions += n
            if n:  # keep the snapshot copy sanitized too
                open(p, "wb").write(data)
            manifest[rel] = hashlib.sha256(data).hexdigest()
            ti = tarfile.TarInfo(rel)
            ti.size = len(data)
            ti.mtime = int(os.path.getmtime(srcmap[rel]))
            ti.mode = 0o644
            tf.addfile(ti, io.BytesIO(data))
    os.replace(lean_tgz + ".tmp", lean_tgz)
    for alias in (f"{date}-md-only-origin.tgz", f"steadfast-canon-{date}.tgz"):
        a = os.path.join(DEST, alias)
        if os.path.exists(a):
            os.remove(a)
        os.link(lean_tgz, a)
    mpath = os.path.join(DEST, f"{date}-lean-manifest.json")
    json.dump(manifest, open(mpath, "w"), indent=0, sort_keys=True)
    # changed vs previous manifest
    prev = sorted(f for f in os.listdir(DEST) if f.endswith("-lean-manifest.json") and f < f"{date}-")
    changed, removed = list(manifest), []
    if prev:
        old = json.load(open(os.path.join(DEST, prev[-1])))
        changed = [k for k, v in manifest.items() if old.get(k) != v]
        removed = [k for k in old if k not in manifest]
    with open(os.path.join(DEST, f"{date}-changed.txt"), "w") as fh:
        fh.write("\n".join(changed) + ("\n" if changed else ""))
    with open(os.path.join(DEST, f"{date}-removed.txt"), "w") as fh:
        fh.write("\n".join(removed) + ("\n" if removed else ""))
    with open(os.path.join(tmp, "MANIFEST.txt"), "w") as fh:
        fh.write(f"Steadfast daily backup {date}\nBuilt: {dt.datetime.now().astimezone().isoformat(timespec='seconds')}\n"
                 f"Source: {SRC} + " + ", ".join(f"{s} -> {d}/" for s, d in EXTRA_SRCS) + f" ({extra_files} training files)\nFiles: {files}  Size: {total/1e6:.0f}MB  Skipped: {skipped}\n"
                 f"Lean pack: {os.path.basename(lean_tgz)} ({len(lean)} files, {os.path.getsize(lean_tgz)/1e6:.1f}MB, {redactions} redactions)\n"
                 f"Changed since previous: {len(changed)}  Removed: {len(removed)}\n"
                 f"Origin: {ORIGIN_REPO} (private)  GitHub: {GITHUB_REPO} (private)  Drive folder: {DRIVE_BACKUPS_FOLDER}\n"
                 "Skipped: class tape (training/source), audio/video, asr raw, api-probes, secrets/keys/tokens, LOGINS mirrors,\n"
                 "  mercury/stripe signup dirs, login/password-wall/2FA shots, export builds, files >100MB. Home address redacted.\n"
                 f"Quarantined by secret scan ({len(quarantined)}): " + ", ".join(quarantined) + "\n"
                 "Public aaronmaberry/steadfast is NOT the book. No spend. No publish.\n")
    shutil.rmtree(snap, ignore_errors=True)
    os.replace(tmp, snap)
    print(json.dumps({"date": date, "snapshot": snap, "files": files, "bytes": total, "skipped": skipped,
                      "lean_tgz": lean_tgz, "lean_files": len(lean), "lean_bytes": os.path.getsize(lean_tgz),
                      "drive_upload": os.path.join(DEST, f"steadfast-canon-{date}.tgz"),
                      "training_files": extra_files, "audio_files": len(audio_manifest), "audio_changed": len(audio_changed),
                      "audio_changed_list": os.path.join(DEST, f"{date}-audio-changed.txt"), "changed": len(changed), "removed": len(removed), "redactions": redactions, "quarantined": quarantined}, indent=1))


def cutoff(date, keep):
    return (dt.date.fromisoformat(date) - dt.timedelta(days=keep)).isoformat()


def du(p):
    if os.path.isfile(p):
        return os.path.getsize(p)
    return sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(p) for f in fs
               if not os.path.islink(os.path.join(r, f)))


def prune(date, keep, dry):
    cut = cutoff(date, keep)
    victims = []
    for name in sorted(os.listdir(DEST)):
        m = re.match(r"^(?:steadfast-canon-)?(\d{4}-\d{2}-\d{2})(?:$|[-.])", name)
        if m and m.group(1) < cut:
            victims.append(os.path.join(DEST, name))
    if os.path.isdir(FULL):
        for name in sorted(os.listdir(FULL)):
            m = DATE_RE.search(name)
            if not m:
                continue
            hold = FULL_KEEP_UNTIL.get(m.group(1))
            if (hold and date >= hold) or (not hold and m.group(1) < cut):
                victims.append(os.path.join(FULL, name))
    freed = 0
    for v in victims:
        sz = du(v)
        freed += sz
        print(("WOULD DELETE " if dry else "deleted ") + f"{v}  ({sz/1e6:.1f}MB)")
        if not dry:
            shutil.rmtree(v) if os.path.isdir(v) and not os.path.islink(v) else os.remove(v)
    print(f"cutoff={cut} keep>= {cut}  items={len(victims)}  freed={freed/1e9:.2f}GB{' (dry run)' if dry else ''}")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    for c in ("build", "prune", "cutoff", "expired"):
        p = sp.add_parser(c)
        p.add_argument("--date", default=today_ct())
        p.add_argument("--keep-days", type=int, default=3)
        if c == "prune":
            p.add_argument("--dry-run", action="store_true")
        if c == "expired":
            p.add_argument("--names", nargs="+", required=True)
    a = ap.parse_args()
    if a.cmd == "build":
        build(a.date)
    elif a.cmd == "prune":
        prune(a.date, a.keep_days, a.dry_run)
    elif a.cmd == "cutoff":
        print(cutoff(a.date, a.keep_days))
    else:
        cut = cutoff(a.date, a.keep_days)
        for n in a.names:
            m = DATE_RE.search(n)
            if m and m.group(1) < cut:
                print(n)


if __name__ == "__main__":
    main()
