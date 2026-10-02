#!/usr/bin/env python3
"""Lint the Steadfast Men scripts against the 2026-10-01 rewrite brief.

usage: python3 lint.py [--stats] [--ngrams] [FILES...]
  default FILES: every sessions/*.txt (W01-W24, the live training sessions) under the output folder.
  S01-S04 are shelved in _shelved/lectures-S01-S04/ and are not linted or counted unless named.
  --stats   also write meta/STATS.tsv and meta/VERSES.tsv
  --ngrams  report repeated 6-word strings across all files (scripture and creed excluded)
Verse plan: meta/tools/verse-plan.tsv (script, reference, exact NIV text, source).
"""
import sys, re, os, glob, subprocess, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CHECK = os.environ.get('CHECK_PY', '/workspace/_inputs/pipeline/check.py')

CREED = "A steadfast man stops waiting, picks up the weight, goes first, and works for God's pay, not the room's."
MARKS = ["stop waiting", "pick up the weight", "go first", "work for god's pay"]
FOCUS = {
    'W04': 'stop waiting', 'S04': 'stop waiting', 'W05': 'pick up the weight',
    'W06': 'go first', 'W07': "work for god's pay",
}
ALLOWED_TAGS = {'[warmly]', '[dry]', '[amused]'}
BANNED = [
    r'\bweeks?\b', r'\btonight\b', r'\bsession (one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b',
    r'\blesson\b', r'\blessons\b', r'twenty-?four', r'\[beat\]', r'\[laughs', r'\[quietly\]', r'applau',
    r'\bcoffee crew', r'lewis', r'passiv', r'accepts responsib', r'courageous', r'greater reward',
    r'a real man', r"men's fraternity", r'modern-day knight', r'authentic manhood', r'look who',
    r'fellowship bible', r"god's reward", r'rejects? ', r'next time', r'next session', r'\bnumbered\b',
    r'\bof twenty\b', r'\bweekly\b',
]
W_BANNED = [r'\bviewers?\b', r'\bsubscrib\w*', r'\byoutube\b']
FILLER_RE = re.compile(r'\b(u+h+|u+m+|uhm+|e+h+)\b', re.I)  # uh, uhh, um, umm, uhm, eh, ehh
MARKERS = ["Now", "So", "Look", "Okay", "Listen", "Well", "Here's the thing", "Stay with me"]


def norm(s):
    s = s.lower().replace('\u2019', "'").replace('\u2018', "'")
    s = re.sub(r'\[[a-z ]+\]', ' ', s)
    s = s.replace("'", '')
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return ' '.join(s.split())


def parse(path):
    secs = []
    for n, l in enumerate(open(path).read().split('\n'), 1):
        l = l.strip()
        if not l:
            continue
        if l.startswith('# SECTION:'):
            secs.append({'title': l[10:].strip(), 'lines': []})
            continue
        t, p = l.rsplit('|', 1)
        secs[-1]['lines'].append((n, t, p))
    return secs


def pval(p):
    return 3.0 if p == 'ROOM_HANDS' else 1.7 if p == 'ROOM_CHUCKLE' else float(p)


def load_plan():
    plan = collections.defaultdict(list)
    extra = sorted(glob.glob(os.environ.get('VERSE_EXTRA', '')))
    for f in [os.path.join(HERE, 'verse-plan.tsv')] + extra:
        if not os.path.exists(f):
            continue
        for l in open(f):
            if not l.strip() or l.startswith('script\t'):
                continue
            sc, ref, text, src = l.rstrip('\n').split('\t')
            plan[sc].append((ref, text, src))
    return plan


def spoken_ref(ref):
    return ref  # informational only


