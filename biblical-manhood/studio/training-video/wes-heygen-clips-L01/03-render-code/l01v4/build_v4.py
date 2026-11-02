"""v4 EDL from v3: (a) per bubble run crop choice (wide 680x800 only if hand check allows), (b) MED 1280x720 card on WES_FULL framing
segments inside hand-free stretches >=5 s, (c) hide C fades out in the pause after 'job.' (1-frame), not during the word."""
import json,sys
sys.path.insert(0,'/workspace/l01v4/build')
from tmap import s2o
E=json.load(open('/workspace/l01v3/build/edl_v3.json'))
H={int(k):v for k,v in json.load(open('/workspace/l01v3/qc/hp0.json')).items()}
IX={s['id']:s for s in E['shots']}
MARG=0
def handsec(box,a,b):
    x0,y0,x1,y1=box;x0-=MARG;y0-=MARG;x1+=MARG;y1+=MARG;c=0;n=0
    for f in range(int(a*25)//5*5,int(b*25)+1,5):
        if f not in H:continue
        n+=1;c+=any(min(x1,q[2])-max(x0,q[0])>0 and min(y1,q[3])-max(y0,q[1])>0 for q in H[f]['h'])
    return c*0.2,n
NARROW=(660,-10,600,706);WIDE=(620,-40,680,800)
box=lambda c:(c[0],max(c[1],0),c[0]+c[2],c[1]+c[3])
E['bubble_crop']=[]
for a,b in E['bubble_runs']:
    t0,t1=IX[a]['t0x'],IX[b]['t1x'];hn,_=handsec(box(NARROW),t0,t1);hw,_=handsec(box(WIDE),t0,t1)
    pick=WIDE if hw-hn<=2.5 else NARROW
    E['bubble_crop'].append(dict(run=[a,b],t0=t0,t1=t1,crop=pick,hand_narrow=hn,hand_wide=hw))
    print('bubble run',a,b,round(t1-t0,1),'s hand narrow',hn,'wide',hw,'->','WIDE' if pick==WIDE else 'narrow')
MED=(320,0,1280,720)
fr=E['framing'];
for f in fr:f['hf']=handsec(box(MED),f['a'],f['b'])[0]==0
# stretches: consecutive hand-free segments of the same shot, contiguous
i=0;nmed=0;tmed=0
while i<len(fr):
    j=i
    while j+1<len(fr) and fr[j+1]['shot']==fr[i]['shot'] and abs(fr[j+1]['a']-fr[j]['b'])<0.05 and fr[j]['hf'] and fr[j+1]['hf']:j+=1
    if fr[i]['hf'] and fr[j]['b']-fr[i]['a']>=5:
        for k in range(i,j+1):fr[k]['f']=['MED',1.0,0];nmed+=1;tmed+=fr[k]['b']-fr[k]['a']
    i=j+1
print('MED segments',nmed,'of',len(fr),'MED s',round(tmed,1),'CARD s',round(sum(f['b']-f['a'] for f in fr if f['f'][0]=='CARD'),1))
sw=sum(1 for k in range(1,len(fr)) if fr[k]['shot']==fr[k-1]['shot'] and abs(fr[k]['a']-fr[k-1]['b'])<0.05 and fr[k]['f'][0]!=fr[k-1]['f'][0]);print('in-shot CARD<->MED switches',sw)
for w in E['hide']:
    if 'AUDIO CUT C' in str(w['why']):w['a']=263.56;w['ramp_in']=0.04
json.dump(E,open('/workspace/l01v4/build/edl_v4.json','w'),indent=1)
# (d) WES_FULL is now the HeyGen wide take; SPLIT/bubble stay on the old take -> no morph across takes. Morph -> dip (in the word gap) or hard.
nd=nh=0
for c in E['cuts']:
    if c['type']!='morph':continue
    g0,g1=c['gap'];h=min(0.30,(g1-g0-0.06)/2,c['cut']-g0-0.03,g1-c['cut']-0.03)
    if h>=0.18:
        s_,e_=c['cut']-h,c['cut']+h;L=e_-s_;c.update(type='dip',s=s_,e=e_,out=[s_,s_+0.4*L],empty=[s_+0.4*L,s_+0.6*L],inn=[s_+0.6*L,e_]);nd+=1
    else:
        c.update(type='hard',s=c['cut'],e=c['cut']);nh+=1
from collections import Counter
print('morph->dip',nd,'morph->hard',nh,Counter(c['type'] for c in E['cuts']))
json.dump(E,open('/workspace/l01v4/build/edl_v4.json','w'),indent=1)
