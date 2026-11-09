#!/usr/bin/env python3
"""Refuse finalize if any chunk is missing or short (L02 OOM lesson)."""
import os,sys,json,subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
WORK=os.environ.get('LESSON_WORK', os.path.dirname(HERE))
E=json.load(open(f'{WORK}/p7/edl.json'))
N=int(round(E['end']*25))
K=int(os.environ.get('CHUNKS', '16'))
S=(N+K-1)//K
bad=0
for i in range(K):
    a=i*S; b=min((i+1)*S,N); exp=b-a
    o=f'{WORK}/p7/chunks/c{i:02d}.mp4'
    if not os.path.isfile(o) or os.path.getsize(o)<1000:
        print(f'{o} missing/empty expected {exp} BAD -> delete it and re-run run_chunks.sh'); bad+=1; continue
    try:
        n=int(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-count_packets','-show_entries','stream=nb_read_packets','-of','csv=p=0',o],text=True).strip() or '0')
    except Exception:
        n=0
    if n!=exp:
        print(f'{o} {n} expected {exp} BAD -> delete it and re-run run_chunks.sh'); bad+=1
        try: os.remove(o)
        except: pass
    else:
        print(f'{o} {n} expected {exp} OK')
sys.exit(1 if bad else 0)
