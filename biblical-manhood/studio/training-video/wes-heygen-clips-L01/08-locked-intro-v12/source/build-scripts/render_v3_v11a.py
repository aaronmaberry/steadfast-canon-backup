#!/usr/bin/env python3
"""INTRO v3 renderer (DIRECTOR-NOTES-v3). Plan = plan_calm cues (swappable audio via AUDIO_WORDS/AUDIO_LINES), Wes = WES env.
Usage: render_v3.py t0 t1 out.mp4 | --still t ..."""
import os,sys,numpy as np,cv2
os.environ.setdefault('PLAN','plan_calm');HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import render_v2 as R, plan_calm as P
sys.path.insert(0,HERE+'/../v3qa');import demask as DM
WD,HT,FPS=1920,1080,25;M=96;ROOT=HERE+'/..'
TX,MU,AC,SU,BG=R.TX,R.MU,R.AC,R.SU,R.BG
hx=R.hx;I=P.I;BAN=P.BAN;s=P.s;cue=P.cue;Bk=P.B
# ---- easing (director's three)
def bez(x1,y1,x2,y2):
    ts=np.linspace(0,1,2001);bx=3*(1-ts)**2*ts*x1+3*(1-ts)*ts**2*x2+ts**3;by=3*(1-ts)**2*ts*y1+3*(1-ts)*ts**2*y2+ts**3
    return lambda p:float(np.interp(min(max(p,0),1),bx,by))
EO=bez(0.22,1,0.36,1);EIO=bez(0.65,0,0.35,1);EI=bez(0.4,0,1,1)
pr=lambda t,a,d:min(max((t-a)/d,0),1)
# ---- timeline (re-derived from words JSON every run)
T_A,T_B=0.0,Bk('I08');T_C=Bk('I13');T_D1=Bk('I17');T_D2=Bk('I19');T_E=Bk('I21');T_F=Bk('I23');T_G=Bk('I25');T_H=Bk('I28');T_I=Bk('I31');T_J=Bk('I34')
END=P.END;TOTAL=P.TOTAL
BUB=[(s('I13')-0.1,T_D1-0.45),(T_D2+0.03,T_F),(T_G+0.26,T_H-0.45),  # v11: bubbles 1/3 finish exiting by the C->D / G->H cut (sequential, no overlap with full Wes)
     (T_I+0.1,T_J)]  # v4b: plain exit/entrance at G->H and H->I (morphs retired: they covered text)  # bubble 3 ends in bubble->full, 4 starts with full->bubble
# ---- Wes source, cleaned (sign mask), padded headroom
PAD=80;_wc={}
def wes_clean(t):
    n=int(round(t*FPS))
    if n not in _wc:
        _wc.clear();f=R.vid('W',P.WES,t,t,WD,HT,'cover',rel=False).astype(np.float32)
        if os.environ.get('MASK')=='1':f=DM.clean(f,n)
        if os.environ.get('BGPATCH','1')=='1':import bg_patch_v4 as BP;f=BP.apply(f)   # legacy per-frame matte (v3 only); v4 render is sign-free at source
        f=R.chair_crush(f).astype(np.float32)
        _wc[n]=np.vstack([np.repeat(f[:1],PAD,0),f])
    return _wc[n]
wes_full=lambda t:wes_clean(t)[PAD:]
OV=tuple(int(v) for v in os.environ.get('OV','1508,608,340,400').split(','));SRC_OV=tuple(int(v) for v in os.environ.get('SRC_OV','528,0,850,1000').split(','))   # eye-mid 953,319 -> 50% / 36%; head 640px -> 64% of oval
lerp=lambda a,b,k:tuple(x+(y-x)*k for x,y in zip(a,b))
_em={}
def ell(w,h,grow=0.0):
    k=(w,h,round(grow,3))
    if k not in _em:
        if grow<=0:
            m=np.zeros((h*2,w*2),np.float32);cv2.ellipse(m,(w,h),(w-2,h-2),0,0,360,1,-1,cv2.LINE_AA);_em[k]=cv2.resize(m,(w,h),interpolation=cv2.INTER_AREA)
        else:  # superellipse n: 2 -> 14 (oval -> soft rectangle)
            n=2+12*grow/0.45;yy,xx=np.mgrid[0:h,0:w].astype(np.float32);u=np.abs((xx+0.5-w/2)/(w/2))**n+np.abs((yy+0.5-h/2)/(h/2))**n
            _em[k]=np.clip((1-u)*min(w,h)/(2*n)+0.5,0,1)
        if len(_em)>40:_em.pop(next(iter(_em)))
    return _em[k]
