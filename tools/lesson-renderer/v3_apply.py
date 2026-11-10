#!/usr/bin/env python3
"""L08 v3 EDL apply: boards, b-roll, covers, layouts, text gate. Last writer of p7/edl.json."""
import os, sys, json, re, copy, collections, shutil
from pathlib import Path

WORK = '/workspace/l08'
EDL_P = f'{WORK}/p7/edl.json'
WORDS_P = f'{WORK}/p7/edl_words.json'
STILL = '/workspace/steadfast-main/img/lesson-08.jpg'
MEZZ = f'{WORK}/broll/mezz'
MAP_P = f'{WORK}/broll/broll_map.md'

E = json.load(open(EDL_P))
W = json.load(open(WORDS_P))
if not isinstance(W, list):
    W = W.get('words') or W
shutil.copy2(EDL_P, f'{WORK}/p7/edl_v2_backup.json')

def nz(s):
    return re.sub(r"[^a-z0-9']", '', str(s).lower())

WN = [nz(w['word']) for w in W]

def find_phrase(ph, t0=0, t1=1e9):
    p = [nz(x) for x in ph.split() if nz(x)]
    if not p:
        return None
    for i, w in enumerate(W):
        if w['start'] < t0 - 1.0 or w['start'] > t1 + 1.0:
            continue
        if WN[i:i+len(p)] == p:
            return (round(w['start'], 3), round(W[i+len(p)-1]['end'], 3))
    # unscoped fallback
    for i, w in enumerate(W):
        if WN[i:i+len(p)] == p:
            return (round(w['start'], 3), round(W[i+len(p)-1]['end'], 3))
    return None

def find_start(ph, t0=0, t1=1e9):
    r = find_phrase(ph, t0, t1)
    return r[0] if r else None

def words_in(t0, t1):
    return [w for w in W if t0 - 0.15 <= w['start'] <= t1 + 0.15]

def spoken(t0, t1):
    return ' '.join(w['word'] for w in words_in(t0, t1)).strip()

def gaps(minlen=0.28):
    g = []
    if W:
        if W[0]['start'] >= minlen:
            g.append((0.0, W[0]['start']))
        for i in range(len(W) - 1):
            a, b = W[i]['end'], W[i+1]['start']
            if b - a >= minlen:
                g.append((a, b))
        end = float(E['end'])
        if end - W[-1]['end'] >= minlen:
            g.append((W[-1]['end'], end))
    return g

GAPS = gaps()

def in_word(t, pad=0.02):
    return any(w['start'] + pad < t < w['end'] - pad for w in W)

def snap_in_gap(t, win=4.0, minlen=0.28):
    best = None
    for g0, g1 in GAPS:
        if g1 - g0 < minlen:
            continue
        for p in (g0 + 0.04, (g0 + g1) / 2, g1 - 0.04):
            d = abs(p - t)
            if d <= win and (best is None or d < best[0]):
                best = (d, p)
    if best:
        return round(best[1], 2)
    # widen
    for g0, g1 in GAPS:
        for p in (g0 + 0.04, (g0 + g1) / 2, g1 - 0.04):
            d = abs(p - t)
            if best is None or d < best[0]:
                best = (d, p)
    return round(best[1], 2) if best else round(t, 2)

