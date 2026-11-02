#!/usr/bin/env python3
"""L01 proof-v4 FREE recut renderer. numpy/cv2 compositor, PIL text. Site palette + Geist only.
Wes is never scaled above 1.0 of the raw HeyGen frame (max width = intro v5 width). Usage: render_v4.py [t0 t1] [--still t ...]"""
import sys,os,json,subprocess,math,numpy as np,cv2
from PIL import Image,ImageDraw,ImageFont
import importlib;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));P=importlib.import_module(os.environ.get('PLAN','plan_v2'))
FPS=25;WD,HT=1920,1080
V3='/workspace/artifacts/training/lesson-plan-2026-10-26/production-scripts/L01/proof-v3/'
HIDE=[False]  # True while rendering transition bases: Wes panels drawn empty, the morph layer draws him once
_cw={}
def chair_crush(f):
    """Crush the near-black background shapes (dim folding-chair silhouettes) outside Wes's body ellipse to black."""
    h,w=f.shape[:2]
    if (w,h) not in _cw:
        yy,xx=np.mgrid[0:h,0:w].astype(np.float32);d=((xx/w-0.5)/0.30)**2+((yy/h-0.62)/0.62)**2
        _cw[(w,h)]=np.clip((d-1.0)/0.5,0,1)[...,None]
    L=f.astype(np.float32).mean(2,keepdims=True);k=np.clip((L-30)/40,0,1);k=k*k*(3-2*k)
    return f.astype(np.float32)*(1-_cw[(w,h)]*(1-k))
hx=lambda h:np.array([int(h[i:i+2],16) for i in (1,3,5)],np.float32)
BG,SU,S2,TX,MU,FA,AC,AC2=[hx(x) for x in("#07070a","#121218","#18181f","#f4f4f5","#a1a1aa","#71717a","#8b9cff","#5b6ef5")]
F='/workspace/steadfast-main/fonts/ttf/';_fc={}
def fnt(n,s):
    k=(n,s)
    if k not in _fc:_fc[k]=ImageFont.truetype(F+n,s)
    return _fc[k]
def ease(p):p=min(max(p,0),1);return 1-(1-p)**3
# ---------- Wes clips
CLIPS=[]  # intro final: one continuous render (P.WES_SINGLE)
def wes_src(t):
    for a,b,p in getattr(P,'OVERRIDES',[]):
        if CUR[0] is not None and CUR[0]['t0']-1e-6<=a<CUR[0]['t1']:return p,t-a
    if getattr(P,'WES_SINGLE',None):return P.WES_SINGLE,t
    for a,b,p in CLIPS:
        if a-1e-3<=t<b+1e-3:return p,max(t-a,0)
    # gap (transition tail running past a clip): hold the most recent clip's last frame (reader holds at EOF)
    prev=[c for c in CLIPS if c[0]<=t]
    if prev:a,b,p=max(prev,key=lambda c:c[0]);return p,t-a
    raise ValueError('no Wes footage at %.3f'%t)
class Reader:
    def __init__(s,path,ss,w,h,mode,grade=False):
        vf=f"fps={FPS},"
        if mode=='cover':vf+=f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=bicubic,crop={w}:{h}"
        else:vf+=f"scale={w}:{h}:flags=bicubic"
        if grade:vf+=",eq=saturation=0.86:contrast=1.04:brightness=-0.025"
        inp=['-loop','1','-framerate',str(FPS),'-i',path] if path.lower().endswith(('.jpg','.jpeg','.png')) else ['-ss',f'{ss:.3f}','-i',path]  # stills loop forever (no seek)
        s.p=subprocess.Popen(['ffmpeg','-v','error']+inp+['-vf',vf,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
        s.w,s.h,s.n,s.last=w,h,0,None
    def get(s,k):
        while s.n<=k:
            b=s.p.stdout.read(s.w*s.h*3)
            if len(b)<s.w*s.h*3:break
            s.last=np.frombuffer(b,np.uint8).reshape(s.h,s.w,3);s.n+=1
        if s.last is None:
            global LASTW
            return LASTW.get((s.w,s.h),np.broadcast_to(BG.astype(np.uint8),(s.h,s.w,3)))
        LASTW[(s.w,s.h)]=s.last
        return s.last
    def close(s):s.p.kill()
RD={};LASTW={};LASTOUT=[None,None]
def vid(key,path,ss,t_local,w,h,mode='cover',grade=False,rel=True):
    k=(key,path,w,h)
    if k not in RD:RD[k]=(Reader(path,ss+(max(t_local,0) if rel else 0),w,h,mode,grade),t_local)
    r,t0=RD[k];return r.get(int(round((t_local-t0)*FPS)))
def wes(key,t,w,h):
    """Wes at scale<=1: if w,h==full -> raw; else raw scaled to fit (zoom OUT) or 1:1 crop (same face width)."""
    if HIDE[0]:return card(w,h,SU)
    p,lt=wes_src(t);return chair_crush(vid(key+'|'+p,p,lt,lt,w,h,'cover',rel=False))
def wes_crop(key,t,w,h):
    """1:1 window from the raw 1920x1080 frame (no scaling, face width unchanged = v5 width)."""
    f=wes(key,t,WD,HT);x0=(WD-w)//2;y0=max(0,min(HT-h,40));return f[y0:y0+h,x0:x0+w]
# ---------- drawing helpers
def rr_mask(w,h,r):
    m=Image.new('L',(w,h),0);ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),r,fill=255);return np.asarray(m,np.float32)/255