def put(fr,img,x,y,m):
    h,w=img.shape[:2];x0,y0=max(x,0),max(y,0);x1,y1=min(x+w,WD),min(y+h,HT)
    if x1<=x0 or y1<=y0:return
    a=m[y0-y:y1-y,x0-x:x1-x,None];d=fr[y0:y1,x0:x1];d[:]=d*(1-a)+img[y0-y:y1-y,x0-x:x1-x]*a
def wes_window(fr,t,src,dst,m):
    sx,sy,sw,sh=src;X,Y,Wd,Hd=[int(round(v)) for v in dst];F=wes_clean(t)
    crop=F[int(sy)+PAD:int(sy+sh)+PAD,int(sx):int(sx+sw)]
    put(fr,cv2.resize(crop,(Wd,Hd),interpolation=cv2.INTER_AREA),X,Y,m(Wd,Hd))
# bubble chrome (cached at k=0)
def _chrome():
    w,h=OV[2],OV[3];m=ell(w,h);er3=cv2.erode(m,np.ones((7,7),np.uint8));er4=cv2.erode(m,np.ones((9,9),np.uint8))
    yy,xx=np.mgrid[0:h,0:w].astype(np.float32);g=np.clip((xx/w+yy/h)/2,0,1)[...,None]
    col=hx('#f4f4f5')*(1-g)+hx('#a1a1aa')*g;al=(0.95*(1-g)+0.55*g)[...,0]
    rim=np.clip(m-er3,0,1)*al;hair=np.clip(er3-er4,0,1)*0.6
    vg=1-0.11*np.clip((((xx-w/2)/(w/2))**2+((yy-h/2)/(h/2))**2-0.55)/0.45,0,1)
    P_=100;big=np.pad(m,P_)
    amb=np.roll(cv2.GaussianBlur(big,(0,0),32),24,0)*0.55;con=np.roll(cv2.GaussianBlur(big,(0,0),8),6,0)*0.5
    sh=1-(1-amb)*(1-con)
    chip=R.text('WES',16,'GeistMono-Medium.ttf',hx('#e4e4e7'))
    return dict(m=m,rim=rim,rcol=col,hair=hair,vg=vg[...,None],sh=sh,P=P_,chip=chip)
CH=None
def bubble(fr,t,a,scale=1.0,dy=0.0,chip=1.0):
    global CH
    if a<=0:return
    if CH is None:CH=_chrome()
    w,h=OV[2],OV[3];F=wes_clean(t);sx,sy,sw,sh=SRC_OV
    img=cv2.resize(F[sy+PAD:sy+sh+PAD,sx:sx+sw],(w,h),interpolation=cv2.INTER_AREA)*CH['vg']
    hh=CH['hair'][...,None];img=img*(1-hh)+hx('#07070a')*hh;rr=CH['rim'][...,None];img=img*(1-rr)+CH['rcol']*rr
    layer=np.zeros((h+200,w+200,3),np.float32);Pp=CH['P'];layer[Pp:Pp+h,Pp:Pp+w]=img
    m=np.pad(CH['m'],Pp);shd=CH['sh']
    if scale!=1.0:
        W2,H2=int((w+200)*scale),int((h+200)*scale);layer=cv2.resize(layer,(W2,H2));m=cv2.resize(m,(W2,H2));shd=cv2.resize(shd,(W2,H2))
    H2,W2=m.shape;ox=OV[0]+w+Pp-int((w+Pp)*scale)-Pp*0;x=int(OV[0]+w-(w+Pp)*scale);y=int(OV[1]+h-(h+Pp)*scale+dy)
    # shadow then image (origin bottom-right)
    x0,y0=max(x,0),max(y,0);x1,y1=min(x+W2,WD),min(y+H2,HT)
    d=fr[y0:y1,x0:x1];sa=shd[y0-y:y1-y,x0-x:x1-x,None]*a;d*=1-sa
    ma=m[y0-y:y1-y,x0-x:x1-x,None]*a;d[:]=d*(1-ma)+layer[y0-y:y1-y,x0-x:x1-x]*ma
    if chip>0 and scale>0.99:
        c=CH['chip'];cw,chh=c.shape[1]+28,30;px,py=OV[0]+w//2-cw//2,int(OV[1]+h-16+dy)
        R.paste(fr,R.card(cw+2,chh+2,hx('#71717a')),px-1,py-1,a*chip,R.mask(cw+2,chh+2,16));R.paste(fr,R.card(cw,chh,hx('#07070a')),px,py,a*chip*0.9,R.mask(cw,chh,15))
        R.paste(fr,c,px+14,py+5,a*chip)
