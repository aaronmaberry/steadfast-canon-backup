#!/usr/bin/env python3
"""Closing music and credits slot (SHOW-BIBLE section 13, locked by Aaron 2026-10-03).
usage:
  python3 _build/credits.py scripts/E0xx-*.md ...   write or refresh the slot (idempotent)
  python3 _build/credits.py --check FILE            print a problem, or nothing if the slot is right
  python3 _build/credits.py --strip FILE            print FILE with the one allowed credits line removed (for lint)
The slot goes at the very end of the ## Script section, after the outro's last line:
  [CLOSING MUSIC 3s]
  [CREDITS]
  (Wes, normal credits volume, read like a producer credit. No gap, no ducking. SHOW-BIBLE section 13.)
  WES: Produced with AI voice and video tools."""
import sys,re
LINE="WES: Produced with AI voice and video tools."
NOTE="(Wes, normal credits volume, read like a producer credit. No gap, no ducking. SHOW-BIBLE section 13.)"
SLOT=f"[CLOSING MUSIC 3s]\n[CREDITS]\n{NOTE}\n{LINE}\n"
def split(s):
    head,rest=s.split('## Script',1)
    body,tail=rest.split('\n## Shorts',1)
    return head,body,tail
def clean(body):
    body=re.sub(r'\n*\[CLOSING MUSIC[^\]]*\]\n\[CREDITS\]\n(?:\([^\n]*\)\n)?WES: Produced with AI voice and video tools\.\n?','\n',body)
    return body.rstrip('\n')+'\n'
def apply(p):
    s=open(p).read(); head,body,tail=split(s)
    body=clean(body)+'\n'+SLOT
    open(p,'w').write(head+'## Script'+body+'\n## Shorts'+tail)
def check(p):
    s=open(p).read()
    if s.count('Produced with AI voice and video tools.')!=1: return f"the credits line appears {s.count('Produced with AI voice and video tools.')} times (need exactly 1)"
    head,body,tail=split(s)
    if not body.rstrip('\n').endswith(SLOT.rstrip('\n')): return "the slot is missing, changed, or not at the end of the script"
    spoken=[l for l in body.split('\n') if re.match(r'(WES|JONATHON):',l)]
    if spoken[-1]!=LINE: return "the credits line is not the last spoken line"
    return ''
def strip(p):
    s=open(p).read()
    return s.replace(SLOT,'',1) if not check(p) else s
if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='--check': print(check(a[1]),end='')
    elif a and a[0]=='--strip': sys.stdout.write(strip(a[1]))
    else:
        for p in a: apply(p); print(p.split('/')[-1][:4],'credits ok' if not check(p) else check(p))
