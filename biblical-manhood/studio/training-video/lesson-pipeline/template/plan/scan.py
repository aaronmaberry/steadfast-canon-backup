"""Scan the L03 master every `step` frames at 640x360: face box (largest skin blob in the top 70%), face sharpness
(Laplacian variance inside the face), and any other skin blob (a hand) with its box. Writes master/scan_olive.json."""
# Skin test (SOP v2 step 5): wardrobe can read as skin. L06's tan chore coat sat at Cr 141-145 / hue 13-15 and flagged a 'hand'
# in every frame; skin is Cr ~152 / hue 4-10. If scan.py reports a hand-sized blob in nearly every frame, raise SKIN_CR_MIN and set SKIN_HUE_MAX.
SKIN_CR_MIN = 138
SKIN_HUE_MAX = None   # OpenCV hue 0-180; None = off
SKIN_CR_MAX = 175     # upper Cr bound; lower it for red/brick wardrobe (L09 brick tee: shirt Cr ~165, face ~149 -> 161)
import json, subprocess, sys, numpy as np, cv2
SRC = "/home/claude/l04/master/l04_master.mp4"
STEP = 5
W, H = 640, 360
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", SRC, "-vf", f"select='not(mod(n\\,{STEP}))',scale={W}:{H}", "-vsync", "0",
                      "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
frames = []; i = 0
k5 = np.ones((5, 5), np.uint8)
while True:
    b = p.stdout.read(W * H * 3)
    if len(b) < W * H * 3:
        break
    img = np.frombuffer(b, np.uint8).reshape(H, W, 3)
    ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    sk = ((ycc[..., 1] > SKIN_CR_MIN) & (ycc[..., 1] < SKIN_CR_MAX) & (ycc[..., 2] > 85) & (ycc[..., 2] < 125) & (ycc[..., 0] > 45)).astype(np.uint8)
    if SKIN_HUE_MAX is not None:
        hh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[..., 0]
        sk &= ((hh <= SKIN_HUE_MAX) | (hh >= 170)).astype(np.uint8)
    sk = cv2.morphologyEx(sk, cv2.MORPH_OPEN, k5)
    n, lab, st, cen = cv2.connectedComponentsWithStats(sk, 8)
    face = None; hand = 0.0; hb = None
    if n > 1:
        cand = [j for j in range(1, n) if st[j, 1] < H * 0.5]
        if cand:
            j = max(cand, key=lambda j: st[j, 4])
            x, y, w, h, a = [int(v) for v in st[j]]
            face = [x, y, w, h, a]
            g = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)
            sharp = float(cv2.Laplacian(g, cv2.CV_64F).var()) if g.size else 0.0
            others = [o for o in range(1, n) if o != j and st[o, 4] > 150]
            if others:
                o = max(others, key=lambda o: st[o, 4])
                hand = float(st[o, 4]) / (W * H)
                hb = [int(v) for v in st[o]]
    fr = dict(i=i, face=face, hand=hand, hand_box=hb)
    if face:
        fr["sharp"] = sharp
    frames.append(fr)
    i += STEP
json.dump(dict(step=STEP, frames=frames), open("/home/claude/l04/master/scan_olive.json", "w"))
print(len(frames), "scanned;", sum(1 for f in frames if not f["face"]), "without a face;", sum(1 for f in frames if f["hand"] > 0.03), "with a hand-sized blob")
