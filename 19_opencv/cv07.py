import cv2
import numpy as np

#画像を読み込む
img = cv2.imread("zophie.jpg")
height,width = img.shape[:2]
#同じ大きさのゼロデータを作成する
zeros = np.zeros((height,width),img.dtype)
#RGB成分を分離する
blue,green,red = cv2.split(img)
#分離した色成分とゼロデータを合成する
blue = cv2.merge((blue,zeros,zeros))
green = cv2.merge((zeros,green,zeros))
red = cv2.merge((zeros,zeros,red))

#画像を保存する
cv2.imwrite("img/blue.jpg",blue)
cv2.imwrite("img/green.jpg",green)
cv2.imwrite("img/red.jpg",red)