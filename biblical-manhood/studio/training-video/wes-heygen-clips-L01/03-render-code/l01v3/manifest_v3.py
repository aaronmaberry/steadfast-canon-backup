import json,csv,sys
sys.path.insert(0,'/workspace/l01v3/build');from tmap import s2o
B=json.load(open('broll_plan_v3.json'));V2=list(csv.DictReader(open('/workspace/artifacts/training/lesson-plan-2026-10-26/L01-build-2026-10-29/L01-P7-2026-10-29-v2/broll-manifest-v2.csv')))
v2={r['mixkit_id']:r for r in V2}
W=json.load(open('/workspace/artifacts/training/lesson-plan-2026-10-26/L01-audio-2026-10-29/v2/L01-A-Quiet-Tuesday-v2_words.json'))
from tmap import CUTS
W=[w for w in W if not any(a-0.03<=w['start']<b for a,b,_ in CUTS)]
CR={'px7841657':'RDNE Stock project','px28339282':'AP Vibes','px4297124':'August de Richelieu','px3051693':'Ricky Esquivel','px5534367':'Anna Shvets','px4052821':'Katrin Bolovtsova','px5029481':'Ketut Subiyanto','px8060562':'Ron Lach'}
fmt=lambda t:'%d:%05.2f'%(t//60,t%60)
rows=[]
for k,b in enumerate(B):
    i=b['id'];spoken=' '.join(w['word'] for w in W if b['a']<=w['start']<b['b'])
    if b['src']=='mixkit':
        r=v2[i];title=r['title'];page=r['page'];lic='Mixkit Stock Video Free License';lurl='https://mixkit.co/license/#videoFree';attr='Not required (credit to Mixkit appreciated). Verified from Mixkit licence text (mixkit.co/license/modal/videoFree/) 2026-11-02 ~08:58 CT';chk='item page free tag verified '+r['licence_checked']+' (v2); not re-fetched in v3 (Mixkit rate-limits this box)';creator='Mixkit'
    else:
        title=b['title'];page=b['page'];lic='Pexels License (free)';lurl='https://www.pexels.com/license/';attr='Not required (credit appreciated). Verified from pexels.com/license 2026-11-02 ~08:45 CT';chk='item page shows Free, fetched 2026-11-02 09:2x CT';creator=CR.get(i,'')
    rows.append(dict(n=k+1,out_in=fmt(s2o(b['a'])),out_out=fmt(s2o(b['b'])),dur_s=round(s2o(b['b'])-s2o(b['a']),2),source=b['src'],clip_id=i.replace('px',''),title=title,creator=creator,page=page,licence=lic,licence_url=lurl,attribution=attr,licence_checked=chk,clip_in_s=b['clip_in'],spoken_line=spoken,purpose=b['why'],v3_change=('REPLACED v2 clip %s'%b['replaced']) if b.get('replaced') else ('NEW (covers week cut D)' if i=='px8060562' else 'kept')))
w=csv.DictWriter(open('/workspace/l01v3/broll-manifest-v3.csv','w',newline=''),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows);print(len(rows))
