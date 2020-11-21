import cv2
import numpy as np

#画像を読み込む
img = cv2.imread("zophie.jpg")
#ぼかす
blur = cv2.blur(img,(5,5))  #カーネルサイズ5X5

#画像を保存する
cv2.imwrite("img/blur.jpg",blur)
