#!/usr/bin/env python3
"""L07-class EDL builder. Reads inputs.json; upgrades p5 edl or builds from storyboard.
Enforces L5 (<=40% any transition type), injects kinetic covers from cover_master, fixes scripture."""
import os,sys,json,re,copy,collections
inp=json.load(open(sys.argv[1]))
LC=inp['lesson']; WORK=LC['work'].rstrip('/'); B=LC['build'].rstrip('/')
W=json.load(open(inp['words']))
words=[w['word'] for w in W]
def nz(s): return re.sub(r"[^a-z0-9']","",s.lower().replace("'","'").replace("'","'"))
WN=[nz(w) for w in words]

def find_phrase(ph, t0, t1):
    p=[nz(x) for x in ph.split() if nz(x)]
    if not p: return t0
    for i,w in enumerate(W):
        if w['start']<t0-0.5 or w['start']>t1+0.5: continue
        if WN[i:i+len(p)]==p: return round(w['start']-0.04,3)
    return round(t0+0.2,3)

def gap_at(c):
    pe=max([w['end'] for w in W if w['end']<=c+0.05]+[0])
    ns=min([w['start'] for w in W if w['start']>=c-0.05]+[1e9])
    return pe,ns

# ---- load base EDL (prefer p5, else p7 existing, else storyboard rebuild stub)
p5=f'{WORK}/p5/edl.json'
if os.path.isfile(p5):
    E=json.load(open(p5)); print('base p5 edl')
elif os.path.isfile(inp['edl']) and os.path.getsize(inp['edl'])>1000:
    E=json.load(open(inp['edl'])); print('base existing edl')
else:
    raise SystemExit('no base edl — run p5 build first or provide storyboard edl')

# audio end
END=float(inp['audio_dur'])
# ensure LOGO_END
if E['shots'][-1]['kind']!='LOGO_END':
    last=E['shots'][-1]
    E['shots'].append(dict(id='logo',kind='LOGO_END',t0=END,t1=END+4.0,t0x=END-0.75,t1x=END+4.0,spec={},trans='dip',wes='none'))
E['audio_dur']=END
E['end']=E['shots'][-1]['t1x']
E['fps']=25

# ---- fill empty AGENDA / board rows from spoken window
for s in E['shots']:
    sp=s.setdefault('spec',{})
    if s['kind']=='AGENDA' and not sp.get('rows'):
        # pull short cue phrases from words in shot
        ww=[w for w in W if s['t0']<=w['start']<=s['t1']]
        # split on sentence ends into up to 5 pills
        text=' '.join(w['word'] for w in ww)
        parts=[x.strip() for x in re.split(r'(?<=[.?!])\s+', text) if x.strip()]
        rows=[]
        for part in parts[:5]:
            # cue at first word of part
            at=find_phrase(part.split()[0] if part.split() else part, s['t0'], s['t1'])
            short=' '.join(part.split()[:6])
            if short: rows.append([short, at])
        sp['rows']=rows
        sp['style']=sp.get('style') or 'pills'
    if s['kind'] in ('TYPE_BOARD_BUBBLE','SPLIT') and not sp.get('rows'):
        ww=[w for w in W if s['t0']<=w['start']<=s['t1']]
        if ww:
            # one key line: first ~12 words
            phrase=' '.join(w['word'] for w in ww[:12])
            sp['rows']=[[phrase, round(ww[0]['start'],3)]]
            sp.setdefault('style','rows'); sp.setdefault('paper', False)

