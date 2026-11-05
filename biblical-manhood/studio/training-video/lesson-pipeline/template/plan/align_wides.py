"""Place each L04 wide take on the master clock by cross-correlating its audio with the master narration (8 kHz)."""
import json, glob, os, subprocess, numpy as np
from scipy.signal import fftconvolve
SR = 8000
def pcm(p):
    return np.frombuffer(subprocess.check_output(["ffmpeg","-v","error","-i",p,"-vn","-ac","1","-ar",str(SR),"-f","f32le","-"]),np.float32).astype(np.float64)
M = pcm("/home/claude/l04/audio/narr_raw.wav")
out = []
for f in sorted(glob.glob("/home/claude/l04/wide/L04W-*.mp4")):
    w = pcm(f); wid = os.path.basename(f)[5:-4]
    c = fftconvolve(M, w[::-1], mode="valid")
    k = int(np.argmax(c)); seg = M[k:k+len(w)]
    corr = float(np.dot(seg, w) / (np.linalg.norm(seg) * np.linalg.norm(w) + 1e-12))
    pr = subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height,r_frame_rate:format=duration","-of","csv=p=0",f]).decode().split()
    out.append(dict(id=wid, file=os.path.basename(f), a=round(k/SR,2), dur=round(float(pr[1]),2), corr=round(corr,3), wh=pr[0]))
out.sort(key=lambda d: d["a"])
json.dump(out, open("/home/claude/l04/wide/wide.json","w"), indent=1)
for d in out: print(d["id"][:8], d["a"], d["dur"], d["corr"], d["wh"])
