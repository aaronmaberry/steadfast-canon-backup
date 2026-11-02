import numpy as np,cv2
M=np.load('/workspace/artifacts/training/intro-final-2026-10-27/v3qa/masks.npy',mmap_mode='r')
H,W=1080,1920
reg=np.zeros((H,W),np.float32);reg[0:430,0:1600]=1;reg=cv2.GaussianBlur(reg,(0,0),40)
yy=np.linspace(0,1,H,dtype=np.float32)[:,None]
def fill_for(fr):
    s=fr[440:520,0:400].reshape(-1,3);c=np.median(s,0)
    return np.broadcast_to(c,(H,W,3)).astype(np.float32)*(0.85+0.15*yy[...,None])
_c=None
def clean(fr,n):
    """fr float32 RGB 1920x1080 frame n of raw HeyGen render; returns sign-free frame."""
    global _c
    if _c is None:_c=fill_for(fr)
    k=[M[max(0,min(len(M)-1,n+d))].astype(np.float32) for d in (-1,0,1)]
    p=cv2.resize((k[0]+2*k[1]+k[2])/1020.,(W,H),interpolation=cv2.INTER_LINEAR)
    p=np.clip((p-0.25)*2.5,0,1);p=cv2.dilate(p,np.ones((9,9),np.uint8));p=cv2.GaussianBlur(p,(0,0),3)
    a=reg*(1-p);a[p>=0.97]=0
    # edge spill suppression: in the matte edge band inside the sign region, pull blue down to the warm/neutral level
    band=(reg*np.clip(1-np.abs(p-0.6)/0.4,0,1)*(p<0.97))[...,None]
    o=fr.copy();nb=np.minimum(fr[...,2],np.maximum(fr[...,0],fr[...,1])*1.02);o[...,2]=fr[...,2]*(1-band[...,0])+nb*band[...,0]
    o=o*(1-band*0.35)+_c*band*0.35*(1-p[...,None])
    a=a[...,None];return o*(1-a)+_c*a
