#!/usr/bin/env python3
"""L07-class lesson renderer (rebuilt 2026-11-09 from render_l01 + L07 EDL/QC API).
Usage: render_l07.py n0 n1 out.mp4 | --still t ...
Importable as render_l07 for QC (layout.py): E, CUTS, shot_at, kin_at, bubble_state, PX,PY,PW,PH,OV.
"""
import os,sys,json,subprocess,numpy as np,cv2
from PIL import Image,ImageDraw,ImageFont

WORK=os.environ.get('LESSON_WORK', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Allow QC to pass cfg as argv[1] path to inputs.json
if len(sys.argv)>1 and sys.argv[1].endswith('inputs.json'):
    INP=json.load(open(sys.argv[1])); sys.argv=sys.argv[:1]+sys.argv[2:]
elif os.path.isfile(f'{WORK}/p7/inputs.json'):
    INP=json.load(open(f'{WORK}/p7/inputs.json'))
else:
    INP=None

LC=(INP or {}).get('lesson') or json.load(open(f'{WORK}/lesson.json'))
WORK=LC.get('work', WORK).rstrip('/')
_edl=(INP or {}).get('edl') or f'{WORK}/p7/edl.json'
if not os.path.isabs(_edl): _edl=os.path.join(WORK,_edl)
E=json.load(open(_edl))
CUTS=E['cuts']; SH=E['shots']; FPS=int(E.get('fps',25)); WD,HT=1920,1080; M=96
MASTER=(INP or {}).get('wes_master',{}).get('path') or ''
WIDE=(INP or {}).get('wes_wide') or []
TRACK_P=(INP or {}).get('track') or f'{WORK}/p7/track.json'
if not os.path.isabs(TRACK_P): TRACK_P=os.path.join(WORK,TRACK_P)
FACE=(INP or {}).get('face') or [997.0, 400.0]
CRF=int((INP or {}).get('crf') or 16)
AC_HEX=LC.get('accent','#8b9cff'); AC2_HEX=LC.get('accent2', AC_HEX)
GLOW=LC.get('glow_corner','tr'); BUB=LC.get('bubble_home','bottom-right')
STILL_ASSET=LC.get('still_asset','')
LOGO='/workspace/artifacts/training/lesson-plan-2026-10-26/L01-build-2026-10-29/assets/logo-lockup-LIVE-2026-10-29.jpg'
FD='/workspace/steadfast-main/fonts/ttf/'

hx=lambda h:np.array([int(h[i:i+2],16) for i in (1,3,5)],np.float32)
BG,SU,TX,MU,AC,AC2=[hx(x) for x in("#07070a","#121218","#f4f4f5","#a1a1aa",AC_HEX,AC2_HEX)]
_fc={}
def fnt(n,s):
    if (n,s) not in _fc:_fc[(n,s)]=ImageFont.truetype(FD+n,s)
    return _fc[(n,s)]
def bez(x1,y1,x2,y2):
    ts=np.linspace(0,1,2001);bx=3*(1-ts)**2*ts*x1+3*(1-ts)*ts**2*x2+ts**3;by=3*(1-ts)**2*ts*y1+3*(1-ts)*ts**2*y2+ts**3
    return lambda p:float(np.interp(min(max(p,0),1),bx,by))
EO=bez(0.22,1,0.36,1);EI=bez(0.4,0,1,1)
pr=lambda t,a,d:min(max((t-a)/max(d,1e-6),0),1)
_mk={}
def mask(w,h,r):
    k=(w,h,r)
    if k not in _mk:
        m=Image.new('L',(w,h),0);ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),r,fill=255);_mk[k]=np.asarray(m,np.float32)/255
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
def card(w,h,col=SU):return np.broadcast_to(col,(h,w,3)).copy()
def panel(dst,img,x,y,r=18,a=1.0):
    h,w=img.shape[:2];sh=np.zeros((h+48,w+48,4),np.float32);sh[...,3]=cv2.GaussianBlur(np.pad(mask(w,h,r)*255*0.45,24),(0,0),16);paste(dst,sh,x-24,y-12,a)
    b=np.dstack([np.full((h+2,w+2,3),255,np.float32),mask(w+2,h+2,r+1)*255*0.14]);paste(dst,b,x-1,y-1,a);paste(dst,img,x,y,a,mask(w,h,r))
