#!/usr/bin/env python3
"""Build p7/inputs.json from master video + wide_rendered.json + lesson.json."""
import os,sys,json,subprocess
WORK=os.environ.get('LESSON_WORK','/workspace/l08')
LC=json.load(open(os.environ.get('LESSON_JSON',f'{WORK}/lesson.json')))
B=LC['build'].rstrip('/')
master=sys.argv[1]
wide_json=sys.argv[2]
outdir=sys.argv[3] if len(sys.argv)>3 else f'{WORK}/p7'
os.makedirs(outdir, exist_ok=True)
words=f"{B}/audio/job/{LC['audio_name']}_words.json"
audio=f"{B}/audio/job/delivery/{LC['audio_name']}-minus26-LUFS.wav"
assert os.path.isfile(words), words
assert os.path.isfile(audio), audio
# duration from wav
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',audio],text=True).strip())
wide=json.load(open(wide_json)) if os.path.getsize(wide_json)>2 else []
# normalize wide entries
segs=[]
for w in wide:
    segs.append(dict(path=w.get('video') or w.get('path'), t0=float(w.get('a', w.get('t0'))), t1=float(w.get('b', w.get('t1')))))
cover=f"{B}/heygen/qc/cover_master.json"
inp=dict(
    words=words, audio=audio, audio_dur=dur,
    out=f'{outdir}/edl.json', edl=f'{outdir}/edl.json',
    broll=f'{WORK}/broll/manifest.json',
    wes_master=dict(type='video', path=master),
    wes_wide=segs,
    track=f'{outdir}/track.json',
    cover=cover if os.path.isfile(cover) else None,
    stills=f'{outdir}/stills',
    crf=16, face=None,
    lesson=LC,
)
json.dump(inp, open(f'{outdir}/inputs.json','w'), indent=1)
print(f'wrote {outdir}/inputs.json {len(segs)} wide segs')
