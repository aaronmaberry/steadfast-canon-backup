"""v3 week cuts on top of the v2 work copy (decoded float, v2-out timeline). Sample-accurate trims at phrase ends,
short fade on the kept side, room tone (the file's own pause floor) where a pause must be lengthened.
Removed length rounded to whole video frames (0.04 s) so the picture map stays frame-exact."""
import json,sys,numpy as np
sys.path.insert(0,'/workspace/l01v2/build');from tmap import s2o,o2s
sr=48000;x=np.fromfile('wc.f32',np.float32).astype(np.float64)
db=lambda s:20*np.log10(np.sqrt(np.mean(s**2))+1e-12)
def quiet(t,w=0.01):return db(x[int(t*sr)-int(w*sr/2):int(t*sr)+int(w*sr/2)])<-85
# label, a (v2-out s, end of kept speech), fade-out ms, b search window in src, target pause after join (s), text
C=[('A',36.946,6,(37.70,38.30),None,'this week.'),
   ('B',193.365,25,(198.36,198.62),0.30,'this week,'),
   ('C',None,0,None,None,'That weekend retreat where you came home feeling like a new man.'),
   ('D',622.565,18,(628.04,628.12),0.24,'for a week,')]
cuts=[]
for lab,a,fo,bw,pause,txt in C:
    if lab=='C':   # whole sentence, pause to pause: keep the original 'job.'->'That' pause length
        g0e,g0s=s2o(263.44),s2o(264.02);g1e,g1s=s2o(267.44),s2o(268.06)
        a=g0e+0.29;keep=(g0s-g0e)
        # b so that pause after join = keep, L multiple of 0.04
        b=g1s-(keep-(a-g0e));L=round((b-a)/0.04)*0.04;b=a+L
        assert quiet(a) and quiet(b),(lab,a,b);fill=0.0
    else:
        b0,b1=s2o(bw[0]),s2o(bw[1])
        qs=[t for t in np.arange(b0,b1,0.001) if quiet(t)]
        assert qs,lab
        # next speech onset after the quiet run
        t=qs[-1]
        while quiet(t):t+=0.001
        ns=t
        if pause is None:
            b=qs[0]+0.02;fill=0.0
        else:
            b=qs[0]+0.01;fill=max(0.0,pause-(ns-b)-(fo/1000))
        L=b-a-fill;Lr=round(L/0.04)*0.04;fill+=L-Lr  # absorb rounding into fill (room tone)
        if fill<0:b-=fill;fill=0.0
    cuts.append(dict(label=lab,text=txt,a_v2out=round(a,6),b_v2out=round(b,6),fade_ms=fo,fill_s=round(fill,6),removed_s=round(b-a-fill,6)))
# room tone source: a long quiet run (from cut C's removed pause)
rt0=int(s2o(264.75)*sr) if False else None
rt=x[int((cuts[2]['a_v2out']+0.05)*sr):int((cuts[2]['a_v2out']+0.05)*sr)+int(0.25*sr)]
qa=[c for c in cuts]
out=[];p=0
for c in cuts:
    ia,ib=int(round(c['a_v2out']*sr)),int(round(c['b_v2out']*sr));fo=int(c['fade_ms']*sr/1000)
    seg=x[p:ia].copy()
    if fo:seg[-fo:]*=np.cos(np.linspace(0,np.pi/2,fo))**2
    out.append(seg)
    nf=int(round(c['fill_s']*sr))
    if nf:
        f=np.resize(rt,nf).copy();k=min(240,nf//2);f[:k]*=np.linspace(0,1,k);f[-k:]*=np.linspace(1,0,k)
        out.append(f)
    fi=240;nxt=x[ib:ib+fi].copy()*np.linspace(0,1,fi);out.append(nxt);p=ib+fi
out.append(x[p:]);y=np.concatenate(out)
y.astype(np.float32).tofile('v3.f32')
# src-time cut list (for tmap v3): v2 cuts + new ones. new cut in src = (o2s(a), o2s(a)+removed)
AC=json.load(open('/workspace/l01v2/audio_cuts.json'))['cuts']
src=[dict(a=c['a'],b=c['b'],L=c['b']-c['a'],text=c['text'],v='v2') for c in AC]
for c in cuts:
    sa=o2s(c['a_v2out']);src.append(dict(a=round(sa,6),b=round(sa+c['removed_s'],6),L=c['removed_s'],text=c['text'],v='v3'))
src.sort(key=lambda d:d['a'])
json.dump(dict(base='/workspace/l01v2/L01-v2-weekcut-minus26-LUFS.mp3',cuts_v3=cuts,src_cuts=src,out_len=len(y)/sr),open('audio_cuts_v3.json','w'),indent=1)
for c in cuts:print(c)
print('len',len(y)/sr,'removed',sum(c['removed_s'] for c in cuts))
