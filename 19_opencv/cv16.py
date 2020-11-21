import cv2

#回転
img = cv2.imread("zophie.jpg")
height,width = img.shape[:2]
center = (int(width / 2),int(height / 2))
size = (width,height)

#45度
rot45 = cv2.getRotationMatrix2D(center,45.0,1.0)
dst1 = cv2.warpAffine(img,rot45,size,flags=cv2.INTER_CUBIC)
cv2.imwrite("img/rot45.jpg",dst1)


