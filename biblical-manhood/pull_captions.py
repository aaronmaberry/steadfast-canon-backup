#!/usr/bin/env python3
"""Serial English caption pull for Biblical Manhood YouTube videos. No A/V download."""
from __future__ import annotations

import json
import random
import re
import shutil
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

ROOT = Path("/workspace/biblical-manhood")
CAP = ROOT / "captions"
TMP = ROOT / ".caption-tmp"
TRANS = ROOT / "transcripts"
BRIEFS = ROOT / "briefs"
CATALOG_PATH = ROOT / "catalog.json"
CAP.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)
TRANS.mkdir(parents=True, exist_ok=True)
BRIEFS.mkdir(parents=True, exist_ok=True)
STATUS_PATH = CAP / "status.json"

EPISODES = [
    ("01-introduction", "sk_sp_m-Fzw", "https://onemissionbible.churchcenter.com/episodes/607498"),
    ("02-consequences-of-an-absent-father", "LPP1coLE9i4", "https://onemissionbible.churchcenter.com/episodes/607525"),
    ("03-healing-the-father-wound", "pSaWY9otTaM", "https://onemissionbible.churchcenter.com/episodes/607527"),
    ("04-overly-bonded-mother-wound", "ZgqwWWtuixI", "https://onemissionbible.churchcenter.com/episodes/607530"),
    ("05-moving-beyond-mom-to-manhood", "IVj-bB7_ruA", "https://onemissionbible.churchcenter.com/episodes/607532"),
    ("06-men-and-mentors", "J8hpKYOTzVg", "https://onemissionbible.churchcenter.com/episodes/607533"),
    ("07-making-friends-finding-a-mentor", "S5BreS-WwQk", "https://onemissionbible.churchcenter.com/episodes/607535"),
    ("08-the-depravity-wound", "z9AtC99ztt0", "https://onemissionbible.churchcenter.com/episodes/607536"),
    ("09-depravity-specifically-for-men", "T3vTHDPC__w", "https://onemissionbible.churchcenter.com/episodes/607538"),
    ("10-lack-of-masculine-vision-wound", "yVpugbFuJRw", "https://onemissionbible.churchcenter.com/episodes/607539"),
    ("11-first-semester-review", "xXUQ6JKRcdw", "https://onemissionbible.churchcenter.com/episodes/608409"),
    ("12-genesis-to-manhood", "GLk605vgwks", "https://onemissionbible.churchcenter.com/episodes/608426"),
    ("13-biblical-definition-of-manhood-p1", "1xtJgaOpmZ8", "https://onemissionbible.churchcenter.com/episodes/608439"),
    ("14-biblical-definition-of-manhood-p2", "a9P1EVOBbHE", "https://onemissionbible.churchcenter.com/episodes/609690"),
    ("15-a-man-and-his-wife-p1", "3Ps3ezdRO6Y", "https://onemissionbible.churchcenter.com/episodes/609697"),
    ("16-25-ways-to-be-a-servant-leader", "apJIZ8QYT_E", "https://onemissionbible.churchcenter.com/episodes/609698"),
    ("17-a-man-and-his-wife-p2", "T4VCs8hIarg", "https://onemissionbible.churchcenter.com/episodes/609702"),
    ("18-a-man-and-his-sexuality", "KS3dzdmW_tU", "https://onemissionbible.churchcenter.com/episodes/609704"),
    ("19-a-man-and-his-daughters", "BscWJ0bjRuQ", "https://onemissionbible.churchcenter.com/episodes/609710"),
    ("20-a-man-and-his-sons", "LADY_IIFVE0", "https://onemissionbible.churchcenter.com/episodes/609711"),
    ("21-a-man-and-his-design", "kRouEA2E1cs", "https://onemissionbible.churchcenter.com/episodes/609713"),
    ("22-a-man-and-his-life-journey", "Cncr63S_otE", "https://onemissionbible.churchcenter.com/episodes/609715"),
    ("23-a-man-and-his-legacy", "NN32wsW_cWo", "https://onemissionbible.churchcenter.com/episodes/609716"),
    ("24-final-session-bold-action", "4b6q9go_0eE", "https://onemissionbible.churchcenter.com/episodes/609718"),
]

