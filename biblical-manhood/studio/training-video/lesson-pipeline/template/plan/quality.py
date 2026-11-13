"""Per-frame quality of the L02 olive master (on the narration clock), for the two ways it is shown.

W  full frame, bottom faded into the field from 1080p y=780 (gone by 1000).
P  card: crop 1260x900 at (330,0) scaled into the 840x600 card, so anything below 1080p y=900 is out of view.
bad if: hand skin in view, chin jut / lean (face width > 1.08 x rolling median), mouth-area smear, or within
0.12 s of a v5 join (the picture jumps there, so no Wes shot may sit on one)."""
import json, sys
import numpy as np
JOINS = []

FPS = 25
TOTAL = 1287.88
N = int(round(TOTAL * FPS))
TOP = {"W": 840 / 3, "P": 800 / 3, "T": 700 / 3}           # scan is 640x360 = 1080p / 3: W fades out by y=880, P crop ends at y=840
XR = {"W": (0, 640), "P": (400 / 3, 1520 / 3), "T": (470 / 3, 1450 / 3)}   # T: tight card crop 980x700 at x 470 (L12)  # P crop is x 372..1548


def roll_med(x, k):
    x = np.asarray(x, float); out = np.empty_like(x)
    for i in range(len(x)):
        a, b = max(0, i - k), min(len(x), i + k + 1); out[i] = np.nanmedian(x[a:b])
    return out


