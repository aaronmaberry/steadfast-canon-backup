import numpy as np, subprocess, json, sys, re, difflib, wave
SR=44100
def load(p):
    raw=subprocess.run(["ffmpeg","-loglevel","error","-i",p,"-f","f32le","-ac","1","-ar",str(SR),"-"],capture_output=True).stdout
    return np.frombuffer(raw,np.float32).copy()
def save(p,y):
    w=wave.open(p,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes());w.close()
norm=lambda w: re.sub(r"[^a-z0-9']","",w.lower().replace("’","'"))
inp, timing, out, room = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
x=load(inp)
if len(sys.argv)>6:
    sc=float(sys.argv[6]); W=[(w[0],w[1]*sc,w[2]*sc) for w in json.load(open(sys.argv[5]))]
else:
    from faster_whisper import WhisperModel
    m=WhisperModel("medium.en",device="cpu",compute_type="int8")
    segs,_=m.transcribe(inp,word_timestamps=True,beam_size=5,condition_on_previous_text=False)
    W=[(norm(w.word),w.start,w.end) for s in segs for w in s.words if norm(w.word)]
json.dump(W,open(out+'.words.json','w'))
lines=[l.rsplit('|',1) for l in open(timing).read().strip().split('\n')]
T=[];owner=[]
for i,(t,p) in enumerate(lines):
    for w in t.split():
        if norm(w): T.append(norm(w)); owner.append(i)
sm=difflib.SequenceMatcher(None,T,[w[0] for w in W],autojunk=False)
t2w={}
for a,b,n in sm.get_matching_blocks():
    for k in range(n): t2w[a+k]=b+k
print("matched %d/%d script words, whisper %d"%(len(t2w),len(T),len(W)))
# first/last whisper idx per line
first={};last={}
for ti,li in enumerate(owner):
    if ti in t2w:
        first.setdefault(li,t2w[ti]); last[li]=t2w[ti]
hop=int(SR*0.01); n=len(x)//hop
db=20*np.log10(np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2)+1e-12) for i in range(n)]))
thr=np.percentile(db,90)-45
cuts=[]  # (gap_start_sample, gap_end_sample, target or tag)
for i in range(len(lines)-1):
    if i not in last or i+1 not in first:
        print("WARN unmatched line",i,lines[i][0]); continue
    e=W[last[i]][2]; s=W[first[i+1]][1]
    lo=int(max(e-0.12,0)*100); hi=int((s+0.12)*100)
    if hi<=lo: hi=lo+1
    q=db[lo:hi]<thr
    # longest quiet run
    best=(0,lo,lo);j=0
    while j<len(q):
        if q[j]:
            k=j
            while k<len(q) and q[k]: k+=1
            if k-j>best[0]: best=(k-j,lo+j,lo+k)
            j=k
        else: j+=1
    if best[0]<3:
        mn=lo+int(np.argmin(db[lo:hi])); best=(1,mn,mn+1)
    ga,gb=best[1],best[2]
    if best[0]>=3:
        while ga>0 and db[ga-1]<thr: ga-=1
        while gb<n and db[gb]<thr: gb+=1
    cuts.append((ga*hop,gb*hop,lines[i][1],lines[i][0]))
ctrl=[];parts=[np.zeros(int(SR*0.6),np.float32)]; pos=0; events=[]; t_out=0.6
# trim leading silence
lead=np.where(db>thr)[0]; pos=max(lead[0]-5,0)*hop; endp=min(lead[-1]+30,n)*hop
def emit(y):
    global t_out
    parts.append(y); t_out+=len(y)/SR
for a,b,tag,txt in cuts:
    emit(x[pos:a])
    G=(b-a)/SR
    ctrl.append(t_out)
    if tag.startswith('ROOM'):
        target=3.0 if tag=='ROOM_HANDS' else 1.7
        events.append((tag,t_out))
    else: target=float(tag)
    gap=x[a:b]
    if tag.startswith('ROOM') or (G>=0.10 and target>=0.5) or (G>=0.10 and G>target+0.3):
        head=min(int(SR*0.15),len(gap)); tail=min(int(SR*0.30),len(gap)-head)
        fill=int(SR*target)-head-tail
        h=gap[:head].copy(); tl=gap[len(gap)-tail:].copy()
        f=int(SR*0.012)
        if len(h)>f: h[-f:]*=np.linspace(1,0,f)
        if len(tl)>f: tl[:f]*=np.linspace(0,1,f)
        emit(h); emit(np.zeros(max(fill,0),np.float32)); emit(tl)
    else:
        emit(gap)  # connected speech or small gap: leave the model's own flow
    pos=b
emit(x[pos:endp]); emit(np.zeros(int(SR*0.8),np.float32))
y=np.concatenate(parts); save(out,y)
json.dump(events,open(out+'.events.json','w'));json.dump(ctrl,open(out+'.ctrl.json','w'))
print("dur %.1f"%(len(y)/SR), events)
