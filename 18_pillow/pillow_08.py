from PIL import Image,ImageDraw,ImageFont

im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)

jfont = ImageFont.truetype('msmincho.ttc',24,index=1)
draw.text((20,20),'こんにちは',fill='black',font=jfont)

jfont = ImageFont.truetype('msgothic.ttc',24,index=2)
draw.text((20,50),'こんにちは',fill='black',font=jfont)

jfont = ImageFont.truetype('meiryo.ttc',24,index=0)
draw.text((20,80),'こんにちは',fill='black',font=jfont)

im.save('data/jtext.png')