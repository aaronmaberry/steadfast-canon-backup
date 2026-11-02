"""Static background patch for raw HeyGen render 39d6f626 (clean look A): darkens the sign-mount remnant
(blurry light ledge/panel, x0-690 y230-445 and x0-590 y440-640) toward the surrounding dark plate. Multiplicative gain map, so the
render's own grain keeps moving (no frozen patch). Region stays >=70 px left of Wes's leftmost face/hair (face bbox
min x 771 over the whole take): Wes pixels are never touched (gain exactly 1.0 for x>=712)."""
import numpy as np,cv2,os
_G=None
def gain():
    global _G
    if _G is None:
        d=os.path.dirname(os.path.abspath(__file__));mp_=os.environ.get('BG_MEDIAN') or next(q for q in (d+'/v4raw_median.png',d+'/../v3qa/v4raw_median.png') if os.path.exists(q))
        med=cv2.imread(mp_).astype(np.float32)
        L=cv2.GaussianBlur(med.mean(2),(0,0),12);T=2.5
        g=np.clip(T/np.maximum(L,1e-3),0.15,1.0)
        reg=np.zeros(L.shape,np.float32);reg[230:445,0:690]=1;reg[440:640,0:590]=1   # ledge/teal bar + light blob (chair back) left of Wes
        reg=cv2.GaussianBlur(reg,(0,0),14);reg[:,712:]=0
        _G=(1-reg*(1-g))[...,None].astype(np.float32)
    return _G
def apply(f):return f*gain()
