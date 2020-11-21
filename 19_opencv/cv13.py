import cv2

#拡大
img = cv2.imread("zophie.jpg")

height,width = img.shape[:2]

#2倍のサイズにする
dst = cv2.resize(img,(width *2, height * 2))

cv2.imwrite("img/double.jpg",dst)