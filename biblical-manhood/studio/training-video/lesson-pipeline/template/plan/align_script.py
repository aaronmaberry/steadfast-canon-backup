"""No subtitle file came with the L08 release: build one by aligning the spoken script to the narration.

Word-level dynamic program. The narration is marked voiced/unvoiced in 10 ms frames (same rule as words.py) and cut
into voiced runs at gaps of 120 ms or more. Every run gets a block of consecutive script words; the block's voiced time
should match its length in letters at the lesson's own speaking rate. A run should end at a sentence end (cheap), a
comma (some cost) or between two words (dear), and a sentence end inside a run costs a lot (the voice nearly always
stops there). Cues are then cut from the script (one sentence; long ones split at a comma) and timed from the words.
usage: python3 plan/align_script.py <audio.wav> <script.txt> <out.srt> [words_out.json]
Prints the cues whose timing is least certain; read them before trusting the result."""
import json, re, subprocess, sys
import numpy as np

wav, scr, out = sys.argv[1:4]
SR, HOP = 16000, 160
x = np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-i", wav, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]), np.float32)
n = len(x) // HOP
db = 20 * np.log10(np.sqrt((x[:n * HOP].reshape(n, HOP) ** 2).mean(1) + 1e-12))
floor = np.percentile(db, 8)
v = db > max(floor + 14, -52)


def runs(b):
    r, i = [], 0
    while i < len(b):
        j = i
        while j < len(b) and b[j] == b[i]: j += 1
        r.append((bool(b[i]), i, j)); i = j
    return r


for val, i, j in runs(v):
    if not val and 0 < i and j < len(v) and j - i <= 8: v[i:j] = True
for val, i, j in runs(v):
    if val and j - i <= 4: v[i:j] = False
S = []
for val, i, j in runs(v):
    if not val: continue
    if S and i - S[-1][1] < 12: S[-1] = [S[-1][0], j]
    else: S.append([i, j])
S = np.array(S)
dur = (S[:, 1] - S[:, 0]) / 100.0
gap = np.r_[(S[1:, 0] - S[:-1, 1]) / 100.0, 9.0]
R = len(S)

# ---- words with the kind of junction after each (in/LNN-lines.txt: one spoken line per row, in/LNN-pauses.txt: the
# script's own pause after each line in seconds; [beat] inside a line is a short stop)
lines = [l.rstrip("\n") for l in open(scr) if l.strip()]
pauses = [float(x) for x in open(scr.replace("-lines.txt", "-pauses.txt")) if x.strip()]
toks, kind, pexp, line_of = [], [], [], []   # kind: 3 line end, 2 sentence end/beat, 1 comma, 0 none
for li, (ln, pz) in enumerate(zip(lines, pauses)):
    ws = ln.replace("[beat]", " [beat] ").split()
    for k, w in enumerate(ws):
        if w == "[beat]":
            kind[-1] = max(kind[-1], 2); continue
        toks.append(w); line_of.append(li); pexp.append(pz)
        if k == len(ws) - 1: kind.append(3)
        elif re.search(r"[.?!][\"”’']*$", w): kind.append(2)
        elif re.search(r"[,;:—–-][\"”’']*$", w): kind.append(1)
        else: kind.append(0)
M = len(toks)
wt = np.array([len(re.sub(r"[^\w']", "", t)) + 1.6 for t in toks])
cw = np.r_[0, np.cumsum(wt)]
kind = np.array(kind)
pexp = np.array(pexp)
send = np.r_[0, np.cumsum(np.where(kind == 3, np.where(pexp >= 0.7, 3.0, 1.0), (kind == 2) * 1.0))]  # weighted stops inside
rate = dur.sum() / wt.sum()
print(f"{M} words, {R} voiced runs, {dur.sum():.1f} s voiced, {rate:.4f} s per unit")

