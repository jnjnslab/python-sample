from PIL import Image

cat_im = Image.open('zophie.png')
cat_im_width,cat_im_height = cat_im.size
#サイズを変更する
quaterized_im = cat_im.resize((int(cat_im_width / 2), int(cat_im_height / 2)))
quaterized_im.save('data/quaterized.png')

svelte_im = cat_im.resize((cat_im_width, cat_im_height + 300))
svelte_im.save('data/svelte.png')
#サムネイルの作成
thumb_im = cat_im.copy()
print(thumb_im.size)
thumb_im.thumbnail((100,100))
thumb_im.save('data/thumbnail.png')