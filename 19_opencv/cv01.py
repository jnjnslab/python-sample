import cv2

#画像を読み込む
img = cv2.imread("zophie.jpg")
height,width = img.shape[:2]
print("width:" + str(width))
print("height:" + str(height))
#画像を表示する
cv2.imshow("img",img)

cv2.waitKey(0)