import sys,json,cv2,numpy as np,mediapipe as mp,glob
from mediapipe.tasks.python import vision,BaseOptions
HL=vision.HandLandmarker.create_from_options(vision.HandLandmarkerOptions(base_options=BaseOptions(model_asset_path='/workspace/artifacts/training/lesson-plan-2026-10-26/production-scripts/L01/proof-v5/scr/hand_landmarker.task'),num_hands=2,min_hand_detection_confidence=0.4))
FL=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path='/home/box/models/face_landmarker.task'),num_faces=1))
res={}
for f in sys.argv[1:]:
    cap=cv2.VideoCapture(f);n=0;H=[];S=[];W=[];DZ=[]
    while True:
        ok,F=cap.read()
        if not ok:break
        im=mp.Image(image_format=mp.ImageFormat.SRGB,data=np.ascontiguousarray(F[...,::-1]))
        if n%2==0:
            r=HL.detect(im);top=min([min(l.y for l in h)*1080 for h in r.hand_landmarks],default=None);H.append([n,top])
            fr=FL.detect(im)
            if fr.face_landmarks:
                L=fr.face_landmarks[0];W.append((max(l.x for l in L)-min(l.x for l in L))*1920);DZ.append((L[152].z-L[10].z)*1920)
        b=cv2.cvtColor(F[860:1000],cv2.COLOR_BGR2HSV);S.append(int(((b[...,0]<25)&(b[...,1]>40)&(b[...,1]<170)&(b[...,2]>110)).sum()))
        n+=1
    res[f]=dict(frames=n,hand_any=sum(1 for h in H if h[1] is not None)*2,hand_visible_above1000=sum(1 for h in H if h[1] is not None and h[1]<1000)*2,skin_band_frames=int((np.array(S)>600).sum()),face_w=float(np.median(W)),jut150=int((np.array(DZ)<-150).sum())*2,hand_frames=[h[0] for h in H if h[1] is not None and h[1]<1000])
    print(f,{k:v for k,v in res[f].items() if k!='hand_frames'},flush=True)
json.dump(res,open('wqc_%s.json'%sys.argv[1].split('/')[-1][:-4],'w'))
