from PIL import Image,ImageDraw,ImageFont

im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)
#テキストを描画する
draw.text((20,150),'Hello', fill='purple')
arial_font = ImageFont.truetype('arial.ttf',32)
draw.text((100,150), 'Howdy', fill='gray', font=arial_font)

im.save('data/text.png')