def lint(path, plan, verse_rows):
    name = os.path.basename(path)[:3]
    secs = parse(path)
    issues = []
    words = 0
    tags = collections.Counter()
    hands = chk = 0
    uh_total = 0
    ell = 0
    hank = 0
    markers = []
    dash = 0
    youknow = imean = tagq = 0
    full = []
    for si, s in enumerate(secs):
        chars = sum(len(t) + 1 for _, t, _ in s['lines'])
        s['chars'] = chars
        if not 1500 <= chars <= 1900:
            issues.append(f'section {si+1} "{s["title"]}" {chars} chars (want 1500-1900)')
        if not s['lines']:
            issues.append(f'section {si+1} empty'); continue
        lp = s['lines'][-1][2]
        if lp in ('ROOM_HANDS', 'ROOM_CHUCKLE') or not 1.0 <= float(lp) <= 1.4:
            issues.append(f'section {si+1} last pause {lp} (want 1.0-1.4)')
        sec_ell = sum(t.count('...') for _, t, _ in s['lines'])
        mid_ell = sum(len(re.findall(r'\.\.\.(?!$)', t)) for _, t, _ in s['lines'])
        if sec_ell > 2 or mid_ell > 1:
            issues.append(f'section {si+1} has {sec_ell} ellipses, {mid_ell} mid-line (max 2, 1 mid-line)')
        for n, t, p in s['lines']:
            if p not in ('ROOM_HANDS', 'ROOM_CHUCKLE'):
                try:
                    v = float(p)
                except ValueError:
                    issues.append(f'L{n} bad pause {p}'); v = 0.5
            hands += p == 'ROOM_HANDS'; chk += p == 'ROOM_CHUCKLE'
            for tg in re.findall(r'\[[a-z ]+\]', t):
                tags[tg] += 1
                if tg not in ALLOWED_TAGS:
                    issues.append(f'L{n} tag not allowed {tg}')
            if re.search(r'\S\s*\[[a-z ]+\]', t):
                issues.append(f'L{n} tag not at line start: {t[:50]}')
            body = re.sub(r'^(\[[a-z ]+\]\s*)+', '', t)
            words += len(re.sub(r'\[[a-z ]+\]', '', t).split())
            low = t.lower()
            for b in BANNED:
                if re.search(b, low):
                    issues.append(f'L{n} banned /{b}/: {t[:60]}')
            if name.startswith('W'):
                for b in W_BANNED:
                    if re.search(b, low):
                        issues.append(f'L{n} W scripts are live training sessions, banned /{b}/: {t[:60]}')
            if re.search(r'\b(ray|dale)\b', low):
                issues.append(f'L{n} "Ray"/"Dale" not allowed (book men; S02 wallet man is Hank): {t[:60]}')
            if name != 'S02' and re.search(r'\bhank\b', low):
                issues.append(f'L{n} "Hank" is reserved for the S02 wallet man: {t[:60]}')
            if name == 'S02' and re.search(r'\bhank\b', low):
                hank += 1
            if name != 'W10' and re.search(r'\bphilip\b', low):
                issues.append(f'L{n} "Philip" only as the apostle in W10 (John 14:9); the S02 breakfast man is Ike: {t[:60]}')
            if name != 'S02' and re.search(r'\bike\b', low):
                issues.append(f'L{n} "Ike" is reserved for the S02 breakfast man: {t[:60]}')
            # 2026-10-01: fillers are banned outright. Every uh/um/eh is now a silent beat
            # (line break + post pause) or a short restart. Case-insensitive, whole word only,
            # so "the ER" (W10) and words like "umbrella" or "them" never match.
            for fm in FILLER_RE.finditer(t):
                uh_total += 1
                issues.append(f'L{n} filler "{fm.group(0)}" not allowed (use a silent beat or a restart): {t[:60]}')
            ell += t.count('...')
            for d in re.finditer(r'[\u2014\u2013]', t):
                dash += 1
                m = re.search(r"([\w']+)[\u2014\u2013] ([\w']+)", t)
                if not m or m.group(1).lower() != m.group(2).lower():
                    issues.append(f'L{n} dash not in restart form: {t[:60]}')
            if '--' in t:
                issues.append(f'L{n} double hyphen')
            for mk in MARKERS:
                if re.match(re.escape(mk) + (r'\b' if ' ' in mk else r'[,.]'), body):
                    markers.append(mk); break
            youknow += len(re.findall(r'(, you know\b|^you know,|\byou know,)', low))
            imean += len(re.findall(r'(, i mean\b|^i mean,|\bi mean,)', low))
            tagq += len(re.findall(r"(right\?|you with me\?|fair\?|(?:is|was|does|do|did|are|were|has|have|ca|could|should|would|wo)n't (?:it|he|she|they|we|you|i|that)\?)$", low))
            full.append((si, t))
    if not 3300 <= words <= 3800:
        issues.append(f'{words} words (want 3300-3800)')
    if ell > 4:
        issues.append(f'{ell} ellipses (max 4)')
    if name == 'S02' and not (hank and re.search(r'wallet', ' '.join(t for _, t in full).lower())):
        issues.append('S02 must carry the Hank wallet story (workbook points at it)')
    if name == 'S02' and not re.search(r"never going to shake hands", ' '.join(t for _, t in full).lower()):
        issues.append('S02 Hank story must say his two lines were "never going to shake hands" (workbook Q5)')
    if dash > 3:
        issues.append(f'{dash} dashes (max 3)')
    if hands + 0 > 3:
        issues.append(f'{hands} ROOM_HANDS (max 3)')
    if chk > 4:
        issues.append(f'{chk} ROOM_CHUCKLE (max 4)')
    tone = sum(tags.values())
    if tone > 6:
        issues.append(f'{tone} tone tags (keep rare)')
    for a, b in zip(markers, markers[1:]):
        pass
    # consecutive identical discourse markers (in order of appearance)
    for i in range(1, len(markers)):
        if markers[i] == markers[i - 1]:
            issues.append(f'discourse marker "{markers[i]}" twice in a row')
    if youknow > 5: issues.append(f'"you know" x{youknow}')
    if imean > 5: issues.append(f'"I mean" x{imean}')
    alltext = norm(' '.join(t for _, t in full))
    creed = alltext.count(norm(CREED))
    marks = {m: alltext.count(norm(m)) for m in MARKS}
    focus = FOCUS.get(name)
    fsecs = []
    if focus:
        for si, s in enumerate(secs):
            if norm(focus) in norm(' '.join(t for _, t, _ in s['lines'])):
                fsecs.append(si + 1)
        if not fsecs or fsecs[0] > 3 or fsecs[-1] < len(secs) - 2:
            issues.append(f'focus mark "{focus}" sections {fsecs} (want early and in recap)')
    # verses
    refs_spoken = []
    for si, s in enumerate(secs):
        for n, t, p in s['lines']:
            if re.match(r'^(\[[a-z ]+\]\s*)?[A-Z][a-z]+( [a-z]+)*( [A-Z][a-z]+)? [a-z\- ]+, (starting at )?verses? [a-z\- ]+\.$', t) or \
               re.match(r'^(First|Second) [A-Z][a-z]+ [a-z\- ]+, (starting at )?verses? [a-z\- ]+\.$', t):
                refs_spoken.append((si + 1, t))
    if len(refs_spoken) != 3:
        issues.append(f'{len(refs_spoken)} spoken verse references (want 3): {[r for _, r in refs_spoken]}')
    vp = plan.get(name, [])
    if len(vp) != 3:
        issues.append(f'verse plan has {len(vp)} rows')
    for ref, text, src in vp:
        nt = norm(text)
        found = None
        for si, s in enumerate(secs):
            if nt in norm(' '.join(t for _, t, _ in s['lines'])):
                found = si + 1; break
        if not found:
            issues.append(f'verse {ref} not quoted exactly')
        verse_rows.append((os.path.basename(path)[:-4], str(found) + (': ' + secs[found - 1]['title'] if found else ''), ref, text, src))
    # check.py
    r = subprocess.run([sys.executable, CHECK, path], capture_output=True, text=True).stdout.strip().split('\n')
    head = r[0] if r else ''
    ok = head.endswith('out-of-range sections []') and len(r) == 1
    if not ok:
        issues.append('check.py: ' + ' / '.join(r))
    stats = dict(script=os.path.basename(path)[:-4], words=words, sections=len(secs), uh=uh_total,
                 tags=' '.join(f'{k}x{v}' for k, v in sorted(tags.items())) or '0', hands=hands, chuckles=chk,
                 focus=(f'{focus}: {len(fsecs)} sections {fsecs}' if focus else 'n/a'), creed=creed,
                 check='PASS' if ok else 'FAIL', ellipses=ell, markers=len(markers), dashes=dash,
                 marks=marks, youknow=youknow, imean=imean, tagq=tagq,
                 secchars=[s['chars'] for s in secs])
    return issues, stats, full


