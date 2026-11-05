"""Caption-change QC sheet: every band -> band change in the delivered file, 5 frames each (+0.04 .. +0.32 s).
usage: python3 edit/bandcheck.py deliver/<file>.mp4 OUTDIR
Look at every sheet: each row must read old line -> fading -> EMPTY -> new line fading in -> new line. Two lines on top of
each other in any frame = FAIL (Aaron, L03 6:24, Nov 5 2026)."""
import pathlib, subprocess, sys
import layout
F, D = sys.argv[1], pathlib.Path(sys.argv[2]); D.mkdir(parents=True, exist_ok=True)
T = []
for s in layout.build():
    b = s.get("bands") or s.get("label") or []
    T += [t2 for (t1, k1), (t2, k2) in zip(b, b[1:]) if k1 and k2 and t2 > s["t0"] + 0.02]
rows = []
for i, t in enumerate(T):
    fs = []
    for j, d in enumerate((0.04, 0.10, 0.16, 0.24, 0.32)):
        o = D / f"{i:02d}_{j}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{4 + t + d:.3f}", "-i", F, "-frames:v", "1",
                        "-vf", "crop=1600:240:160:800,scale=400:-2", "-y", str(o)], check=True); fs.append(str(o))
    r = D / f"row{i:02d}.png"
    subprocess.run(["ffmpeg", "-v", "error", *sum([["-i", x] for x in fs], []), "-filter_complex", "hstack=5", "-y", str(r)], check=True)
    rows.append(str(r))
for g in range(0, len(rows), 10):
    part = rows[g:g + 10]
    subprocess.run(["ffmpeg", "-v", "error", *sum([["-i", x] for x in part], []), "-filter_complex",
                    f"vstack={len(part)}" if len(part) > 1 else "null", "-y", str(D / f"sheet{g // 10}.png")], check=True)
print(len(T), "band changes ->", sorted(str(p) for p in D.glob("sheet*.png")))
