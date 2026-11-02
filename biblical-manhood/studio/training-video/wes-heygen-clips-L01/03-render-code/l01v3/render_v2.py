#!/workspace/cvenv/bin/python
"""L01-P7-ASSEMBLED-v2 renderer. Output timeline = week-cut audio; everything is specified in src (approved-audio) time and
mapped with tmap. Helpers (text, panels, bubble chrome) imported from the v1 renderer (intro v12 helpers).
Usage: render_v2.py n0 n1 out.mp4 | --still out_t ..."""
import os,sys,json,subprocess,numpy as np,cv2
sys.path.insert(0,'/workspace/l01p6');sys.path.insert(0,'/workspace/l01v3/build')
import render_l01 as R
from render_l01 import fnt,text,paste,card,panel,mask,rows,T,still,logo,LBG,EO,EI,pr,wrap,BG,TX,AC,AC2,MU,M,WD,HT,FPS,PW,PH,PANEL_SRC,X0,hx
from tmap import s2o,o2s,OUT_END
from stab import path,matrix
from scipy.ndimage import gaussian_filter1d
E=json.load(open('/workspace/l01v3/build/edl_v2.json'));SH=E['shots'];IX={s['id']:s for s in SH};CUTS=E['cuts']
NOUT=int(round(OUT_END*FPS))
WES='/workspace/artifacts/training/lesson-plan-2026-10-26/L01-P5-2026-10-29/L01-P5-PATCHED-v2.mp4';WES_N=30852
K_STAB=0.6
# ---- Wes reader (uint8), shared with v1 bubble helper
class Reader:
    def __init__(s,n0):s.n=n0;s.p=subprocess.Popen(['ffmpeg','-v','error','-ss',f'{n0/FPS:.3f}','-i',WES,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE);s.f=None
    def get(s,n):
        if n>=WES_N:n=WES_N-1
        while s.f is None or s.n<=n:
            b=s.p.stdout.read(WD*HT*3)
            if len(b)<WD*HT*3:break
            s.f=np.frombuffer(b,np.uint8).reshape(HT,WD,3);s.n+=1
        return s.f
RD=[None]
def wes_u8(t):
    n=int(round(t*FPS))
    if RD[0] is None or RD[0].n-1>n or n-RD[0].n>400:RD[0]=Reader(n)
    return RD[0].get(n)
_wf={}
def wes(t):
    n=int(round(t*FPS))
    if n not in _wf:
        _wf.clear();_wf[n]=wes_u8(t).astype(np.float32)
    return _wf[n]
R.wes=wes
# ---- stabilization paths per Wes shot (face-locked partial lock k=0.6, tested 2026-11-02 on frames 6840-7340)
PATHS={}
for s in SH:
    if s['kind'] in('WES_FULL','SPLIT'):
        n0=int(s['t0x']*FPS)-30;n1=int(s['t1x']*FPS)+30;P,_=path(max(n0,0),min(n1,WES_N),K_STAB);PATHS[s['id']]=P
def stab_frame(sid,t,Z=1.0,anchor=(960,0)):
    n=int(round(t*FPS));P=PATHS.get(sid);F=wes_u8(t)
    if P is None or n not in P:
        if Z==1.0:return F.astype(np.float32)
        A=np.array([[Z,0,-Z*(anchor[0]-WD/Z/2)],[0,Z,-Z*anchor[1]]],np.float32)
    else:raw,sm=P[n];A=matrix(raw,sm,K_STAB,Z,anchor)
    return cv2.warpAffine(F,A,(WD,HT),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REPLICATE).astype(np.float32)
FRAMING=E['framing']
def framing_at(sid,t):
    for f in FRAMING:
        if f['shot']==sid and f['a']-0.01<=t<f['b']+0.01:return f['f']
    return ['A',1.12,0]
# ---- backdrop with slow drift (look plan glow top-left), static dither
PADX,PADY=120,80
def _bd():
    H2,W2=HT+2*PADY,WD+2*PADX;yy,xx=np.mgrid[0:H2,0:W2].astype(np.float32);xx-=PADX;yy-=PADY
    g=np.exp(-(((xx-250)/950)**2+((yy-120)/620)**2))*0.30+np.exp(-(((xx-1750)/700)**2+((yy-1050)/450)**2))*0.08
    return (BG*(1-g[...,None])+R.AC2*g[...,None]).astype(np.float32)
BDL=_bd();NZ=cv2.GaussianBlur(np.random.default_rng(11).normal(0,1,(HT,WD)).astype(np.float32),(0,0),0.8);NZ=(NZ/NZ.std()*2.6)[...,None]
def BDt(t):
    ox=int(PADX+PADX*0.8*np.sin(2*np.pi*t/47));oy=int(PADY+PADY*0.8*np.sin(2*np.pi*t/61+1))
    return BDL[oy:oy+HT,ox:ox+WD]+NZ
# ---- workbook inset (oblique, depth falloff) for the persistent list
def _inset():
    im=cv2.imread('/workspace/l01p6/boards/assets/workbook-open-textblur.png')[...,::-1].astype(np.float32)
    im=cv2.resize(im,(1120,630),interpolation=cv2.INTER_AREA)
    w,h=860,470;src=np.float32([[0,0],[1120,0],[1120,630],[0,630]]);dst=np.float32([[0,60],[w,0],[w,h],[0,h-45]])
    Mx=cv2.getPerspectiveTransform(src,dst);sharp=cv2.warpPerspective(im,Mx,(w,h));al=cv2.warpPerspective(np.ones((630,1120),np.float32),Mx,(w,h))
    blur=cv2.GaussianBlur(sharp,(0,0),7);g=np.clip(1-np.linspace(0,1,w,dtype=np.float32)*1.3,0,1)[None,:,None]**1.2
    out=sharp*(1-g)+blur*g;sh=np.clip(np.linspace(0.88,1.08,w,dtype=np.float32),0,1)[None,:,None];out*=sh
    return np.dstack([out,cv2.GaussianBlur(al,(0,0),0.7)*255])
INSET=[None]
def inset(fr,a,b,t):
    if INSET[0] is None:INSET[0]=_inset()
    pin=EO(pr(t,a,0.6));pout=EI(pr(t,b-0.5,0.5));al=pin*(1-pout)
    if al<=0:return
    im=INSET[0];sc=0.94+0.06*pin;h,w=im.shape[:2];im2=cv2.resize(im,(int(w*sc),int(h*sc)))
    sh=np.zeros((im2.shape[0]+60,im2.shape[1]+60,4),np.float32);sh[...,3]=cv2.GaussianBlur(np.pad(im2[...,3]*0.5,30),(0,0),18);paste(fr,sh,900-30+60*(1-pin)+40*pout,540-10,al)
    paste(fr,im2,900+60*(1-pin)+40*pout,540,al)
# ---- shot renderer (v1 + framing/stab + counter + inset + still push-in)
def render(sh,t,with_panel=True,full_override=None):
    k=sh['kind'];sp=sh['spec']
    if k=='WES_FULL':
        f=framing_at(sh['id'],t);return stab_frame(sh['id'],t,f[1],(960+f[2],0))
    if k=='LOGO_END':
        im,m=logo();fr=card(WD,HT,LBG[0]);t0=sh['t0x'];a=pr(t,t0+0.4,0.8)*(1-pr(t,t0+0.4+0.8+1.6,0.8))
        paste(fr,im,(WD-im.shape[1])//2,(HT-im.shape[0])//2,a,m);return fr
    fr=BDt(t).copy()
    if k=='TITLE_CARD':
        y=380;T(fr,text(sp['kicker'],26,'GeistMono-Medium.ttf',AC),M+60,y,sp['kat'][1],t)
        if 'lat' in sp:T(fr,text(sp['lat'][0],44,'Geist-Medium.ttf',MU),M+60,y+56+190,sp['lat'][1],t)
        at=sp['title'][1];T(fr,text(sp['title'][0],120,'Geist-SemiBold.ttf',TX),M+60,y+56,at,t)
        L=int(560*EO(pr(t,at+0.45,0.6)))
        if L>1:paste(fr,card(L,3,AC2),M+60,y+56+175,1.0)
        return fr
    if k=='SPLIT':
        y=M+40
        if 'lt' in sp:
            T(fr,text('YOUR TEACHER',24,'GeistMono-Medium.ttf',AC),X0,y,sp['lt'][1],t);T(fr,text(sp['lt'][0],72,'Geist-SemiBold.ttf',TX),X0,y+40,sp['lt'][1],t)
            L=int(300*EO(pr(t,sp['lt'][1]+0.4,0.5)))
            if L>1:paste(fr,card(L,2,AC2),X0,y+145,1.0)
            y+=190
        rows(fr,sp.get('rows',[]),t,X0,y,WD-X0-M,50,26,chips=sp.get('chips',False),big_first=sp.get('big_first',False),big_idx=sp.get('big_idx'))
        if with_panel:
            sx,sy,sw,sh_=PANEL_SRC;F=stab_frame(sh['id'],t);paste(fr,F[sy:sy+sh_,sx:sx+sw],27,27,1.0,mask(PW,PH,24))
        return fr
    full=k=='COVER_BOARD';MW=sp.get('maxw',1700 if full else 1180)
    if 'still' in sp:
        p=R.ASSET[sp['still']]
        z=1.04-0.04*EO(pr(t,sh['t0x'],1.6))
        im=still(p,680);im=cv2.resize(im,(int(680*z),int(im.shape[0]*z)));panel(fr,im,M+40-(im.shape[1]-680)//2,(HT-im.shape[0])//2,18)
        rows(fr,[(s_,at if at>sh['t0'] else sp['rows'][0][1]+2.5) for s_,at in sp['rows']],t,M+40+680+60,(HT-int(im.shape[0]/z))//2+20,1460-(M+40+680+60),40,26)
        return fr
    y=M+60
    if 'ref' in sp:
        T(fr,text(sp['ref'][0],28,'GeistMono-Medium.ttf',AC),M+60,y,sp['ref'][1],t);y+=70;hi_on=1.0
        if 'hi_at' in sp:hi_on=0.5+0.5*abs(np.cos(np.pi*pr(t,sp['hi_at'],1.2)))
        dimv=1.0 if 'side' not in sp else 1-0.35*pr(t,sp['side'][0][1]-0.05,0.4)
        hcol=AC*hi_on+TX*(1-hi_on) if 'hi' in sp else AC
        for s_,at in sp['verse']:
            im=text(s_,52,'Geist-Medium.ttf',TX*dimv+BG*(1-dimv),MW,1.25,hi=sp.get('hi'),hcol=hcol*dimv+BG*(1-dimv));T(fr,im,M+60,y,at,t);y+=im.shape[0]+22
        if 'side' in sp:
            y+=20;L=int(160*EO(pr(t,sp['side'][0][1],0.5)))
            if L>1:paste(fr,card(L,2,AC2),M+60,y,1.0)
            rows(fr,sp['side'],t,M+60,y+30,MW,42,18,dim=False)
        return fr
    if 'kicker' in sp:T(fr,text(sp['kicker'],26,'GeistMono-Medium.ttf',AC),M+60,y,sh['t0x']+0.3,t);y+=70
    if 'counter' in sp:
        N,at=sp['counter'];v=int(round(N*EO(pr(t,at,1.2))));T(fr,text(f'{v:02d}',230,'Geist-SemiBold.ttf',AC),M+50,y+40,at,t)
        rr=sp['rows'];T(fr,text(rr[0][0],62,'Geist-SemiBold.ttf',TX),M+60,y+330,rr[0][1],t)
        T(fr,text(rr[1][0],62,'Geist-Medium.ttf',MU),M+60,y+430,rr[1][1],t);return fr
    rr=sp.get('rows',[]);size=(62 if full else 56) if len(rr)<=3 else 50
    if full:y=max(y,(HT-sum(text(s_,int(size*1.45) if (sp.get('big_first') and i==0) or sp.get('big_idx')==i else size,'Geist-SemiBold.ttf',TX,MW).shape[0]+30 for i,(s_,_) in enumerate(rr)))//2)
    rows(fr,[(s_,max(at,sh['t0x']+0.25)) for s_,at in rr],t,M+60,y,MW,size,30,chips=sp.get('chips',False),big_first=sp.get('big_first',False),big_idx=sp.get('big_idx'))
    if 'inset' in sp:inset(fr,sp['inset'][1],sp['inset'][2],t)
    if sp.get('rule') and rr:
        L=int(420*EO(pr(t,rr[-1][1]+0.5,0.6)))
        if L>1:paste(fr,card(L,3,AC2),M+60,y+150,1.0)
    return fr
def shot_at(t):
    for s in SH:
        if s['t0x']<=t<s['t1x']:return s
    return SH[-1]
# ---- callouts (WES_FULL lower band), drawn above B-roll
def callouts(fr,sh,t):
    cs=sh['spec'].get('callouts')
    if sh['kind']!='WES_FULL' or not cs or t<cs[0][1]-0.4:return fr
    a=EO(pr(t,cs[0][1]-0.4,0.5))*(1-pr(t,sh['t1x']-0.45,0.35))
    g=np.clip((np.linspace(0,1,HT,dtype=np.float32)-0.62)/0.38,0,1)[:,None,None]**1.3*0.78*a;fr=fr*(1-g)+BG*g
    full=' '.join(c[0] for c in cs);f=fnt('Geist-SemiBold.ttf',50);lines=wrap(full,f,1600);x0=(WD-f.getlength(lines[0]))/2 if len(lines)==1 else None
    x=x0 if x0 is not None else M+60;y=905
    for s_,at in cs:
        im=text(s_,50,'Geist-SemiBold.ttf',TX,1700);T(fr,im,x,y,at,t,1-pr(t,sh['t1x']-0.45,0.35));x+=f.getlength(s_+' ')
    return fr
# ---- bubble runs + hide windows
BRUN=[]
for a,b in E['bubble_runs']:
    A,B=IX[a],IX[b];ci=[c for c in CUTS if c['b']==a];co=[c for c in CUTS if c['a']==b]
    t_in=(ci[0]['e'] if ci and ci[0]['type']!='hard' else A['t0x'])+0.35;t_out=co[0]['s'] if co and co[0]['type']!='hard' else B['t1x']
    BRUN.append((t_in,t_out))
def bubble_state(t):
    for a,b in BRUN:
        if a<=t<b:
            if t<b-0.45:e=EO(pr(t,a,0.7));return [pr(t,a,0.5),0.92+0.08*e,28*(1-e),pr(t,a+0.15,0.3)]
            p=EI(pr(t,b-0.45,0.45));return [1-p,1-0.04*p,12*p,1-p]
    return None
def hide_alpha(t):
    h=0.0
    for w in E['hide']:
        if w['a']-0.3<=t<=w['b']+0.3:h=max(h,min(pr(t,w['a']-0.3,0.3),1-pr(t,w['b'],0.3)))
    return h
# ---- B-roll (out-time), push-in alternating; even k: hard cut in + 0.16 s dissolve out; odd k: 0.2 s dissolve in + hard cut out
BR=E['broll']
for k,b in enumerate(BR):b['oa']=s2o(b['a']);b['ob']=s2o(b['b']);b['k']=k
class Clip:
    def __init__(s,path,n0):s.n=n0;s.p=subprocess.Popen(['ffmpeg','-v','error','-ss',f'{n0/FPS:.3f}','-i',path,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE);s.f=None;s.path=path
    def get(s,n):
        while s.f is None or s.n<=n:
            b=s.p.stdout.read(WD*HT*3)
            if len(b)<WD*HT*3:break
            s.f=np.frombuffer(b,np.uint8).reshape(HT,WD,3);s.n+=1
        return s.f
CL={}
def broll(fr,to):
    for b in BR:
        if b['oa']<=to<b['ob']:
            n=int((to-b['oa'])*FPS+1e-6)
            c=CL.get(b['k'])
            if c is None or c.n-1>n:c=CL[b['k']]=Clip(b['mezz'],n)
            F=c.get(n).astype(np.float32);L=b['ob']-b['oa'];p=(to-b['oa'])/L
            z=1.0+0.06*(p if b['k']%2==0 else 1-p)
            if z>1.001:
                cw,ch=int(WD/z),int(HT/z);x0=(WD-cw)//2+int((b['k']%3-1)*0.25*(WD-cw));y0=(HT-ch)//2
                F=cv2.resize(F[y0:y0+ch,x0:x0+cw],(WD,HT),interpolation=cv2.INTER_LINEAR)
            ain=1.0 if b['k']%2==0 else pr(to,b['oa'],0.2);aout=1-pr(to,b['ob']-0.16,0.16) if b['k']%2==0 else 1.0;a=ain*aout
            return fr*(1-a)+F*a
    return fr
OB=E['overlay_boards']
for o in OB:o['oa']=s2o(o['t0']);o['ob']=s2o(o['t1']);o['t0x']=o['t0'];o['t1x']=o['t1']
def overlay_boards(fr,to,ts):
    for o in OB:
        if o['oa']-0.3<=to<o['ob']+0.3:
            a=min(pr(to,o['oa']-0.3,0.3),1-pr(to,o['ob'],0.3))
            if a>0:fr=fr*(1-a)+render(o,ts)*a
    return fr
sm=lambda p:p*p*(3-2*p)
def morph(A,B,t,p):
    """shared-element reframe between WES_FULL (punched, stabilized) and SPLIT panel"""
    W_,S_=(A,B) if A['kind']=='WES_FULL' else (B,A);q=p if A['kind']=='WES_FULL' else 1-p;q=sm(q)
    f=framing_at(W_['id'],t);Z=f[1];ax=960+f[2]
    sid=W_['id'];F=stab_frame(sid,t)
    bg=render(S_,t,with_panel=False);base=BDt(t)*(1-q)+bg*q if q<1 else bg
    dx,dy,dw,dh=27*q,27*q,WD+(PW-WD)*q,HT+(PH-HT)*q
    sc=Z+(1-Z)*q;cx0,cy0=ax,HT/Z/2;cx1,cy1=PANEL_SRC[0]+PW/2,PANEL_SRC[1]+PH/2
    cx,cy=cx0+(cx1-cx0)*q,cy0+(cy1-cy0)*q;sw,sh_=dw/sc,dh/sc
    Mx=np.array([[sc,0,-sc*(cx-sw/2)],[0,sc,-sc*(cy-sh_/2)]],np.float32)
    w_,h_=int(round(dw)),int(round(dh));crop=cv2.warpAffine(F,Mx,(w_,h_),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REPLICATE)
    r=max(1,int(24*q));paste(base,crop,dx,dy,1.0,mask(w_,h_,r) if q>0.02 else None);return base
def frame_out(to):
    ts=o2s(to);sh=shot_at(ts);fr=None
    for c in CUTS:
        if c['type']=='hard' or not(c['s']<=ts<c['e']):continue
        p=(ts-c['s'])/(c['e']-c['s']);A,B=IX[c['a']],IX[c['b']]
        if c['type']=='dip':
            fr=render(sh,ts);bd=BDt(ts)
            if ts<c['empty'][0]:a=pr(ts,c['out'][0],c['out'][1]-c['out'][0]);fr=fr*(1-a)+bd*a
            elif ts<c['inn'][0]:fr=bd.copy()
            else:a=pr(ts,c['inn'][0],c['inn'][1]-c['inn'][0]);fr=bd*(1-a)+fr*a
        elif c['type']=='xfade':q=sm(p);fr=render(A,ts)*(1-q)+render(B,ts)*q
        elif c['type']=='push':
            q=EO(p) if p<1 else 1.0;off=int(round(WD*q));fa=render(A,ts);fb=render(B,ts);fr=np.empty_like(fa)
            fr[:,:WD-off]=fa[:,off:];fr[:,WD-off:]=fb[:,:off]
            if 0.15<p<0.85:fr=cv2.blur(fr,(9,1))
        elif c['type']=='morph':fr=morph(A,B,ts,p)
        break
    if fr is None:fr=render(sh,ts)
    st=bubble_state(ts)
    if st:
        h=hide_alpha(ts);st[0]*=1-h
        if st[0]>0:R.bubble(fr,ts,*st)
    fr=overlay_boards(fr,to,ts)
    fr=broll(fr,to)
    fr=callouts(fr,sh,ts)
    return fr
if __name__=='__main__':
    a=sys.argv[1:]
    if a[0]=='--still':
        os.makedirs('/workspace/l01v3/stills',exist_ok=True)
        for x in a[1:]:
            t=float(x);RD[0]=None;CL.clear();cv2.imwrite(f'/workspace/l01v3/stills/s_{t:07.2f}.jpg',np.clip(frame_out(t),0,255).astype(np.uint8)[...,::-1],[cv2.IMWRITE_JPEG_QUALITY,85])
        sys.exit()
    n0,n1,out=int(a[0]),int(a[1]),a[2];n1=min(n1,NOUT)
    enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r',str(FPS),'-i','-','-c:v','libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p','-threads','2',out+'.part.mp4'],stdin=subprocess.PIPE)
    for n in range(n0,n1):
        enc.stdin.write(np.clip(frame_out(n/FPS)+0.5,0,255).astype(np.uint8).tobytes())
        if n%250==0:print(n,flush=True)
    enc.stdin.close();enc.wait();os.rename(out+'.part.mp4',out)
