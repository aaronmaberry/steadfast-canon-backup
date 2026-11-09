"""Check staged HeyGen downloads (LNNW-<id>.mp4 wides, or a joined master) against in/etags.txt
(id size etag per line; etag = S3 ETag: md5 of 8 MiB part md5s + "-N", or a plain md5 for a single-part upload).
usage: python3 plan/verify_heygen.py               -> moves matching LNNW-*.mp4 from the staging folder into wide/
       python3 plan/verify_heygen.py master FILE   -> checks the joined master"""
import hashlib, os, pathlib, shutil, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]; NN = ROOT.name[1:]
UP = "/mnt/user-data/uploads/Downloads"
rows = [l.split() for l in open(ROOT / "in/etags.txt") if l.strip()]
exp = {r[1]: (r[0], int(r[2]), r[3]) for r in rows}


def etag(p, multi):
    md, whole = [], hashlib.md5()
    with open(p, "rb") as f:
        while (b := f.read(8 << 20)):
            md.append(hashlib.md5(b).digest()); whole.update(b)
    return hashlib.md5(b"".join(md)).hexdigest() + f"-{len(md)}" if multi else whole.hexdigest()


def ok(p, i):
    k, size, want = exp[i]
    if os.path.getsize(p) != size:
        return k, f"size {os.path.getsize(p)} != {size}"
    got = etag(p, "-" in want)
    return k, "MATCH" if got == want else f"MISMATCH {got} != {want}"


if sys.argv[1:2] == ["master"]:
    mid = [r[1] for r in rows if r[0] == "master"][0]
    print(*ok(sys.argv[2], mid)); sys.exit(0)
for f in sorted(os.listdir(UP)):
    if f.startswith(f"L{NN}W-") and f.endswith(".mp4"):
        k, res = ok(f"{UP}/{f}", f[5:-4]); print(k, res)
        if res == "MATCH":
            shutil.move(f"{UP}/{f}", ROOT / "wide" / f)
have = {f[5:-4] for f in os.listdir(ROOT / "wide") if f.endswith(".mp4")}
print("verified:", len(have), "| missing:", sorted(v[0] for i, v in exp.items() if i not in have and v[0] != "master"))
