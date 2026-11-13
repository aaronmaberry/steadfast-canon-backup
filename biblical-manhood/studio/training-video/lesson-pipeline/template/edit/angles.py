"""Two-camera pass over the spec's Wes shots.

Cameras: the master (close talking head: W full frame, P card beside a board) and the HeyGen wide takes (waist-up with
gestures: WW full frame, WS half screen = Wes on the right, the same board text on the left).
1. Clean every Wes shot: where the master has a face glitch, cut at the nearest pauses to the wide angle (if it covers
   that stretch cleanly), else to the full-frame version of the board (P) — W leftovers are reported for hand edits.
2. Variety: long master moments inside a clean wide stretch switch to the wide angle at a pause part-way through.
Pieces of one original shot hard-cut into each other (picture changes, words and board text stay put).
"""
import json, numpy as np

FPS = 25
QW = np.load("/home/claude/l04/plan/q_wide.npy"); QP = np.load("/home/claude/l04/plan/q_panel.npy"); QPT = np.load("/home/claude/l04/plan/q_tight.npy")
QWW = np.load("/home/claude/l04/plan/q_ww.npy"); WIDX = np.load("/home/claude/l04/plan/w_idx.npy")
PAUSES = [(a, b) for a, b in json.load(open("/home/claude/l04/plan/pauses.json"))]
MIN = 1.6          # shortest piece
MIDS = [round(((a + b) / 2) * FPS) for a, b in PAUSES]
LEFT = []          # W stretches with no clean alternative (reported)


def clean(q, f0, f1):
    return f1 > f0 and bool((q[f0:f1] == 0).all())


USE_WIDE = True    # v6: back on (Aaron checked the HeyGen wide renders: clean). v5's face issues came from my encode, not HeyGen.
_WS = json.load(open("/home/claude/l04/wide/widescan.json"))
_VER = json.load(open("/home/claude/l04/wide/verified.json"))["wide"]
BAD_TAKES = {i for i, c in enumerate(_WS) if not _VER.get(c["id"], False)}   # local copy does not match HeyGen's file


# v7: Aaron - no waist-up in these stretches (narration seconds)
NO_WIDE = []
W_COVER = True     # L12: W stretches with hands up and no clean wide -> full-frame band board


def wide_ok(f0, f1):
    if not USE_WIDE or not clean(QWW, f0, f1):
        return False
    if any(f0 < b * FPS and f1 > a * FPS for a, b in NO_WIDE):
        return False
    if int(WIDX[f0]) in BAD_TAKES:
        return False
    return len(set(WIDX[f0:f1].tolist())) == 1     # one take for the whole piece


def cuts_in(f0, f1):
    return [m for m in MIDS if f0 + MIN * FPS <= m <= f1 - MIN * FPS]


def active(lst, f):
    cur = None
    for t, k in lst:
        if round(t * FPS) <= f:
            cur = k
    return cur


def piece(s, kind, f0, f1, src):
    p = dict(s); p.update(kind=kind, f0=f0, f1=f1, t0=f0 / FPS, t1=f1 / FPS, cam=src)
    key = "states" if s["kind"] == "P" else "bands"
    lst = s.get(key) or []
    inside = [(t, k) for t, k in lst if f0 < round(t * FPS) < f1]
    cur = active(lst, f0)
    new = ([(f0 / FPS, cur)] if cur is not None else []) + inside
    if kind == "F":
        new = [(t, (k + "F") if k else k) for t, k in new]
        p.pop("bands", None); p["states"] = new
    elif kind == "WS":
        p["states"] = new
    else:
        p[key] = new
    return p


