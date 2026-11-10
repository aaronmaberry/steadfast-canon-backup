#!/usr/bin/env python3
"""Mandatory v3 visual gate: 1 frame / 20s plus every B-roll and board frame."""
import os, sys, json, cv2, numpy as np
from pathlib import Path

WORK='/workspace/l08'
B='/workspace/artifacts/training/lesson-plan-2026-10-26/L08-build-2026-11-09'
E=json.load(open(f'{WORK}/p7/edl.json'))
src=sys.argv[1] if len(sys.argv)>1 else f'{B}/L08-P7-ASSEMBLED-v3.mp4'
out_root=sys.argv[2] if len(sys.argv)>2 else f'{WORK}/p7/contact_v3'
Path(out_root).mkdir(parents=True, exist_ok=True)
(Path(out_root)/'every20').mkdir(exist_ok=True)
(Path(out_root)/'broll').mkdir(exist_ok=True)
(Path(out_root)/'boards').mkdir(exist_ok=True)

end=float(E['end'])
times=[]
# 1 / 20s
t=0.0
while t<end:
    times.append(('every20', round(t,2)))
    t+=20.0
# last frame
times.append(('every20', round(max(0,end-0.08),2)))
for b in E.get('broll') or []:
    times.append(('broll', round(b['t0']+0.35,2)))
    times.append(('broll', round((b['t0']+b['t1'])/2,2)))
for s in E['shots']:
    if s['kind'] in ('TITLE_CARD','AGENDA','TYPE_BOARD_BUBBLE','SPLIT','SCRIPTURE_CARD','SCRIPTURE_BUBBLE','BRANDED_STILL_BUBBLE','LOWER_THIRD','LOGO_END'):
        times.append(('boards', round(min(s['t1x']-0.15, s['t0x']+0.9),2)))
        times.append(('boards', round((s['t0x']+s['t1x'])/2,2)))

# unique per folder
cap=cv2.VideoCapture(src)
if not cap.isOpened():
    raise SystemExit(f'cannot open {src}')
fps=cap.get(cv2.CAP_PROP_FPS) or 25
written=[]
for folder,t in times:
    cap.set(cv2.CAP_PROP_POS_MSEC, t*1000)
    ok,fr=cap.read()
    if not ok:
        print('miss', t); continue
    dest=f'{out_root}/{folder}/t_{t:07.2f}.jpg'
    cv2.imwrite(dest, fr, [cv2.IMWRITE_JPEG_QUALITY, 85])
    written.append((folder,t,dest,fr))
cap.release()
print('frames', len(written))

def sheets(items, prefix, cols=6, page_rows=8):
    thumbs=[]
    for folder,t,dest,fr in items:
        th=cv2.resize(fr,(320,180),interpolation=cv2.INTER_AREA)
        label=f'{int(t//60):02d}:{int(t%60):02d}'
        cv2.putText(th,label,(8,22),cv2.FONT_HERSHEY_SIMPLEX,0.55,(0,0,0),3,cv2.LINE_AA)
        cv2.putText(th,label,(8,22),cv2.FONT_HERSHEY_SIMPLEX,0.55,(255,255,255),1,cv2.LINE_AA)
        thumbs.append(th)
    if not thumbs: return []
    pages=[]
    for p,i0 in enumerate(range(0,len(thumbs), cols*page_rows)):
        chunk=thumbs[i0:i0+cols*page_rows]
        rows=(len(chunk)+cols-1)//cols
        canvas=np.full((rows*180, cols*320, 3), 20, np.uint8)
        for i,th in enumerate(chunk):
            r,c=divmod(i,cols)
            canvas[r*180:(r+1)*180, c*320:(c+1)*320]=th
        path=f'{out_root}/{prefix}_{p+1:02d}.jpg'
        cv2.imwrite(path, canvas, [cv2.IMWRITE_JPEG_QUALITY, 82])
        pages.append(path)
        print('sheet', path, canvas.shape)
    return pages

pages=[]
pages += sheets([x for x in written if x[0]=='every20'], 'sheet_every20')
pages += sheets([x for x in written if x[0]=='broll'], 'sheet_broll', cols=4, page_rows=4)
pages += sheets([x for x in written if x[0]=='boards'], 'sheet_boards')
# also copy to artifacts
art=f'{B}/L08-v3-contact'
os.makedirs(art, exist_ok=True)
import shutil
for p in pages:
    shutil.copy2(p, f"{art}/{os.path.basename(p)}")
print('PAGES', pages)
print('ART', art)
