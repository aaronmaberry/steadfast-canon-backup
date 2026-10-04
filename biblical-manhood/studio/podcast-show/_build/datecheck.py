"""Date check for Walk Steadfast opens and slates (Aaron, 2026-10-03: the open and slate say the episode number and title only, never a date).
Used by intro_lint.py and lint.sh. Changes nothing.
usage: python3 _build/datecheck.py [--cold]   (all opens; --cold also lists cold-open dates for review)
       python3 _build/datecheck.py --file scripts/E0xx-*.md   (one script's open and slate)
A date here is a calendar date or a year, spoken or written:
  - a month with a day ("January fifth", "Jan 5", "the fifth of January", "Fourth of July")
  - a weekday with a day ("Tuesday, the fifth", "Saturday the thirteenth"), or "on the thirteenth" ending a phrase
  - a weekday followed by a month ("Tuesday, January")
  - a year ("2027", "twenty twenty-seven", "two thousand twenty-seven")
  - a numeric date ("1/5", "01-05-2027")
Plain weekday names ("Friday we report"), a month on its own ("since January"), holiday names ("Good Friday")
and ordinals that count things ("the first garden", "The First Check") are not dates.
ALLOW holds (episode, text) pairs reviewed by hand: a past year inside a host fact, not a date for the episode."""
ALLOW={(4,'2000'),(65,'2000'),(77,'2019')}   # reviewed 2026-10-03: "married since 2000" (E004, E065), "In 2019 I lost a title" (E077)
import re
MON=r"(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept?|Oct|Nov|Dec)\.?"
DAY=r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
ONES="first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth thirtieth".split()
ORDW=r"(?i:(?:twenty|thirty)[- ](?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth)|"+"|".join(ONES)+r")"
NUMD=r"(?:[0-3]?\d(?:st|nd|rd|th)?)"
ORD=rf"(?:{ORDW}|{NUMD})"
PATS=[
 ('month and day', rf"\b{MON},? (?:the )?{ORD}\b"),
 ('day of month', rf"\b(?:the )?{ORD} of {MON}\b"),
 ('weekday and day', rf"\b{DAY},? the {ORD}\b"),
 ('weekday and month', rf"\b{DAY},? {MON}\b"),
 ('ordinal day', rf"\b(?:on|by|until|till|before|after|since) the {ORD}\b(?!\s+[A-Za-z])"),
 ('year', r"\b(?:19|20)\d\d\b|\btwenty (?:twenty|thirty)(?:[- ][a-z]+)?\b|\btwo thousand(?: and)?[- ](?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)\b"),
 ('numeric date', r"\b\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?\b"),
]
RX=[(k,re.compile(p,re.I if k in ('year','numeric date','ordinal day') else 0)) for k,p in PATS]
def find(text,n=None):
    """returns [(kind, matched text)] for every date in text (episode n's reviewed ALLOW pairs skipped)"""
    out=[]
    for k,rx in RX:
        for m in rx.finditer(text):
            if (n,m.group(0)) not in ALLOW: out.append((k,m.group(0)))
    return out
def intro_block(path):
    """spoken lines of the [CHAPTER: Intro] block (open and slate) plus the 'Intro and slate' header row"""
    s=open(path).read(); lines=[]
    m=re.search(r'^\| (?:Intro and slate|Slate) \|(.*)\|$',s,re.M)
    if m: lines.append(('header row',m.group(1)))
    blk=re.search(r'\[CHAPTER: Intro\]\n((?:(?!\[CHAPTER: )[^\n]*\n)*)',s)
    if blk:
        for l in blk.group(1).splitlines():
            mm=re.match(r'(WES|JONATHON): (.*)',l)
            if mm: lines.append((mm.group(1),mm.group(2)))
    return lines
def cold_block(path):
    s=open(path).read(); out=[]
    blk=re.search(r'\[CHAPTER: Cold open\]\n((?:(?!\[CHAPTER: )[^\n]*\n)*)',s)
    if blk:
        for l in blk.group(1).splitlines():
            mm=re.match(r'(WES|JONATHON): (.*)',l)
            if mm: out.append((mm.group(1),mm.group(2)))
    return out
if __name__=='__main__':
    import sys,glob,os
    root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
    if sys.argv[1:2]==['--file']:   # lint.sh: one script, prints one line per date found in its open or slate
        for p in sys.argv[2:]:
            n=int(re.search(r'E(\d{3})',os.path.basename(p)).group(1))
            for w,t in intro_block(p):
                for k,x in find(t,n): print(f"{k} '{x}' in {w}")
        sys.exit(0)
    from intros_data import I
    for n in sorted(I):
        for w,t in I[n]:
            for k,x in find(t,n): print(f"intros_data E{n:03d} {k}: '{x}' in {w}: {t}")
    for p in sorted(glob.glob(os.path.join(root,'scripts','E*.md'))):
        n=int(os.path.basename(p)[1:4])
        for w,t in intro_block(p):
            for k,x in find(t,n): print(f"{os.path.basename(p)[:4]} intro {k}: '{x}' in {w}: {t[:120]}")
        if '--cold' in sys.argv:   # cold opens are story clips, outside the rule. Shown for review only.
            for w,t in cold_block(p):
                for k,x in find(t,n): print(f"{os.path.basename(p)[:4]} cold open (info) {k}: '{x}' in {w}: {t[:120]}")
