import cv2
import numpy as np

#画像を読み込む
img = cv2.imread("zophie.jpg")
#ビットを反転する
inv = cv2.bitwise_not(img)

#画像を保存する
cv2.imwrite("img/inv.jpg",inv)