def complete_clauses(t0, t1, max_rows=3, max_chars=48):
    """2-4 complete short phrases from the spoken window. Never mid-word."""
    ww = words_in(t0, t1)
    if not ww:
        return []
    text = ' '.join(w['word'] for w in ww).strip()
    # extend to sentence end if the next words finish it within 2.5s
    last_end = ww[-1]['end']
    extra = [w for w in W if last_end - 0.05 < w['start'] <= last_end + 2.5]
    if extra and not re.search(r'[.?!]$', text):
        acc = text
        for w in extra:
            acc = (acc + ' ' + w['word']).strip()
            if re.search(r'[.?!]$', w['word']):
                text = acc
                break
    parts = [x.strip() for x in re.split(r'(?<=[.?!])\s+', text) if x.strip()]
    rows = []
    def flush_long(p):
        if len(p) <= max_chars:
            return [p]
        # split on comma/semicolon, keep complete clauses
        bits = re.split(r'[,;:]\s+', p)
        out, acc = [], ''
        for c in bits:
            cand = (acc + ', ' + c).strip(', ') if acc else c
            if len(cand) <= max_chars:
                acc = cand
            else:
                if acc:
                    out.append(acc)
                if len(c) <= max_chars + 8:
                    acc = c
                else:
                    line = ''
                    for tok in c.split():
                        trial = (line + ' ' + tok).strip()
                        if len(trial) <= max_chars:
                            line = trial
                        else:
                            if line:
                                out.append(line)
                            line = tok
                    acc = line
        if acc:
            out.append(acc)
        return out
    for p in parts:
        # drop leading filler crumbs
        p = re.sub(r'^(and|or|but|so|then)\s+', '', p, flags=re.I).strip()
        if not p:
            continue
        rows.extend(flush_long(p))
    # cue times
    out = []
    used = set()
    for r in rows:
        at = find_start(r, t0 - 0.5, t1 + 2.5)
        if at is None:
            at = find_start(' '.join(r.split()[:4]), t0 - 0.5, t1 + 2.5)
        if at is None:
            at = round(t0 + 0.15 + 0.4 * len(out), 3)
        key = (r, round(at, 2))
        if key in used:
            continue
        used.add(key)
        out.append([r, round(at, 3)])
        if len(out) >= max_rows:
            break
    return out

def complete_sentence(t0, t1, max_chars=110):
    """One complete headline from a window, ending on .?! if possible."""
    ww = words_in(t0, t1)
    if not ww:
        return 'Stay with that.'
    text = ' '.join(w['word'] for w in ww).strip()
    last_end = ww[-1]['end']
    extra = [w for w in W if last_end - 0.05 < w['start'] <= last_end + 2.8]
    if extra and not re.search(r'[.?!]$', text):
        acc = text
        for w in extra:
            acc = (acc + ' ' + w['word']).strip()
            if re.search(r'[.?!]$', w['word']):
                text = acc
                break
    # if still mid-sentence, trim to last complete sentence, else keep clauses
    if not re.search(r'[.?!]$', text):
        m = list(re.finditer(r'[.?!]', text))
        if m and m[-1].start() > 12:
            text = text[:m[-1].end()].strip()
        else:
            # take up to a comma if long
            if len(text) > max_chars:
                cut = text[:max_chars].rsplit(' ', 1)[0]
                text = cut
    text = re.sub(r'^(and|or|but|so|then)\s+', '', text, flags=re.I).strip()
    return text or 'Stay with that.'

# ---------- 1. AGENDA pills ----------
AGENDA_PILLS = [
    "The chair that raised you",
    "What Paul put in a father's place",
    "What took the seat when the father was thin",
    "Dean and a table hired by the mail",
    "The chair explains you",
]
for s in E['shots']:
    if s['kind'] != 'AGENDA':
        continue
    sp = s.setdefault('spec', {})
    rows = []
    for p in AGENDA_PILLS:
        at = find_start(p, s['t0'] - 0.4, s['t1'] + 0.4)
        if at is None:
            at = round(s['t0'] + 0.4 + 1.2 * len(rows), 3)
        rows.append([p, round(at, 3)])
    sp['rows'] = rows
    sp['style'] = 'pills'
    kick = sp.get('kicker')
    if not kick:
        sp['kicker'] = ["HERE'S HOW THIS GOES", 9.28]
    elif isinstance(kick, (list, tuple)):
        sp['kicker'] = [str(kick[0]).replace('item', '').strip() or "HERE'S HOW THIS GOES", kick[1]]
    print('AGENDA', sp['rows'])