def bubble_state(t):
    for i,(a,b) in enumerate(BUB):
        if a<=t<b+0.45:
            if t<b:
                p=pr(t,a,0.5);e=EO(pr(t,a,0.7));return (p,0.92+0.08*e,28*(1-e),pr(t,a+0.15,0.3))
            p=EI(pr(t,b,0.45));return (1-p,1-0.04*p,12*p,1-p)
    return None
# ---- text helpers: 0.45 s fade + 14 px rise ease-out, 0.05 s before cue
def T(fr,s_,x,y,size,col,at,t,font='Geist-Medium.ttf',maxw=None,a=1.0,rise=True):
    im=R.text(s_,size,font,col,maxw);p=EO(pr(t,at-0.05,0.45))*a
    if p>0:R.paste(fr,im,x,y+(14*(1-EO(pr(t,at-0.05,0.45))) if rise else 0),p)
    return im.shape[0]
def rows(fr,rr,t,x,y,maxw,size=48,gap=26,idx=False,dimto=0.45,alldim=None):
    for i,(at,s_) in enumerate(rr):
        if t<at-0.05:break
        nxt=rr[i+1][0] if i+1<len(rr) else 1e9;d=1-(1-dimto)*pr(t,nxt-0.05,0.3)
        if alldim and t>=alldim[0]-0.05 and i<len(rr)-1:d=min(d,1-(1-alldim[1])*pr(t,alldim[0]-0.05,0.3))
        col=TX*d+BG*(1-d);xx=x
        if idx:T(fr,f'{i+1:02d}',x,y+size*0.18,size*0.6,AC*d+BG*(1-d),at,t,'GeistMono-Medium.ttf');xx=x+90
        h=T(fr,s_,xx,y,size,col,at,t,'Geist-SemiBold.ttf' if d>0.99 else 'Geist-Medium.ttf',maxw);y+=h+gap
    return y
_bd=R.backdrop(0.0)
def bd(t):return _bd+0  # static navy + static dither
# ---- stills: prescale once to 2x display (lanczos+light unsharp), never > native
_ps={}
def pres(p,w2):
    k=(p,w2)
    if k not in _ps:
        im=cv2.imread(p,cv2.IMREAD_COLOR)[...,::-1];ih,iw=im.shape[:2];w2=min(w2,iw);h2=int(ih*w2/iw)
        im=cv2.resize(im,(w2,h2),interpolation=cv2.INTER_LANCZOS4 if w2!=iw else cv2.INTER_NEAREST).astype(np.float32)
        if 'podcast' in p:   # v4b: source has dark-area noise (sd 3.3, only source of the approved still): light NLM denoise, no unsharp
            _ps[k]=cv2.fastNlMeansDenoisingColored(np.clip(im,0,255).astype(np.uint8)[...,::-1],None,4,4,7,21)[...,::-1].astype(np.float32)
        else:
            bl=cv2.GaussianBlur(im,(0,0),0.8);_ps[k]=np.clip(im+0.3*(im-bl),0,255)
    return _ps[k]
def show(p,w,scale=1.0):
    """display p at width w (<= native) * scale (<=1 unless native allows) via area downscale"""
    src=pres(p,2*w);ww=int(round(w*scale));hh=int(round(src.shape[0]*ww/src.shape[1]))
    return cv2.resize(src,(ww,hh),interpolation=cv2.INTER_AREA)
