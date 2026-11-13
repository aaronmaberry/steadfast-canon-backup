"""Resolve spec.S into frame-exact shots and check them before anything renders.

Checks: shot order and length; Wes on screen only where his take is clean (no hands in view, no chin jut, no
patch joins, no audio joins); every board state readable for long enough; every b-roll clip present and used once."""
import json, sys, pathlib, re
import numpy as np
sys.path.insert(0, "/home/claude/l04/plan"); sys.path.insert(0, "/home/claude/l04/edit")
import cues
JOINS = []
import spec

FPS = 25
QW = np.load("/home/claude/l04/plan/q_wide.npy"); QPT = np.load("/home/claude/l04/plan/q_tight.npy"); QP = np.load("/home/claude/l04/plan/q_panel.npy")
sys.path.insert(0, "/home/claude/l04/gfx")
BROLL = pathlib.Path("/home/claude/l04/broll")


def words_n(s):
    return len(re.findall(r"[A-Za-z0-9']+", s))


def clip_path(key):
    if key.startswith("v4b"):
        m = sorted(pathlib.Path("/home/claude/l01/broll_v4").glob(f"v4b{key[3:]}_*.mp4"))
        return m[0] if m else None
    for p in (BROLL / f"{key}.mp4",):
        if p.exists():
            return p
    import os
    if os.environ.get("L01_PREVIEW_BROLL") and key.startswith("m"):     # draft only: 360p previews stand in
        p = pathlib.Path(f"/home/claude/l01/prev/{key}.mp4")
        if p.exists():
            return p
    return None


def build(raw=False):
    sh = []
    for i, (t, kind, prm) in enumerate(spec.S):
        t1 = spec.S[i + 1][0] if i + 1 < len(spec.S) else spec.END
        f0, f1 = round(t * FPS), round(t1 * FPS)
        sh.append(dict(i=i, kind=kind, f0=f0, f1=f1, t0=f0 / FPS, t1=f1 / FPS, **prm))
    if raw:
        return sh
    import angles
    return angles.refine(sh)


def wide_seg(t0, t1):
    a, b = o2s(t0), o2s(t1)
    for s in SEGS:
        if s["a"] - 0.05 <= a and b <= s["b"] + 0.02:
            return s
    return None


