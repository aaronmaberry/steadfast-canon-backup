#!/usr/bin/env python3
"""Eye-aid + numeric QC for L08 v4 wides. Does not ship; reports smear/hands/arc/jut."""
import sys,json,cv2,numpy as np
from pathlib import Path
sys.path.insert(0,'/workspace/artifacts/training/lipsync-tests-2026-10-26/scripts')
import evaluate as E
from mediapipe.tasks.python import vision,BaseOptions
n=lambda v:v/np.linalg.norm(v)
VI=n(np.load('/workspace/steadfast-main/training-locked/INTRO-LOOK-A-MASTER-LOCKED-2026-10-26/intro_ref_embedding.npy').ravel())
fa=E.app()
FL=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='/home/box/models/face_landmarker.task'),num_faces=1))

def smear_score(im, y0=0.70, y1=1.0, xhalf=220):
    h,w=im.shape[:2]
    a,b=int(h*y0),int(h*y1)
    band=im[a:b, w//2-xhalf:w//2+xhalf].astype(np.float32)
    if band.shape[0]<3: return 0.0
    d=np.mean(np.abs(band[1:]-band[:-1]),axis=(1,2))
    return float(np.median(d))  # clean fabric ~5-8; smear band ~1.1

def sample_times(dur, n=5):
    if dur<=0: return [0]
    return [dur*(i+1)/(n+1) for i in range(n)]

def analyze(path):
    cap=cv2.VideoCapture(str(path))
    fps=cap.get(cv2.CAP_PROP_FPS) or 25
    nfr=int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    dur=nfr/fps if fps else 0
    arcs,dzs,cys,smears,fws=[],[],[],[],[]
    jut=0
    frames_for_sheet=[]
    ts=sample_times(dur,6)
    for t in ts:
        cap.set(cv2.CAP_PROP_POS_MSEC, t*1000)
        ok,im=cap.read()
        if not ok: continue
        frames_for_sheet.append((t,im))
        smears.append(smear_score(im))
        try:
            g=E.biggest(fa.get(im))
            rgb=np.ascontiguousarray(im[...,::-1])
            L=FL.detect(mp_image(rgb)).face_landmarks[0]
            dz=(L[152].z-L[10].z)*1920
            fw=float(g.bbox[2]-g.bbox[0])
            cy=(g.bbox[1]+g.bbox[3])/2
            arc=float(n(g.embedding)@VI)
            arcs.append(arc); dzs.append(dz); cys.append(cy); fws.append(fw)
            if dz < -150: jut += 1
        except Exception:
            pass
    cap.release()
    return {
        "path":str(path),"dur":round(dur,2),"n":len(arcs),
        "arc_mean":round(float(np.mean(arcs)),3) if arcs else None,
        "arc_min":round(float(np.min(arcs)),3) if arcs else None,
        "fw_mean":round(float(np.mean(fws)),1) if fws else None,
        "dz_mean":round(float(np.mean(dzs)),1) if dzs else None,
        "jut_frames":jut,
        "cy_range":round(float(np.max(cys)-np.min(cys)),1) if len(cys)>1 else 0,
        "smear_med":round(float(np.median(smears)),2) if smears else None,
        "smear_min":round(float(np.min(smears)),2) if smears else None,
        "frames":frames_for_sheet,
    }

def mp_image(rgb):
    import mediapipe as mp
    return mp.Image(image_format=mp.ImageFormat.SRGB,data=rgb)

def contact(results, outdir, cols=6):
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    # one row of mid frames + one of lower-third crops
    mids=[]
    labels=[]
    for r in results:
        if not r["frames"]: continue
        t,im=r["frames"][len(r["frames"])//2]
        mids.append(cv2.resize(im,(320,180)))
        labels.append(Path(r["path"]).stem)
    if not mids: return []
    # also a lower-body strip sheet
    lows=[]
    for r in results:
        if not r["frames"]: continue
        t,im=r["frames"][len(r["frames"])//2]
        h,w=im.shape[:2]
        lows.append(cv2.resize(im[int(h*0.55):,:],(320,80)))
    def grid(ims,h=180,cols=6,path=None,labs=None):
        rows=(len(ims)+cols-1)//cols
        canv=np.zeros((rows*h+ (20 if labs else 0)*rows, cols*320,3),np.uint8)
        for i,im in enumerate(ims):
            r,c=divmod(i,cols)
            y=r*(h+(20 if labs else 0))
            canv[y:y+im.shape[0], c*320:c*320+im.shape[1]]=im
            if labs:
                cv2.putText(canv,labs[i],(c*320+4,y+im.shape[0]+16),cv2.FONT_HERSHEY_SIMPLEX,0.4,(220,220,220),1,cv2.LINE_AA)
        if path:
            cv2.imwrite(str(path),canv,[cv2.IMWRITE_JPEG_QUALITY,90])
        return path
    p1=grid(mids,180,6,outdir/'sheet_mids.jpg',labels)
    p2=grid(lows,80,6,outdir/'sheet_lower.jpg',labels)
    # per-clip 6-frame strips for first-pass eye
    strips=[]
    for r in results:
        ims=[cv2.resize(im,(240,135)) for t,im in r["frames"]]
        if not ims: continue
        canv=np.zeros((135,240*len(ims),3),np.uint8)
        for i,im in enumerate(ims):
            canv[:,i*240:(i+1)*240]=im
        p=outdir/f"strip_{Path(r['path']).stem}.jpg"
        cv2.imwrite(str(p),canv,[cv2.IMWRITE_JPEG_QUALITY,88])
        strips.append(str(p))
    return [str(p1),str(p2)]+strips

if __name__=='__main__':
    paths=sorted(Path(sys.argv[1]).glob('w*.mp4')) if len(sys.argv)>1 else []
    outdir=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/tmp/l08v4_qc')
    outdir.mkdir(parents=True,exist_ok=True)
    results=[]
    for p in paths:
        r=analyze(p)
        frames=r.pop('frames')
        results.append((r,frames))
        print(json.dumps(r), flush=True)
    # rebuild with frames for contact
    results_frames=[]
    recs=[]
    for r,frames in results:
        recs.append(r)
        r=dict(r); r['frames']=frames
        results_frames.append(r)
    results=results_frames
    sheets=contact(results,outdir)
    for r in results:
        r.pop('frames',None)
    summary={"n":len(results),
             "arc_mean":round(float(np.mean([r['arc_mean'] for r in results if r['arc_mean'] is not None])),3) if results else None,
             "jut_total":sum(r['jut_frames'] for r in results),
             "smear_med_min":min((r['smear_min'] or 99) for r in results) if results else None,
             "fail_arc":[r['path'] for r in results if (r['arc_mean'] or 0)<0.90],
             "fail_smear":[r['path'] for r in results if (r['smear_min'] or 99)<2.0],
             "sheets":sheets,
             "clips":results}
    (outdir/'qc_wide_v4.json').write_text(json.dumps(summary,indent=2))
    print('WROTE',outdir/'qc_wide_v4.json')
