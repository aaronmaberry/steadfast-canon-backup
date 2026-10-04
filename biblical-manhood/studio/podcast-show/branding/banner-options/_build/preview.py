import sys
from PIL import Image, ImageDraw
OUT='/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/'
for n in sys.argv[1:]:
    im=Image.open(OUT+f'banner-{int(n):02d}.png').convert('RGB')
    d=ImageDraw.Draw(im); d.rectangle((507,508,2053,931),outline=(255,60,60),width=4); d.rectangle((0,508,2559,931),outline=(255,200,0),width=3)
    im.resize((1280,720)).save(f'/tmp/p{int(n):02d}.png')
