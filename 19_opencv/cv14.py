import cv2

#縮小
img = cv2.imread("zophie.jpg")

height,width = img.shape[:2]

#1/2倍のサイズにする
dst = cv2.resize(img,(int(width / 2), int(height / 2)))

cv2.imwrite("img/half.jpg",dst)