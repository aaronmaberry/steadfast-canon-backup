import re,sys
f=sys.argv[1]
secs=[];cur=None
for l in open(f).read().split('\n'):
    l=l.strip()
    if not l: continue
    if l.startswith('# SECTION'): cur=[l[11:],[]]; secs.append(cur); continue
    t,p=l.rsplit('|',1); cur[1].append((t,p))
alltext=' '.join(t for s in secs for t,_ in s[1])
low=alltext.lower()
def c(rx): return len(re.findall(rx,low))
print('words',len(re.sub(r'\[[a-z ]+\]','',alltext).split()))
print('uh',c(r'\buh\b'),'um',c(r'\bum\b'))
print('restart dash',alltext.count('—'),'you know',c(r'\byou know\b'),'I mean',c(r'\bi mean\b'))
print('tags',re.findall(r'\[[a-z ]+\]',alltext),'quietly',c(r'\[quietly'))
print('tagq', c(r'right\?'), c(r'fair\?'), c(r'with me\?'))
dm=['now','so','look','okay','listen','well','here\'s the thing','stay with me']
starts=[t.lower().lstrip('[warmly] ').lstrip('[dry] ') for s in secs for t,_ in s[1]]
for d in dm:
    n=sum(1 for t in starts if re.match(re.escape(d)+r'\b[,.]',t) or (d in('stay with me',"here's the thing") and t.startswith(d)))
    print(' marker',d,n)
for w in ['week','tonight','session','lesson','applau','maps','north','diner','tailgate','manual','hum']:
    n=c(r'\b'+w)
    if n: print('  WORD',w,n)
# uh paragraph check
for title,lines in secs:
    para=[];paras=[]
    for t,p in lines:
        para.append(t); v=3 if p=='ROOM_HANDS' else 1.7 if p=='ROOM_CHUCKLE' else float(p)
        if v>=1.0: paras.append(para); para=[]
    if para: paras.append(para)
    for pa in paras:
        n=sum(len(re.findall(r'\b(uh|um)\b',t.lower())) for t in pa)
        if n>1: print('  TWO UH in para',title,pa)
print('verses:')
for v in ['Then we will no longer be infants, tossed back and forth by the waves, and blown here and there by every wind of teaching and by the cunning and craftiness of people in their deceitful scheming.',
 'He answered, I heard you in the garden, and I was afraid because I was naked; so I hid.',
 'So God created mankind in his own image, in the image of God he created them; male and female he created them.']:
    print(' ',v[:30], v in alltext)
refs=re.findall(r'(?:Genesis|Exodus|Ephesians|Matthew|Luke|John|Romans|Corinthians|Proverbs|Psalm|James|Hebrews|Peter|Galatians|Philippians|Colossians|Timothy|Deuteronomy|Joshua|Isaiah)[a-z]* [a-z-]+, verse [a-z-]+',alltext)
print('refs',refs)