# ---------- 2. Board / split rows: complete phrases ----------
for s in E['shots']:
    if s['kind'] not in ('TYPE_BOARD_BUBBLE', 'SPLIT', 'BRANDED_STILL_BUBBLE'):
        continue
    sp = s.setdefault('spec', {})
    rr = complete_clauses(s['t0'], s['t1'], max_rows=3 if s['kind'] == 'SPLIT' else 4)
    if not rr:
        rr = [[complete_sentence(s['t0'], s['t1'], 56), round(s['t0'] + 0.15, 3)]]
    sp['rows'] = rr
    sp.setdefault('style', 'rows')
    sp.setdefault('paper', False)

# ---------- 3. Scripture → full-screen card ----------
for s in E['shots']:
    if s['kind'] == 'SCRIPTURE_BUBBLE':
        s['kind'] = 'SCRIPTURE_CARD'
        sp = s.setdefault('spec', {})
        sp['style'] = 'scripture_card'
        if not sp.get('verse'):
            sp['verse'] = 'Fathers, do not exasperate your children. Instead, bring them up in the training and instruction of the Lord.'
        if not sp.get('ref'):
            sp['ref'] = ['EPHESIANS 6:4 (NIV)', 256.24]
        print('SCRIPTURE_CARD', s['id'], sp.get('ref'), sp.get('verse')[:40])

# ---------- 4. Convert one mid TYPE_BOARD to BRANDED_STILL ----------
# Prefer a mid-lesson board ~8s+ that is not the first/last
cands = [s for s in E['shots'] if s['kind'] == 'TYPE_BOARD_BUBBLE' and 200 < s['t0'] < 1200 and (s['t1x'] - s['t0x']) >= 6]
# pick one near "chair" language if possible
pick = None
for s in cands:
    tx = spoken(s['t0'], s['t1']).lower()
    if 'chair' in tx or 'father' in tx:
        pick = s
        break
