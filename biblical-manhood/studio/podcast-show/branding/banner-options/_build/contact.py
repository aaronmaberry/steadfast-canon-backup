import sys
sys.path.insert(0, '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/_build')
from bannerlib import font
from PIL import Image, ImageDraw
OUT = '/workspace/biblical-manhood/studio/podcast-show/branding/banner-options/'
titles = ['The table', 'Type only', 'Hill Country oak', 'Bible and coffee, line art', 'The road',
          'Dark studio mic', 'Brand-color field', 'Schedule strip', 'The walk', 'Book, mug and lamp (current art)']
TW, TH = 1000, 563; M = 50; LAB = 70
cols, rows = 2, 5
sheet = Image.new('RGB', (cols * TW + (cols + 1) * M, 150 + rows * (TH + LAB + M)), (24, 24, 28))
d = ImageDraw.Draw(sheet)
d.text((M, 40), 'Walk Steadfast  |  YouTube banner concepts  |  2026-10-03', font=font(48, 500), fill=(244, 244, 245))
d.text((M, 100), 'Red box = YouTube safe area (1546 x 423, shows on every device). Yellow band = desktop view (full width).', font=font(26, 400), fill=(161, 161, 170))
s = TW / 2560
for i in range(10):
    im = Image.open(OUT + f'banner-{i + 1:02d}.png').convert('RGB').resize((TW, TH), Image.LANCZOS)
    dd = ImageDraw.Draw(im)
    dd.rectangle((0, 508 * s, TW - 1, 931 * s), outline=(255, 200, 0), width=2)
    dd.rectangle((507 * s, 508 * s, 2053 * s, 931 * s), outline=(255, 60, 60), width=3)
    c, r = i % cols, i // cols
    x = M + c * (TW + M); y = 150 + r * (TH + LAB + M)
    d.text((x, y + 10), f'{i + 1:02d}', font=font(46, 600), fill=(139, 156, 255))
    d.text((x + 80, y + 20), titles[i], font=font(32, 450), fill=(230, 230, 235))
    sheet.paste(im, (x, y + LAB))
sheet.save(OUT + 'contact-sheet.png', optimize=True)
print(sheet.size)