def split_shot(s, extra_wide=False):
    f0, f1 = s["f0"], s["f1"]
    q = QW if s["kind"] == "W" else QP
    alt = "WW" if s["kind"] == "W" else "WS"
    # label every frame: 'm' master ok, 'w' wide ok, 'x' neither
    lab = np.array(["m" if q[f] == 0 else ("w" if QWW[f] == 0 else "x") for f in range(f0, f1)])
    if (lab == "m").all() and not extra_wide:
        return [s]
    cuts = [f0] + cuts_in(f0, f1) + [f1]
    segs = list(zip(cuts[:-1], cuts[1:]))
    choice = []
    for a, b in segs:
        if clean(q, a, b):
            choice.append("m")
        elif wide_ok(a, b):
            choice.append("w")
        elif s["kind"] == "W" and W_COVER and clean(QP, a, b):
            choice.append("p")
        elif W_COVER and clean(QPT, a, b):
            choice.append("t")          # L12: tighter Wes card (crop to y 700) keeps Wes on screen above the hands
        else:
            choice.append("x")
    if extra_wide and all(c == "m" for c in choice) and len(segs) >= 2:
        # variety (v6): switch one part to the waist-up angle at a pause, back part first, then front part; try the
        # pauses nearest the middle first; both parts must be >= 3 s so the camera changes are paced, not choppy
        mid = (f0 + f1) / 2
        for k in sorted(range(1, len(segs)), key=lambda i: abs(segs[i][0] - mid)):
            cut = segs[k][0]
            if (cut - f0) / FPS < 3.0 or (f1 - cut) / FPS < 3.0:
                continue
            if wide_ok(cut, f1):
                choice = ["m"] * k + ["w"] * (len(segs) - k); break
            if wide_ok(f0, cut):
                choice = ["w"] * k + ["m"] * (len(segs) - k); break
    # pacing: a close-up piece shorter than 3.5 s between cover pieces is not worth the flip - cover it too
    if s["kind"] == "P":
        for i, ((a, b), c) in enumerate(zip(segs, choice)):
            if c == "m" and (b - a) / FPS < 3.5 and any(x == "x" for x in choice):
                choice[i] = "x"
    # L12: no Wes piece under 3 s and no cover board under 2.4 s inside a split shot (C2). A short run takes a
    # neighbour's camera when that camera is clean over it; otherwise a Wes run becomes cover.
    if any(c != "m" for c in choice):
        def ok(c, a, b):
            return {"m": lambda: clean(q, a, b), "w": lambda: wide_ok(a, b),
                    "p": lambda: s["kind"] == "W" and W_COVER and clean(QP, a, b),
                    "t": lambda: W_COVER and clean(QPT, a, b), "x": lambda: True}[c]()
        for _ in range(12):
            runs = []
            for j, c in enumerate(choice):
                if runs and runs[-1][2] == c: runs[-1][1] = j
                else: runs.append([j, j, c])
            changed = False
            for r, (j0, j1, c) in enumerate(runs):
                d = (segs[j1][1] - segs[j0][0]) / FPS
                if d >= (2.44 if c == "x" else 3.0):
                    continue
                nbs = []
                if r > 0: nbs.append(runs[r - 1])
                if r < len(runs) - 1: nbs.append(runs[r + 1])
                nbs.sort(key=lambda n: -(segs[n[1]][1] - segs[n[0]][0]))
                for n0, n1, nc in nbs:
                    lo, hi = segs[min(j0, n0)][0], segs[max(j1, n1)][1]
                    if nc != "x" and ok(nc, lo, hi):
                        for j in range(j0, j1 + 1): choice[j] = nc
                        changed = True; break
                else:
                    if c != "x":
                        for j in range(j0, j1 + 1): choice[j] = "x"
                        changed = True
                    elif nbs:                      # a short cover: fold the shorter neighbour Wes run into it,
                        n0, n1, nc = nbs[-1]           # or take the neighbour's nearest pause-to-pause chunk
                        if (segs[n1][1] - segs[n0][0]) / FPS < 6.0:
                            for j in range(n0, n1 + 1): choice[j] = "x"
                            changed = True
                        else:
                            for n0, n1, nc in nbs:
                                if n1 > n0:
                                    jn = n1 if n1 < j0 else n0
                                    rest = (segs[n1][1] - segs[n0][0] - (segs[jn][1] - segs[jn][0])) / FPS
                                    if rest >= 3.0:
                                        choice[jn] = "x"; changed = True; break
                if changed: break
            if not changed: break
    # merge equal neighbours
    pieces = []
    for (a, b), c in zip(segs, choice):
        if pieces and pieces[-1][2] == c:
            pieces[-1][1] = b
        else:
            pieces.append([a, b, c])
    out = []
    for a, b, c in pieces:
        if c == "m":
            out.append(piece(s, s["kind"], a, b, "master"))
        elif c == "w":
            out.append(piece(s, alt, a, b, "wide"))
        elif c == "t" and s["kind"] == "P":
            p_ = piece(s, "P", a, b, "master"); p_["tight"] = True; out.append(p_)
        elif c in "pt":
            p_ = piece(s, "F", a, b, "master")
            if c == "t": p_["tight"] = True
            p_["kind"] = "P"; p_["states"] = [(t, k[:-1] + "P") for t, k in p_["states"]]
            if not p_["states"] or p_["states"][0][1] is None or round(p_["states"][0][0] * FPS) > a:
                first = next((k for t, k in p_["states"] if k), None)
                if first is None:
                    LEFT.append((round(a / FPS, 2), round(b / FPS, 2), s["i"])); out.append(piece(s, "W", a, b, "master")); continue
                p_["states"] = [(a / FPS, first)] + [x for x in p_["states"] if x[1] and x[1] != first]; p_["early"] = True
            p_["states"] = [x for x in p_["states"] if x[1]]
            out.append(p_)
        else:
            if s["kind"] == "P":
                out.append(piece(s, "F", a, b, "board"))
            elif s["kind"] == "W" and W_COVER and (active(s.get("bands") or [], a) is not None or
                                                   any(a < round(t * FPS) < b for t, k in (s.get("bands") or []))):
                p_ = piece(s, "F", a, b, "board")
                if p_["states"] and p_["states"][0][1] is None:      # no band yet at the cut: show the first one early
                    first = next(k for t, k in p_["states"] if k)
                    p_["states"] = [(a / FPS, first)] + [x for x in p_["states"][1:] if x[1] != first]; p_["early"] = True
                p_["states"] = [x for x in p_["states"] if x[1]]
                LEFT.append((round(a / FPS, 2), round(b / FPS, 2), s["i"], "F"))
                out.append(p_)
            else:
                LEFT.append((round(a / FPS, 2), round(b / FPS, 2), s["i"]))
                out.append(piece(s, s["kind"], a, b, "master"))
    for j in range(1, len(out)):
        out[j]["cont"] = True       # hard cut inside one original shot
    if len(out) > 1 or out[0]["kind"] != s["kind"]:
        for p_ in out:
            p_["split"] = True
    return out


def refine(shots, variety=True):
    """variety: every master W of >= 5 s gets a wide second half where the wide angle is clean; every P of >= 6 s that
    sits inside one clean wide take becomes a half screen (WS) for the whole shot."""
    res = []
    np_ = 0
    for s in shots:
        if s["kind"] in ("W", "P"):
            d = (s["f1"] - s["f0"]) / FPS
            if variety and s["kind"] == "P" and d >= 6.0 and wide_ok(s["f0"], s["f1"]):
                np_ += 1
                p = piece(s, "WS", s["f0"], s["f1"], "wide"); p["split"] = True
                res.append(p); continue
            ew = variety and ((s["kind"] == "W" and d >= 5.0) or (s["kind"] == "P" and d >= 6.5))
            res += split_shot(s, extra_wide=ew)
        else:
            res.append(s)
    for i, s in enumerate(res):
        s["i"] = i
    return res