_ts={}
def wrap(s,f,maxw):
    lines=[];cur=''
    for wd in str(s).split():
        t=(cur+' '+wd).strip()
        if maxw and f.getlength(t)>maxw and cur:lines.append(cur);cur=wd
        else:cur=t
    return lines+[cur] if cur or not lines else ['']
def text(s,size,font='Geist-SemiBold.ttf',col=TX,maxw=None,lh=1.2,hi=None,hcol=AC,center=False):
    k=(s,size,font,tuple(map(float,col)),maxw,tuple(hi) if isinstance(hi,(list,tuple)) else hi,center)
    if k in _ts:return _ts[k]
    f=fnt(font,size);lines=wrap(s,f,maxw);W_=int(max((f.getlength(l) for l in lines),default=8))+8;H_=int(size*lh*len(lines)+size*0.35)
    im=Image.new('RGBA',(max(W_,8),max(int(H_),8)),(0,0,0,0));d=ImageDraw.Draw(im)
    hw=set(); flat=[(i,j,w) for i,l in enumerate(lines) for j,w in enumerate(l.split())]
    if hi:
        hs=[]
        for h in (hi if isinstance(hi,(list,tuple)) else [hi]):
            hs += [x.strip(',.') for x in str(h).lower().split()]
        ws=[w.lower().strip('",.;:?!') for _,_,w in flat]
        for q in range(len(ws)-len(hs)+1):
            if ws[q:q+len(hs)]==hs: hw.update(range(q,q+len(hs)))
    q=0
    for i,l in enumerate(lines):
        x=(W_-8-f.getlength(l))/2 if center else 0
        for j,w in enumerate(l.split()):
            c=hcol if q in hw else col;d.text((x,i*size*lh),w,font=f,fill=tuple(int(v) for v in c)+(255,));x+=f.getlength(w+' ');q+=1
    a=np.asarray(im,np.float32);_ts[k]=a
    if len(_ts)>400:_ts.pop(next(iter(_ts)))
    return a

# backdrop with glow corner
def _bd():
    yy,xx=np.mgrid[0:HT,0:WD].astype(np.float32)
    cx,cy={'tl':(250,120),'tr':(1670,120),'bl':(250,960),'br':(1670,960)}.get(GLOW,(1670,120))
    g=np.exp(-(((xx-cx)/950)**2+((yy-cy)/620)**2))*0.30+np.exp(-(((xx-(WD-cx))/700)**2+((yy-(HT-cy))/450)**2))*0.08
    n=cv2.GaussianBlur(np.random.default_rng(11).normal(0,1,(HT,WD)).astype(np.float32),(0,0),0.8);n=n/(n.std()+1e-6)*2.6
    return (BG*(1-g[...,None])+AC2*g[...,None]+n[...,None]).astype(np.float32)
BD=_bd()

# face track lookup
_TR=None
def face_at(t):
    global _TR
    if _TR is None:
        if os.path.isfile(TRACK_P):
            tr=json.load(open(TRACK_P)); _TR=(tr.get('n') or [], tr.get('xy') or [])
        else:
            _TR=([],[])
    ns,xys=_TR
    if not ns: return FACE
    n=int(round(t*FPS))
    # nearest
    i=min(range(len(ns)), key=lambda j: abs(ns[j]-n))
    return xys[i]