_mk={}
def mask(w,h,r):
    k=(w,h,r)
    if k not in _mk:_mk[k]=rr_mask(w,h,r)
    return _mk[k]
def paste(dst,img,x,y,a=1.0,m=None):
    h,w=img.shape[:2];x,y=int(round(x)),int(round(y))
    x0,y0,x1,y1=max(x,0),max(y,0),min(x+w,WD),min(y+h,HT)
    if x1<=x0 or y1<=y0 or a<=0:return
    src=img[y0-y:y1-y,x0-x:x1-x].astype(np.float32)
    if src.shape[2]==4:al=src[...,3:4]/255*a;src=src[...,:3]
    else:al=np.full(src.shape[:2]+(1,),a,np.float32)
    if m is not None:al=al*m[y0-y:y1-y,x0-x:x1-x,None]
    d=dst[y0:y1,x0:x1];d[:]=d*(1-al)+src*al
def panel(dst,img,x,y,r=24,a=1.0,border=True):
    h,w=img.shape[:2]
    if border:# 1px line-strong border + soft shadow
        sh=np.zeros((h+48,w+48,4),np.float32);sh[...,3]=cv2.GaussianBlur(np.pad(mask(w,h,r)*255*0.45,24),(0,0),16);paste(dst,sh,x-24,y-12,a)
        b=np.dstack([np.full((h+2,w+2,3),255,np.float32),mask(w+2,h+2,r+1)*255*0.14]);paste(dst,b,x-1,y-1,a)
    paste(dst,img,x,y,a,mask(w,h,r))
def card(w,h,col=SU):return np.broadcast_to(col,(h,w,3)).copy()
_ts={}
def text(s,size,font='Geist-SemiBold.ttf',col=TX,maxw=None,lh=1.2):
    k=(s,size,font,tuple(col),maxw)
    if k in _ts:return _ts[k]
    f=fnt(font,size);words=s.split();lines=[];cur=''
    for wd in words:
        t=(cur+' '+wd).strip()
        if maxw and f.getlength(t)>maxw and cur:lines.append(cur);cur=wd
        else:cur=t
    lines.append(cur);W_=int(max(f.getlength(l) for l in lines))+8;H_=int(size*lh*len(lines)+size*0.35)
    im=Image.new('RGBA',(W_,H_),(0,0,0,0));d=ImageDraw.Draw(im)
    for i,l in enumerate(lines):d.text((0,i*size*lh),l,font=f,fill=tuple(int(c) for c in col)+(255,))
    a=np.asarray(im,np.float32);_ts[k]=a;return a
_glow=None
def backdrop(t):
    global _glow
    if _glow is None:
        yy,xx=np.mgrid[0:1400,0:2400].astype(np.float32)
        g=np.exp(-(((xx-1500)/900)**2+((yy-500)/600)**2))*0.30+np.exp(-(((xx-600)/700)**2+((yy-1000)/500)**2))*0.14
        _glow=(BG*(1-g[...,None])+AC2*g[...,None]).astype(np.float32)
    ox=int(240+200*math.sin(t*0.05));oy=int(160+120*math.cos(t*0.04));g=_glow[oy:oy+HT,ox:ox+WD].copy()
    global _bn
    if '_bn' not in globals():_bn=[(lambda z:z/z.std()*2.6)(cv2.GaussianBlur(np.random.default_rng(11+i).normal(0,1,(HT,WD)).astype(np.float32),(0,0),0.8))[...,None] for i in range(6)]
    return g+_bn[int(t*25)%6]
