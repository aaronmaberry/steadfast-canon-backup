"""Mux the rendered picture with the narration and run the delivery checks."""
import subprocess, sys, json, pathlib
R = pathlib.Path("/home/claude/l04/render_1080")
OUT = pathlib.Path("/home/claude/l04/deliver/L04-Stop-Waiting-v3-1080p.mp4")
AUD = "/home/claude/l04/audio/l04_prog_m20.wav"


def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:]); raise SystemExit(1)
    return r


run(["ffmpeg", "-y", "-v", "error", "-i", str(R / "video.mp4"), "-i", AUD, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
     "-af", "pan=stereo|c0=0.7071*c0|c1=0.7071*c0", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", "-shortest", str(OUT)])
p = json.loads(run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate,nb_frames,duration:format=duration,size",
                    "-of", "json", str(OUT)]).stdout)
print(json.dumps(p, indent=1))
lo = run(["ffmpeg", "-v", "info", "-i", str(OUT), "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
print("\n".join(l for l in lo.splitlines()[-14:] if any(k in l for k in ("I:", "LRA:", "Peak:"))))
