import json,sys,numpy as np
sys.path.insert(0,'/workspace/l01v2/build');from tmap import s2o
sr=48000;x=np.fromfile('wc.f32',np.float32)
def rms(t,w=0.01):
    i=int(t*sr);s=x[i-int(w*sr/2):i+int(w*sr/2)];return 20*np.log10(np.sqrt(np.mean(s**2))+1e-12)
# (label, src a-window, src b-window, text removed)
C=[('A',(36.92,37.00),(37.56,38.0),'this week.'),
   ('B',(197.67,197.81),(198.35,198.62),'this week,'),
   ('C',(263.46,264.0),(267.46,268.04),'That weekend retreat where you came home feeling like a new man.'),
   ('D',(626.99,627.08),(627.80,628.13),'for a week,')]
out=[]
for lab,(a0,a1),(b0,b1),txt in C:
    A=np.arange(s2o(a0),s2o(a1),0.002);B=np.arange(s2o(b0),s2o(b1),0.002)
    ra=[rms(t) for t in A];rb=[rms(t) for t in B]
    print(lab,'a-window min %.1f dB at %.3f'%(min(ra),A[int(np.argmin(ra))]),' b-window min %.1f at %.3f'%(min(rb),B[int(np.argmin(rb))]))
    # floor profile
    print('  a-win profile',' '.join('%.0f'%rms(t) for t in np.arange(s2o(a0)-0.03,s2o(a1)+0.03,0.01)))
    print('  b-win profile',' '.join('%.0f'%rms(t) for t in np.arange(s2o(b0)-0.03,s2o(b1)+0.03,0.01)))
