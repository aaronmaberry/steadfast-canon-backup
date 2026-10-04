exec(open('qa/tag.py').read().split('for f in sorted')[0])
for f in sorted(glob.glob('raw/*.mp3')):
    b=os.path.basename(f);a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.float32)
    print('==',b)
    for s in range(0,len(a)-16000*2,16000*3):
        x=fe(a[s:s+16000*4],sampling_rate=16000,return_tensors='pt')
        with torch.no_grad(): p=torch.sigmoid(m(**x).logits)[0].numpy()
        t=[i for i in np.argsort(-p)[:7] if lab[i] not in ('Music','Musical instrument')][:5]
        print(f'  {s//16000:2d}s',', '.join(f'{lab[i]} {p[i]:.2f}' for i in t))
