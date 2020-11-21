from PIL import Image

cat_im = Image.open('zophie.png')
#回転
cat_im.rotate(90).save('data/rotated90.png')
cat_im.rotate(180).save('data/rotated180.png')
cat_im.rotate(270).save('data/rotated270.png')

cat_im.rotate(6).save('data/rotated6.png')
cat_im.rotate(6, expand=True).save('data/rotated6_expanded.png')
#左右反転
cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('data/horizontal_flip.png')
#上下反転
cat_im.transpose(Image.FLIP_TOP_BOTTOM).save('data/vertical_flip.png')