d = json.load(open("/home/claude/l04/master/scan_olive.json"))
fr = d["frames"]; step = d["step"]
fw = np.array([f["face"][2] if f["face"] else np.nan for f in fr], float)
sh = np.array([f.get("sharp", np.nan) if f["face"] else np.nan for f in fr], float)
med_w = roll_med(fw, 25 // step * 2); med_s = roll_med(sh, 25 // step * 2)
why = {"W": np.zeros(N, np.int8), "P": np.zeros(N, np.int8), "T": np.zeros(N, np.int8)}
counts = {}
for j, f in enumerate(fr):
    for view in ("W", "P", "T"):
        r = []
        if not f["face"]:
            r.append("noface")
        else:
            hb = f.get("hand_box")
            if f["hand"] > 0.03 and hb:
                x0, y0, w, h, a = f["face"]
                bx, by, bw, bh, ba = hb
                bcx = bx + bw / 2
                below = by < y0 + h + max(0.6 * h, 70)          # starts right under the chin
                collar = below and ((ba < 1200 and abs(bcx - (x0 + w / 2)) < 1.0 * w) or abs(bcx - (x0 + w / 2)) < 0.6 * w)
                inx = bx < XR[view][1] and bx + bw > XR[view][0]
                if not collar and inx and by < TOP[view]:
                    r.append("hand")
            if fw[j] > med_w[j] * 1.14:   # L03: 1.08 flagged normal laughs (checked by eye at 988 s)
                r.append("jut")
            if sh[j] < 0.25 * med_s[j]:
                r.append("smear")
        for x in r:
            counts[(view, x)] = counts.get((view, x), 0) + 1
        if r:
            k = f["i"]
            why[view][k:min(N, k + step)] = 1
def clean(a, min_run=3, pad=5):
    """drop isolated 1-2 frame flags (blob flicker, blinks); pad real events by 0.2 s for a hand rising/falling"""
    out = np.zeros_like(a); i = 0
    while i < N:
        if a[i]:
            j = i
            while j < N and a[j]: j += 1
            if j - i >= min_run:
                out[max(0, i - pad):min(N, j + pad)] = 1
            i = j
        else:
            i += 1
    return out


for view in why:
    why[view] = clean(why[view])
# v5 joins: the picture jumps there, but a shot may start or end on one (layout.check refuses shots that span one)
np.save("/home/claude/l04/plan/q_wide.npy", why["W"]); np.save("/home/claude/l04/plan/q_panel.npy", why["P"]); np.save("/home/claude/l04/plan/q_tight.npy", why["T"])
# L12: frame-level hand maps (plan/dense_*.npy, every frame) on top of the 5-frame scan
import os
for nm, dn in (("q_wide", "dense_w"), ("q_panel", "dense_p"), ("q_tight", "dense_t")):
    fp = f"/home/claude/l04/plan/{dn}.npy"
    if os.path.exists(fp):
        q = np.load(f"/home/claude/l04/plan/{nm}.npy"); d = np.load(fp).astype(int)[:N]
        m = np.convolve(d, np.ones(11, int), "same") > 0; q[:len(m)][m & (q[:len(m)] == 0)] = 9
        np.save(f"/home/claude/l04/plan/{nm}.npy", q); print(nm, "bad s", round((q != 0).sum() / FPS, 1))
print({f"{v}:{x}": round(c * step / FPS, 1) for (v, x), c in counts.items()}, "seconds")
for v in why:
    print(v, "bad", round(why[v].sum() / FPS, 1), "s of", round(N / FPS, 1))

# ---- HeyGen face glitches (soft / morphing face for a few frames), both angles ---------------------------------------
import json as _json
PADG = 3   # 0.12 s each side
_runs = _json.load(open("/home/claude/l04/master/warp_runs.json"))
# v6: off. These runs are HeyGen's normal blinks (detail dips as the eyes close); Aaron checked the HeyGen renders and
# they are clean. Covering them cost ~150 s of Wes. The face problems in v3-v5 were my encode + zoom, now fixed.
USE_WARP = False
for _a, _b, _m in (_runs if USE_WARP else []):
    for _v in ("W", "P"):
        why[_v][max(0, int(_a * FPS) - PADG):min(N, int(_b * FPS) + PADG)] = 1
np.save("/home/claude/l04/plan/q_wide.npy", why["W"]); np.save("/home/claude/l04/plan/q_panel.npy", why["P"]); np.save("/home/claude/l04/plan/q_tight.npy", why["T"])
# L12: frame-level hand maps (plan/dense_*.npy, every frame) on top of the 5-frame scan
import os
for nm, dn in (("q_wide", "dense_w"), ("q_panel", "dense_p"), ("q_tight", "dense_t")):
    fp = f"/home/claude/l04/plan/{dn}.npy"
    if os.path.exists(fp):
        q = np.load(f"/home/claude/l04/plan/{nm}.npy"); d = np.load(fp).astype(int)[:N]
        m = np.convolve(d, np.ones(11, int), "same") > 0; q[:len(m)][m & (q[:len(m)] == 0)] = 9
        np.save(f"/home/claude/l04/plan/{nm}.npy", q); print(nm, "bad s", round((q != 0).sum() / FPS, 1))
_ws = _json.load(open("/home/claude/l04/wide/widescan.json"))
qww = np.full(N, -1, np.int8); widx = np.full(N, -1, np.int16)
for _k, _c in enumerate(_ws):
    f0, f1 = int(np.ceil(_c["a"] * FPS)) + 12, int((_c["a"] + _c["dur"]) * FPS) - 12   # stay 0.5 s inside each wide (QC: dips at w01/w08 ends)
    seg = np.zeros(f1 - f0, np.int8)
    for _a, _b in _c["glitch"]:
        seg[max(0, int(_a * FPS) - PADG - f0):max(0, int(_b * FPS) + PADG - f0)] = 1
    take = (qww[f0:f1] != 0)        # prefer a clean frame from any clip
    qww[f0:f1][take] = seg[take]; widx[f0:f1][take] = _k
np.save("/home/claude/l04/plan/q_ww.npy", qww); np.save("/home/claude/l04/plan/w_idx.npy", widx)
print("master glitch frames", int(sum((_b - _a) * FPS for _a, _b, _ in _runs)), "| wide covered", round((qww >= 0).sum() / FPS, 1),
      "s, clean", round((qww == 0).sum() / FPS, 1), "s")
