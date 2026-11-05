"""Word timings for L02 without a speech recognizer.

Each subtitle cue gives the exact words and a time span. Inside the span, 10 ms frames are marked voiced/unvoiced from
the narration's own energy. Words are laid along the voiced time only, in proportion to their length, so a word after
a pause starts when the voice comes back. Pauses (for cuts) come straight from the audio, not from this estimate.
writes plan/words.json [{w,s,e}] and plan/lines.json [{n,a,b,text}] (line n = subtitle cue n)."""
import json, re, subprocess
import numpy as np

SR = 16000; HOP = 160
x = np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-i", "/home/claude/l04/audio/narr_raw.wav", "-ac", "1", "-ar", str(SR),
                                           "-f", "f32le", "-"]), np.float32)
n = len(x) // HOP
rms = np.sqrt((x[:n * HOP].reshape(n, HOP) ** 2).mean(1) + 1e-12)
db = 20 * np.log10(rms)
floor = np.percentile(db, 8)
voiced = db > max(floor + 14, -52)
# close tiny gaps (stops inside words) and drop tiny blips
def close(v, k):
    v = v.copy(); i = 0
    while i < len(v):
        if not v[i]:
            j = i
            while j < len(v) and not v[j]: j += 1
            if 0 < i and j < len(v) and j - i <= k: v[i:j] = True
            i = j
        else: i += 1
    return v
voiced = close(voiced, 8)          # gaps <= 80 ms are inside speech

cues = json.load(open("/home/claude/l04/plan/cues_srt.json"))
words, lines = [], []
for c in cues:
    toks = re.findall(r"\S+", c["text"])
    a, b = max(0, int((c["a"] - 0.25) * 100)), min(n, int((c["b"] + 0.25) * 100))
    fr = np.where(voiced[a:b])[0] + a
    if len(fr) == 0:
        fr = np.arange(int(c["a"] * 100), int(c["b"] * 100))
    wt = np.array([len(re.sub(r"[^\w']", "", t)) + 1.5 for t in toks], float)
    # voiced runs inside the cue, split at gaps >= 150 ms
    runs = []; st = fr[0]; pv = fr[0]
    for f in fr[1:]:
        if f - pv > 15: runs.append((st, pv + 1)); st = f
        pv = f
    runs.append((st, pv + 1))
    # word boundaries after punctuation are where gaps may go; give each gap to the nearest such boundary (in order)
    bnd = [i + 1 for i, t in enumerate(toks[:-1]) if re.search(r"[.,;:?!\u201d\"]$", t)]
    vt = sum(b_ - a_ for a_, b_ in runs)
    pos = np.concatenate([[0], np.cumsum(wt)]) / wt.sum()
    groups = [0]; used = set()
    acc = 0
    for g in range(len(runs) - 1):
        acc += runs[g][1] - runs[g][0]
        frac = acc / vt
        cand = [b_ for b_ in bnd if b_ > max(g_ for g_ in groups if g_ is not None) and b_ not in used]
        if not cand:
            groups.append(None); continue
        best = min(cand, key=lambda b_: abs(pos[b_] - frac))
        if abs(pos[best] - frac) < 0.25:
            groups.append(best); used.add(best)
        else:
            groups.append(None)
    # build word->time: words in group k spread over the runs assigned to that group
    gi = [k for k in range(len(groups)) if groups[k] is not None]
    starts = [groups[k] for k in gi] + [len(toks)]
    # run index ranges per word group
    run_bounds = []; r0 = 0
    for k_i, k in enumerate(gi):
        nxt = gi[k_i + 1] if k_i + 1 < len(gi) else len(runs)
        run_bounds.append((r0, nxt)); r0 = nxt
    for gk, (w0, w1) in enumerate(zip(starts[:-1], starts[1:])):
        ra, rb = run_bounds[gk]
        gfr = np.concatenate([np.arange(runs[r][0], runs[r][1]) for r in range(ra, rb)]) if rb > ra else np.arange(runs[-1][0], runs[-1][1])
        ww = wt[w0:w1]; cum = np.concatenate([[0], np.cumsum(ww)]) / ww.sum() * (len(gfr) - 1)
        for j in range(w1 - w0):
            s_ = gfr[int(round(cum[j]))] / 100
            e_ = max(s_ + 0.05, gfr[max(0, int(round(cum[j + 1])) - (1 if j < w1 - w0 - 1 else 0))] / 100)
            words.append(dict(w=toks[w0 + j], s=round(s_, 3), e=round(e_ + 0.01, 3), n=c["n"]))
    lines.append(dict(n=c["n"], a=round(fr[0] / 100, 3), b=round(fr[-1] / 100 + 0.01, 3), text=c["text"]))
json.dump(words, open("/home/claude/l04/plan/words.json", "w")); json.dump(lines, open("/home/claude/l04/plan/lines.json", "w"))
# pauses straight from the audio (for cut placement)
p, i = [], 0
while i < n:
    if not voiced[i]:
        j = i
        while j < n and not voiced[j]: j += 1
        if (j - i) >= 20: p.append((round(i / 100, 2), round(j / 100, 2)))
        i = j
    else: i += 1
json.dump(p, open("/home/claude/l04/plan/pauses.json", "w"))
print(len(words), "words", len(lines), "lines", len(p), "pauses >=0.2 s; last word ends", words[-1]["e"])
