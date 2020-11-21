import cv2

#反転
img = cv2.imread("zophie.jpg")

#上下反転
dst1 = cv2.flip(img,0)
cv2.imwrite("img/af01.jpg",dst1)

#左右反転
dst2 = cv2.flip(img,1)
cv2.imwrite("img/af02.jpg",dst2)

#上下左右反転
dst3 = cv2.flip(img,-1)
cv2.imwrite("img/af03.jpg",dst3)