# ---- layouts
SQ_OUT,SQ_GAP=0.30,0.12
SEQ=('D','H')   # v11: section cuts done sequentially (outgoing fully gone, empty beat, then incoming)
PW,PH=912,1026;PANEL_SRC=(504,40,912,1026)
def split_bg(fr,t,stills,x0,ta):
    y=M+20;sw=WD-x0-M
    if stills:
        st=[q for q in stills if t>=q[0]];cur=st[-1] if st else stills[0];k=cur[0]
        def one(q,a):
            sc=1.0 if q is stills[0] else 1.0-0.04*(1-EO(pr(t,q[0],1.4)))   # 1.04->1.00 on a 2x prescale (shown downsampled)
            im=show(q[1],sw);
            if sc!=1.0:
                big=show(q[1],sw,1.04);z=sc/1.04;cut=cv2.resize(big,(int(big.shape[1]*z),int(big.shape[0]*z)),interpolation=cv2.INTER_AREA);hh,ww=im.shape[:2];oy,ox=(cut.shape[0]-hh)//2,(cut.shape[1]-ww)//2
                im=cut[max(oy,0):max(oy,0)+hh,max(ox,0):max(ox,0)+ww] if oy>=0 else im
            R.panel(fr,im,x0,y,18,a)
            return im.shape[0]
        if len(st)>1 and t-k<0.6:one(st[-2],1.0)
        hgt=one(cur,EO(pr(t,k,0.6)) if len(st)>1 else ta);y+=hgt+44
    return y
