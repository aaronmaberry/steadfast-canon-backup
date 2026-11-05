"""Render the L01 cut from layout.build(): one exact-length H.264 segment per shot, concatenated, then muxed with the
week-free narration (one continuous track, untouched apart from level).

usage: python3 render.py [--res 1080|720] [--only i,j,...] [--force]
"""
import sys, json, math, subprocess, pathlib, argparse, shlex
sys.path.insert(0, "/home/claude/l04/edit"); sys.path.insert(0, "/home/claude/l04/plan")
import layout

ap = argparse.ArgumentParser()
ap.add_argument("--res", default="1080"); ap.add_argument("--only", default=""); ap.add_argument("--force", action="store_true")
ap.add_argument("--crf", default="18"); ap.add_argument("--out", default="")
A = ap.parse_args()
W, H = (1920, 1080) if A.res == "1080" else (1280, 720)
SC = W / 1920
FPS = 25
PRE = 4.0                       # silent logo open before the first word
ROOT = pathlib.Path("/home/claude/l04")
GFX = ROOT / "gfx/out"
WORK = ROOT / f"render_{A.res}"; WORK.mkdir(exist_ok=True)
KIT = ROOT / "repo/biblical-manhood/studio/training-video/wes-heygen-clips-L01"
MASTER = ROOT / "master/l04_master.mp4"   # olive henley master, rendered on this narration (lips frame-exact)
FIELD_COL = "0x09090C"
DIP_IN, DIP_OUT = 0.30, 0.25
BUILD = 0.30                    # board build crossfade
# v6: slow preset + film tuning at CRF 16 so Wes's face keeps HeyGen's detail. Every segment MUST use identical settings
# (the segments are joined without re-encoding, and they share one set of stream headers).
ENC = ["-c:v", "libx264", "-preset", "slow", "-tune", "film", "-crf", A.crf, "-profile:v", "high", "-level:v", "4.1",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]
# v7: easier to play (in-app player hiccuped on v6's sound): level 4.1, 4 reference frames, peaks capped at 12 Mb/s
X264 = "ref=4:vbv-maxrate=12000:vbv-bufsize=24000"
# b-roll: same CRF (so the stream headers stay identical) but a quality floor, so stock footage grain does not eat the
# file size - keeps the master under the 400 MB send limit while Wes keeps full quality
R_CAP = ":qpmin=20"


def png(key):
    p = GFX / f"{key}.png"
    if A.res == "1080":
        return str(p)
    q = WORK / "png" / f"{key}.png"
    if not q.exists():
        q.parent.mkdir(exist_ok=True)
        from PIL import Image
        Image.open(p).resize((W, H), Image.LANCZOS).save(q)
    return str(q)


def masks():
    from PIL import Image, ImageDraw
    import numpy as np
    m = {}
    y = np.arange(1080)[:, None].astype(float)
    ss = lambda e0, e1, v: (lambda t: t * t * (3 - 2 * t))(np.clip((v - e0) / (e1 - e0), 0, 1))
    wide = (1 - ss(660, 840, y)) * np.ones((1080, 1920))
    p = WORK / "mask_wide.png"; Image.fromarray((wide * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS).save(p); m["wide"] = str(p)
    card = Image.new("L", (840, 600), 0); ImageDraw.Draw(card).rounded_rectangle((0, 0, 839, 599), 16, fill=255)
    p = WORK / "mask_card.png"; card.resize((round(840 * SC), round(600 * SC)), Image.LANCZOS).save(p); m["card"] = str(p)
    return m


MASK = masks()
import numpy as _np
from PIL import Image as _Image
WIDE = json.load(open(str(ROOT / "wide/widescan.json")))
WIDX = _np.load(str(ROOT / "plan/w_idx.npy"))
WS_SHIFT = 420                       # half screen: Wes moves right, board text sits left (x 128-908)


def _ws_mask():
    x = _np.arange(1920)[None, :].astype(float)
    t = _np.clip((x - (WS_SHIFT + 40)) / 260, 0, 1); a = t * t * (3 - 2 * t)        # feather the shifted frame's left edge
    p = WORK / "mask_ws.png"; _Image.fromarray((_np.repeat(a, 1080, 0) * 255).astype(_np.uint8)).resize((W, H), _Image.LANCZOS).save(p)
    return str(p)


MASK["ws"] = _ws_mask()


def wide_take(s):
    """v6: the wide clip's exact first frame (nearest frame to the narration time), picked by frame number - seeking
    by time landed one frame late on some shots (lips 40 ms behind)"""
    k = int(WIDX[s["f0"]]); c = WIDE[k]
    return ROOT / "wide" / c["file"], max(0, round((s["t0"] - c["a"]) * FPS))


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(shlex.quote(c) for c in cmd)[:4000]); print(r.stderr[-3000:]); raise SystemExit(1)