if not pick and cands:
    pick = cands[len(cands)//2]
if pick:
    pick['kind'] = 'BRANDED_STILL_BUBBLE'
    pick['spec']['still'] = STILL
    print('BRANDED_STILL', pick['id'], pick['t0'], pick['t1'], pick['spec'].get('rows'))

# ---------- 5. B-roll (literal, men, Mixkit Free) ----------
# Times prefer the spoken line; edges snapped to word gaps.
PICKS = [
    dict(id='42140', prefer=87.92,
         line='Who sat at the end of the table. Who never did.',
         picture='A man seated at a dining table, a chair filled at supper',
         why='Literal chair at the table; a man, not a random stock woman. Used for the opening table question.'),
    dict(id='4542', prefer=1075.66,
         line='An older man sat with us.',
         picture='Father and son reading together',
         why='Fathers and sons. Maps to the older man who sat with the group (Warren’s story).'),
    dict(id='4553', prefer=1272.0,
         line='Show up in the ordinary hours.',
         picture='A father on the floor playing with his son',
         why='Ordinary hours with a son, not a generic lifestyle clip.'),
    dict(id='43350', prefer=668.06,
         line=spoken(665, 675) or 'at the table',
         picture='A father and his child at the kitchen table',
         why='Kitchen table / father and child, as the lesson keeps returning to the table.'),
    dict(id='771', prefer=353.26,
         line='I learned a man handles fear by getting useful.',
         picture='A man at a carpenter’s workbench',
         why='Workbench / getting useful with your hands — the pattern Wes names after the tryout story.'),
    dict(id='871', prefer=326.88,
         line='When I was scared of something ordinary, a tryout.',
         picture='A baseball batter at the plate (the tryout)',
         why='Dad-and-ballgame / tryout beat. A man at the plate, not a sports car.'),
    dict(id='4793', prefer=1414.44,
         line='Write your father a letter.',
         picture='A man writing with a pen',
         why='The close invitation: write your father a letter. A man writing, not a green-screen laptop.'),
]

# refine 43350 line from actual words around "at the table"
tline = find_phrase('at the table')
if tline:
    PICKS[3]['prefer'] = tline[1]
    PICKS[3]['line'] = complete_sentence(tline[0] - 2.0, tline[1] + 2.0, 90)

PROTECTED = set()
for s in E['shots']:
    if s['kind'] in ('TITLE_CARD', 'AGENDA', 'SCRIPTURE_CARD', 'SCRIPTURE_BUBBLE', 'LOGO_END'):
        PROTECTED.add((s['t0x'], s['t1x']))

def overlaps_prot(a, b):
    for u, v in PROTECTED:
        if not (b <= u or a >= v):
            return True
    return False

def place_clip(prefer, dur=4.6, taken=()):
    # start at a gap near prefer (just after the line when possible)
    t0 = snap_in_gap(prefer, win=5.0)
    # if start is before the line by a lot, prefer a gap after
    if t0 < prefer - 1.0:
        t0 = snap_in_gap(prefer + 0.4, win=5.0)
    t1 = snap_in_gap(t0 + dur, win=5.0)
    if t1 <= t0 + 3.2:
        t1 = snap_in_gap(t0 + 5.0, win=8.0)
    if t1 <= t0 + 2.8:
        t1 = round(t0 + 4.4, 2)
        t1 = snap_in_gap(t1, win=6.0)
        if t1 <= t0 + 2.8:
            return None
    # stay off protected
    if overlaps_prot(t0, t1):
        t0 = snap_in_gap(t1 + 0.8, win=8.0)
        t1 = snap_in_gap(t0 + dur, win=6.0)
        if t1 <= t0 + 2.8 or overlaps_prot(t0, t1):
            return None
    # no overlap with taken
    for a, b in taken:
        if not (t1 <= a or t0 >= b):
            t0 = snap_in_gap(b + 0.6, win=6.0)
            t1 = snap_in_gap(t0 + dur, win=6.0)
            if t1 <= t0 + 2.8 or overlaps_prot(t0, t1):
                return None
            for a2, b2 in taken:
                if not (t1 <= a2 or t0 >= b2):
                    return None
    if t1 > float(E['end']) - 2:
        return None
    if in_word(t0) or in_word(t1):
        t0, t1 = snap_in_gap(t0), snap_in_gap(t1)
        if t1 <= t0 + 2.8 or in_word(t0) or in_word(t1):
            return None
    return round(t0, 2), round(t1, 2)

TRANS_CYCLE = ['xfade', 'dip', 'hard', 'push']
broll = []
taken = []
for i, pk in enumerate(PICKS):
    clip = f"{MEZZ}/{pk['id']}.mp4"
    if not os.path.isfile(clip):
        print('MISSING mezz', clip)
        continue
    pl = place_clip(pk['prefer'], 4.6, taken)
    if not pl:
        print('NO SLOT', pk['id'], pk['prefer'])
        continue
    t0, t1 = pl
    # cap to mezz duration (~6s)
    if t1 - t0 > 6.0:
        t1 = snap_in_gap(t0 + 5.5, win=3.0)
        if t1 <= t0 + 2.8:
            t1 = round(t0 + 5.5, 2)
    tin = TRANS_CYCLE[i % 4]
    tout = TRANS_CYCLE[(i + 1) % 4]
    rec = dict(n=i + 1, clip=clip, t0=t0, t1=t1,
               line=pk['line'], picture=pk['picture'],
               grade='normal', mixkit_id=pk['id'], license='Mixkit Free',
               why=pk['why'], tin=tin, tout=tout)
    broll.append(rec)
    taken.append((t0 - 0.4, t1 + 0.4))
    print('BROLL', rec['n'], rec['mixkit_id'], rec['t0'], rec['t1'], rec['line'][:60])

E['broll'] = broll

# ---------- 6. Kinetic covers: complete text, merge, cover jumps/bob/smear ----------
# Reviewer jump + bob times (seconds)
JUMPS = [39, 46, 48, 64, 67]
BOB = [42, 104, 165, 210, 312, 454, 646, 882, 1027, 1215, 1409]
# First WES smear starts ~38-39; cover from the first gap near 38 through end of that shot
COVER_FORCE = []  # (t0, t1, why)

def shot_at_t(t):
    for s in E['shots']:
        if s['t0x'] <= t < s['t1x']:
            return s
    return None

# Force first WES (35.34-53.64) cover from ~38.2 to shot end
s0 = next(s for s in E['shots'] if s['kind'] == 'WES_FULL' and s['t0x'] < 40)
cover_from = snap_in_gap(38.2, win=2.5)
COVER_FORCE.append((max(s0['t0x'] + 2.6, cover_from), s0['t1x'], 'smear+jumps in opening wide'))

# Cover the short WES after the 1:04 board (64.64-70.97) entirely — jump at 1:04 / 1:07
s1 = next((s for s in E['shots'] if s['kind'] == 'WES_FULL' and abs(s['t0x'] - 64.64) < 1.0), None)
if s1:
    COVER_FORCE.append((s1['t0x'], s1['t1x'], 'jump 1:04 / 1:07 opening return to wide'))

# Cover each bob/jump ± window, snapped, on WES_FULL (or PANEL if it's a split — still cover with card over? 
# For SPLIT, bob on the panel: cover with a type-board already there or a kinetic cover. render only applies cover cards when kin cover is set, even mid-SPLIT.
for t in JUMPS + BOB:
    sh = shot_at_t(t)
    if not sh:
        continue
    if sh['kind'] in ('TITLE_CARD', 'AGENDA', 'SCRIPTURE_CARD', 'LOGO_END', 'TYPE_BOARD_BUBBLE', 'BRANDED_STILL_BUBBLE'):
        continue  # already off his body / a board
    a = snap_in_gap(t - 1.2, win=2.5)
    b = snap_in_gap(t + 2.6, win=2.5)
    if b <= a + 2.2:
        b = round(a + 3.2, 2)
    # stay inside shot
    a = max(a, sh['t0x'])
    b = min(b, sh['t1x'])
    if b - a >= 1.6:
        COVER_FORCE.append((a, b, f'bob/jump @{t}'))

# existing covers + new, rewrite text, merge
kin_old = E.get('kinetic') or []
windows = []
for k in kin_old:
    if k.get('cover') or k.get('style') == 'lower_third':
        if k.get('style') == 'lower_third':
            continue  # rebuild lower thirds later
        windows.append([k['t0'], k['t1'], 'prior'])
    else:
        # keep non-cover headlines only if they are complete; we'll re-add as covers if on WES
        if k.get('cover'):
            windows.append([k['t0'], k['t1'], 'prior'])

windows.extend([list(x) for x in COVER_FORCE])
windows.sort()

# merge if gap < 2.8s (don't return mid-wide for a blink)
merged = []
for a, b, why in sorted(windows, key=lambda x: x[0]):
    if merged and a - merged[-1][1] <= 2.8:
        merged[-1][1] = max(merged[-1][1], b)
        merged[-1][2] = why
    else:
        merged.append([a, b, why])

# Absorb leftover WES < 3.5s after/before a cover (no mid-pose return)
def wes_uncovered(covers):
    segs = []
    for s in E['shots']:
        if s['kind'] not in ('WES_FULL', 'LOWER_THIRD'):
            continue
        pieces = [(s['t0x'], s['t1x'], s)]
        for a, b, _ in covers:
            n = []
            for u, v, sh in pieces:
                if b <= u or a >= v:
                    n.append((u, v, sh)); continue
                if a > u:
                    n.append((u, a, sh))
                if b < v:
                    n.append((b, v, sh))
            pieces = n
        segs.extend(pieces)
    return segs

changed = True
while changed:
    changed = False
    leftovers = wes_uncovered(merged)
    for u, v, sh in leftovers:
        dur = v - u
        if dur <= 0.05:
            continue
        # still-run: uncovered WES > 8s → drop a 4s cover in the middle
        if dur > 8.0:
            mid = (u + v) / 2
            a = snap_in_gap(mid - 2.0, win=2.0)
            b = snap_in_gap(mid + 2.2, win=2.0)
            a = max(u, a); b = min(v, max(a + 3.2, b))
            merged.append([a, b, 'still-run'])
            merged.sort()
            # re-merge
            m2 = []
            for a, b, why in merged:
                if m2 and a - m2[-1][1] <= 2.8:
                    m2[-1][1] = max(m2[-1][1], b); m2[-1][2] = why
                else:
                    m2.append([a, b, why])
            merged = m2
            changed = True
            break
        # short leftover after a cover: absorb into adjacent cover (don't return mid-pose)
        if dur < 3.5:
            # find adjacent
            for i, (a, b, why) in enumerate(merged):
                if abs(a - v) < 0.2 or abs(b - u) < 0.2 or (a <= u and b >= v):
                    merged[i][0] = min(a, u)
                    merged[i][1] = max(b, v)
                    merged[i][2] = why + '+absorb'
                    changed = True
                    break
            if changed:
                # clip to shot
                break

# clamp covers to not over title/agenda/scripture/logo (those already aren't WES)
kin_new = []
# Preserve nothing from old lower thirds; rebuild below
for a, b, why in merged:
    # skip if this window is entirely on a board already (optional keep for safety)
    sh = shot_at_t((a + b) / 2) or shot_at_t(a)
    if not sh:
        continue
    if sh['kind'] in ('TITLE_CARD', 'AGENDA', 'SCRIPTURE_CARD', 'LOGO_END'):
        continue
    a = max(a, sh['t0x']); b = min(b, sh['t1x'])
    # if cover spans two shots, split
    # (simple: clamp to the mid shot; also add for start shot if different)
    if b - a < 1.4:
        continue
    text = complete_sentence(a, b, 110)
    ww = [(w['word'], w['start']) for w in words_in(a, b + 1.0)]
    kin_new.append(dict(
        shot=sh['id'], t0=round(a, 2), t1=round(b, 2),
        text=text, words=ww, cover=1, why=why,
        **{'in': 'xfade', 'out': 'xfade'}
    ))

# ---------- 7. Lower-thirds on remaining short WES at punchy lines ----------
LT_LINES = [
    "What you do with the chair is yours",
    "What sat in the chair was handed to you",
    "You can father with a hole",
    "An empty seat is not a pass to stay a boy",
    "Say the true sentence out loud",
    "The chair explains you. It does not excuse you",
]
# remaining WES after covers
cov_for_lt = [(k['t0'], k['t1']) for k in kin_new]
def covered(t):
    return any(a - 0.05 <= t < b + 0.05 for a, b in cov_for_lt)

lt_added = 0
for line in LT_LINES:
    fr = find_phrase(line)
    if not fr:
        # try first 6 words
        fr = find_phrase(' '.join(line.split()[:6]))
    if not fr:
        print('LT miss', line)
        continue
    t0 = fr[0] - 0.12
    t1 = max(fr[1] + 0.8, t0 + 3.2)
    sh = shot_at_t((t0 + t1) / 2) or shot_at_t(fr[0])
    if not sh or sh['kind'] not in ('WES_FULL', 'LOWER_THIRD'):
        # if it's a split/board, skip — layout already different
        print('LT skip (not wide)', line, sh['kind'] if sh else None)
        continue
    # if fully covered, skip (card already there)
    if covered((t0 + t1) / 2) and covered(t0) and covered(t1):
        print('LT skip (covered)', line)
        continue
    # shrink to uncovered portion of this WES if needed, but prefer leaving this stretch as WES+LT
    # If a cover overlaps, punch a hole in the cover so the lower-third can show Wes
    for k in list(kin_new):
        if not (k['t1'] <= t0 or k['t0'] >= t1):
            # split or trim cover away from LT window
            if k['t0'] < t0 - 1.2 and k['t1'] > t1 + 1.2:
                # split
                right = copy.deepcopy(k)
                k['t1'] = round(t0, 2)
                right['t0'] = round(t1, 2)
                kin_new.append(right)
            elif k['t0'] < t0:
                k['t1'] = min(k['t1'], t0)
            else:
                k['t0'] = max(k['t0'], t1)
    # drop tiny leftover covers
    kin_new = [k for k in kin_new if k['t1'] - k['t0'] >= 1.4]
    t0 = max(t0, sh['t0x']); t1 = min(t1, sh['t1x'])
    if t1 - t0 < 2.2:
        print('LT too short', line)
        continue
    kin_new.append(dict(
        shot=sh['id'], t0=round(t0, 2), t1=round(t1, 2),
        text=line, words=[], style='lower_third', cover=0,
        **{'in': 'hard', 'out': 'hard'}
    ))
    lt_added += 1
    print('LOWER_THIRD', line, t0, t1)

# sort, no overlaps (prefer cover > lt already handled)
kin_new.sort(key=lambda k: (k['t0'], 0 if k.get('cover') else 1))
# de-overlap: if two covers overlap, merge text
outk = []
for k in kin_new:
    if outk and k.get('cover') and outk[-1].get('cover') and k['t0'] < outk[-1]['t1']:
        outk[-1]['t1'] = max(outk[-1]['t1'], k['t1'])
        outk[-1]['text'] = complete_sentence(outk[-1]['t0'], outk[-1]['t1'], 110)
        continue
    outk.append(k)
E['kinetic'] = outk
print('kinetic covers', sum(1 for k in outk if k.get('cover')), 'lower_thirds', lt_added, 'total', len(outk))

# ---------- 8. L5 mix ----------
def edge_counts():
    C = collections.Counter(c['type'] for c in E['cuts'])
    for k in E['kinetic']:
        C[k.get('in', 'xfade')] += 1
        C[k.get('out', 'xfade')] += 1
    for b in E.get('broll') or []:
        C[b.get('tin', 'hard')] += 1
        C[b.get('tout', 'xfade')] += 1
    return C

def fail(C):
    t = sum(C.values()) or 1
    return any(v / t > 0.40 for v in C.values())

# rotate cover in/out
ci = 0
for k in E['kinetic']:
    if not k.get('cover'):
        continue
    ci += 1
    k['out'] = ['xfade', 'dip', 'hard', 'push'][ci % 4]
    k['in'] = ['dip', 'hard', 'xfade', 'push'][(ci + 1) % 4]
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
mix = {k: (v, round(100 * v / total)) for k, v in C.items()}
print('transition mix', {k: f'{v[0]} ({v[1]}%)' for k, v in mix.items()}, 'total', total)
if fail(C):
    # last resort: convert remaining xfade cuts
    for i, c in enumerate(E['cuts']):
        if c['type'] == 'xfade':
            c['type'] = ['dip', 'hard', 'push'][i % 3]
    C = edge_counts(); total = sum(C.values()) or 1
    mix = {k: (v, round(100 * v / total)) for k, v in C.items()}
    print('mix after last resort', mix)
if fail(C):
    sys.exit('FAIL L5: mix still over 40%')
print('PASS L5')

# ---------- 9. bubble_runs ----------
BUBK = ('TYPE_BOARD_BUBBLE', 'SCRIPTURE_BUBBLE', 'BRANDED_STILL_BUBBLE', 'AGENDA')
runs, cur = [], None
for s in E['shots']:
    if s['kind'] in BUBK:
        if cur is None:
            cur = [s['id'], s['id']]; runs.append(cur)
        else:
            cur[1] = s['id']
    else:
        cur = None
E['bubble_runs'] = runs

# ---------- 10. Text gate ----------
BAD_RE = re.compile(r'(?i)\b(item|TODO|lorem)\b|\{')
hits = []

def check(label, s):
    if s is None:
        return
    t = str(s).strip()
    if t == '':
        hits.append((label, 'EMPTY'))
        return
    if BAD_RE.search(t):
        hits.append((label, t[:80]))

for s in E['shots']:
    sp = s.get('spec') or {}
    sid = s.get('id')
    for key in ('kicker', 'title', 'lesson', 'line', 'text', 'verse'):
        v = sp.get(key)
        if isinstance(v, (list, tuple)):
            check(f'shot{sid}.{key}', v[0] if v else '')
        else:
            check(f'shot{sid}.{key}', v)
    if isinstance(sp.get('ref'), (list, tuple)):
        check(f'shot{sid}.ref', sp['ref'][0])
    else:
        check(f'shot{sid}.ref', sp.get('ref'))
    for i, r in enumerate(sp.get('rows') or []):
        check(f'shot{sid}.row{i}', r[0] if isinstance(r, (list, tuple)) else r)
for k in E['kinetic']:
    check(f"kin@{k['t0']}", k.get('text'))
    for w in k.get('words') or []:
        check(f"kin@{k['t0']}.w", w[0] if isinstance(w, (list, tuple)) else w)

# mid-sentence kinetic: warn (fail if ends with a dangling article / mid word cut like "we'll")
mid = []
for k in E['kinetic']:
    tx = (k.get('text') or '').strip()
    if not tx:
        continue
    if re.search(r"\b(the|a|an|and|or|but|to|of|for|we'll|we'll|we'll)$", tx, re.I) or tx.endswith(','):
        mid.append((k['t0'], tx))

print('text-gate hits', hits)
print('mid-sentence kinetic', mid)
if hits:
    sys.exit('FAIL text gate: placeholder or empty text')
if mid:
    # auto-fix by running complete_sentence again with a wider window
    for k in E['kinetic']:
        tx = (k.get('text') or '').strip()
        if re.search(r"\b(the|a|an|and|or|but|to|of|for|we'll)$", tx, re.I) or tx.endswith(','):
            k['text'] = complete_sentence(k['t0'], k['t1'] + 2.0, 110)
    mid2 = []
    for k in E['kinetic']:
        tx = (k.get('text') or '').strip()
        if re.search(r"\b(the|a|an|and|or|but|to|of|for|we'll)$", tx, re.I) or tx.endswith(','):
            mid2.append((k['t0'], tx))
    print('mid-sentence after fix', mid2)
    if mid2:
        sys.exit('FAIL kinetic mid-sentence leftovers')
print('PASS text gate')

# kinds tally
print('kinds', collections.Counter(s['kind'] for s in E['shots']))
# leftover long WES
leftovers = []
for u, v, sh in wes_uncovered([(k['t0'], k['t1'], '') for k in E['kinetic'] if k.get('cover')]):
    leftovers.append((round(u, 2), round(v, 2), round(v - u, 2), sh['id']))
longs = [x for x in leftovers if x[2] > 8]
print('WES uncovered segments', len(leftovers), 'max', max((x[2] for x in leftovers), default=0), 'over8', longs)

# ---------- 11. broll_map ----------
lines = []
lines.append('# L08 v3 B-roll map')
lines.append('')
lines.append('Lesson: The Empty Chair. Source: Mixkit Free (videoFree / copyrightNotice Free) only. Landscape 1080p. Edges snapped to word gaps. Men, literal to the spoken line. L07 reuse clips and the flagged off-topic stock (woman sleeping, skincare, laptop, typist, sports car, hazmat hallway, woman reading, green-screen laptop) are out.')
lines.append('')
lines.append('Restricted Mixkit clips that would have been a closer literal match (father-son dinner, a man praying, a man with a pickup, an empty dining chair) were rejected under the SOP. No Pexels download was possible here (Cloudflare). Quality over a fake count of 30.')
lines.append('')
lines.append('| # | Mixkit | In | Out | Spoken line | Picture | Why |')
lines.append('|---|--------|----|-----|-------------|---------|-----|')
for b in E['broll']:
    def mm(t):
        m=int(t//60); s=t-60*m
        return f'{m}:{s:05.2f}'
    lines.append(f"| {b['n']} | {b.get('mixkit_id')} | {mm(b['t0'])} | {mm(b['t1'])} | {b.get('line','').replace('|','/')} | {b.get('picture','').replace('|','/')} | {b.get('why','').replace('|','/')} |")
lines.append('')
Path(MAP_P).write_text('\n'.join(lines) + '\n')
print('wrote', MAP_P)

# write EDL
json.dump(E, open(EDL_P, 'w'), indent=1)
print('wrote', EDL_P)
print('shots', len(E['shots']), 'broll', len(E['broll']), 'kinetic', len(E['kinetic']), 'end', E['end'])