# Wes readers
class Reader:
    def __init__(s, path, n0):
        s.path=path; s.n=n0
        s.p=subprocess.Popen(['ffmpeg','-v','error','-ss',f'{n0/FPS:.3f}','-i',path,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
        s.f=None; s.eof=False
    def get(s,n):
        while (s.f is None or s.n<=n) and not s.eof:
            b=s.p.stdout.read(WD*HT*3)
            if len(b)<WD*HT*3: s.eof=True; break
            s.f=np.frombuffer(b,np.uint8).reshape(HT,WD,3); s.n+=1
        return s.f
_RD={}
def _reader(path, n):
    r=_RD.get(path)
    if r is None or r.n-1>n or r.path!=path:
        if r: 
            try: r.p.kill()
            except: pass
        r=Reader(path, max(0,n-1)); _RD[path]=r
    return r

def wes_frame(t, kind='WIDE'):
    """Return Wes RGB float frame for time t, cropped/scaled for kind."""
    path=MASTER; local_t=t
    for w in WIDE:
        if w['t0']-0.05 <= t < w['t1']+0.05 and kind=='WIDE':
            path=w['path']; local_t=t-w['t0']; break
    if not path or not os.path.isfile(path):
        return BD.copy()
    n=int(round(local_t*FPS))
    fr=_reader(path, n).get(n)
    if fr is None: return BD.copy()
    F=fr.astype(np.float32)
    if kind=='WIDE':
        return F.copy()
    cx,cy=face_at(t)
    if kind=='MEDIUM':
        # panel crop ~912x640 face-locked, 1.5x wider than tight
        pw,ph=912,640
        # source crop around face
        sw,sh=int(pw/1.15), int(ph/1.15)
        sx=int(np.clip(cx-sw/2,0,WD-sw)); sy=int(np.clip(cy-sh*0.42,0,HT-sh))
        crop=F[sy:sy+sh,sx:sx+sw]
        return cv2.resize(crop,(pw,ph),interpolation=cv2.INTER_AREA)
    # CLOSE bubble source
    sw,sh=850,1000
    sx=int(np.clip(cx-sw/2,0,WD-sw)); sy=int(np.clip(cy-sh*0.38,0,HT-sh))
    return F[sy:sy+sh,sx:sx+sw].copy()

# layout constants
PW,PH=912,640
PX=WD-PW-27; PY= (HT-PH)//2
if BUB.startswith('bottom'):
    if 'left' in BUB: OV=(72, HT-400-48, 340, 400)
    else: OV=(WD-340-72, HT-400-48, 340, 400)
else:
    if 'left' in BUB: OV=(72, 72, 340, 400)
    else: OV=(WD-340-72, 72, 340, 400)
SRC_OV_CLOSE=None  # computed per-frame via wes_frame CLOSE

def ell(w,h):
    m=np.zeros((h*2,w*2),np.float32);cv2.ellipse(m,(w,h),(w-2,h-2),0,0,360,1,-1,cv2.LINE_AA);return cv2.resize(m,(w,h),interpolation=cv2.INTER_AREA)
def _chrome():
    w,h=OV[2],OV[3];m=ell(w,h);er3=cv2.erode(m,np.ones((7,7),np.uint8));er4=cv2.erode(m,np.ones((9,9),np.uint8))
    yy,xx=np.mgrid[0:h,0:w].astype(np.float32);g=np.clip((xx/w+yy/h)/2,0,1)[...,None]
    col=hx('#f4f4f5')*(1-g)+hx('#a1a1aa')*g;al=(0.95*(1-g)+0.55*g)[...,0]
    rim=np.clip(m-er3,0,1)*al;hair=np.clip(er3-er4,0,1)*0.6
    vg=1-0.11*np.clip((((xx-w/2)/(w/2))**2+((yy-h/2)/(h/2))**2-0.55)/0.45,0,1)
    P_=100;big=np.pad(m,P_);amb=np.roll(cv2.GaussianBlur(big,(0,0),32),24,0)*0.55;con=np.roll(cv2.GaussianBlur(big,(0,0),8),6,0)*0.5
    return dict(m=m,rim=rim,rcol=col,hair=hair,vg=vg[...,None],sh=1-(1-amb)*(1-con),P=P_,chip=text('WES',16,'GeistMono-Medium.ttf',hx('#e4e4e7')))
CH=_chrome()

def bubble(fr,t,a,scale=1.0,dy=0.0,chip=1.0):
    if a<=0:return
    w,h=OV[2],OV[3]
    crop=wes_frame(t,'CLOSE')
    if crop.shape[0]<10: return
    img=cv2.resize(crop,(w,h),interpolation=cv2.INTER_AREA)*CH['vg']
    hh=CH['hair'][...,None];img=img*(1-hh)+BG*hh;rr=CH['rim'][...,None];img=img*(1-rr)+CH['rcol']*rr
    Pp=CH['P'];layer=np.zeros((h+2*Pp,w+2*Pp,3),np.float32);layer[Pp:Pp+h,Pp:Pp+w]=img;m=np.pad(CH['m'],Pp);shd=CH['sh']
    if scale!=1.0:
        W2,H2=int((w+2*Pp)*scale),int((h+2*Pp)*scale);layer=cv2.resize(layer,(W2,H2));m=cv2.resize(m,(W2,H2));shd=cv2.resize(shd,(W2,H2))
    H2,W2=m.shape;cx,cy=OV[0]+w/2,OV[1]+h/2;x=int(cx-W2/2);y=int(cy-H2/2+dy)
    x0,y0=max(x,0),max(y,0);x1,y1=min(x+W2,WD),min(y+H2,HT)
    d=fr[y0:y1,x0:x1];sa=shd[y0-y:y1-y,x0-x:x1-x,None]*a;d*=1-sa
    ma=m[y0-y:y1-y,x0-x:x1-x,None]*a;d[:]=d*(1-ma)+layer[y0-y:y1-y,x0-x:x1-x]*ma
    if chip>0 and scale>0.99:
        c=CH['chip'];cw,chh=c.shape[1]+28,30;px,py=int(OV[0]+w//2-cw//2),int(OV[1]+h-16+dy)
        paste(fr,card(cw+2,chh+2,hx('#71717a')),px-1,py-1,a*chip,mask(cw+2,chh+2,16));paste(fr,card(cw,chh,BG),px,py,a*chip*0.9,mask(cw,chh,15));paste(fr,c,px+14,py+5,a*chip)

IX={s['id']:s for s in SH}
BRUN=[]
BUBK=('TYPE_BOARD_BUBBLE','SCRIPTURE_BUBBLE','BRANDED_STILL_BUBBLE','AGENDA')
for a,b in E.get('bubble_runs') or []:
    A,B=IX.get(a),IX.get(b)
    if not A or not B: continue
    ci=[c for c in CUTS if c['b']==a]; co=[c for c in CUTS if c['a']==b]
    t_in=(ci[0]['e'] if ci and ci[0]['type']=='dip' else A['t0x'])+0.35
    t_out=co[0]['s'] if co and co[0]['type']=='dip' else B['t1x']
    BRUN.append((t_in,t_out))
# also continuous bubble while on bubble kinds
def bubble_state(t):
    for a,b in BRUN:
        if a<=t<b:
            if t<b-0.45:e=EO(pr(t,a,0.7));return (pr(t,a,0.5),0.92+0.08*e,28*(1-e),pr(t,a+0.15,0.3))
            p=EI(pr(t,b-0.45,0.45));return (1-p,1-0.04*p,12*p,1-p)
    sh=shot_at(t)
    if sh['kind'] in BUBK:
        return (1.0,1.0,0.0,1.0)
    return None

def T(fr,im,x,y,at,t,a=1.0):
    if at is None: at=t
    p=EO(pr(t,at-0.05,0.45))*a
    if p>0:paste(fr,im,x,y+14*(1-EO(pr(t,at-0.05,0.45))),p)
def dimc(t,nxt,to=0.5):d=1-(1-to)*pr(t,nxt-0.05,0.3);return TX*d+BG*(1-d),d
def rows(fr,rr,t,x,y,maxw,size=50,gap=26,chips=False,big_first=False,dim=True,big_idx=None):
    if big_first: big_idx=0
    for i,item in enumerate(rr):
        if isinstance(item,(list,tuple)) and len(item)>=2: s_,at=item[0],item[1]
        else: s_,at=str(item),t
        if at is None: at=t
        nxt=rr[i+1][1] if (dim and i+1<len(rr) and isinstance(rr[i+1],(list,tuple)) and rr[i+1][1] is not None) else 1e9
        if nxt is None: nxt=1e9
        col,d=dimc(t,nxt); sz=int(size*1.45) if i==big_idx else size; xx=x
        if chips:
            T(fr,text(f'{i+1:02d}',int(size*0.6),'GeistMono-Medium.ttf',AC*d+BG*(1-d)),x,y+size*0.22,at,t); xx=x+92
        im=text(s_,sz,'Geist-SemiBold.ttf' if d>0.99 else 'Geist-Medium.ttf',col,maxw-(xx-x));T(fr,im,xx,y,at,t);y+=im.shape[0]+gap
    return y

_still={}
def still(p,w):
    k=(p,w)
    if k not in _still:
        im=cv2.imread(p,cv2.IMREAD_COLOR)
        if im is None: _still[k]=card(w,int(w*0.56),SU); return _still[k]
        im=im[...,::-1].astype(np.float32);ih,iw=im.shape[:2];w=min(w,iw);_still[k]=cv2.resize(im,(w,int(ih*w/iw)),interpolation=cv2.INTER_AREA)
    return _still[k]
_lg=[None];LBG=[BG]
def logo():
    if _lg[0] is None:
        im=cv2.imread(LOGO)
        if im is None: _lg[0]=(card(857,309,SU), np.ones((309,857),np.float32)); return _lg[0]
        im=im[...,::-1].astype(np.float32);im=cv2.resize(im,(857,309),interpolation=cv2.INTER_AREA)
        h,w=im.shape[:2];m=np.ones((h,w),np.float32);m=cv2.GaussianBlur(np.pad(m[12:-12,12:-12],12),(0,0),8);_lg[0]=(im,m)
        LBG[0]=np.median(np.concatenate([im[:20].reshape(-1,3),im[-20:].reshape(-1,3)]),0).astype(np.float32)
    return _lg[0]

def shot_at(t):
    for s in SH:
        if s['t0x']<=t<s['t1x']: return s
    return SH[-1]
def kin_at(t):
    hits=[k for k in E.get('kinetic') or [] if k['t0']<=t<k['t1']]
    if not hits: return None
    for k in hits:
        if k.get('cover') or k.get('style')=='lower_third':
            return k
    return hits[0]

def draw_lower_third(fr,k,t):
    """#12 lower-third over a live Wes frame. No blur."""
    a=1.0
    if t<k['t0']+0.25: a=EO(pr(t,k['t0'],0.25))
    if t>k['t1']-0.25: a*=1-EI(pr(t,k['t1']-0.25,0.25))
    bar_h=168; y0=HT-bar_h
    overlay=fr.copy(); overlay[y0:]=overlay[y0:]*0.22+BG*0.78
    fr=fr*(1-a)+overlay*a
    paste(fr,card(220,4,AC2),M+60,y0+28,a)
    line=(k.get('text') or '').strip()
    if line:
        im=text(line,44,'Geist-SemiBold.ttf',TX,1600)
        paste(fr,im,M+60,y0+52,a)
    return fr

def render_kinetic(k,t):
    if k.get('style')=='lower_third':
        fr=wes_frame(t,'WIDE')
        return draw_lower_third(fr,k,t)
    fr=BD.copy(); a=1.0
    if t<k['t0']+0.28: a=EO(pr(t,k['t0'],0.28))
    if t>k['t1']-0.28: a*=1-EI(pr(t,k['t1']-0.28,0.28))
    raw=(k.get('text') or ' '.join(w if isinstance(w,str) else w[0] for w in (k.get('words') or []))).strip()
    # Short complete card: wrap with the same font metrics, never mid-word at the edge,
    # and show every line as soon as the card is on (no delayed line that leaves a hanging clause).
    size=56; maxw=1480
    f=fnt('Geist-SemiBold.ttf',size); lines=wrap(raw,f,maxw) or [raw]
    while len(lines)>3 and size>42:
        size-=4
        f=fnt('Geist-SemiBold.ttf',size)
        lines=wrap(raw,f,maxw) or [raw]
    ims=[text(line,size,'Geist-SemiBold.ttf',TX,maxw) for line in lines]
    gap=18
    total=sum(im.shape[0]+gap for im in ims)-gap
    y=max(240, (HT-total)//2)
    at=k['t0']+0.06
    for im in ims:
        T(fr,im,M+80,y,at,t,a)
        y+=im.shape[0]+gap
    return fr

def render(sh,t):
    k=sh['kind']; sp=sh.get('spec') or {}
    # kinetic cover overrides
    kk=kin_at(t)
    if kk and kk.get('cover') and kk['t0']+0.05<=t<kk['t1']-0.05:
        return render_kinetic(kk,t)
    if k=='WES_FULL':
        # Show the wide take as rendered (natural arms). No bottom fade, blur, or hand mask.
        fr=wes_frame(t,'WIDE')
        lt=kin_at(t)
        if lt and lt.get('style')=='lower_third' and lt['t0']<=t<lt['t1']:
            fr=draw_lower_third(fr, lt, t)
        return fr
    if k=='LOGO_END':
        im,m=logo();fr=card(WD,HT,LBG[0]);t0=sh['t0x'];a=pr(t,t0+0.4,0.8)*(1-pr(t,t0+0.4+0.8+1.6,0.8))
        paste(fr,im,(WD-im.shape[1])//2,(HT-im.shape[0])//2,a,m);return fr
    fr=BD.copy()
    if k=='TITLE_CARD':
        y=340
        kick=sp.get('kicker'); 
        if isinstance(kick,(list,tuple)): ks,kat=kick[0],kick[1]
        else: ks,kat=str(kick or LC.get('kicker','')), sh['t0x']+0.3
        T(fr,text(ks,26,'GeistMono-Medium.ttf',AC),M+60,y,kat,t)
        les=sp.get('lesson')
        if isinstance(les,(list,tuple)): T(fr,text(les[0],44,'Geist-Medium.ttf',MU),M+60,y+56+190,les[1],t)
        tit=sp.get('title'); 
        if isinstance(tit,(list,tuple)): ts,tat=tit[0],tit[1]
        else: ts,tat=str(tit or LC.get('title','')), sh['t0x']+1.0
        T(fr,text(ts,110,'Geist-SemiBold.ttf',TX,1700),M+60,y+56,tat,t)
        L=int(560*EO(pr(t,tat+0.45,0.6)))
        if L>1: paste(fr,card(L,3,AC2),M+60,y+56+160,1.0)
        return fr
    if k=='LOWER_THIRD':
        fr=wes_frame(t,'WIDE')
        return draw_lower_third(fr, {'t0':sh['t0x'],'t1':sh['t1x'],'text':(sp.get('line') or sp.get('text') or '')}, t)
    if k=='SPLIT':
        # board left, Wes panel right
        y=M+40; rr=sp.get('rows') or []
        rows(fr,rr,t,M+40,y,PX-M-80,48,26)
        panel_img=wes_frame(t,'MEDIUM')
        panel(fr, panel_img, PX, PY, 24)
        lt=kin_at(t)
        if lt and lt.get('style')=='lower_third' and lt['t0']<=t<lt['t1']:
            fr=draw_lower_third(fr, lt, t)
        return fr
    if k=='AGENDA':
        y=M+20
        kick=sp.get('kicker')
        if isinstance(kick,(list,tuple)): T(fr,text(kick[0],26,'GeistMono-Medium.ttf',AC),M+60,y,kick[1],t); y+=58
        rr=sp.get('rows') or []
        # tighter chips so five pills sit above the Wes bubble
        if rr: rows(fr,rr,t,M+60,y,1180,44,14,chips=True)
        else:
            # fallback: show kicker only; pills come from spoken later
            T(fr,text('Stay with the plan.',48,'Geist-Medium.ttf',TX),M+60,y+40,sh['t0x']+1.0,t)
        return fr
    if k=='SCRIPTURE_CARD':
        # #8 / #16 full-screen scripture card (no bubble)
        y=220
        ref=sp.get('ref')
        if isinstance(ref,(list,tuple)): rs,rat=ref[0],ref[1]
        else: rs,rat=str(ref or ''), sh['t0x']+0.3
        T(fr,text('SCRIPTURE',22,'GeistMono-Medium.ttf',AC),M+80,y,rat,t)
        T(fr,text(rs,36,'GeistMono-Medium.ttf',AC),M+80,y+44,rat,t)
        y+=130
        verse=sp.get('verse') or ''
        vat=sp.get('vat', sh['t0x']+1.0)
        hi=sp.get('hi')
        if verse:
            f=fnt('Geist-Medium.ttf',52); lines=wrap(verse,f,1680)
            for i,l in enumerate(lines):
                at=vat+i*0.45
                im=text(l,52,'Geist-Medium.ttf',TX,1680,1.28,hi=hi[0] if hi else None,hcol=AC)
                T(fr,im,M+80,y,at,t); y+=im.shape[0]+16
        return fr
    if k=='SCRIPTURE_BUBBLE':
        y=M+60
        ref=sp.get('ref')
        if isinstance(ref,(list,tuple)): T(fr,text(ref[0],28,'GeistMono-Medium.ttf',AC),M+60,y,ref[1],t); y+=70
        verse=sp.get('verse') or ''
        vat=sp.get('vat', sh['t0x']+1.0)
        hi=sp.get('hi')
        hcol=AC
        if verse:
            # wrap verse as lines typed over time
            f=fnt('Geist-Medium.ttf',48); lines=wrap(verse,f,1600)
            # approximate per-line cue
            for i,l in enumerate(lines):
                at=vat+i*0.55
                im=text(l,48,'Geist-Medium.ttf',TX,1600,1.25,hi=hi[0] if hi else None,hcol=hcol)
                T(fr,im,M+60,y,at,t); y+=im.shape[0]+18
        return fr
    if k=='BRANDED_STILL_BUBBLE':
        p=sp.get('still') or STILL_ASSET
        rr=sp.get('rows') or []
        if p and os.path.isfile(p):
            im=still(p, 900 if rr else 1100)
            if rr:
                panel(fr,im,(WD-im.shape[1])//2, M+8, 18)
                # captions sit to the right of the Wes bubble so they are not covered
                y=M+8+im.shape[0]+16
                rows(fr,rr,t, 420, y, 1400, 40, 14)
            else:
                panel(fr,im,(WD-im.shape[1])//2,(HT-im.shape[0])//2,18)
        elif rr:
            rows(fr,rr,t,420,M+60,1400,52,28)
        return fr
    if k=='TYPE_BOARD_BUBBLE':
        y=M+60; rr=sp.get('rows') or []
        rows(fr,rr,t,M+60,y,1180,52,28)
        return fr
    # fallback
    return fr

def apply_broll(fr,t):
    for b in E.get('broll') or []:
        if not (b['t0']<=t<b['t1']): continue
        path=b.get('clip') or b.get('path')
        if not path or not os.path.isfile(path): return fr
        # local time
        lt=t-b['t0']
        n=int(lt*FPS)
        r=_reader(path, n); F=r.get(n)
        if F is None: return fr
        a=1.0
        # edge fades based on tin/tout
        if b.get('tin') in ('xfade','push') and t<b['t0']+0.3: a=EO(pr(t,b['t0'],0.3))
        if b.get('tout') in ('xfade','push') and t>b['t1']-0.3: a*=1-EI(pr(t,b['t1']-0.3,0.3))
        img=F.astype(np.float32)
        if b.get('tin')=='push' or b.get('tout')=='push':
            z=1.0+0.04*pr(t,b['t0'],b['t1']-b['t0']); 
            h,w=img.shape[:2]; nh,nw=int(h/z),int(w/z); y0=(h-nh)//2; x0=(w-nw)//2
            img=cv2.resize(img[y0:y0+nh,x0:x0+nw],(WD,HT),interpolation=cv2.INTER_AREA)
        else:
            img=cv2.resize(img,(WD,HT),interpolation=cv2.INTER_AREA)
        fr=fr*(1-a)+img*a
        return fr
    return fr

def apply_trans(fr,t):
    for c in CUTS:
        typ=c['type']
        if typ=='hard': continue
        s,e=c.get('s',c.get('cut')), c.get('e',c.get('cut'))
        if not (s<=t<=e): continue
        if typ=='dip':
            # dip to bg mid
            mid=(s+e)/2; half=(e-s)/2
            if t<mid: a=pr(t,s,half); fr=fr*(1-a)+BD*a
            else: a=pr(t,mid,half); fr=BD*(1-a)+fr*a
        elif typ=='xfade':
            # crossfade handled approximately as mix with neighbors — soft dip
            a=pr(t,s,e-s); 
            # slight soften
            fr=fr*(1-0.35*np.sin(a*np.pi))+BD*(0.35*np.sin(a*np.pi))
        elif typ=='push':
            a=EO(pr(t,s,e-s)); fr=fr*(1-0.25*a)+BD*(0.25*a)
        elif typ in ('leak','blur'):
            # light-leak style warm wash — NOT a blurred splice of content
            a=np.sin(pr(t,s,e-s)*np.pi)*0.35
            wash=np.array([40,55,90],np.float32)
            fr=fr*(1-a)+np.clip(fr*0.7+wash,0,255)*a
        break
    return fr

def frame(t):
    sh=shot_at(t); fr=render(sh,t)
    fr=apply_broll(fr,t)
    fr=apply_trans(fr,t)
    st=bubble_state(t)
    if st: bubble(fr,t,*st)
    # safe-area clamp already via layout
    return fr

if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='--still':
        os.makedirs(f'{WORK}/p7/stills',exist_ok=True)
        for x in a[1:]:
            t=float(x); 
            for r in list(_RD.values()):
                try: r.p.kill()
                except: pass
            _RD.clear()
            cv2.imwrite(f'{WORK}/p7/stills/s_{t:07.2f}.jpg',np.clip(frame(t),0,255).astype(np.uint8)[...,::-1],[cv2.IMWRITE_JPEG_QUALITY,88])
        sys.exit()
    n0,n1,out=int(a[0]),int(a[1]),a[2]
    enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r',str(FPS),'-i','-',
        '-c:v','libx264','-preset','medium',f'-crf',str(CRF),'-pix_fmt','yuv420p','-threads','2',out+'.part.mp4'],stdin=subprocess.PIPE)
    for n in range(n0,n1):
        enc.stdin.write(np.clip(frame(n/FPS)+0.5,0,255).astype(np.uint8).tobytes())
        if n%250==0: print(n,flush=True)
    enc.stdin.close(); enc.wait()
    if enc.returncode!=0: raise SystemExit(f'ffmpeg failed {enc.returncode}')
    os.rename(out+'.part.mp4',out)
