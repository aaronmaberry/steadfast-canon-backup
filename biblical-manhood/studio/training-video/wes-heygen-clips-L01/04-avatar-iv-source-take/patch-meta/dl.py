import sys;TK=sys.argv[1] if len(sys.argv)>1 else "t1"
import re,glob,json,subprocess,os
W=json.load(open('windows.json'));m={w.get(TK):w["id"] for w in W if w.get(TK)}
for f in glob.glob('/workspace/agent-tools/*.txt'):
  t=open(f).read()
  for u in re.findall(r'https://files2\.heygen\.ai/\S+?\.mp4\?\S+',t):
    vid=re.search(r'/([0-9a-f]{32})\.mp4',u).group(1)
    if vid in m and not os.path.exists(f'{TK}_{m[vid]}.mp4'):
      subprocess.run(['curl','-s','-o',f'{TK}_{m[vid]}.mp4',u.rstrip('`"\'')]);print('got',m[vid])
