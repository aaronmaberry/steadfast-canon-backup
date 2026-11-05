"""After a re-render: every segment shares one SPS/PPS set, the final file decodes cleanly, size under the send limit."""
import subprocess, collections, os
S = "/tmp/claude-0/-home-claude/ec4db402-e33d-5ed2-8630-a6cf6640e0f1/scratchpad"
OUT = "/home/claude/l04/deliver/L04-Stop-Waiting-v3-1080p.mp4"


def h(f):
    out = subprocess.run([S + "/hdr.sh", f], capture_output=True, text=True).stdout.splitlines()
    return "\n".join(l for l in out if " " in l and not l.split()[0].isdigit() and "(" not in l)


files = [l.strip()[6:-1] for l in open("/home/claude/l04/render_1080/list.txt")]
g = collections.Counter(h(f) for f in files)
print(len(files), "segments ->", len(g), "distinct SPS/PPS (must be 1)")
r = subprocess.run(["ffmpeg", "-v", "error", "-i", OUT, "-f", "null", "-"], capture_output=True, text=True)
print("decode error lines:", len([l for l in r.stderr.splitlines() if l.strip()]))
print("size MiB", round(os.path.getsize(OUT) / 1048576, 1))
