import re,sys
# estimate chapter start times: Wes 145 wpm, Jonathon 170 wpm, 0.45 s gap per line,
# [beat] .6, [pause 1s] 1, [pause 2s] 2, [BREATHER 3s] 3, [STING 3s] 3, B-roll none extra
def times(path):
    t=0.0;out=[]
    for line in open(path):
        line=line.rstrip('\n')
        m=re.match(r'\[CHAPTER: (.*)\]',line)
        if m: out.append((t,m.group(1))); continue
        if line.startswith('[BREATHER'): t+=3
        if line.startswith('[STING'): t+=3
        m=re.match(r'(WES|JONATHON): (.*)',line)
        if m:
            txt=re.sub(r'\([^)]*\)|\[[^]]*\]','',m.group(2))
            w=len(txt.split()); rate=145 if m.group(1)=='WES' else 170
            t+=w/rate*60+0.45
            t+=0.6*m.group(2).count('[beat]')
        elif line.startswith('(') and 'laugh' in line: t+=1.2
        if line.strip()=='[beat]': t+=0.6
        if line.strip()=='[pause 1s]': t+=1
        if line.strip()=='[pause 2s]': t+=2
    return out,t
def fmt(s): s=int(round(s)); return f"{s//60:02d}:{s%60:02d}" if s<3600 else f"{s//3600}:{(s%3600)//60:02d}:{s%60:02d}"
if __name__=='__main__':
    out,t=times(sys.argv[1])
    for a,b in out: print(fmt(a),b)
    print("TOTAL",fmt(t))
