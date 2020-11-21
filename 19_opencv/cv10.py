import cv2
import numpy as np

#画像を読み込む
img = cv2.imread("zophie.jpg")
#ぼかす(GaussianBlur)
blur = cv2.GaussianBlur(img,ksize=(5,5),sigmaX=1.3)  #カーネルサイズ5X5

#画像を保存する
cv2.imwrite("img/gaussianblur.jpg",blur)
