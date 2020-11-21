from PIL import Image

cat_im = Image.open('zophie.png')
#画像を切り抜く
cropped_im = cat_im.crop((335,345,565,560))
cropped_im.save('data/cropped.png')