BOUT, BIN = 0.14, 0.20      # band -> band: old line fades out fully, then the new one fades in (no overlap)


def band_seq(lst):
    """True when a caption band is followed directly by another band (those changes are sequential, not cross-faded)"""
    return any(a[1] is not None and b[1] is not None for a, b in zip(lst, lst[1:]))


def overlays(chain, inputs, last, n_in, k, lst, t0, dur, nfr, first_no_fade=True, seq=False):
    """board/band states: each fades in over BUILD at its time and stays until the next state has fully landed.
    seq=True (caption bands): a band followed by a band fades out over BOUT first; the next fades in after it is gone."""
    lst = [(max(t - t0, 0.0), key) for t, key in lst]
    if seq and len(lst) > 1 and lst[0][0] < 0.02 and lst[0][1] and lst[1][1] and lst[1][0] < 0.5:
        lst = lst[1:]       # a carried-over line that would only flash for a moment after the cut: let the cut take it
    for j, (t, key) in enumerate(lst):
        if key is None:
            continue
        nxt = lst[j + 1] if j + 1 < len(lst) else None
        prv = lst[j - 1] if j > 0 else None
        after_band = seq and prv is not None and prv[1] is not None
        if seq and nxt is not None and nxt[1] is not None:
            end = min(dur, nxt[0] + BOUT + 0.02)
        else:
            end = dur if nxt is None else min(dur, nxt[0] + (BUILD if nxt[1] is not None else 0) + 0.04)
        if end <= t:
            continue
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", png(key)]
        fx = ["format=rgba"]
        fade_in = not (first_no_fade and t < 0.02)
        if after_band:
            fx.append(f"fade=t=in:st={t + BOUT:.3f}:d={BIN:.3f}:alpha=1")
        elif fade_in:
            fx.append(f"fade=t=in:st={t:.3f}:d={BUILD:.3f}:alpha=1")
        if nxt is not None and nxt[1] is None:
            fx.append(f"fade=t=out:st={nxt[0]:.3f}:d={BUILD:.3f}:alpha=1")
        elif seq and nxt is not None:
            fx.append(f"fade=t=out:st={nxt[0]:.3f}:d={BOUT:.3f}:alpha=1")
        chain.append(f"[{n_in}:v]{','.join(fx)}[o{k}]")
        chain.append(f"[{last}][o{k}]overlay=0:0:eof_action=pass:enable='between(t,{t:.3f},{end:.3f})'[x{k}]")
        last = f"x{k}"; n_in += 1; k += 1
    return last, n_in, k


def broll_in(path, dur, src_in):
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                             capture_output=True, text=True).stdout or 0)
    lo, hi = (0.4, d - 0.4) if "broll_v4" in str(path) else (0.0, d)     # v4 extracts: stay clear of v4's own transitions
    if src_in is None:
        room = hi - lo - dur
        src_in = lo + (max(0.0, room * 0.4) if room > 0 else 0.0)
    loop = d < src_in + dur + 0.1
    return src_in, loop


