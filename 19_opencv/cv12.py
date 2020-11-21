import cv2

#トリミング
img = cv2.imread("zophie.jpg")

x = 335
y = 345
width = 230
height = 230

#スライス
dst1 = img[y: (y + height), x: (x + width)]

cv2.imwrite("img/trim.jpg",dst1)