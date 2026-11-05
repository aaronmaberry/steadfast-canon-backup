"""For each wide clip: where Wes stands (face centre, x as a fraction of frame width) and a per-frame upper-face
detail series (same glitch measure as the master). Writes wide/widescan.json."""
import json, subprocess, numpy as np, cv2
from scipy.ndimage import median_filter, uniform_filter1d
W = json.load(open("/home/claude/l04/wide/wide.json"))


def face_box(f):
    img = cv2.imdecode(np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-ss", "3", "-i", f, "-frames:v", "1",
                                                              "-f", "image2", "-c:v", "png", "-"]), np.uint8), cv2.IMREAD_COLOR)
    ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    sk = ((ycc[..., 1] > 138) & (ycc[..., 1] < 175) & (ycc[..., 2] > 85) & (ycc[..., 2] < 122) & (ycc[..., 0] > 55)).astype(np.uint8)
    sk[int(img.shape[0] * 0.45):] = 0                     # face is in the top half of a waist-up frame
    sk = cv2.morphologyEx(sk, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    n, lab, st, cen = cv2.connectedComponentsWithStats(sk, 8)
    j = 1 + int(np.argmax(st[1:, 4]))
    x, y, w, h, a = st[j]
    return int(x), int(y), int(w), int(h)


out = []
for c in W:
    f = "/home/claude/l04/wide/" + c["file"]
    x, y, w, h = face_box(f)
    bx, by, bw, bh = x + w // 8, y + h // 6, ((w * 3) // 4) // 2 * 2, (h // 2) // 2 * 2       # eyes / nose / cheeks (even sizes)
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", f, "-vf", f"crop={bw}:{bh}:{bx}:{by},format=gray", "-f", "rawvideo", "-"])
    fr = np.frombuffer(raw, np.uint8).reshape(-1, bh, bw)
    v = np.array([cv2.Laplacian(g, cv2.CV_64F).var() for g in fr])
    r = v / median_filter(v, size=101, mode="nearest")
    m = uniform_filter1d(r, 8)
    bad = m < 0.82
    runs = []; i = 0
    while i < len(bad):
        if bad[i]:
            j = i
            while j < len(bad) and bad[j]: j += 1
            if j - i >= 8: runs.append((round(c["a"] + i / 25, 2), round(c["a"] + j / 25, 2)))
            i = j
        else:
            i += 1
    out.append(dict(c, face=[x, y, w, h], cx=round((x + w / 2) / 1920, 3), glitch=runs))
    print(c["a"], "cx", round((x + w / 2) / 1920, 2), "face w", w, "glitches", runs)
json.dump(out, open("/home/claude/l04/wide/widescan.json", "w"), indent=1)