YTDLP = shutil.which("yt-dlp") or "/home/box/.local/bin/yt-dlp"
SLEEP_MIN = 8.0
SLEEP_MAX = 15.0
BACKOFF_429 = 60.0
STOP_AFTER_429_VIDEOS = 3
IMPERSONATE_TARGET = "chrome"


def load_status() -> dict:
    if STATUS_PATH.exists():
        try:
            return json.loads(STATUS_PATH.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def save_status(status: dict) -> None:
    STATUS_PATH.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n")


def is_block_page(path: Path) -> bool:
    raw = path.read_bytes()[:8192]
    text = raw.decode("utf-8", errors="replace")
    stripped = text.lstrip()
    low = stripped.lower()
    if low.startswith("<html") or low.startswith("<!doctype html"):
        return True
    if "automated queries" in low:
        return True
    if stripped.startswith("<") and ("sorry" in low) and (
        "unusual traffic" in low
        or "our systems have detected" in low
        or "why did this happen" in low
    ):
        return True
    return False


def is_real_caption(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 16:
        return False
    if is_block_page(path):
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    head = text.lstrip()
    if head.startswith("WEBVTT"):
        return True
    if "-->" in text[:4000] and not head.startswith("<"):
        return True
    if head.startswith("{") or head.startswith("["):
        sample = text[:4000]
        if any(k in sample for k in ("events", "wsWinStyles", "pens", "segs", "tStartMs")):
            return True
    low = head[:2000].lower()
    if any(k in low for k in ("<transcript", "<timedtext", "<tt ", "<tt\n", "xmlns:tt", "<srv3")):
        return True
    return False


def collect_caption_files(work: Path) -> list[Path]:
    files: list[Path] = []
    for ext in ("vtt", "json3", "srv3", "srv1", "srv2", "ttml", "xml"):
        files.extend(work.glob(f"*.{ext}"))
        files.extend(work.glob(f"*.*.{ext}"))
    seen = set()
    out = []
    for f in files:
        if f.resolve() in seen:
            continue
        seen.add(f.resolve())
        if f.is_file() and f.stat().st_size > 0:
            out.append(f)
    return out


def pick_best(files: list[Path]) -> Path | None:
    valid = [f for f in files if is_real_caption(f)]
    if not valid:
        return None

    def rank(p: Path) -> tuple:
        name = p.name.lower()
        ext_rank = 0 if name.endswith(".vtt") else (1 if name.endswith(".json3") else 2)
        # prefer en-orig (manual/original) then en; auto last
        if "en-orig" in name:
            lang_rank = 0
        elif name.endswith(".en.vtt") or ".en." in name:
            lang_rank = 1
        else:
            lang_rank = 2
        auto_rank = 1 if "auto" in name else 0
        size = -p.stat().st_size
        return (ext_rank, lang_rank, auto_rank, size, name)

    valid.sort(key=rank)
    return valid[0]


def run_ytdlp(args: list[str], timeout: int = 180) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    out = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
    return proc.returncode, out


def log_has_429(log: str) -> bool:
    low = (log or "").lower()
    return "http error 429" in low or "too many requests" in low or "http 429" in low


def method_cmds(slug: str, ytid: str, episode_url: str, work: Path) -> list[tuple[str, list[str]]]:
    url = f"https://www.youtube.com/watch?v={ytid}"
    out_tmpl = str(work / f"{slug}.%(ext)s")
    base = [
        YTDLP,
        "--skip-download",
        "--no-playlist",
        "--no-overwrites",
        "--retries", "2",
        "--fragment-retries", "1",
        "--socket-timeout", "30",
        "--write-sub",
        "--write-auto-sub",
        "--sub-langs", "en.*,en",
        "--convert-subs", "vtt",
        "--impersonate", IMPERSONATE_TARGET,
        "-o", out_tmpl,
        "--newline",
    ]
    methods: list[tuple[str, list[str]]] = [
        (
            "impersonate_chrome_android_web_referer",
            base + [
                "--referer", "https://onemissionbible.churchcenter.com/",
                "--add-header", "Origin: https://onemissionbible.churchcenter.com",
                "--extractor-args", "youtube:player_client=android,web",
                url,
            ],
        ),
        (
            "impersonate_chrome_web_episode_referer",
            base + [
                "--referer", episode_url,
                "--add-header", "Origin: https://onemissionbible.churchcenter.com",
                "--extractor-args", "youtube:player_client=web",
                url,
            ],
        ),
    ]
    return methods


def scrub_work_dir(work: Path) -> None:
    for f in collect_caption_files(work):
        if is_block_page(f) or not is_real_caption(f):
            head = f.read_text(encoding="utf-8", errors="replace")[:120].lstrip().lower()
            if (
                head.startswith("<html")
                or head.startswith("<!doctype")
                or "automated queries" in head
                or is_block_page(f)
            ):
                print(f"    deleted block/html page: {f.name} ({f.stat().st_size} bytes)", flush=True)
                f.unlink(missing_ok=True)


def try_episode(slug: str, ytid: str, episode_url: str) -> dict:
    dest = CAP / f"{slug}.en.vtt"
    work = TMP / slug
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    errors: list[str] = []
    saw_429 = False
    for i, (method, cmd) in enumerate(method_cmds(slug, ytid, episode_url, work)):
        print(f"  method {i+1}/{2}: {method} (impersonate={IMPERSONATE_TARGET})", flush=True)
        try:
            code, log = run_ytdlp(cmd)
        except subprocess.TimeoutExpired:
            code, log = 124, "yt-dlp timed out"
        if log_has_429(log):
            saw_429 = True
        scrub_work_dir(work)
        best = pick_best(collect_caption_files(work))
        if best is not None:
            dest.write_bytes(best.read_bytes())
            rec = {
                "ok": True,
                "status": "ok",
                "source": method,
                "bytes": dest.stat().st_size,
                "error": None,
                "slug": slug,
                "file": dest.name,
                "raw_name": best.name,
                "http_429": False,
                "impersonate": IMPERSONATE_TARGET,
            }
            print(f"    SUCCESS via {method}: {dest.name} ({rec['bytes']} bytes) from {best.name}", flush=True)
            return rec
        err_line = None
        for line in (log or "").splitlines()[::-1]:
            s = line.strip()
            if s and (
                "error" in s.lower()
                or "warning" in s.lower()
                or "HTTP" in s
                or "429" in s
                or "caption" in s.lower()
                or "sub" in s.lower()
            ):
                err_line = s[:400]
                break
        if not err_line:
            tail = [ln.strip() for ln in (log or "").splitlines() if ln.strip()][-4:]
            err_line = " | ".join(tail)[:400] if tail else f"exit {code}, no caption files"
        errors.append(f"{method}: {err_line}")
        print(f"    fail: {err_line[:220]}", flush=True)
        if log_has_429(log):
            print(f"    HTTP 429: backing off {int(BACKOFF_429)}s (not hammering timedtext)", flush=True)
            time.sleep(BACKOFF_429)
            # one method already 429'd; do not immediately fire the next client
            break
        if i < 1:
            time.sleep(random.uniform(SLEEP_MIN, SLEEP_MAX))

    rec = {
        "ok": False,
        "status": "fail",
        "source": None,
        "bytes": 0,
        "error": " | ".join(errors)[:1500],
        "slug": slug,
        "file": None,
        "http_429": saw_429,
        "impersonate": IMPERSONATE_TARGET,
    }
    print("    ALL METHODS FAILED", flush=True)
    return rec


TAG_RE = re.compile(r"<[^>]+>")
TS_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}\.\d{3}")


def strip_cue_text(text: str) -> str:
    text = TAG_RE.sub("", text)
    text = unescape(text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", " ", text)
    return text.strip()


def parse_vtt_cues(vtt: str) -> list[str]:
    cues: list[str] = []
    blocks = re.split(r"\n\s*\n", vtt.replace("\r\n", "\n"))
    for block in blocks:
        lines = [ln.strip() for ln in block.split("\n") if ln.strip()]
        if not lines:
            continue
        if lines[0].upper().startswith("WEBVTT") or lines[0].lower().startswith("kind:") or lines[0].lower().startswith("language:"):
            continue
        body_lines: list[str] = []
        seen_ts = False
        for ln in lines:
            if TS_RE.search(ln) or "-->" in ln:
                seen_ts = True
                continue
            if re.fullmatch(r"\d+", ln) and not seen_ts:
                continue
            if ln.startswith("NOTE"):
                continue
            body_lines.append(ln)
        if not body_lines:
            continue
        text = strip_cue_text(" ".join(body_lines))
        if text:
            cues.append(text)
    return cues


def longest_overlap(a: str, b: str) -> int:
    max_n = min(len(a), len(b))
    for n in range(max_n, 0, -1):
        if a[-n:] == b[:n]:
            return n
    return 0


def merge_rolling_cues(cues: list[str]) -> str:
    """Merge YouTube rolling/duplicate auto-caption cues into running text."""
    if not cues:
        return ""
    parts: list[str] = []
    acc = cues[0]
    for cue in cues[1:]:
        if not cue:
            continue
        if cue == acc:
            continue
        if cue in acc:
            continue
        if acc in cue:
            acc = cue
            continue
        ov = longest_overlap(acc, cue)
        # rolling captions share a long suffix/prefix; tiny overlap is likely coincidental
        min_ov = 8 if min(len(acc), len(cue)) > 16 else 3
        if ov >= min_ov:
            acc = acc + cue[ov:]
            continue
        # word-level: if last words of acc match start of cue
        acc_words = acc.split()
        cue_words = cue.split()
        matched = 0
        max_w = min(len(acc_words), len(cue_words))
        for n in range(max_w, 0, -1):
            if acc_words[-n:] == cue_words[:n]:
                matched = n
                break
        if matched >= 2 or (matched == 1 and acc_words[-1].lower() not in {"the", "a", "and", "to", "of", "in"}):
            acc = " ".join(acc_words + cue_words[matched:])
            continue
        parts.append(acc)
        acc = cue
    if acc:
        parts.append(acc)
    return " ".join(parts)


def paragraphize(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    # split on sentence end, keep delimiter
    chunks = re.split(r"(?<=[.!?])\s+", text)
    paras: list[str] = []
    buf: list[str] = []
    char_count = 0
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        buf.append(chunk)
        char_count += len(chunk)
        if char_count >= 420 or chunk.endswith("?") or (char_count >= 220 and chunk.endswith(".")):
            paras.append(" ".join(buf))
            buf = []
            char_count = 0
    if buf:
        paras.append(" ".join(buf))
    return "\n\n".join(paras) + "\n"


def load_catalog_by_ytid() -> dict:
    if not CATALOG_PATH.exists():
        return {}
    try:
        items = json.loads(CATALOG_PATH.read_text())
    except json.JSONDecodeError:
        return {}
    out = {}
    for it in items:
        ytid = (it.get("media") or {}).get("youtube_id") or ""
        if ytid:
            out[ytid] = it
    return out


def write_transcript(slug: str, ytid: str, vtt_path: Path) -> Path | None:
    vtt = vtt_path.read_text(encoding="utf-8", errors="replace")
    if is_block_page(vtt_path) or not vtt.lstrip().startswith("WEBVTT"):
        return None
    cues = parse_vtt_cues(vtt)
    body = paragraphize(merge_rolling_cues(cues))
    if len(body.strip()) < 40:
        return None
    cat = load_catalog_by_ytid().get(ytid, {})
    title = cat.get("title") or cat.get("youtube_title") or slug
    speaker = cat.get("speaker") or ("Cindy Hawks" if slug.startswith("16-") else "Tim Hawks")
    date = cat.get("date") or ""
    header = [
        f"# {title}",
        "",
        f"Speaker: {speaker}",
        f"Date: {date}" if date else "Date: unknown",
        f"Source: YouTube captions (`{vtt_path.name}`)",
        "",
    ]
    out = TRANS / f"{slug}.md"
    out.write_text("\n".join(header) + body, encoding="utf-8")
    return out


def main() -> int:
    only = sys.argv[1:]
    status = load_status()
    items = EPISODES
    if only:
        items = [e for e in EPISODES if e[0] in only or e[1] in only]
    total = len(items)
    consecutive_429 = 0
    attempted = 0
    for idx, (slug, ytid, ep_url) in enumerate(items):
        dest = CAP / f"{slug}.en.vtt"
        prev = status.get(ytid)
        if prev and prev.get("ok") and dest.exists() and is_real_caption(dest):
            print(f"[{idx+1}/{total}] SKIP already ok {slug} ({ytid}) {dest.stat().st_size} bytes", flush=True)
            tpath = TRANS / f"{slug}.md"
            if not tpath.exists():
                tp = write_transcript(slug, ytid, dest)
                if tp:
                    print(f"    wrote transcript {tp.name} ({tp.stat().st_size} bytes)", flush=True)
            consecutive_429 = 0
            continue
        print(f"[{idx+1}/{total}] {slug} | {ytid}", flush=True)
        rec = try_episode(slug, ytid, ep_url)
        status[ytid] = rec
        save_status(status)
        attempted += 1
        if rec.get("ok") and dest.exists() and is_real_caption(dest):
            consecutive_429 = 0
            tp = write_transcript(slug, ytid, dest)
            if tp:
                rec["transcript"] = tp.name
                rec["transcript_bytes"] = tp.stat().st_size
                status[ytid] = rec
                save_status(status)
                print(f"    wrote transcript {tp.name} ({tp.stat().st_size} bytes)", flush=True)
        elif rec.get("http_429"):
            consecutive_429 += 1
            print(f"    429 count this run: {consecutive_429}/{STOP_AFTER_429_VIDEOS}", flush=True)
            if consecutive_429 >= STOP_AFTER_429_VIDEOS:
                status["_meta"] = {
                    "blocker": "HTTP 429 timedtext",
                    "message": (
                        "YouTube timedtext still returns HTTP 429 after TLS impersonation "
                        f"({IMPERSONATE_TARGET}) on {consecutive_429} videos. "
                        "Browser path on a residential IP is required. Stopped to avoid hammering timedtext."
                    ),
                    "impersonate": IMPERSONATE_TARGET,
                    "curl_cffi": True,
                    "videos_attempted_this_run": attempted,
                    "stop_after_429_videos": STOP_AFTER_429_VIDEOS,
                    "ok": 0,
                }
                save_status(status)
                print("\nSTOP: impersonation still 429 after 3 videos. Browser path required.", flush=True)
                return 2
        else:
            consecutive_429 = 0
        if idx < total - 1:
            delay = random.uniform(SLEEP_MIN, SLEEP_MAX)
            print(f"  sleep {delay:.1f}s before next video", flush=True)
            time.sleep(delay)
    save_status(status)
    recs = [v for k, v in status.items() if k != "_meta" and isinstance(v, dict)]
    ok_n = sum(1 for v in recs if v.get("ok"))
    fail_n = sum(1 for v in recs if not v.get("ok"))
    print(f"\nDONE ok={ok_n} fail={fail_n} of {len(recs)}", flush=True)
    return 0 if fail_n == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
