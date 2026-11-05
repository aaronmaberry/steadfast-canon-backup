"""Program audio: the master's own narration, 4.0 s silent open, one continuous track at -20.0 LUFS (+/-0.1).
usage: python3 plan/prog_audio.py            -> audio/lNN_prog_m20.wav (length = picture + pre-roll, rounded up)
The gain is found by measuring (L03 needed +6 dB, L04 +9.1 dB): never assume last lesson's number."""
import pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "edit"))
ROOT = pathlib.Path(__file__).resolve().parents[1]; L = ROOT.name
NARR = ROOT / "audio/narr_raw.wav"; OUT = ROOT / f"audio/{L}_prog_m20.wav"
import layout                                      # picture length from the cut
dur = int(layout.build()[-1]["t1"] + 4.0) + 1


def make(g):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(NARR), "-af",
                    f"adelay=4000,apad=whole_dur={dur},highpass=f=70,volume={g:.2f}dB,alimiter=limit=0.84:level=false",
                    "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(OUT)], check=True)
    e = subprocess.run(["ffmpeg", "-nostats", "-i", str(OUT), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    s = e[e.rindex("Summary:"):]
    return float(re.search(r"I:\s+(-?[\d.]+)", s).group(1)), float(re.search(r"Peak:\s+(-?[\d.]+)", s).group(1))


g = 6.0
for _ in range(6):
    I, pk = make(g)
    if abs(I + 20.0) <= 0.05:
        break
    g += -20.0 - I
print(f"{OUT.name}: gain {g:+.2f} dB, {I} LUFS, true peak {pk} dBFS, {dur} s")
assert abs(I + 20.0) <= 0.1, "loudness off target"
