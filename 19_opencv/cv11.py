import cv2
import numpy as np

#画像を読み込む
img = cv2.imread("zophie.jpg")
#ぼかす(bilateralFilter)
bila = cv2.bilateralFilter(img,9,75,75)

#画像を保存する
cv2.imwrite("img/bilateral.jpg",bila)
