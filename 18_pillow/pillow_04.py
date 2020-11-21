from PIL import Image

cat_im = Image.open('zophie.png')

cat_copy_im = cat_im.copy()
face_im = cat_im.crop((335,345,565,560))
print(face_im.size)
cat_copy_im.paste(face_im,(0,0))
cat_copy_im.paste(face_im,(400,500))
cat_copy_im.save('data/pasted.png')