def render(sec,t):
    ty=sec['type'];fr=None
    if ty=='wes':
        fr=wes_full(t).copy()
        if sec['id']=='A':
            a0,a1=1.0,4.0;out=1-pr(t,a1,0.4)
            if t<a1+0.4:
                L=int(560*EO(pr(t,a0,0.5)))
                if L>1:R.paste(fr,R.card(L,1,hx('#8b9cff')),M,HT-M-70,out)
                T(fr,'STEADFAST MEN',M,HT-M-120,22,AC,a0+0.45,t,'GeistMono-Medium.ttf',a=out);T(fr,'Training for men',M,HT-M-58,36,TX,a0+0.45,t,'Geist-SemiBold.ttf',a=out)
        if sec['id']=='J':
            c=sec['close'];a=EO(pr(t,c[0][0]-0.3,0.6));sc=np.linspace(0,1,HT,dtype=np.float32)[:,None,None]**2*0.7*a;fr=fr*(1-sc)+BG*sc
            T(fr,c[0][1],(WD-R.text(c[0][1],64,'Geist-SemiBold.ttf',AC).shape[1])//2,800,64,AC,c[0][0],t,'Geist-SemiBold.ttf')
            T(fr,c[1][1],(WD-R.text(c[1][1],44,'Geist-SemiBold.ttf',TX).shape[1])//2,900,44,TX,c[1][0],t,'Geist-SemiBold.ttf',rise=False)
        return fr
    fr=bd(t)
    if ty=='split':
        x0=27+PW+80;ta=1.0 if sec['id']!='B' else EO(pr(t,sec['t0'],0.7))
        y=split_bg(fr,t,sec.get('stills'),x0,ta)
        if 'kicker' in sec:T(fr,sec['kicker'],x0,y,24,AC,sec['t0']+0.3,t,'GeistMono-Medium.ttf');y+=56
        if sec['id']=='F':
            mk=sec['rows'];y2=rows(fr,mk,t,x0,y,WD-x0-M,52,28,idx=True,alldim=(mk[-1][0],0.30))
            at=mk[-1][0]+0.45;L=int(500*EO(pr(t,at,0.5)))
            if L>1 and t>=at:R.paste(fr,R.card(L,2,AC),x0+90,y2-14,1.0)
        else:rows(fr,sec['rows'],t,x0,y,WD-x0-M,44,18)
        # Wes panel (morph from full in B handled in frame())
        if not (sec['id']=='B' and t<sec['t0']+0.7):wes_window(fr,t,PANEL_SRC,(27,27,PW,PH),lambda w,h:R.mask(w,h,24))
    elif ty=='stills':
        st=[q for q in sec['stills'] if t>=q[0]];cur=st[-1]
        def lay(q,a):
            p=q[1]
            if 'podcast' in p:   # 1080x1080 (0.77x native) bled left; title right
                im=show(p,1080);R.paste(fr,im,0,(HT-im.shape[0])//2,a)   # v11 = v10 treatment: live hero-table (1472x1174 after chrome crop) 1080 wide, centred vertically, navy above/below
                tt=cue('Walk',s('I14'));T(fr,'THE PODCAST',1200,300,24,AC,tt,t,'GeistMono-Medium.ttf',a=a);T(fr,'Walk Steadfast',1200,340,72,TX,tt,t,'Geist-SemiBold.ttf',a=a)
                L=int(520*EO(pr(t,tt,0.5)));
                if L>1:R.paste(fr,R.card(L,2,hx('#8b9cff')),1200,440,a)
            elif 'youtube' in p:
                im=show(p,1920);R.paste(fr,im,0,0,a);tt=cue('socials',s('I16'))
                if t>=tt-0.05:
                    pa=EO(pr(t,tt-0.05,0.45))*a;R.paste(fr,R.card(380,64,hx('#07070a')),M,HT-M-64,pa*0.8,R.mask(380,64,32));T(fr,'@steadfastwalk',M+30,HT-M-50,32,TX,tt,t,'GeistMono-Medium.ttf',a=a)
            else:  # book: native 1792x1008 max, scale-in 0.97 -> 1.00
                sc=0.97+0.03*EO(pr(t,q[0],1.6));im=show(p,1380,sc);R.paste(fr,im,M+int((1380-im.shape[1])/2),(HT-im.shape[0])//2,a)   # keeps clear of the bubble (x<1476)
        # v11: sequential still change: outgoing fades out (0.30 s), 3-frame empty beat, then incoming fades in (same 0.6 s EO) -- no overlap
        if len(st)>1 and t-cur[0]<SQ_OUT+SQ_GAP:
            if t-cur[0]<SQ_OUT:lay(st[-2],1-EI(pr(t,cur[0],SQ_OUT)))
        else:lay(cur,EO(pr(t,cur[0]+SQ_OUT+SQ_GAP,0.6)) if len(st)>1 else 1.0)
    elif ty=='sites':
        sites(fr,sec,t)
    elif ty=='board':
        y=M+60;T(fr,sec['kicker'],M+60,y,24,AC,sec['t0']+0.3,t,'GeistMono-Medium.ttf');y+=64
        if sec.get('big_first'):
            at=cue('24',s('I21'));c0=at-0.9;n=int(round(24*EO(pr(t,c0,0.9)))) if t>=c0 else 0
            if t>=c0-0.3:R.paste(fr,R.text(f'{n:02d}',150,'GeistMono-Medium.ttf',TX),M+60,y,EO(pr(t,c0-0.3,0.3)))
            T(fr,'sessions',M+60+250,y+50,72,TX,at,t,'Geist-SemiBold.ttf');y+=230
            rows(fr,[(cue('ordinary',s('I22')),'We start with ordinary days')],t,M+60,y,990,56,28)
        else:rows(fr,sec['rows'],t,M+60,y,990,52,30)
    elif ty=='scripture':
        at,ref=sec['ref'];T(fr,ref,M+60,M+40,26,AC,at,t,'GeistMono-Medium.ttf');y=M+120;hi_at=cue('underline',s('I33'))-0.4
        vl=sec['vlines'];f=R.fnt('Geist-Medium.ttf',56);MW=990
        for i,(at,s_) in enumerate(vl):
            if t<at-0.05:break
            nxt=vl[i+1][0] if i+1<len(vl) else 1e9;d=1-0.55*pr(t,nxt-0.05,0.3)
            if 'fully' not in s_:d=min(d,1-0.65*pr(t,hi_at,0.3))
            else:d=max(d,pr(t,hi_at,0.3))
            col=TX*d+BG*(1-d);h=T(fr,s_,M+60,y,56,col,at,t,'Geist-Medium.ttf',MW)
            if 'fully' in s_ and t>=hi_at:
                words=s_.split();line='';ly=0;lx=None
                for wd in words:
                    tt=(line+' '+wd).strip()
                    if f.getlength(tt)>MW and line:line=wd;ly+=1
                    else:line=tt
                    if wd.startswith('fully') and lx is None:lx=f.getlength(line)-f.getlength(wd);lyy=ly
                wl=int(f.getlength('fully')*EIO(pr(t,hi_at,0.6)))
                if wl>0:R.paste(fr,R.card(wl,2,AC),M+60+lx,y+lyy*56*1.2+66,1.0)
            y+=h+22
    return fr
# ---- D2: landing + give windows
LW,LH,BAR=780,468,36;LX,RX,WY=96,1044,110
_site={}
def site_imgs():
    if not _site:
        full=cv2.imread(ROOT+'/assets/live-home-stitched@2.5x.png')[...,::-1];k=LW/full.shape[1];nv=cv2.imread(ROOT+'/assets/live-home-nav@2.5x.png')[...,::-1];_site['nav']=cv2.resize(nv,(LW,int(nv.shape[0]*k)),interpolation=cv2.INTER_AREA).astype(np.float32)
        _site['full']=cv2.resize(full,(LW,int(full.shape[0]*k)),interpolation=cv2.INTER_AREA).astype(np.float32);_site['k']=LW/1100
        g=cv2.imread(ROOT+'/assets/live-give@2.5x.png')[...,::-1];_site['give']=cv2.resize(g,(LW,int(g.shape[0]*LW/g.shape[1])),interpolation=cv2.INTER_AREA).astype(np.float32)[:LH-BAR]
    return _site
def window(fr,x,y,content,url,a,border=0.4):
    sh=np.zeros((LH+160,LW+160,4),np.float32);mm=np.pad(R.mask(LW,LH,14),80)
    sh[...,3]=np.clip(np.roll(cv2.GaussianBlur(mm,(0,0),32),24,0)*0.55+np.roll(cv2.GaussianBlur(mm,(0,0),8),6,0)*0.5,0,1)*255
    R.paste(fr,sh,x-80,y-80,a)
    R.paste(fr,R.card(LW+2,LH+2,hx('#71717a')*border/0.4 if border>0.4 else hx('#71717a')),x-1,y-1,a*(border if border<=0.4 else 1.0),R.mask(LW+2,LH+2,15))
    body=np.zeros((LH,LW,3),np.float32);body[:BAR]=hx('#121218');body[BAR:]=content
    R.paste(fr,body,x,y,a,R.mask(LW,LH,14))
    for d_ in range(3):cv2.circle(fr,(x+22+d_*20,y+18),5,(hx('#71717a')*a+fr[y+18,x+22+d_*20]*(1-a)).tolist(),-1,cv2.LINE_AA)
    u=R.text(url,16,'GeistMono-Medium.ttf',hx('#d4d4d8'));pw=u.shape[1]+28;R.paste(fr,R.card(pw,24,hx('#1c1c24')),x+100,y+6,a,R.mask(pw,24,12));R.paste(fr,u,x+114,y+8,a)
def sites(fr,sec,t):
    S_=site_imgs();t0=sec['t0'];k=S_['k'];CHH=LH-BAR
    a1=EO(pr(t,t0,0.5));a2=EO(pr(t,t0+0.25,0.5))
    sc0,sc1=t0+0.93,t0+3.33;btn=(464*k,1883*k,171*k,44*k);target=btn[1]+btn[3]/2-CHH/2
    off=target*EIO(pr(t,sc0,sc1-sc0));o=int(off);fr_=off-o
    a_=S_['full'][o:o+CHH+1];cont=a_[:CHH]*(1-fr_)+a_[1:CHH+1]*fr_
    if o>0:nvh=S_['nav'].shape[0];cont=cont.copy();cont[:nvh]=S_['nav']
    for which,(x,img,url,a) in enumerate([(LX,cont,'walksteadfast.com',a1),(RX,S_['give'],'walksteadfast.com/give',a2)]):
        if a<=0:continue
        scl=0.97+0.03*a;im=img
        bord=0.4+0.6*EO(pr(t,sc1+0.3,0.7)) if which==1 else 0.4
        window(fr,x+int(LW*(1-scl)/2),WY+int(LH*(1-scl)/2),im,url,a,bord)
    rt=sc1+0.07
    if t>=rt:
        bx,by,bw,bh=LX+btn[0]-8,WY+BAR+btn[1]-off-8,btn[2]+16,btn[3]+16;p=EO(pr(t,rt,0.5))
        per=[(bx,by,bx+bw,by),(bx+bw,by,bx+bw,by+bh),(bx+bw,by+bh,bx,by+bh),(bx,by+bh,bx,by)];tot=2*(bw+bh);L=p*tot
        col=tuple(float(c) for c in hx('#8b9cff'))
        for (x1,y1,x2,y2) in per:
            sl=abs(x2-x1)+abs(y2-y1);u=min(L/sl,1) if sl else 0
            if u<=0:break
            cv2.line(fr,(int(x1),int(y1)),(int(x1+(x2-x1)*u),int(y1+(y2-y1)*u)),col,2,cv2.LINE_AA);L-=sl
        ct=rt+0.2
        if t>=ct:
            q=EIO(pr(t,ct,0.7));xs,ys=bx+bw,by+bh/2;xe=RX-2;cv2.line(fr,(int(xs),int(ys)),(int(xs+(xe-xs)*q),int(ys)),col,2,cv2.LINE_AA)
    rows(fr,[(s('I19'),'A donation keeps the training, the book and the podcast going.'),(s('I20'),"No guilt if now isn't the time.")],t,M,660,1050,40,22)
# ---- sections (plan_calm order + v3 D1/D2 split)
SEC=[]
for x in P.S:
    x=dict(x)
    if x['id']=='D':x['t0']=T_D1
    if x['id']=='D2':x['t0']=T_D2
    SEC.append(x)
for a,b in zip(SEC,SEC[1:]):a['t1']=b['t0']
SEC[-1]['t1']=TOTAL
ID={x['id']:x for x in SEC}
def base(t):
    i=max(k for k,x in enumerate(SEC) if x['t0']<=t) if t>=0 else 0;sec=SEC[i];fr=render(sec,t)
    if sec['id']=='B' and t<sec['t0']+0.7:   # shared-element reframe: full Wes -> split panel
        k=EIO(pr(t,sec['t0'],0.7));src=lerp((0,0,1920,1080),PANEL_SRC,k);dst=lerp((0,0,1920,1080),(27,27,PW,PH),k)
        wes_window(fr,t,src,dst,lambda w,h:R.mask(w,h,max(1,int(24*k))))
    elif False and sec['id']=='H' and t<sec['t0']+0.8:   # bubble -> full
        fr=render(SEC[i-1],t);k=EIO(pr(t,sec['t0'],0.8))
        wes_window(fr,t,lerp(SRC_OV,(0,0,1920,1080),k),lerp(OV,(0,0,1920,1080),k),lambda w,h:ell(w,h,0.45*k))
    elif False and sec['id']=='I' and t<sec['t0']+0.8:   # full -> bubble
        k=1-EIO(pr(t,sec['t0'],0.8))
        wes_window(fr,t,lerp(SRC_OV,(0,0,1920,1080),k),lerp(OV,(0,0,1920,1080),k),lambda w,h:ell(w,h,0.45*k))
    elif i+1<len(SEC) and SEC[i+1]['id'] in SEQ and t>=SEC[i+1]['t0']-0.4:   # v11: outgoing fades to the empty navy backdrop
        a=pr(t,SEC[i+1]['t0']-0.4,0.4);fr=fr*(1-a)+bd(t)*a
    elif sec['id'] in SEQ and t-sec['t0']<SQ_GAP+0.4:   # v11: empty beat, then incoming fades in (same 0.4 s linear)
        a=pr(t,sec['t0']+SQ_GAP,0.4);fr=bd(t)*(1-a)+fr*a
    elif i>0 and t-sec['t0']<0.4 and sec['id'] not in('B',):
        a=pr(t,sec['t0'],0.4);fr=render(SEC[i-1],t)*(1-a)+fr*a
    return fr
def frame(t):
    fr=base(t);st=bubble_state(t)
    if st:bubble(fr,t,st[0],st[1],st[2],st[3])
    if t>END:fr=fr*(1-min((t-END)/P.FADE,1))
    return fr
if __name__=='__main__':
    a=sys.argv[1:]
    if a[0]=='--still':
        os.makedirs('stills3',exist_ok=True)
        for x in a[1:]:
            t=float(x);R.RD.clear();im=np.clip(frame(t),0,255).astype(np.uint8);cv2.imwrite(f'stills3/v3_{t:07.2f}.png',im[...,::-1])
        sys.exit()
    t0,t1,out=float(a[0]),float(a[1]),a[2]
    import subprocess
    enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r',str(FPS),'-i','-','-c:v','libx264','-preset','slow','-crf','12','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
    for n in range(int(round(t0*FPS)),int(round(t1*FPS))):
        enc.stdin.write(np.clip(frame(n/FPS),0,255).astype(np.uint8).tobytes())
    enc.stdin.close();enc.wait()
