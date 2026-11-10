#!/usr/bin/env python3
"""L08 v4 EDL: point wides at the new crop batch, drop smear-driven full-shot covers,
keep v3 text/layout/B-roll/lower-thirds, add mid-shot still-run covers only so no
uncovered WES_FULL run exceeds 8s. Snap cover edges to word gaps. Retally L5 mix."""
import json, collections, shutil
from pathlib import Path

WORK = Path('/workspace/l08')
P7 = WORK / 'p7'
B = Path('/workspace/artifacts/training/lesson-plan-2026-10-26/L08-build-2026-11-09')

# backups
edl_src = P7 / 'edl.json'
if not (P7 / 'edl_v3_backup.json').exists():
    shutil.copy2(edl_src, P7 / 'edl_v3_backup.json')
    print('backed up edl_v3_backup.json')
if not (P7 / 'inputs_v3_backup.json').exists():
    shutil.copy2(P7 / 'inputs.json', P7 / 'inputs_v3_backup.json')

E = json.loads(edl_src.read_text())
inp = json.loads((P7 / 'inputs.json').read_text())
W = json.loads(Path(inp['words']).read_text())

# point inputs at v4 wides (same a/b, new paths)
wide_v4 = json.loads((B / 'heygen/wide_rendered_v4.json').read_text())
segs = [dict(path=w['video'], t0=float(w['a']), t1=float(w['b'])) for w in wide_v4]
assert len(segs) == 30, len(segs)
inp['wes_wide'] = segs
(P7 / 'inputs.json').write_text(json.dumps(inp, indent=1))
print('inputs wes_wide -> v4', segs[0]['path'])

# keep lower_thirds; drop smear covers; remember old cover text per shot
old_covers = [k for k in E['kinetic'] if k.get('cover')]
lt = [k for k in E['kinetic'] if not k.get('cover')]
text_by_shot = {}
for k in old_covers:
    text_by_shot.setdefault(str(k['shot']), k.get('text') or '')

def gaps(minlen=0.28):
    g = []
    if W:
        if W[0]['start'] >= minlen:
            g.append((0.0, W[0]['start']))
        for i in range(len(W) - 1):
            a, b = W[i]['end'], W[i + 1]['start']
            if b - a >= minlen:
                g.append((a, b))
        if E['end'] - W[-1]['end'] >= minlen:
            g.append((W[-1]['end'], E['end']))
    return g

G = gaps()

def snap(t, side='start', win=3.0):
    """Snap t to a gap edge. side=start prefers gap end (after a word); end prefers gap start."""
    cands = []
    for g0, g1 in G:
        pts = (g1, (g0 + g1) / 2, g0) if side == 'start' else (g0, (g0 + g1) / 2, g1)
        for cand in pts:
            if abs(cand - t) <= win:
                cands.append((abs(cand - t), round(cand, 2)))
    return cands[0][1] if cands else round(t, 2)

def in_word(t):
    return any(w['start'] + 0.02 < t < w['end'] - 0.02 for w in W)

def phrase(t0, t1, shot, max_words=16):
    ww = [(w['word'], w['start']) for w in W if t0 - 0.15 <= w['start'] <= t1 + 0.15]
    # prefer a complete-looking slice (end on punctuation if possible)
    words = [w[0] for w in ww]
    text = ' '.join(words[:max_words]).strip()
    # fallback to old v3 cover text if window is thin
    if len(words) < 4:
        text = text_by_shot.get(str(shot), text) or text
    return text, ww[:max_words]

# build mid-shot covers for long WES_FULL runs
kin = list(lt)
covers = []
for s in [x for x in E['shots'] if x['kind'] == 'WES_FULL']:
    a, b = s['t0x'], s['t1x']
    if b - a <= 8.0:
        continue
    # mid ~4.5s cover, leaving wide on both sides when possible
    mid = (a + b) / 2
    t0 = snap(mid - 2.2, 'start', win=3.0)
    t1 = snap(mid + 2.3, 'end', win=3.0)
    t0 = max(a + 0.35, t0)
    t1 = min(b - 0.35, t1)
    if t1 - t0 < 3.0:
        t0 = max(a + 0.35, round(mid - 2.0, 2))
        t1 = min(b - 0.35, round(mid + 2.0, 2))
    if t1 <= t0 + 2.4:
        continue
    # don't start/end inside a word
    if in_word(t0):
        t0 = snap(t0, 'start', win=2.5)
    if in_word(t1):
        t1 = snap(t1, 'end', win=2.5)
    t0 = max(a + 0.2, t0)
    t1 = min(b - 0.2, t1)
    if t1 <= t0 + 2.4:
        continue
    text, ww = phrase(t0, t1, s['id'])
    covers.append(dict(
        shot=s['id'], t0=round(t0, 2), t1=round(t1, 2),
        text=text, words=ww, cover=1,
        why=['v4 still-run mid', round(a, 2), round(b, 2)],
        **{'in': 'xfade', 'out': 'xfade'},
    ))

# rotate cover edges for L5
for i, k in enumerate(covers, 1):
    if i % 2 == 0:
        k['out'] = 'dip'
    if i % 3 == 0:
        k['in'] = 'hard'
    elif i % 5 == 0:
        k['in'] = 'push'

kin.extend(covers)
E['kinetic'] = kin

def edge_counts():
    C = collections.Counter(c['type'] for c in E['cuts'])
    for k in kin:
        C[k.get('in', 'xfade')] += 1
        C[k.get('out', 'xfade')] += 1
    for b in E.get('broll') or []:
        C[b.get('tin', 'hard')] += 1
        C[b.get('tout', 'xfade')] += 1
    return C

def fail(C):
    t = sum(C.values()) or 1
    return any(v / t > 0.40 for v in C.values())

C = edge_counts()
if fail(C):
    n = 0
    for c in E['cuts']:
        if c['type'] == 'xfade':
            n += 1
            if n % 2 == 0:
                c['type'] = 'dip'
            elif n % 3 == 0:
                c['type'] = 'hard'
C = edge_counts()
total = sum(C.values()) or 1
P = {k: (v, round(100 * v / total)) for k, v in C.items()}
print('covers added', len(covers), 'lower_thirds', len(lt), 'kinetic', len(kin))
print('transition mix', {k: f'{v[0]} ({v[1]}%)' for k, v in P.items()}, 'total', total)
if fail(C):
    print('FAIL L5')
    raise SystemExit(2)
print('PASS L5')

edl_src.write_text(json.dumps(E, indent=1))
print('wrote', edl_src)