def rise(t,at,dur=0.6,dy=30):
    p=ease((t-at)/dur);return p,(1-p)*dy
def kicker(dst,s,x,y,t,at):
    p,dy=rise(t,at,0.5,16)
    if p>0:paste(dst,text(s,26,'GeistMono-Medium.ttf',AC),x,y+dy,p)
def bubble(dst,s,t,at,x=120,y=820,hold=3.2,small=False):
    """classic structured lower third: solid surface bar, 4px accent rule at left, text; slides 24px + fades in 450 ms, fades out 300 ms"""
    if t<at-0.001 or t>at+hold+0.3:return
    sz=38 if not small else 32;tx=text(s,sz,'Geist-Medium.ttf',TX);h=int(sz*2.0);w=tx.shape[1]+64
    pin=ease((t-at)/0.45);pout=1-ease((t-at-hold)/0.3) if t>at+hold else 1;a=pin*pout
    x=x+(1-pin)*-24;yy=y-h/2
    paste(dst,card(w,h,SU),x,yy,a*0.94,mask(w,h,6))
    rl=int(h*ease((t-at)/0.35))
    if rl>0:paste(dst,card(4,rl,AC),x,yy+(h-rl)/2,a)
    paste(dst,tx,x+32,yy+(h-sz*1.2)/2-2,a)
def lower_third(dst,t,a0,a1,name,role):
    if t<a0 or t>a1+0.3:return
    p=ease((t-a0)/0.4);po=1-ease((t-a1)/0.3) if t>a1 else 1;a=p*po
    paste(dst,card(720,104,SU),96,890,a*0.92,mask(720,104,16))
    lw=int(680*p);
    if lw>0:paste(dst,card(lw,3,AC),116,900,a)
    pt=ease((t-a0-0.15)/0.4)
    paste(dst,text(name,22,'GeistMono-Medium.ttf',AC),120,914+(1-pt)*10,a*pt);paste(dst,text(role,34,'Geist-SemiBold.ttf',TX),120,944+(1-pt)*10,a*pt)
def node(dst,cx,cy,r,a,on,label):
    im=np.zeros((2*r+8,2*r+8,4),np.float32);c=[float(v) for v in (AC if on else MU)]
    cv2.circle(im,(r+4,r+4),r,(*[float(v) for v in SU],255),-1,cv2.LINE_AA);cv2.circle(im,(r+4,r+4),r,(*c,255),2,cv2.LINE_AA)
    paste(dst,im,cx-r-4,cy-r-4,a);tl=text(label,int(r*0.9),'GeistMono-Medium.ttf',AC if on else MU);paste(dst,tl,cx-tl.shape[1]/2+3,cy-r*0.62,a)
def rows_draw(dst,rows,t,x,y,maxw,size=54,gap=26,static_before=None,highlight_last=True,flow=False):
    shown=[r for r in rows if t>=r[0]-0.2]
    if flow:
        x=x+70;ys=[];yy=y
        for at,s_ in rows:
            im=text(s_,size,'Geist-Medium.ttf',MU,maxw-70);ys.append((yy,im.shape[0]));yy+=im.shape[0]+gap
        for i in range(1,len(rows)):
            at=rows[i][0];p=1 if (static_before is not None and at<static_before) else ease((t-at+0.45)/0.45)
            if t<at-0.45:break
            y0=ys[i-1][0]+size*0.6+24;y1=ys[i][0]+size*0.6-24;L=int((y1-y0)*p)
            if L>0:paste(dst,card(2,L,AC2),x-46,y0,0.8)
        for i,(at,s_) in enumerate(rows):
            if t<at-0.2:break
            p=1 if (static_before is not None and at<static_before) else ease((t-at+0.2)/0.5)
            node(dst,x-45,ys[i][0]+size*0.6,22,p,i==len(shown)-1,str(i+1))
    for i,(at,s) in enumerate(rows):
        if t<at-0.2:break
        cur=(i==len(shown)-1) and highlight_last
        col=TX if cur else MU
        im=text(s,size,'Geist-SemiBold.ttf' if cur else 'Geist-Medium.ttf',col,maxw-(70 if flow else 0))
        if static_before is not None and at<static_before:p,dy=1,0
        else:p,dy=rise(t,at-0.2,0.6,30)
        if cur and not flow:paste(dst,card(5,im.shape[0]-int(size*0.3),AC),x-28,y+dy+6,p)
        paste(dst,im,x,y+dy,p);y+=im.shape[0]+gap
    return y
