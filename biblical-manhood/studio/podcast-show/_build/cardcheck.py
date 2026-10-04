import re,glob,subprocess,sys,json,os
cache_p='/workspace/tmp/niv_cache.json'
cache=json.load(open(cache_p)) if os.path.exists(cache_p) else {}
def niv(ref):
    if ref not in cache:
        out=subprocess.run(['bash','/workspace/tmp/niv.sh',ref],capture_output=True,text=True).stdout.strip()
        cache[ref]=out
    return cache[ref]
def norm(t): 
    t=t.replace('\u201c','"').replace('\u201d','"').replace('\u2018',"'").replace('\u2019',"'")
    return re.sub(r'\s+',' ',t).strip()
files=sys.argv[1:] or sorted(glob.glob('scripts/E0*.md'))
for p in files:
    L=open(p).read().split('\n')
    for i,l in enumerate(L):
        m=re.match(r'\[CARD: (.+?)\]',l)
        if not m: continue
        ref=m.group(1)
        # next speaker line
        j=i+1
        while j<len(L) and not re.match(r'(WES|JONATHON): ',L[j]): j+=1
        spoken=L[j].split(': ',1)[1]
        q=re.findall(r'"(.*?)"(?=\s*$|\s*\()',spoken) or re.findall(r'"(.*)"',spoken)
        q=q[0] if q else spoken
        n=norm(niv(ref)).lstrip('> ').strip()
        qn=q.rstrip('.').rstrip(' ').rstrip('.')
        if norm(q)==n: continue
        # tolerance: LORD case
        if norm(q).lower()==n.lower(): continue
        print(f"{p[8:12]} {ref}\n  SCRIPT: {q}\n  NIV:    {n}")
json.dump(cache,open(cache_p,'w'))