# ---- fix SCRIPTURE_BUBBLE specs from spoken words
WORDS_NUM={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','ten':'10','eleven':'11','twelve':'12'}
VERSE_RE=re.compile(r'(Ephesians|Eph\.?|Matthew|Matt\.?|Hebrews|Heb\.?|John|Romans|Prov(?:erbs)?)\s*(?:chapter\s*)?(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)[,:]?\s*(?:verse\s*)?(\d+(?:\s*-\s*\d+)?|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)', re.I)
NIV_Q=re.compile(r'[""]([^""]{20,400})[""]')
for s in E['shots']:
    if s['kind']!='SCRIPTURE_BUBBLE': continue
    sp=s.setdefault('spec',{})
    # gather spoken text in window
    spoken=' '.join(w['word'] for w in W if s['t0']-0.5<=w['start']<=s['t1']+0.5)
    m=VERSE_RE.search(spoken)
    q=NIV_Q.search(spoken)
    # also try storyboard spoken
    if not m or not q:
        sb_path=f'{B}/storyboard.json'
        if os.path.isfile(sb_path):
            sb=json.load(open(sb_path))
            for sh in sb.get('shots',[]):
                if sh.get('kind')=='SCRIPTURE_BUBBLE' and abs(sh.get('t_in',0)-s['t0'])<30:
                    spoken=sh.get('spoken','')+' '+spoken
                    m=m or VERSE_RE.search(spoken); q=q or NIV_Q.search(spoken)
                    break
    bookmap={'ephesians':'EPHESIANS','eph':'EPHESIANS','matthew':'MATTHEW','matt':'MATTHEW',
             'hebrews':'HEBREWS','heb':'HEBREWS','john':'JOHN','romans':'ROMANS','proverbs':'PROVERBS','prov':'PROVERBS'}
    if m:
        bk=bookmap.get(m.group(1).lower().rstrip('.'), m.group(1).upper())
        ch=WORDS_NUM.get(m.group(2).lower(), m.group(2)); vs=WORDS_NUM.get(m.group(3).lower().replace(' ',''), m.group(3).replace(' ','')); ref=f"{bk} {ch}:{vs} (NIV)"
        sp['ref']=[ref, find_phrase(m.group(0)[:40], s['t0'], s['t1'])]
    if q:
        verse=q.group(1).strip()
        sp['verse']=verse
        sp['vat']=find_phrase(verse.split()[:6] and ' '.join(verse.split()[:4]), s['t0'], s['t1'])
        sp['vend']=s['t1']
        # default highlight: last clause / key phrase
        if 'hi' not in sp or not sp['hi']:
            parts=re.split(r'[.;]', verse)
            hi=parts[-1].strip() if len(parts)>1 and len(parts[-1].split())>=3 else ' '.join(verse.split()[:6])
            sp['hi']=[hi]
    sp['style']=sp.get('style') or 'scripture'
    if 'side' in sp and not sp['side']:
        del sp['side']
    print('scripture', s['id'], sp.get('ref'), 'verse' in sp, sp.get('hi'))

# ---- load covers from cover_master
covers=[]
cp=inp.get('cover')
if cp and os.path.isfile(cp):
    cm=json.load(open(cp))
    for a,b in cm.get('hands') or []: covers.append([a,b,'hand'])
    for a,b in cm.get('arc') or []: covers.append([a,b,'arc'])
    for a,b in cm.get('grin12') or []: covers.append([a,b,'grin'])
    j=cm.get('jump')
    if j and isinstance(j,(list,tuple)) and len(j)>=1:
        jt=j[0] if isinstance(j[0],(int,float)) else j
        covers.append([float(jt)-0.2, float(jt)+0.2, 'jump'])
# merge nearby
covers=sorted(covers)
merged=[]
for a,b,why in covers:
    if merged and a-merged[-1][1]<=0.35: merged[-1][1]=max(merged[-1][1],b); merged[-1][2]=why
    else: merged.append([a,b,why])

# ---- ensure kinetic list; add cover cards over cover ranges on WES_FULL
kin=E.setdefault('kinetic',[])
def wes_full_at(t):
    for s in E['shots']:
        if s['kind']=='WES_FULL' and s['t0x']<=t<s['t1x']: return s
    return None
# mark existing covers
for k in kin:
    if k.get('cover'): continue
existing_cov=sum(1 for k in kin if k.get('cover'))
for a,b,why in merged:
    s=wes_full_at((a+b)/2) or wes_full_at(a)
    if not s: 
        # also cover CLOSE/MEDIUM jump/arc with cover card
        s=next((x for x in E['shots'] if x['t0x']<=(a+b)/2<x['t1x']), None)
    if not s: continue
    # skip if already covered
    if any(k.get('cover') and not (k['t1']<=a or k['t0']>=b) for k in kin): continue
    # build text from words in window
    ww=[(w['word'], w['start']) for w in W if a-0.3<=w['start']<=b+1.5]
    if not ww:
        ww=[(w['word'], w['start']) for w in W if s['t0']<=w['start']<=s['t1']][:14]
    text=' '.join(x[0] for x in ww[:16])
    t0=max(s['t0x'], a-0.4); t1=min(s['t1x'], max(b+0.6, t0+2.5))
    kin.append(dict(shot=s['id'], t0=round(t0,2), t1=round(t1,2), text=text, words=ww[:16],
                    cover=1, why=[round(a,2),round(b,2)], **{'in':'xfade','out':'xfade'}))
# still-run covers: any WES_FULL uncovered >8s
changed=True
while changed:
    changed=False
    for s in [x for x in E['shots'] if x['kind']=='WES_FULL']:
        a,b=s['t0x'],s['t1x']
        segs=[(a,b)]
        for k in sorted([k for k in kin if k.get('cover')], key=lambda x:x['t0']):
            n=[]
            for u,v in segs:
                if k['t1']<=u or k['t0']>=v: n.append((u,v)); continue
                if k['t0']>u: n.append((u,k['t0']))
                if k['t1']<v: n.append((k['t1'],v))
            segs=n
        for u,v in segs:
            if v-u<=8: continue
            # place cover in the middle ~4s
            mid=(u+v)/2; t0=mid-2; t1=mid+2
            ww=[(w['word'], w['start']) for w in W if t0<=w['start']<=t1]
            text=' '.join(x[0] for x in ww) or 'Stay with that.'
            kin.append(dict(shot=s['id'], t0=round(t0,2), t1=round(t1,2), text=text, words=ww,
                            cover=1, why=[round(u,2),round(v,2)], **{'in':'xfade','out':'dip'}))
            changed=True

# ---- cover-edge rotation for L5 (kinetic in/out + shot cuts)
# count ALL transition edges: shot cuts + kinetic in/out + broll
def edge_counts():
    C=collections.Counter(c['type'] for c in E['cuts'])
    for k in kin:
        C[k.get('in','xfade')]+=1; C[k.get('out','xfade')]+=1
    for b in E.get('broll') or []:
        C[b.get('tin','hard')]+=1; C[b.get('tout','xfade')]+=1
    return C
# rotate kinetic edges if any type >40%
def pct(C):
    t=sum(C.values()) or 1
    return {k: (v, round(100*v/t)) for k,v in C.items()}
C=edge_counts()
# force rotation: every 2nd cover out->dip, every 3rd cover in->hard
ci=0
for k in kin:
    if not k.get('cover'): continue
    ci+=1
    if ci%2==0: k['out']='dip'
    if ci%3==0: k['in']='hard'
# also rotate some shot cuts if still failing
def fail(C):
    t=sum(C.values()) or 1
    return any(v/t>0.40 for v in C.values())
C=edge_counts()
if fail(C):
    # convert some xfade cuts to dip/hard alternately
    n=0
    for c in E['cuts']:
        if c['type']=='xfade':
            n+=1
            if n%2==0: c['type']='dip'
            elif n%3==0: c['type']='hard'
C=edge_counts(); P=pct(C)
mix_s={k: f"{v[0]} ({v[1]}%)" for k,v in P.items()}
total=sum(C.values())
print('covers', collections.Counter(('cover card' if k.get('cover') else 'kin') for k in kin))
print('shots', len(E['shots']), 'broll', len(E.get('broll') or []), 'kinetic', len(kin), 'end', E['end'])
print('transition mix', mix_s, 'total', total)
if fail(C):
    print('FAIL L5: one transition type >40% -> re-plan storyboard transitions / B-roll edges before P7')
    raise SystemExit(2)
print('PASS L5')

# ---- drop broll that cuts inside/near end awkwardly (keep simple)
br=E.get('broll') or []
kept=[]
for b in br:
    if b['t1']>E['end']-2: print('drop broll (cut inside/near end)', b.get('n'), b['t0'], b['t1']); continue
    kept.append(b)
E['broll']=kept
E['kinetic']=kin

# bubble_runs from bubble-kind shots
BUBK=('TYPE_BOARD_BUBBLE','SCRIPTURE_BUBBLE','BRANDED_STILL_BUBBLE','AGENDA')
runs=[]; cur=None
for s in E['shots']:
    if s['kind'] in BUBK:
        if cur is None: cur=[s['id'],s['id']]; runs.append(cur)
        else: cur[1]=s['id']
    else: cur=None
E['bubble_runs']=runs

# write
os.makedirs(os.path.dirname(inp['edl']), exist_ok=True)
json.dump(E, open(inp['edl'],'w'), indent=1)
# words sidecar + covers list for QC
json.dump([[a,b,w] for a,b,w in merged], open(f"{WORK}/p7/edl_covers.json",'w'), indent=1)
# edl_words: pass through
if os.path.isfile(f'{WORK}/p5/edl_words.json'):
    open(f'{WORK}/p7/edl_words.json','w').write(open(f'{WORK}/p5/edl_words.json').read())
else:
    json.dump(W, open(f'{WORK}/p7/edl_words.json','w'))
print('wrote', inp['edl'])