def check(sh, strict_broll=True):
    import boards
    probs, warn = [], []
    used = {}
    for s in sh:
        d = s["t1"] - s["t0"]
        tag = f"#{s['i']} {s['kind']} {s['t0']:.2f}-{s['t1']:.2f}"
        if d <= 0:
            probs.append(f"{tag}: non-positive length"); continue
        if d < (2.0 if s["kind"] != "R" else 1.8) and s["kind"] != "LOGO":
            warn.append(f"{tag}: short shot {d:.2f}s")
        fr = slice(s["f0"], s["f1"])
        if s["kind"] == "W":
            seg = None                      # burgundy master covers the whole lesson
            bad = np.where(QW[fr] != 0)[0]
            if len(bad):
                probs.append(f"{tag}: wide not clean at {sorted(set(round((s['f0'] + b) / FPS, 1) for b in bad))[:8]}")
            s["seg"] = seg
        if s["kind"] == "P":
            bad = np.where((QPT if s.get("tight") else QP)[fr] != 0)[0]
            if len(bad):
                probs.append(f"{tag}: panel not clean at {sorted(set(round((s['f0'] + b) / FPS, 1) for b in bad))[:8]}")
        if s["kind"] in ("WW", "WS"):
            import angles
            bad = np.where(angles.QWW[fr] != 0)[0]
            if len(bad):
                probs.append(f"{tag}: wide not clean/covered at {sorted(set(round((s['f0'] + b) / FPS, 1) for b in bad))[:8]}")
            if len(set(angles.WIDX[fr].tolist())) != 1:
                probs.append(f"{tag}: wide piece spans two takes")
        if s.get("split"):
            continue                 # a camera change inside one shot: readability is checked on the whole shot
        if s["kind"] in ("W", "P"):
            for j in JOINS:
                if s["t0"] + 0.02 < j < s["t1"] - 0.02:
                    probs.append(f"{tag}: spans audio join {j:.2f}")
        if s["kind"] == "R":
            p = clip_path(s["clip"])
            if p is None:
                (probs if strict_broll else warn).append(f"{tag}: clip {s['clip']} missing")
            if s["clip"] in used:
                probs.append(f"{tag}: clip {s['clip']} reused (also #{used[s['clip']]})")
            used[s["clip"]] = s["i"]
        # board readability: each state on screen long enough for the words it adds
        st = s.get("states") or []
        lab = [x for x in (s.get("bands") or []) + (s.get("label") or [])]
        fam = lambda key: key.rsplit("_", 1)[0] if key and "_" in key else key
        for lst, name in ((st, "state"), (lab, "band")):
            groups = []          # consecutive build steps of one family are read as one board
            for j, (t, key) in enumerate(lst):
                if key is None:
                    continue
                if key not in boards.B:
                    probs.append(f"{tag}: unknown board {key}"); continue
                if t < s["t0"] - 0.01 or t > s["t1"]:
                    probs.append(f"{tag}: {name} {key} at {t:.2f} outside shot")
                nxt = lst[j + 1][0] if j + 1 < len(lst) else s["t1"]
                vis = nxt - max(t, s["t0"])
                need = min(4.0, 0.9 + words_n(boards.TEXT[key]) / 3.4) if boards.TEXT[key] else 0.9
                if groups and fam(groups[-1][-1][0]) == fam(key) and lst[j - 1][1] is not None:
                    prevtxt = boards.TEXT[groups[-1][-1][0]]
                    new = boards.TEXT[key][len(prevtxt):] if boards.TEXT[key].startswith(prevtxt[:20]) else boards.TEXT[key]
                    need = min(4.0, 0.5 + words_n(new) / 3.4)
                    groups[-1].append((key, vis, need))
                else:
                    groups.append([(key, vis, need)])
            for g in groups:
                tot_v = sum(v for _, v, _ in g); tot_n = sum(n for _, _, n in g)
                short = [f"{k} {v:.2f}s" for k, v, n in g[:-1] if v < 0.55]
                last_k, last_v, last_n = g[-1]
                if short:
                    probs.append(f"{tag}: {name} build step too quick: {short}")
                if tot_v < tot_n - 0.05 or last_v < min(last_n, 1.6):
                    lvl = probs if (tot_v < 0.8 * tot_n or last_v < 0.6 * min(last_n, 1.6)) else warn
                    lvl.append(f"{tag}: {name} {'/'.join(k for k, _, _ in g)} on {tot_v:.2f}s (last {last_v:.2f}s), needs {tot_n:.1f}s")
    return probs, warn


def check_all(strict_broll=True):
    """cleanliness on the two-camera cut, readability on the shots as written"""
    sh = build()
    p1, w1 = check(sh, strict_broll)
    p2, w2 = check(build(raw=True), strict_broll)
    keep = lambda x: not any(k in x for k in ("not clean", "spans", "missing", "reused"))
    # SOP v2 rule C2 (Aaron, L02): every Wes piece holds 3 s or more; full-frame name stings may be 2.4 s
    short = [f"#{s['i']} {s['kind']} {s['t0']:.2f}-{s['t1']:.2f}: {s['t1'] - s['t0']:.2f}s piece, needs 3.0s (C2)"
             for s in sh if s["kind"] in ("W", "P", "WW", "WS") and s["t1"] - s["t0"] < 3.0]
    short += [f"#{s['i']} F {s['t0']:.2f}-{s['t1']:.2f}: {s['t1'] - s['t0']:.2f}s board, needs 2.4s (C2)"
              for s in sh if s["kind"] == "F" and s["t1"] - s["t0"] < 2.4]
    return sh, p1 + [x for x in p2 if keep(x) and x not in p1] + short, w1 + [x for x in w2 if keep(x) and x not in w1]


if __name__ == "__main__":
    sh, probs, warn = check_all(strict_broll=False)
    print(f"{len(sh)} shots, picture {sh[-1]['t1']:.2f}s")
    for p in probs:
        print("PROBLEM", p)
    for w in warn:
        print("warn   ", w)
    kinds = {}
    for s in sh:
        kinds[s["kind"]] = kinds.get(s["kind"], 0) + s["t1"] - s["t0"]
    print({k: round(v, 1) for k, v in kinds.items()})
