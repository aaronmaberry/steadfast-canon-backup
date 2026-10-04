"""Cold-open and first-line retell check for the per-episode opens (SHOW-BIBLE section 5).
An open's fact or hook must not retell the cold open or step on the first line after the slate.
Used by intro_lint.py. Changes nothing."""
import re,glob,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOP=set("""this that with what when where which while your yours you'd you're they them their there then than have has had
been being were will would could should about after again also just only into onto from over under very more most much many
some such each every like said says say tell told know knew want wants need needs make made take took give gave come came
goes went going gone here week weeks today tonight time year years still back down well good right yeah okay because
first last next even ever never always mine ours ourselves myself himself herself dont didn't don't doesn't isn't wasn't i'm i've i'll
he's she's it's that's what's there's we're we've we'll let's walk steadfast wes hart jonathon book training video videos walksteadfast
following jesus man men friday fridays tuesday tuesdays report reports talk straight plainly twice show both found find live lives
asks ask asked question answer whether help""".split())
# (episode, word) pairs reviewed by hand on 2026-10-03 and judged not a retelling (different sense or a topic word).
ALLOW={(25,'nine'),(36,'game'),(37,'sister'),(38,'name'),(48,'father'),(63,'sick'),(65,'since'),(73,'nobody')}
def stem(w):
    w=w.lower().strip("'")
    for suf in ("'s","ing","ed","es","s"):
        if w.endswith(suf) and len(w)-len(suf)>=4: return w[:-len(suf)]
    return w
def content(s):
    return {stem(w) for w in re.findall(r"[A-Za-z']+",s) if len(w)>=4 and w.lower() not in STOP and stem(w) not in STOP}
def script_for(n):
    g=glob.glob(os.path.join(ROOT,'scripts',f'E{n:03d}-*.md'))
    return g[0] if g else None
def parts(path):
    """returns (cold-open spoken text, first spoken line after the Intro chapter)"""
    cold=[];first=None;ch=None;after=False
    for line in open(path):
        m=re.match(r'\[CHAPTER: (.*)\]',line)
        if m:
            if ch=='Intro': after=True
            ch=m.group(1); continue
        m=re.match(r'(WES|JONATHON): (.*)',line)
        if not m: continue
        t=re.sub(r'\([^)]*\)|\[[^]]*\]','',m.group(2))
        if ch=='Cold open': cold.append(t)
        elif after and first is None and ch!='Intro': first=t
        if line.startswith('## Shorts'): break
    return ' '.join(cold),first or ''
def check(n,lines,limit=2):
    """returns a list of (line, target, shared words) where an open line shares >= limit content words"""
    p=script_for(n)
    if not p: return None
    cold,first=parts(p)
    out=[]
    for k,(_,t) in enumerate(lines):
        x=re.sub(r"^This is Walk Steadfast[^.]*\.","",t) if k==0 else t
        x=re.sub(r"\b(And )?I'm (Wes Hart|Jonathon)\b","",x)
        cw=content(x)
        for name,tgt in (('cold open',cold),('first line after the slate',first)):
            sh=cw&content(tgt)
            if len(sh)>=limit: out.append((t,name,sorted(sh)))
    return out
