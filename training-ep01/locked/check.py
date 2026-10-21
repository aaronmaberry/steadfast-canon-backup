import sys,re
for f in sys.argv[1:]:
    secs=[];bad=[];words=0;cur=None;tags=0;hands=0;chk=0
    for n,l in enumerate(open(f).read().split('\n'),1):
        l=l.strip()
        if not l: continue
        if l.startswith('# SECTION'): cur=[l,0]; secs.append(cur); continue
        if l.startswith('#'): continue  # [CUT SCREEN]/board marker lines (video only, not spoken)
        if '|' not in l: bad.append(f'L{n} no pause'); continue
        t,p=l.rsplit('|',1)
        if p not in('ROOM_HANDS','ROOM_CHUCKLE'):
            try: float(p)
            except: bad.append(f'L{n} bad pause {p}')
        hands+=p=='ROOM_HANDS'; chk+=p=='ROOM_CHUCKLE'
        if cur: cur[1]+=len(t)+1
        tags+=len(re.findall(r'\[[a-z ]+\]',t))
        words+=len(re.sub(r'\[[a-z ]+\]','',t).split())
        low=t.lower()
        for b in [r'\bweeks?\b',r'\btonight\b',r'\bsession (one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b',r'\blesson \w+\b',r'twenty-?four',r'\[beat\]',r'\[laughs',r'applau',r'\bcoffee crew']:
            if re.search(b,low): bad.append(f'L{n} banned {b}: {t[:60]}')
    big=[(s[0][11:40],s[1]) for s in secs if s[1]>2000 or s[1]<1200]
    print(f'{f.split("/")[-1]}: {words} words, {len(secs)} sections, tags {tags}, hands {hands}, chuckles {chk}, out-of-range sections {big}')
    for b in bad[:15]: print('   ',b)
