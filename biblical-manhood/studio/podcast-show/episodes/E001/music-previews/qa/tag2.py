exec(open('qa/tag.py').read().split('for f in sorted')[0])
chk={'B_limestone.mp3':['Speech','Singing','Male speech, man speaking','Acoustic guitar','Strum','Double bass'],
     'C_dancehall-waltz.mp3':['Accordion','Organ','Harmonica','Guitar','Double bass','Drum','Waltz','Singing'],
     'D_pedal-steel-evening.mp3':['Steel guitar, slide guitar','Acoustic guitar','Strum','Drum','Snare drum','Double bass'],
     'E_1604-at-night.mp3':['Electric guitar','Drum','Bass drum','Snare drum','Double bass','Heart sounds, heartbeat'],
     'A_two-chairs.mp3':['Cello','Double bass','Guitar','Acoustic guitar','Pizzicato']}
for f in sorted(glob.glob('raw/*.mp3')):
    b=os.path.basename(f);a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.float32)
    rows=[]
    for s in range(0,len(a)-16000*2,16000*3):
        x=fe(a[s:s+16000*4],sampling_rate=16000,return_tensors='pt')
        with torch.no_grad(): p=torch.sigmoid(m(**x).logits)[0].numpy()
        rows.append((s//16000,p))
    print('==',b)
    for w in chk[b]:
        print(f'  {w:28s}',' '.join(f'{p[idx[w]]:.2f}' for _,p in rows))