def ngrams(files, plan):
    seen = collections.defaultdict(list)
    for f in files:
        name = os.path.basename(f)[:3]
        secs = parse(f)
        text = ' ' + norm(' '.join(t for s in secs for _, t, _ in s['lines'])) + ' '
        for ref, vt, src in plan.get(name, []):
            text = text.replace(' ' + norm(vt) + ' ', ' | ')
        text = text.replace(' ' + norm(CREED) + ' ', ' | ')
        for chunk in text.split('|'):
            toks = chunk.split()
            for i in range(len(toks) - 5):
                seen[' '.join(toks[i:i + 6])].append(os.path.basename(f)[:3])
    reps = {k: v for k, v in seen.items() if len(set(v)) > 1}
    return reps


def main():
    args = sys.argv[1:]
    do_stats = '--stats' in args
    do_ng = '--ngrams' in args
    files = [a for a in args if not a.startswith('--')]
    allfiles = sorted(glob.glob(os.path.join(ROOT, 'sessions', '*.txt')))
    if not files:
        files = allfiles
    plan = load_plan()
    rows = []
    vrows = []
    bad = 0
    for f in files:
        issues, st, _ = lint(f, plan, vrows)
        rows.append(st)
        flag = 'OK ' if not issues else 'ERR'
        bad += bool(issues)
        print(f"{flag} {st['script']}: {st['words']}w {st['sections']}sec uh{st['uh']} hands{st['hands']} chk{st['chuckles']} "
              f"tags[{st['tags']}] ell{st['ellipses']} dash{st['dashes']} mk{st['markers']} yk{st['youknow']} im{st['imean']} tq{st['tagq']} "
              f"creed{st['creed']} focus[{st['focus']}] marks{[st['marks'][m] for m in MARKS]}")
        print('     chars', st['secchars'])
        for i in issues:
            print('     -', i)
    if do_ng:
        reps = ngrams(allfiles, plan)
        print(f'\nrepeated 6-grams: {len(reps)}')
        for k, v in sorted(reps.items(), key=lambda kv: kv[1]):
            print(f'  {",".join(v)}: {k}')
    if do_stats:
        with open(os.path.join(ROOT, 'meta', 'STATS.tsv'), 'w') as o:
            o.write('script\twords\tsections\tuh_um\ttags\tROOM_HANDS\tROOM_CHUCKLE\tfocus_mark_mentions\tcreed_uses\tellipses\tcheck_py\n')
            for st in rows:
                o.write(f"{st['script']}\t{st['words']}\t{st['sections']}\t{st['uh']}\t{st['tags']}\t{st['hands']}\t{st['chuckles']}\t{st['focus']}\t{st['creed']}\t{st['ellipses']}\t{st['check']}\n")
        with open(os.path.join(ROOT, 'meta', 'VERSES.tsv'), 'w') as o:
            o.write('script\tsection\treference\texact_niv_text\tverified_source\n')
            for r in vrows:
                o.write('\t'.join(r) + '\n')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
