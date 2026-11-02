import json,numpy as np
from scipy.ndimage import gaussian_filter1d
T=json.load(open('/workspace/l01v4/build/track_all.json'))
Z=1.15
def path(n0,n1,k=0.6,sig=20):
    ns=list(range(n0,n1));a=np.array([T[str(n)][1:4] if str(n) in T else [np.nan]*3 for n in ns],float)
    for j in range(3):
        m=np.isnan(a[:,j])
        if m.all():a[:,j]=[960,290,145][j]
        elif m.any():a[m,j]=np.interp(np.flatnonzero(m),np.flatnonzero(~m),a[~m,j])
    s=np.stack([gaussian_filter1d(a[:,j],sig,mode='nearest') for j in range(3)],1)
    return {n:(a[i],s[i]) for i,n in enumerate(ns)},k
def matrix(raw,sm,k,Z=Z,anchor=(960,0)):
    cx,cy,iod=raw;sx,sy,siod=sm
    s=(siod/iod)**k
    tx,ty=cx+k*(sx-cx),cy+k*(sy-cy)   # where the face centre should land (source coords)
    # warp: p' = s*(p-c)+t ; then punch: o = Z*(p'-O), O = crop origin
    W,H=1920,1080;cw,ch=W/Z,H/Z;O=(anchor[0]-cw/2,anchor[1])
    A=np.array([[Z*s,0,Z*(tx-s*cx-O[0])],[0,Z*s,Z*(ty-s*cy-O[1])]],np.float32)
    return A
