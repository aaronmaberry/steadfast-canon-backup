"""Write the intro and slate (SHOW-BIBLE section 5) into a script.
usage: python3 _build/intro.py scripts/E0xx-*.md ...
Idempotent: replaces an existing [CHAPTER: Intro] block or the old [CHAPTER: Slate] block.
Open system v3 (2026-10-03): each episode's own intro comes from _build/intros_data.py
(lint it with _build/intro_lint.py). An episode with no entry there falls back to the
legacy rotating variants A/B/C and prints a WARN, so new scripts never break."""
import re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
try:
    from intros_data import I as UNIQUE
except Exception:
    UNIQUE={}
SP={'W':'WES','J':'JONATHON','WES':'WES','JONATHON':'JONATHON'}
ONES="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS="_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
ORD={'one':'first','two':'second','three':'third','five':'fifth','eight':'eighth','nine':'ninth','twelve':'twelfth'}
def words(n):
    if n<20: return ONES[n]
    if n<100: return TENS[n//10]+('' if n%10==0 else '-'+ONES[n%10])
    return ONES[n//100]+' hundred'+('' if n%100==0 else ' '+words(n%100))
def ordinal(n):
    w=words(n); parts=w.split('-'); last=parts[-1]
    if last in ORD: last=ORD[last]
    elif last.endswith('y'): last=last[:-1]+'ieth'
    else: last=last+'th'
    return '-'.join(parts[:-1]+[last])
DAYS={'Tue':'Tuesday','Fri':'Friday','Mon':'Monday','Wed':'Wednesday','Thu':'Thursday','Sat':'Saturday','Sun':'Sunday'}
MONTHS={'Jan':'January','Feb':'February','Mar':'March','Apr':'April','May':'May','Jun':'June','Jul':'July','Aug':'August','Sep':'September','Oct':'October','Nov':'November','Dec':'December'}
V={
'A':[('WES',"This is Walk Steadfast. I'm Wes Hart. Twenty-something years at tables with men, and I wrote a book about what I heard."),
     ('JONATHON',"And I'm Jonathon. Husband, dad of two, sales manager, still learning."),
     ('WES',"Twice a week we talk straight about following Jesus as a man. At home, at work, with your friends."),
     ('JONATHON',"Steadfast is the book, a video training for men, and this table. It's all at walksteadfast.com.")],
'B':[('JONATHON',"This is Walk Steadfast. I'm Jonathon. Husband, dad of two, sales manager, still learning."),
     ('WES',"And I'm Wes Hart. Twenty-something years at tables with men, and a book about what I heard."),
     ('JONATHON',"Twice a week we talk straight about following Jesus as a man. Your marriage, your kids, your work, your friends."),
     ('WES',"Steadfast is the book, a video training for men, and this table. It's all at walksteadfast.com.")],
'C':[('WES',"This is Walk Steadfast. I'm Wes Hart. I've sat at tables with men for twenty-something years, and I wrote a book about it."),
     ('JONATHON',"I'm Jonathon. Husband, dad of two, sales manager, and the younger man at this table."),
     ('WES',"Twice a week we talk straight about following Jesus on the ordinary days. At home, at work, with your friends."),
     ('JONATHON',"Steadfast is the book, a video training for men, and this show. It's all at walksteadfast.com.")],
}
def block(n,title,rel):
    if n in UNIQUE:
        var='U'
        lines=[(SP[w],t) for w,t in UNIQUE[n]]
    else:
        var='ABC'[(n-1)%3]
        print(f"WARN E{n:03d}: no entry in intros_data.py, legacy variant {var} used",file=sys.stderr)
        lines=list(V[var])
        if n==1:
            lines[2]=('WES',"Starting today, twice a week, we talk straight about following Jesus as a man. At home, at work, with your friends.")
    m=re.match(r'\s*(\w{3}) (\w{3}) (\d+), (\d{4})',rel)
    day,mon,d,y=m.groups()
    date=f"{DAYS[day]}, {MONTHS[mon]} {ordinal(int(d))}"
    if n==1: date+=", twenty twenty-seven"
    fn=title.startswith('Field Notes: ')
    a='WES' if lines[-1][0]=='JONATHON' else 'JONATHON'; b='JONATHON' if a=='WES' else 'WES'
    if fn:
        t=title[len('Field Notes: '):].replace(': ','. ')
        slate=[(a,f"Episode {words(n)}. {date}."),(b,f"Field Notes. {t}{'' if t.endswith(('?','!','.')) else '.'}")]
    else:
        slate=[(a,f"Episode {words(n)}."),(b,f"{date}."),(a,f"{title}{'' if title.endswith(('?','!','.')) else '.'}")]
    if var=='U':
        note=f"(Walk Steadfast open written for E{n:03d}{', launch' if n==1 else ''}. Same beats every week, new words. SHOW-BIBLE section 5.)"
        desc=f"Per-episode open{' (launch)' if n==1 else ''}, {lines[0][0].title()} leads (SHOW-BIBLE section 5, open system v3, text in _build/intros_data.py)"
    else:
        note=f"(Standard intro, variant {var}{', launch wording' if n==1 else ''}. SHOW-BIBLE section 5.)"
        desc=f"Standard intro, variant {var}{' (launch wording)' if n==1 else ''} (SHOW-BIBLE section 5)"
    out=['[CHAPTER: Intro]','[CAM: 2S]',note]
    seen=set()
    for who,txt in lines:
        out.append(f"{who}: {txt}")
        if who not in seen:
            seen.add(who); out.append('[LOWER THIRD: Wes Hart]' if who=='WES' else '[LOWER THIRD: Jonathon]')
    for who,txt in slate: out.append(f"{who}: {txt}")
    row=f"| Intro and slate | {desc}. Slate: "+' '.join(f'{w} "{t}"' for w,t in slate)+" |"
    return '\n'.join(out)+'\n',row,var
def apply(p):
    s=open(p).read()
    n=int(re.search(r'E(\d{3})',os.path.basename(p)).group(1))
    title=s.splitlines()[0].split(' · ',1)[1].strip()
    rel=re.search(r'^\| Release \|([^|]*)\|',s,re.M).group(1)
    blk,row,var=block(n,title,rel)
    head,rest=s.split('## Script',1)
    body,tail=rest.split('\n## Shorts',1)
    # header row
    head=re.sub(r'^\| (Slate|Intro and slate) \|.*\|$',row.replace('\\','\\\\'),head,count=1,flags=re.M)
    # remove old slate / intro chapters
    body=re.sub(r'\[CHAPTER: (Slate|Intro)\]\n(?:(?!\[CHAPTER: )[^\n]*\n)*?(?=\n|\[CHAPTER: )','',body)
    # remove standalone host lower thirds elsewhere
    body=re.sub(r'^\[LOWER THIRD: (Wes Hart|Jonathon)\]\n','',body,flags=re.M)
    # insert after cold open block (before the next chapter), else at top after first [CAM: WIDE]
    m=re.search(r'\[CHAPTER: Cold open\]\n(?:(?!\[CHAPTER: )[^\n]*\n)*',body)
    if m:
        seg=m.group(0); seg_s=seg.rstrip('\n')
        body=body[:m.start()]+seg_s+'\n\n'+blk+'\n'+body[m.end():].lstrip('\n')
    else:
        i=body.index('[CHAPTER: ')
        body=body[:i]+blk+'[STING 3s]\n\n'+body[i:]
    body=re.sub(r'\n{3,}','\n\n',body)
    open(p,'w').write(head+'## Script'+body+'\n## Shorts'+tail)
    return var
if __name__=='__main__':
    for p in sys.argv[1:]: print(os.path.basename(p)[:4],apply(p))