# ---- DP: cost[j, m] = best cost with runs [0, j) covering words [0, m)
INF = 1e18; L = 70
END_COST = np.where(kind >= 2, 0.0, np.where(kind == 1, 1.5, 6.0))
cost = np.full((R + 1, M + 1), INF); back = np.zeros((R + 1, M + 1), np.int32)
cost[0, 0] = 0
ms = np.arange(M + 1)
for j in range(1, R + 1):
    best = np.full(M + 1, INF); arg = np.zeros(M + 1, np.int32)
    for l in range(1, L + 1):
        m0 = ms[l:] - l; m1 = ms[l:]
        prev = cost[j - 1, m0]
        E = (cw[m1] - cw[m0]) * rate
        c = prev + (dur[j - 1] - E) ** 2 / (0.08 * E + 0.05)
        c += 8.0 * (send[m1 - 1] - send[m0])                  # sentence ends inside the run (the last word excluded)
        c += END_COST[m1 - 1] * (1.0 if gap[j - 1] < 0.35 else 1.6)
        g = gap[j - 1]
        c += np.where(kind[m1 - 1] == 3, 2.0 * np.log(min(g, 3.0) / np.maximum(pexp[m1 - 1], 0.3)) ** 2, 0.0)
        upd = c < best[l:]
        best[l:][upd] = c[upd]; arg[l:][upd] = m0[upd]
    cost[j] = best; back[j] = arg
# walk back
m = M; seg = []
for j in range(R, 0, -1):
    m0 = back[j, m]; seg.append((j - 1, m0, m)); m = m0
seg.reverse()
assert m == 0, "alignment did not reach the first word"
# word times: inside a run, by weight
W = []
for j, m0, m1 in seg:
    a, b = S[j, 0] / 100.0, S[j, 1] / 100.0
    tot = cw[m1] - cw[m0]
    for k in range(m0, m1):
        s = a + (b - a) * (cw[k] - cw[m0]) / tot; e = a + (b - a) * (cw[k + 1] - cw[m0]) / tot
        W.append(dict(w=toks[k], s=round(s, 3), e=round(e, 3)))
fitq = [(dur[j] / ((cw[m1] - cw[m0]) * rate), j, m0, m1) for j, m0, m1 in seg]

# ---- cues: one per spoken line; long lines split at a sentence end, else a comma
cues, cur = [], []
for k in range(M):
    cur.append(k)
    if kind[k] == 3:
        cues.append(cur); cur = []
out_cues = []
for c in cues:
    while len(" ".join(toks[i] for i in c)) > 92:
        mid = len(" ".join(toks[i] for i in c)) / 2
        cand = [p for p in range(2, len(c) - 2) if kind[c[p]] == 2] or [p for p in range(3, len(c) - 3) if kind[c[p]] == 1] \
            or list(range(4, len(c) - 4))
        if not cand: break
        p = min(cand, key=lambda p: abs(len(" ".join(toks[i] for i in c[:p + 1])) - mid))
        out_cues.append(c[:p + 1]); c = c[p + 1:]
    out_cues.append(c)
fmt = lambda t: f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(round(t % 1 * 1000)) % 1000:03d}"
with open(out, "w") as f:
    for n_, c in enumerate(out_cues, 1):
        f.write(f"{n_}\n{fmt(W[c[0]]['s'])} --> {fmt(W[c[-1]]['e'])}\n{' '.join(toks[i] for i in c)}\n\n")
if len(sys.argv) > 4:
    json.dump(W, open(sys.argv[4], "w"))
r = np.array([q for q, *_ in fitq])
print(f"{len(out_cues)} cues; run fit voiced/expected p5 {np.percentile(r, 5):.2f} p50 {np.percentile(r, 50):.2f} p95 {np.percentile(r, 95):.2f}")
ends = {m1 - 1: g for (j, m0, m1), g in zip(seg, gap[[j for j, _, _ in seg]])}
le = [(k, pexp[k], ends.get(k)) for k in range(M) if kind[k] == 3]
print("line ends with a stop:", sum(1 for k, p, g in le if g is not None), "of", len(le),
      "| 0.7 s+ line ends with no stop:", [lines[line_of[k]][:40] for k, p, g in le if g is None and p >= 0.7][:8])
gg = np.array([[p, g] for k, p, g in le if g is not None and g < 9])
for pv in (0.7, 1.2, 2.0): print(f"  script pause {pv}: measured gap median {np.median(gg[gg[:, 0] == pv, 1]):.2f}")
print("sentence ends inside a run:", sum(int(send[m1 - 1] - send[m0]) for _, m0, m1 in seg),
      "| runs ending mid-phrase:", sum(int(kind[m1 - 1] == 0) for _, m0, m1 in seg))
for q, j, m0, m1 in sorted(fitq, key=lambda z: abs(np.log(z[0])), reverse=True)[:10]:
    print(f"{q:5.2f} {S[j, 0] / 100:8.2f}-{S[j, 1] / 100:8.2f} {' '.join(toks[m0:m1])[:80]}")
