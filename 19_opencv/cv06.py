import cv2

#画像を読み込む
img = cv2.imread("zophie.jpg")
#RGB成分を分離する
blue,green,red = cv2.split(img)

#画像を保存する
cv2.imwrite("img/blue.jpg",blue)
cv2.imwrite("img/green.jpg",green)
cv2.imwrite("img/red.jpg",red)