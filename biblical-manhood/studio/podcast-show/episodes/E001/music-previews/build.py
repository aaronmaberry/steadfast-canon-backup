import json,subprocess,os,re
from PIL import Image,ImageDraw,ImageFont
ART='/workspace/biblical-manhood/studio/podcast-show/launch-kit/art/LOCKED/walk-steadfast-art-A-3000.png'
GEIST='/usr/share/fonts/truetype/sand-box/google/Geist/Geist-VariableFont_wght.ttf'
P=[('A','Two chairs','A_two-chairs'),('B','Limestone','B_limestone'),('C','Dancehall waltz','C_dancehall-waltz'),('D','Pedal steel evening','D_pedal-steel-evening'),('E','1604 at night','E_1604-at-night')]
os.makedirs('work',exist_ok=True)
base=Image.open(ART).convert('RGB').resize((1080,1080),Image.LANCZOS)
def frame(text,out):
    im=base.copy().convert('RGBA');ov=Image.new('RGBA',im.size,(0,0,0,0));d=ImageDraw.Draw(ov)
    for y in range(900,1080):  # soft bottom shade for legibility
        a=int(150*((y-900)/180)**1.5);d.line([(0,y),(1080,y)],fill=(7,7,10,a))
    im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
    f=ImageFont.truetype(GEIST,40)
    try: f.set_variation_by_axes([500])
    except Exception: pass
    w=d.textlength(text,font=f);d.text(((1080-w)/2,1000),text,font=f,fill=(244,244,245))
    im.convert('RGB').save(out)
def norm(src,dst,pre_silence=0.0):
    af=f"atrim=0:30,asetpts=N/SR/TB,afade=t=out:st=29:d=1"
    if pre_silence: af+=f",adelay={int(pre_silence*1000)}:all=1"
    e=subprocess.run(['ffmpeg','-hide_banner','-i',src,'-af',af+',loudnorm=I=-16:TP=-1.5:LRA=20:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
    j=json.loads(e[e.rindex('{'):e.rindex('}')+1])
    ln=f"loudnorm=I=-16:TP=-1.5:LRA=20:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-af',af+','+ln+',aresample=48000','-ac','2','-c:a','pcm_s16le',dst],check=True)
def mp4(img,wav,out):
    dur=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',wav],capture_output=True,text=True).stdout.strip()
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',img,'-i',wav,'-t',dur,'-c:v','libx264','-tune','stillimage','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out],check=True)
for L,name,stem in P:
    cap=f'{L}. {name}';frame(cap,f'work/{stem}.png')
    norm(f'raw/{stem}.mp3',f'work/{stem}.wav');mp4(f'work/{stem}.png',f'work/{stem}.wav',f'{stem}.mp4')
    if L!='A': norm(f'raw/{stem}.mp3',f'work/{stem}_gap.wav',1.5)
# combined: A (30 s), then B-E each with 1.5 s lead gap, caption per section
lst=open('work/concat.txt','w')
for L,name,stem in P:
    w=f'work/{stem}.wav' if L=='A' else f'work/{stem}_gap.wav'
    mp4(f'work/{stem}.png',w,f'work/seg_{stem}.mp4');lst.write(f"file 'seg_{stem}.mp4'\n")
lst.close()
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','work/concat.txt','-c','copy','-movflags','+faststart','walk-steadfast-music-previews-A-E.mp4'],check=True)