def shot_cmd(s, dip_in, dip_out, out):
    dur = (s["f1"] - s["f0"]) / FPS; N = s["f1"] - s["f0"]; nfr = N + 2
    t0 = s["t0"]
    inputs = ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", png("FIELD")]
    chain = ["[0:v]format=rgba[b0]"]; last = "b0"; n_in = 1; k = 0
    kind = s["kind"]
    if kind == "W":
        inputs += ["-ss", f"{t0:.3f}", "-i", str(MASTER),
                   "-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", MASK["wide"]]
        chain += [f"[1:v]fps={FPS},scale={W}:{H}{settle(s, W, H)},format=rgba,setpts=PTS-STARTPTS[wv]", "[2:v]format=gray[wm]",
                  "[wv][wm]alphamerge[wa]", f"[{last}][wa]overlay=0:0:eof_action=repeat[wb]"]
        last = "wb"; n_in = 3
        last, n_in, k = overlays(chain, inputs, last, n_in, k, s.get("bands", []), t0, dur, nfr, first_no_fade=bool(s.get("cont")), seq=True)
    elif kind == "P":
        ss = t0
        cw, chh, cx = round(840 * SC), round(600 * SC), round(1000 * SC)
        inputs += ["-ss", f"{ss:.3f}", "-i", str(MASTER), "-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", MASK["card"]]
        chain += [f"[1:v]fps={FPS},crop=1120:800:400:0,scale={cw}:{chh}{settle(s, cw, chh)},format=rgba,setpts=PTS-STARTPTS[pv]", "[2:v]format=gray[pm]",
                  "[pv][pm]alphamerge[pa]", f"[{last}][pa]overlay={cx}:{round(210 * SC)}:eof_action=repeat[pb]"]
        last = "pb"; n_in = 3
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", png("CARD")]
        chain.append(f"[{n_in}:v]format=rgba[cf]"); chain.append(f"[{last}][cf]overlay=0:0[pc]"); last = "pc"; n_in += 1
        last, n_in, k = overlays(chain, inputs, last, n_in, k, s["states"], t0, dur, nfr, first_no_fade=True)
    elif kind == "WW":
        f, j0 = wide_take(s)
        inputs += ["-i", str(f)]
        chain += [f"[1:v]trim=start_frame={j0},setpts=PTS-STARTPTS,fps={FPS},scale={W}:{H},format=rgba[wv]", f"[{last}][wv]overlay=0:0:eof_action=repeat[wb]"]
        last = "wb"; n_in = 2
        if any(kk for _, kk in s.get("bands", [])):     # caption over the wide gesture take: darken behind the text (hands)
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", "/home/claude/l04/gfx/out/WWSCRIM.png"]
            chain += ["[2:v]format=rgba[ws]", "[wb][ws]overlay=0:0[wsb]"]; last = "wsb"; n_in = 3
        last, n_in, k = overlays(chain, inputs, last, n_in, k, s.get("bands", []), t0, dur, nfr, first_no_fade=bool(s.get("cont")), seq=True)
    elif kind == "WS":
        f, j0 = wide_take(s)
        sh_ = round(WS_SHIFT * SC)
        inputs += ["-i", str(f), "-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", MASK["ws"]]
        chain += [f"[1:v]trim=start_frame={j0},setpts=PTS-STARTPTS,fps={FPS},scale={W}:{H},pad={W + sh_}:{H}:{sh_}:0:black,crop={W}:{H}:0:0,format=rgba[wv]",
                  "[2:v]format=gray[wm]", "[wv][wm]alphamerge[wa]", f"[{last}][wa]overlay=0:0:eof_action=repeat[wb]"]
        last = "wb"; n_in = 3
        last, n_in, k = overlays(chain, inputs, last, n_in, k, s["states"], t0, dur, nfr, first_no_fade=True)
    elif kind == "F":
        last, n_in, k = overlays(chain, inputs, last, n_in, k, s["states"], t0, dur, nfr, first_no_fade=True)
    elif kind == "R":
        p = layout.clip_path(s["clip"])
        src_in, loop = broll_in(p, dur, s.get("src_in"))
        inputs += (["-stream_loop", "-1"] if loop else []) + ["-ss", f"{src_in:.3f}", "-i", str(p)]
        z = 1.07
        sw, sh = math.ceil(W * z / 2) * 2, math.ceil(H * z / 2) * 2
        chain += [f"[1:v]fps={FPS},scale={sw}:{sh}:force_original_aspect_ratio=increase,crop={sw}:{sh},setsar=1,"
                  f"crop={W}:{H}:x='({sw}-{W})*(0.15+0.7*t/{dur:.3f})':y='({sh}-{H})/2',"
                  f"eq=saturation=0.88:brightness=-0.02:contrast=1.03,vignette=PI/5,format=rgba,setpts=PTS-STARTPTS[rv]",
                  f"[{last}][rv]overlay=0:0:eof_action=repeat[rb0]",
                  "[2:v]format=rgba[rs]", "[rb0][rs]overlay=0:0[rb]"]
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", "/home/claude/l04/gfx/out/RSCRIM.png"]
        last = "rb"; n_in = 3   # L04: bottom scrim so band text reads over bright footage
        last, n_in, k = overlays(chain, inputs, last, n_in, k, s.get("label", []), t0, dur, nfr, first_no_fade=False, seq=True)
    elif kind == "LOGO":
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", png("LOGO")]
        hold_end = dur - 0.2 - 0.8
        chain += [f"[1:v]format=rgba,fade=t=in:st=0.4:d=0.8:alpha=1,fade=t=out:st={hold_end:.3f}:d=0.8:alpha=1[lg]",
                  f"[{last}][lg]overlay=0:0[lb]"]
        last = "lb"; n_in = 2
    elif kind == "OPEN":
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", png("OPEN")]
        chain = ["[0:v]format=rgba,drawbox=c=black:t=fill[b0]",
                 f"[1:v]format=rgba,fade=t=in:st=0.3:d=1.0:alpha=1[op]", "[b0][op]overlay=0:0[lb]"]
        last = "lb"; n_in = 2
    if s.get("xin"):
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur + 0.2:.3f}", "-i", s["xin"]]
        chain += [f"[{n_in}:v]format=rgba,fade=t=out:st=0:d={XFADE}:alpha=1[xp]", f"[{last}][xp]overlay=0:0:eof_action=pass[xo]"]
        last = "xo"; n_in += 1
    fx = []
    if dip_in:
        fx.append(f"fade=t=in:st=0:d={DIP_IN}:color={FIELD_COL}")
    if dip_out:
        fx.append(f"fade=t=out:st={dur - DIP_OUT:.3f}:d={DIP_OUT}:color={FIELD_COL}")
    chain.append(f"[{last}]format=yuv420p{(',' + ','.join(fx)) if fx else ''}[vout]")
    return ["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(chain), "-map", "[vout]", "-frames:v", str(N), *ENC, "-x264-params", X264 + (R_CAP if kind == "R" else ""), str(out)]


XFADE = 0.7          # board -> Wes: cross-dissolve
SETTLE = 1.5         # Wes entry: eases from 2.5% zoom to framed over 1.5 s


def settle(s, w, h):
    # v6: off. ffmpeg's zoompan snaps the frame to whole pixels, so the slow push-in made his face shimmer/wobble by
    # half a pixel every frame for 1.5 s on every entry. Entries are now the board dissolve / soft dip only.
    if True or not s.get("entry"):
        return ""
    n = round(SETTLE * FPS)
    return (f",zoompan=z='1+0.025*pow(max(0\\,1-on/{n})\\,2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":d=1:s={w}x{h}:fps={FPS}")


def entry_kind(prev, s):
    """how a Wes shot comes in: 'x' dissolve from a board, 'd' soft dip, None (camera change inside a shot / first shot)"""
    if s["kind"] not in ("W", "P") or prev is None or s.get("cont"):
        return None
    return "x" if prev["kind"] == "F" else "d"


def boundary(a, b):
    """dip through the field between anything involving boards or the panel; hard cut between picture and picture"""
    if a is None or b is None:
        return True
    if b.get("cont"):
        return False                  # camera change inside one shot: hard cut, words and board text carry on
    if entry_kind(a, b) == "x":
        return False                  # board dissolves straight into Wes
    if entry_kind(a, b) == "d":
        return True                   # soft dip into Wes after b-roll / another Wes shot
    if a["kind"] in ("W", "R", "WW") and b["kind"] in ("W", "R", "WW"):
        return False
    return True


if __name__ == "__main__":
    sh, probs, warn = layout.check_all()
    hard = [p for p in probs if "band PH_3 on" not in p]   # PH_3 carries over from the previous shot
    if hard:
        for p in hard:
            print("PROBLEM", p)
        raise SystemExit("layout check failed")
    shots = [dict(i=-1, kind="OPEN", f0=0, f1=round(PRE * FPS), t0=0.0, t1=PRE)] + sh
    only = {int(x) for x in A.only.split(",") if x}
    files = []
    for j, s in enumerate(shots):
        prev = shots[j - 1] if j > 0 else None; nxt = shots[j + 1] if j + 1 < len(shots) else None
        ek = entry_kind(prev, s)
        s["entry"] = bool(ek)
        if ek == "x":
            pf = WORK / f"last_{files[-1].stem}.png"
            if not pf.exists():
                run(["ffmpeg", "-y", "-v", "error", "-sseof", "-0.06", "-i", str(files[-1]), "-frames:v", "1", "-update", "1", str(pf)])
            s["xin"] = str(pf)
        dip_in = s["kind"] != "OPEN" and boundary(prev, s)
        dip_out = boundary(s, nxt) and nxt is not None
        if s["kind"] == "OPEN":
            dip_out = True
        import hashlib
        key = json.dumps({kk: v for kk, v in s.items() if kk not in ("i", "seg")}, sort_keys=True, default=str) + \
            f"{dip_in}{dip_out}{A.crf}slowfilm{X264}l41{'qpmin20rscrim' if s['kind'] == 'R' else ''}{s['seg']['i'] if s.get('seg') else ''}" + \
            ("wwscrim1" if s["kind"] == "WW" and any(kk for _, kk in s.get("bands", [])) else "") + ("seqband2" if band_seq(s.get("bands") or s.get("label") or []) else "") + \
            (f"olive:{MASTER.stat().st_size}:660-840:1120x800:v6slowfilm:nosettle" if s["kind"] in ("W", "P") else "") + \
            (f"wide:{WIDX[s['f0']]}:{WS_SHIFT}:v6slowfilm:trimframe:{(ROOT / 'wide' / WIDE[int(WIDX[s['f0']])]['file']).stat().st_size}" if s["kind"] in ("WW", "WS") else "") + "".join(
            hashlib.md5(open(png(kk), "rb").read()).hexdigest()[:8]
            for _, kk in (s.get("states") or []) + (s.get("bands") or []) + (s.get("label") or []) if kk)
        out = WORK / f"seg_{s['kind']}_{hashlib.sha1(key.encode()).hexdigest()[:12]}.mp4"; files.append(out)
        if only and s["i"] not in only:
            continue
        if out.exists() and not A.force:
            continue
        run(shot_cmd(s, dip_in, dip_out, out))
        print(f"{j:3d} #{s['i']:3d} {s['kind']:4s} {s['t0']:8.2f}-{s['t1']:8.2f} {'dip' if dip_in else 'cut'}", flush=True)
    if only:
        raise SystemExit(0)
    (WORK / "list.txt").write_text("".join(f"file '{f}'\n" for f in files))
    raw = WORK / "video.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(WORK / "list.txt"), "-c", "copy", str(raw)])
    total_frames = round(PRE * FPS) + sh[-1]["f1"]
    print("video frames", total_frames, "=", total_frames / FPS, "s")
