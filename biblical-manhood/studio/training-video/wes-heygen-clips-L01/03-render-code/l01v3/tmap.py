import json
AC=json.load(open('/workspace/l01v3/audio/audio_cuts_v3.json'))
CUTS=[(c['a'],c['b'],c['L']) for c in AC['src_cuts']]   # src(approved-audio) intervals removed; 3 from v2 + 4 week cuts v3
def s2o(ts):
    d=0
    for a,b,L in CUTS:
        if ts>=b:d+=L
        elif ts>a:d+=ts-a
    return ts-d
def o2s(to):
    d=0
    for a,b,L in CUTS:
        if to+d>=a:d+=L
    return to+d
OUT_END=AC['out_len']
