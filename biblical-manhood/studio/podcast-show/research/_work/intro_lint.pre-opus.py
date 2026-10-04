#!/usr/bin/env python3
"""Lint the per-episode intros in _build/intros_data.py (SHOW-BIBLE section 5).
usage: python3 _build/intro_lint.py [--verbose]
FAIL (exit 1):
  - a 6-gram shared by two intros within 8 episodes (anchor phrases collapsed first)
  - a 5-gram shared by two intros within 4 episodes
  - a 6-gram used in more than 12 intros (one offer-bank shape overused)
  - an intro that doesn't open with the anchor "This is Walk Steadfast"
  - a missing beat: Walk Steadfast, Wes Hart, Jonathon, the word Steadfast on the offer,
    book, video training, walksteadfast.com, a today hook
  - word count outside the window (mains 42-62, Field Notes 32-52, E001 60-75)
  - hook line over 14 words, or two hooks within 3 episodes opening with the same three words
  - dashes, curly quotes, semicolons, a mid-sentence colon, banned words, fillers,
    'welcome back', "on today's episode", "out now", prices, any AI mention
WARN: a 5-gram in more than 12 intros overall, two hooks sharing a 4-gram; lead speaker the same 4 episodes running."""
import re,sys,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from intros_data import I
FN={n for n in I if n%2==0}
ANCHORS=[('book and the steadfast video training','OFFER'),('book and the video training','OFFER'),('book and a video training','OFFER'),('walksteadfast.com','SITE'),('walk steadfast','SHOW'),('wes hart','WES'),('video training','VT'),
         ('following jesus as a man','MISSION'),('steadfast','SF'),('jonathon','JON')]
BANNED=r"\b(additionally|crucial|delve|enduring|enhance|fostering|garner|interplay|intricate|landscape|pivotal|showcase|tapestry|testament|underscore|vibrant|serves as|journey|navigate|unpack|dive in|robust|realm|leverage|game-changer|uh|um)\b"
def norm(s):
    s=s.lower()
    for a,b in ANCHORS: s=s.replace(a,' x'+b.lower()+' ')
    return re.findall(r"[a-z0-9']+",s)
def grams(toks,k):
    # toks is a list of lines (lists of tokens); n-grams never cross a line
    if toks and isinstance(toks[0],str): toks=[toks]
    return {tuple(t[i:i+k]) for t in toks for i in range(len(t)-k+1)}
def hook(lines):
    for who,t in reversed(lines):
        m=re.search(r"\b(Today|today)\b[^.]*\.(?:[^.]*\.)?",t)
        if m: return m.group(0)
    return None
def main(verbose=False):
    fails=[];warns=[]
    def body(n):
        out=[]
        for k,(_,x) in enumerate(I[n]):
            if k==0: x=re.sub(r"^This is Walk Steadfast[^.]*\.","",x)
            x=re.sub(r"\b(And )?I'm (Wes Hart|Jonathon)\b","",x)
            out.append(norm(x))
        return out
    toks={n:body(n) for n in I}
    for n in I:
        if not I[n][0][1].startswith("This is Walk Steadfast"): fails.append(f"E{n:03d} does not open with the anchor 'This is Walk Steadfast'")
    for n in sorted(I):
        L=I[n]; txt=' '.join(t for _,t in L); low=txt.lower(); wc=len(txt.split())
        lo,hi=(32,52) if n in FN else (42,62)
        if n==1: lo,hi=60,75
        if not lo<=wc<=hi: fails.append(f"E{n:03d} words {wc} (window {lo}-{hi})")
        for need,rx in [('show name',r'walk steadfast'),('Wes Hart',r'wes hart'),('Jonathon',r'\bjonathon\b'),
('video training',r'video training'),('site',r'walksteadfast\.com'),
                        ('book or Steadfast Men',r'\bbook\b|steadfast men')]:
            if not re.search(rx,low): fails.append(f"E{n:03d} missing beat: {need}")
        h=hook(L)
        if not h: fails.append(f"E{n:03d} no today hook")
        elif len(h.split())>14: fails.append(f"E{n:03d} hook {len(h.split())} words: {h}")
        if re.search(r"[\u2014\u2013\u201c\u201d\u2018\u2019;]|--",txt): fails.append(f"E{n:03d} dash, curly quote or semicolon")
        if re.search(r"\w: \w",txt): fails.append(f"E{n:03d} mid-sentence colon")
        if re.search(BANNED,low): fails.append(f"E{n:03d} banned word: {re.search(BANNED,low).group(0)}")
        if re.search(r"welcome back|on today's episode|out now|\$\d|\bai\b|artificial",low): fails.append(f"E{n:03d} forbidden phrase")
        for w,t in L:
            if (w=='W' and re.search(r"Wes's book|\bHis book",t)) or (w=='J' and re.search(r"\b[Mm]y book",t)): fails.append(f"E{n:03d} speaker mismatch on the book line: {w}: {t}")
        if [w for w,_ in L[:1]]!=[] and len({w for w,_ in L})<2: fails.append(f"E{n:03d} one speaker only")
    ns=sorted(I)
    for i,a in enumerate(ns):
        for b in ns[i+1:]:
            g6=grams(toks[a],6)&grams(toks[b],6)
            if g6 and b-a<=8: fails.append(f"E{a:03d}/E{b:03d} share 6-gram: {' '.join(sorted(g6)[0])}")
            if b-a<=4:
                g5=grams(toks[a],5)&grams(toks[b],5)
                if g5: fails.append(f"E{a:03d}/E{b:03d} share 5-gram within 4: {' '.join(sorted(g5)[0])}")
    c=collections.Counter(g for n in I for g in grams(toks[n],5))
    hk={n:norm(hook(I[n]) or '')[:3] for n in ns}
    for i,a in enumerate(ns):
        for b in ns[i+1:i+4]:
            if hk[a] and hk[a]==hk[b]: fails.append(f"E{a:03d}/E{b:03d} hooks open the same way within 3: {' '.join(hk[a])}")
    c6=collections.Counter(g for n in I for g in grams(toks[n],6))
    hooks=[hook(I[n]) or '' for n in ns]
    for i,a in enumerate(ns):
        for b in ns[i+1:]:
            if b-a<=8 and hooks[i] and set(grams(norm(hooks[i])[3:],4))&set(grams(norm(hooks[ns.index(b)])[3:],4)): warns.append(f"E{a:03d}/E{b:03d} hooks share a 4-gram after the opener")
    for g,k in c6.items():
        if k>12: fails.append(f"6-gram in {k} intros (bank shape overused): {' '.join(g)}")
    for g,k in c.items():
        if k>12: warns.append(f"5-gram in {k} intros: {' '.join(g)}")
    leads=[I[n][0][0] for n in ns]
    for i in range(len(ns)-3):
        if len(set(leads[i:i+4]))==1: warns.append(f"E{ns[i]:03d}-E{ns[i+3]:03d} same lead four running")
    for f in fails: print("FAIL",f)
    for w in warns: print("WARN",w)
    wcs=[len(' '.join(t for _,t in I[n]).split()) for n in ns]
    mw=[w for n,w in zip(ns,wcs) if n not in FN and n!=1]; fw=[w for n,w in zip(ns,wcs) if n in FN]
    print(f"intros {len(ns)}  mains avg {sum(mw)/max(1,len(mw)):.1f} words  Field Notes avg {sum(fw)/max(1,len(fw)):.1f}  fails {len(fails)}  warns {len(warns)}")
    return 1 if fails else 0
if __name__=='__main__': sys.exit(main('--verbose' in sys.argv))
