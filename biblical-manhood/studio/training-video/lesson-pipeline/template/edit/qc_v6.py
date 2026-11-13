"""v6 delivery checks: clean decode, length, loudness, and how faithfully every Wes shot keeps HeyGen's face
(PSNR of the face box vs the HeyGen file at the same moment, skipping each shot's first 0.8 s of dissolve/dip)."""
import sys, json, subprocess, numpy as np
sys.path.insert(0, "/home/claude/l04/edit"); sys.path.insert(0, "/home/claude/l04/plan")
import layout
OUT = "/home/claude/l04/deliver/L04-Stop-Waiting-v3-1080p.mp4"
MASTER = "/home/claude/l04/master/l04_master.mp4"
WIDE = json.load(open("/home/claude/l04/wide/widescan.json"))
WIDX = np.load("/home/claude/l04/plan/w_idx.npy")
PRE, FPS = 4.0, 25


def grab(f, ss, n, crop):
    b = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", f"{ss:.3f}", "-i", f, "-frames:v", str(n),
                                 "-vf", f"crop={crop},format=gray", "-f", "rawvideo", "-"])
    w, h = [int(v) for v in crop.split(":")[:2]]
    return np.frombuffer(b, np.uint8).reshape(-1, h, w).astype(np.float32)


def psnr(a, b):
    n = min(len(a), len(b)); m = ((a[:n] - b[:n]) ** 2).mean(axis=(1, 2))
    return 10 * np.log10(255 ** 2 / np.maximum(m, 1e-6))


if __name__ == "__main__":
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", OUT, "-f", "null", "-"], capture_output=True, text=True)
    print("decode errors:", len(r.stderr.strip().splitlines()) if r.stderr.strip() else 0, r.stderr[:500])
    p = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration,size,bit_rate", "-of", "json", OUT]))
    print("duration", p["format"]["duration"], "size MB", round(int(p["format"]["size"]) / 1e6, 1), "Mbps", round(int(p["format"]["bit_rate"]) / 1e6, 2))
    sh = layout.build()
    res = []
    for s in sh:
        if s["kind"] not in ("W", "P", "WW", "WS") or s["t1"] - s["t0"] < 1.6:
            continue
        t = s["t0"] + 0.8; n = min(25, int((s["t1"] - t) * FPS) - 2)
        if n < 5:
            continue
        if s["kind"] == "W":
            a = grab(OUT, PRE + t, n, "440:520:740:40"); b = grab(MASTER, t, n, "440:520:740:40")
        elif s["kind"] == "P":      # card: master crop 1120x800@400,0 scaled 0.75 to 840x600 at 1000,210 -> face box inside
            a = grab(OUT, PRE + t, n, "330:390:1255:240")
            b = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", MASTER, "-frames:v", str(n), "-vf",
                                         ("crop=980:700:470:0" if s.get("tight") else "crop=1120:800:400:0") + ",scale=840:600,crop=330:390:255:30,format=gray", "-f", "rawvideo", "-"])
            b = np.frombuffer(b, np.uint8).reshape(-1, 390, 330).astype(np.float32)
        else:
            c = WIDE[int(WIDX[s["f0"]])]; x, y, w, h = c["face"]; w, h = w // 2 * 2, h // 2 * 2
            sx = 420 if s["kind"] == "WS" else 0
            a = grab(OUT, PRE + t, n, f"{w}:{h}:{x + sx}:{y}"); b = grab("/home/claude/l04/wide/" + c["file"], t - c["a"], n, f"{w}:{h}:{x}:{y}")
        v = psnr(a, b); res.append((s["kind"], round(PRE + s["t0"], 1), round(float(np.median(v)), 1), round(float(v.min()), 1)))
    for k in ("W", "P", "WW", "WS"):
        r_ = [x for x in res if x[0] == k]
        if r_:
            print(k, len(r_), "shots: face PSNR median", np.median([x[2] for x in r_]), "worst shot", min(r_, key=lambda x: x[3]))
    bad = [x for x in res if x[3] < 36]
    print("shots under 36 dB:", bad)