def pip_frame(dst,x,y,w,h,a):
    sh=np.zeros((h+80,w+80,4),np.float32);sh[...,3]=cv2.GaussianBlur(np.pad(mask(w,h,20)*255*0.75,40),(0,0),22);paste(dst,sh,x-40,y-28,a)
    b=np.dstack([np.full((h+4,w+4,3),255,np.float32),mask(w+4,h+4,22)*255*0.28]);paste(dst,b,x-2,y-2,a)
def pip(dst,t,key,a=1.0,w=640,h=360):
    f=wes(key+'pip',t,w,h);x,y=WD-48-w,HT-48-h;pip_frame(dst,x,y,w,h,a);paste(dst,f,x,y,a,mask(w,h,20))
def broll_frame(key,path,ss,t,t0,w=WD,h=HT,push=0.045,dur=8):
    """slow push-in on video B-roll: 1.0 -> 1+push over the hold (motion even on near-static stock)"""
    big=vid(key,path,ss,t-t0,int(w*(1+push))//2*2,int(h*(1+push))//2*2,'cover',grade=True)
    if big is None:return np.broadcast_to(BG,(h,w,3)).copy()
    p=min((t-t0)/dur,1);s=1+push*(1-p)*0+push*p;cw,ch=int(big.shape[1]/(1+push)*(1+push-(s-1))) ,0
    sc=(1+push)/s;cw,ch=int(w*sc),int(h*sc);cw=min(cw,big.shape[1]);ch=min(ch,big.shape[0])
    x0=(big.shape[1]-cw)//2;y0=(big.shape[0]-ch)//2
    return cv2.resize(big[y0:y0+ch,x0:x0+cw],(w,h),interpolation=cv2.INTER_LINEAR).astype(np.float32)
# ---------- shot renderers
CUR=[None]
def render(sh,t):
    CUR[0]=sh;return _render(sh,t)
def _render(sh,t):
    ty=sh['type'];k=sh['id'];T0=sh['t0']
    if ty=='wes':
        fr=wes(k,t,WD,HT).astype(np.float32)
        for bb in sh.get('bubbles',[]):at,s=bb[0],bb[1];bubble(fr,s,t,at,y=bb[2] if len(bb)>2 else 820,hold=min(3.2,sh['t1']-at-0.1))
        if 'lower' in sh:lower_third(fr,t,*sh['lower'])
        if 'kover' in sh:# kinetic line over a darkened presenter (scrim 55%)
            a=ease((t-sh['kover'][0][0]+0.3)/0.5);sc_=np.linspace(0,1,HT,dtype=np.float32)[:,None,None]**2*0.75*a;fr=fr*(1-sc_)+BG*sc_;y=800
            for at,s,acc in sh['kover']:
                if t<at-0.2:break
                im=text(s,72 if acc else 48,'Geist-SemiBold.ttf',AC if acc else TX,1500);p,dy=rise(t,at-0.2,0.5,24)
                paste(fr,im,(WD-im.shape[1])/2,y+dy,p);y+=im.shape[0]+24
        return fr
    fr=backdrop(t)
    if ty=='pres':# zoomed-out presenter: raw frame scaled 0.62 (face ~209 px) in a panel, text column right
        w,h=1190,670;f=wes(k,t,w,h);pin=ease((t-T0)/0.5)
        ins=sh.get('insert')
        if ins and ins[0]<=t<ins[1]:# silent torso/hands cutaway from look-A G3 wide (no face in crop)
            a0,a1,src,ss,spd,(cx,cy,cw,chh)=ins;lt=ss+(t-a0)*spd
            if ('ins',src) not in RD:RD[('ins',src)]=(Reader(src,0,WD,HT,'fit'),0)
            r=RD[('ins',src)][0]
            g=r.get(int(lt*FPS)).astype(np.float32)[cy:cy+chh,cx:cx+cw];g=cv2.resize(g,(w,h),interpolation=cv2.INTER_CUBIC)
            mix=min(ease((t-a0)/0.3),1-ease((t-a1+0.3)/0.3));f=f*(1-mix)+g*mix
        panel(fr,f,72,(HT-h)//2,24,1.0)
        kicker(fr,sh['kicker'],1320,330,t,T0);rows_draw(fr,sh['rows'],t,1320,390,540,size=52,gap=24)
    elif ty=='split':
        wl=sh['wes']=='left';pw,ph=912,1026;xw=27 if wl else WD-27-pw;xb=WD-27-pw if wl else 27
        panel(fr,wes_crop(k,t,pw,ph).astype(np.float32),xw,27,24,1.0)
        if 'media_right' in sh and t>=sh['media_right'][0]-0.2:
            at,p_,ss=sh['media_right'];b=broll_frame(k+'mr',p_,ss,t,at,pw,ph,0.03,6);a=ease((t-at+0.2)/0.4)
            bc=card(pw,ph,SU);bc=bc*(1-a)+b*a;panel(fr,bc,xb,27,24)
        else:
            pin,dy=rise(t,T0,0.6,0);bx=xb+(1-pin)*60*(1 if wl else -1)
            panel(fr,card(pw,ph,SU),bx,27,24,pin)
            kicker(fr,sh['kicker'],bx+72,300,t,T0);rows_draw(fr,sh['rows'],t,bx+72,370,pw-150,size=56 if sh.get('flow') else 62,gap=40 if sh.get('flow') else 30,static_before=sh.get('static_before'),flow=sh.get('flow',False))
        for at,s in sh.get('bubbles',[]):bubble(fr,s,t,at,x=xb+40,y=900,hold=min(3.2,sh['t1']-at-0.1))
    elif ty=='broll':
        fr=broll_frame(k,sh['src'],sh['ss'],t,T0,dur=sh['t1']-T0)
        sc=np.linspace(0,0.55,HT,dtype=np.float32)[:,None,None]**2;fr=fr*(1-sc)+BG*sc  # bottom scrim for type
        if sh.get('pip') or ('pip_from' in sh and t>=sh['pip_from']):pip(fr,t,k,1.0 if sh.get('pip') else ease((t-sh['pip_from'])/0.56))
        for at,s in sh.get('bubbles',[]):bubble(fr,s,t,at,hold=min(3.6,sh['t1']-at-0.1))
        for i,(at,s) in enumerate(sh.get('pills',[])):bubble(fr,s,t,at,x=120,y=640+i*110,hold=sh['t1']-at-0.4)
    elif ty=='bsplit':
        pw,ph=912,1026
        for side,(at,p_,ss,lab) in (('L',sh['L']),('R',sh['R'])):
            x=27 if side=='L' else WD-27-pw
            if t>=at-0.2:
                a=ease((t-at+0.2)/0.5);b=broll_frame(k+side,p_,ss,t,at,pw,ph,0.04,7);panel(fr,b,x+(1-a)*40,27,24,a)
                lt_=sh.get('Rlab',at) if side=='R' else at;bubble(fr,lab,t,lt_+0.2,x=x+36,y=930,hold=sh['t1']-lt_-0.6,small=True)
            else:panel(fr,card(pw,ph,SU),x,27,24,0.6)
    elif ty=='listboard':
        mw,mh=1100,1026;  # media panel left
        cur=[m for m in sh['media'] if t>=m[0]-1e-3][-1];prev=[m for m in sh['media'] if t>=m[0]-1e-3][:-1]
        def mframe(m):
            if m[1]=='wes':return wes_crop(k,t,mw,mh).astype(np.float32)
            return broll_frame(k+m[2],m[2],m[3],t,m[0],mw,mh,0.04,6)
        img=mframe(cur)
        if prev and t-cur[0]<0.56:
            try:a=ease((t-cur[0])/0.56);img=mframe(prev[-1])*(1-a)+img*a
            except ValueError:pass
        panel(fr,img,27,27,24)
        hp='pip_from' in sh
        kicker(fr,sh['kicker'],1200,120 if hp else 200,t,T0);rows_draw(fr,sh['rows'],t,1200,180 if hp else 262,660,size=44 if hp else 48,gap=20 if hp else 28)
        if 'pip_from' in sh and t>=sh['pip_from']:
            pip(fr,t,k,ease((t-sh['pip_from'])/0.56),560,315)
    elif ty=='kinetic':
        y=(220 if sh.get('pip') else 420) if len(sh['lines'])>1 else 470
        for at,s,acc in sh['lines']:
            at=max(at,T0+0.25)
            if t<at-0.2:break
            im=text(s,76 if acc else 60,'Geist-SemiBold.ttf',AC if acc else TX,1500);p,dy=rise(t,at-0.2,0.5,24)
            paste(fr,im,(WD-im.shape[1])/2,y+dy,p);y+=im.shape[0]+30
    elif ty=='board':# full-screen structured board: kicker + rows, no presenter
        hp=(sh.get('pip') or 'pip_from' in sh)
        kicker(fr,sh['kicker'],220,150 if hp else 240,t,T0);rows_draw(fr,sh['rows'],t,220,215 if hp else 310,1000 if hp else 1400,size=56 if hp else 64,gap=26 if hp else 34)
    elif ty=='kinetic_words':
        words=[w for w in P.W if sh['t0']-0.05<=w['start']<sh['t1']];f=fnt('Geist-SemiBold.ttf',84)
        toks=sh['text'].split();lines=[[]];x=0
        for i,tk in enumerate(toks):
            wl=f.getlength(tk+' ')
            if x+wl>1500:lines.append([]);x=0
            lines[-1].append((i,tk));x+=wl
        y=400
        for ln in lines:
            lw=sum(f.getlength(tk+' ') for _,tk in ln);x=(WD-lw)/2
            for i,tk in ln:
                at=words[i]['start']-0.15 if i<len(words) else sh['t0']
                p,dy=rise(t,at,0.35,24)
                if p>0:paste(fr,text(tk,84,'Geist-SemiBold.ttf',AC if tk in sh['accent'] else TX),x,y+dy,p)
                x+=f.getlength(tk+' ')
            y+=110
    elif ty=='lockup':# STEADFAST / MEN lockup: de-blur + scale 1.04->1, hairline draws, eyebrow
        at,_=sh['big'];p=ease((t-at+0.2)/1.4)
        im=text('S T E A D F A S T',120,'Geist-Medium.ttf',TX);sc=1.04-0.04*p
        im2=cv2.resize(im,(int(im.shape[1]*sc),int(im.shape[0]*sc)));bl=int(18*(1-p))*2+1
        if bl>1:im2=cv2.GaussianBlur(im2,(bl,bl),0)
        paste(fr,im2,(WD-im2.shape[1])/2,420-(im2.shape[0]-im.shape[0])/2,p)
        lw=int(520*ease((t-at-0.3)/1.1));
        if lw>0:paste(fr,card(lw,2,AC),(WD-lw)/2,590,0.9)
        m=text('M E N',44,'GeistMono-Medium.ttf',AC);pm=ease((t-at-0.5)/0.8);paste(fr,m,(WD-m.shape[1])/2,615+(1-pm)*12,pm)
        a0,s0=sh['small'];ps,dy=rise(t,a0-0.2,0.5,12);sm=text(s0,26,'GeistMono-Medium.ttf',MU);paste(fr,sm,(WD-sm.shape[1])/2,330+dy,ps*(1-pm*0.6))
    elif ty in('name','title'):
        at,s=sh['small'];p,dy=rise(t,at-0.2,0.5,16)
        sm=text(s,34 if ty=='name' else 28,'Geist-Medium.ttf' if ty=='name' else 'GeistMono-Medium.ttf',MU);paste(fr,sm,(WD-sm.shape[1])/2,400+dy,p)
        at,s=sh['big'];big=text(s,140,'Geist-SemiBold.ttf',TX);p,dy=rise(t,at-0.2,0.7,30)
        paste(fr,big,(WD-big.shape[1])/2,480+dy,p)
        if p>0:lw=int(big.shape[1]*ease((t-at)/0.6));paste(fr,card(max(lw,1),4,AC),(WD-big.shape[1])/2,660+dy,p)
    elif ty=='stat':
        at,s=sh['label'];p,dy=rise(t,at-0.2);im=text(s,64,'Geist-SemiBold.ttf',TX);paste(fr,im,(WD-im.shape[1])/2,300+dy,p)
        at,n,lab=sh['num']
        if t>=at-1.0:
            p=min(max((t-(at-1.0))/0.9,0),1);p=1-(1-p)**3;val=n*p;v0=int(math.floor(val));fr_=val-v0
            if v0>=n:v0,fr_=n,0.0
            v=min(n,int(round(val)));im=text(f'{v:02d}',220,'GeistMono-Medium.ttf',AC);paste(fr,im,(WD-im.shape[1])/2,430,min(1,p*4+0.2))
            l2=text(lab.upper(),30,'GeistMono-Medium.ttf',MU);paste(fr,l2,(WD-l2.shape[1])/2,700,min(1,p*4+0.2))
        if sh.get('pip') or t>=sh.get('pip_from',1e9):pip(fr,t,k,1.0 if sh.get('pip') else ease((t-sh['pip_from'])/0.56))
    elif ty=='nametag':
        p,dy=rise(t,sh['at']-0.2,0.6,40);w,h=900,560;x,y=(WD-w)/2,(HT-h)/2+dy
        tag=card(w,h,TX);tag[:190]=AC2;panel(fr,tag,x,y,28,p)
        a=text('HELLO',96,'Geist-SemiBold.ttf',TX);paste(fr,a,x+(w-a.shape[1])/2,y+18,p)
        b=text('my name is',40,'Geist-Medium.ttf',TX);paste(fr,b,x+(w-b.shape[1])/2,y+128,p)
        at,s=sh['fill'];n=int(len(s)*min(1,max(0,(t-at)/0.9)))
        if n:c=text(s[:n],64,'Geist-Light.ttf',BG);paste(fr,c,x+60,y+300,p)
    elif ty=='scripture':
        at,ref=sh['ref'];p,dy=rise(t,at-0.2,0.5,16);r=text(ref,30,'GeistMono-Medium.ttf',AC);paste(fr,r,160,170+dy,p)
        v0=sh['vlines'][0][0]
        if t<v0+0.4:
            pb=min(ease((t-at+0.2)/0.7),1-ease((t-v0+0.2)/0.5));bg_=text(ref.split(' · ')[0].title().replace('15:58','15:58'),110,'Geist-SemiBold.ttf',TX);paste(fr,bg_,(WD-bg_.shape[1])/2,420,pb)
        y=250;hi_at,hi=sh['hi']
        for at,s in sh['vlines']:
            if t<at-0.2:break
            p,dy=rise(t,at-0.25,0.5,20);col=TX
            im=text(s,58,'Geist-Medium.ttf',TX,980)
            if t>=hi_at-0.15 and hi in s:
                # draw highlight bar under the phrase
                f=fnt('Geist-Medium.ttf',58);x0=f.getlength(s[:s.index(hi)]);wl=f.getlength(hi)*ease((t-hi_at+0.15)/0.4)
                paste(fr,card(max(int(wl),1),58+18,AC2),160+x0-6,y+dy+4,0.55*p)
            paste(fr,im,160,y+dy,p);y+=im.shape[0]+18
        at,s=sh['after']
        if t>=at-0.2:p,dy=rise(t,at-0.2);paste(fr,card(6,64,AC),160,y+50+dy,p);paste(fr,text(s,48,'Geist-SemiBold.ttf',AC),190,y+46+dy,p)
        if sh.get('pip'):pip(fr,t,k)
        elif 'pip_from' in sh and t>=sh['pip_from']:pip(fr,t,k,ease((t-sh['pip_from'])/0.56))
    if ty in('kinetic','board','title'):
        if sh.get('pip'):pip(fr,t,k)
        elif 'pip_from' in sh and t>=sh['pip_from']:pip(fr,t,k,ease((t-sh['pip_from'])/0.8))
    return fr
D=20  # v2: calmer 0.8 s transitions
def shot_at(t):
    for sh in P.S:
        if sh['t0']-1e-6<=t<sh['t1']-1e-6:return sh
    return P.S[-1]
def wes_rect(sh,t):
    """where Wes sits in this layout: (crop x,y,w,h in the raw frame, dest x,y,w,h, corner radius) or None"""
    ty=sh['type'];FULL=(0,0,WD,HT)
    if ty=='wes':return FULL,FULL,0
    if ty=='pres':return FULL,(72,(HT-670)//2,1190,670),24
    if ty=='split':
        pw,ph=912,1026;xw=27 if sh['wes']=='left' else WD-27-pw;return ((WD-pw)//2,40,pw,ph),(xw,27,pw,ph),24
    if ty=='listboard':
        cm=[m for m in sh['media'] if t>=m[0]-1e-3]
        if cm and cm[-1][1]=='wes':return ((WD-1100)//2,40,1100,1026),(27,27,1100,1026),24
        if 'pip_from' in sh and t>=sh['pip_from']:return FULL,(WD-48-560,HT-48-315,560,315),20
        return None
    if ty in('broll','stat','scripture','kinetic','board','title'):
        if sh.get('pip') or ('pip_from' in sh and t>=sh['pip_from']):return FULL,(WD-48-640,HT-48-360,640,360),20
    return None
def transition(A,B,t,p):
    """every layout change: 14-frame overlap. If Wes is on both sides, he morphs (scale/slide) from one frame to the
    other as ONE continuous picture over a cross-dissolved background; otherwise a blur-dissolve."""
    p=p*p*(3-2*p)
    ra,rb=wes_rect(A,t),wes_rect(B,t)
    if A.get('nomorph') or B.get('nomorph') or A.get('kover') or B.get('kover'):ra=None  # different takes: blur-dissolve, never morph
    if ra and rb:
        HIDE[0]=True
        try:fa=render(A,t);fb=render(B,t)
        finally:HIDE[0]=False
        o=fa*(1-p)+fb*p
        lerp=lambda u,v:tuple(int(round(x+(y-x)*p)) for x,y in zip(u,v))
        cx,cy,cw,ch=lerp(ra[0],rb[0]);dx,dy,dw,dh=lerp(ra[1],rb[1]);r=int(round(ra[2]+(rb[2]-ra[2])*p))
        F=wes('MORPH',t,WD,HT);img=cv2.resize(F[cy:cy+ch,cx:cx+cw],(dw,dh),interpolation=cv2.INTER_AREA if dw<cw else cv2.INTER_LINEAR)
        if r>0:
            if dw<700:pip_frame(o,dx,dy,dw,dh,1.0)
            else:
                sh_=np.zeros((dh+48,dw+48,4),np.float32);sh_[...,3]=cv2.GaussianBlur(np.pad(mask(dw,dh,r)*255*0.45,24),(0,0),16);paste(o,sh_,dx-24,dy-12,1.0)
            paste(o,img,dx,dy,1.0,mask(dw,dh,r))
        else:paste(o,img,dx,dy,1.0)
        return o
    fa=render(A,t);fb=render(B,t);bg=backdrop(t)
    aa=1-min(max(p/0.6,0),1);ab=min(max((p-0.4)/0.6,0),1);aa=aa*aa*(3-2*aa);ab=ab*ab*(3-2*ab)
    fa=cv2.GaussianBlur(fa,(0,0),0.5+3*(1-aa));fb=cv2.GaussianBlur(fb,(0,0),0.5+3*(1-ab))
    o=bg*(1-aa)*(1-ab)+fa*aa+fb*ab*(1-aa)
    return o
    sa=0.5+10*p;sb=0.5+10*(1-p)
    fa=cv2.GaussianBlur(fa,(0,0),sa);fb=cv2.GaussianBlur(fb,(0,0),sb)
    # luminance-preserving mix (avoids the near-black dip on board-to-photo dissolves)
    o=np.sqrt(np.maximum(fa,0)**2*(1-p)+np.maximum(fb,0)**2*p)
    return o
def frame(t):
    for sh in P.S:
        if sh['t0']-1e-6<=t<sh['t1']-1e-6:return render(sh,t)
    return render(P.S[-1],t)
if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='--still':
        for s in a[1:]:
            t=float(s);RD.clear();im=np.clip(frame(t),0,255).astype(np.uint8);cv2.imwrite(f'stills/t{t:07.2f}.jpg',im[...,::-1],[cv2.IMWRITE_JPEG_QUALITY,88])
        sys.exit()
    t0,t1=(float(a[0]),float(a[1])) if a else (0,P.END);out=a[2] if len(a)>2 else 'video-v5.mp4'
    n0,n1=int(round(t0*FPS)),int(round(t1*FPS))
    enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r',str(FPS),'-i','-','-c:v','libx264','-preset','medium','-crf','12','-tune','grain','-x264-params','aq-mode=3:deblock=-2,-2','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
    rng=np.random.default_rng(7);NZ=[rng.normal(0,1.4,(HT,WD,1)).astype(np.float32) for _ in range(8)]
    for n in range(n0,n1):
        t=n/FPS;cur=shot_at(t);prev=[s_ for s_ in P.S if abs(s_['t1']-cur['t0'])<1e-6]
        k=n-int(round(cur['t0']*FPS));prev=prev[0] if prev and 0<=k<D else None
        keep=['MORPH',cur['id']]+([prev['id']] if prev else [])
        for kk in [kk for kk in RD if not any(str(kk[0]).startswith(i_) for i_ in keep)]:RD[kk][0].close();del RD[kk]
        if prev is None:fo=render(cur,t)
        else:fo=transition(prev,cur,t,(k+1)/(D+1))
        fo=fo+NZ[n%8]  # fine dither: kills banding in the dark blue gradients
        enc.stdin.write(np.clip(fo,0,255).astype(np.uint8).tobytes())
        if k==0:print(cur['id'],f'{t:.2f}',flush=True)
    enc.stdin.close();enc.wait()
