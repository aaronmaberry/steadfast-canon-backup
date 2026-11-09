#!/usr/bin/env python3
"""Track Wes face centre over master (+ optional wide) into p7/track.json."""
import os,sys,json,subprocess,numpy as np
WORK=os.environ.get('LESSON_WORK','/workspace/l08')
inp=json.load(open(f'{WORK}/p7/inputs.json'))
E=json.load(open(inp['edl']))
FPS=25;WD,HT=1920,1080
master=inp['wes_master']['path']
# insightface
sys.path.insert(0,'/workspace/cvenv/lib/python3.13/site-packages')
from insightface.app import FaceAnalysis
app=FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=-1, det_size=(640,640))
# which frames need tracking: SPLIT / bubble shots (CLOSE/MEDIUM)
need=set()
for s in E['shots']:
    if s.get('wes') in ('CLOSE','MEDIUM') or s['kind'] in ('SPLIT','TYPE_BOARD_BUBBLE','SCRIPTURE_BUBBLE','BRANDED_STILL_BUBBLE','AGENDA'):
        a=int(s['t0x']*FPS); b=int(s['t1x']*FPS)+1
        for n in range(a,b,2): need.add(n)  # every 2nd
need=sorted(need)
print('track frames', len(need), flush=True)
ns=[]; xys=[]; last=[960.0,400.0]
# stream master
proc=subprocess.Popen(['ffmpeg','-v','error','-i',master,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
n=0; ni=0
while ni<len(need):
    buf=proc.stdout.read(WD*HT*3)
    if len(buf)<WD*HT*3: break
    if n==need[ni]:
        fr=np.frombuffer(buf,np.uint8).reshape(HT,WD,3)
        faces=app.get(fr[:,:,::-1].copy())  # BGR
        if faces:
            f=max(faces, key=lambda x: (x.bbox[2]-x.bbox[0])*(x.bbox[3]-x.bbox[1]))
            cx=(f.bbox[0]+f.bbox[2])/2; cy=(f.bbox[1]+f.bbox[3])/2
            last=[float(cx),float(cy)]
        ns.append(n); xys.append(list(last))
        ni+=1
        if ni%500==0: print('tracked', ni, '/', len(need), flush=True)
    n+=1
proc.kill()
# fill face mean into inputs
face=list(np.mean(xys, axis=0)) if xys else [997.0,401.0]
inp['face']=face
json.dump(inp, open(f'{WORK}/p7/inputs.json','w'), indent=1)
json.dump(dict(n=ns, xy=xys), open(f'{WORK}/p7/track.json','w'))
print('face', face)
print('wrote track', len(ns))
