import sys
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
from bannerlib import font
from PIL import Image, ImageDraw
A='/workspace/biblical-manhood/studio/podcast-show/launch-kit/art/'
V=[('A','Photo, wordmark in the sky','RECOMMENDED'),('B','Typographic, road line',''),('C','Photo, dark top panel with tagline','')]
W=3*900+4*60; H=1500
im=Image.new('RGB',(W,H),(24,24,28)); d=ImageDraw.Draw(im)
d.text((60,40),'Walk Steadfast show art, 3000 x 3000. Thumbnail rows at 150, 90 and 60 px on dark and light app backgrounds.',font=font(30,500),fill=(230,230,235))
for i,(k,label,tag) in enumerate(V):
    x=60+i*960; src=Image.open(A+f'walk-steadfast-art-{k}-3000.png').convert('RGB')
    im.paste(src.resize((900,900),Image.LANCZOS),(x,110))
    d.text((x,1030),f'{k}. {label}',font=font(32,600),fill=(244,244,245))
    if tag: d.text((x,1075),tag,font=font(26,650),fill=(139,156,255))
    # thumbnails on dark and light
    for row,bg in enumerate([(0,0,0),(242,242,247)]):
        y=1130+row*175; d.rectangle((x,y,x+900,y+165),fill=bg)
        xx=x+10
        for s in (150,90,60):
            im.paste(src.resize((s,s),Image.LANCZOS),(xx,y+(165-s)//2)); xx+=s+30
im.save(A+'contact-sheet.png',optimize=True); im.convert('RGB').save(A+'contact-sheet.jpg',quality=90)
print(im.size)
