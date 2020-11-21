import cv2

#画像を読み込む
img = cv2.imread("zophie.jpg")
#色をグレースケールに変換する
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#画像を表示する
#cv2.imshow("gray",gray)
#cv2.waitKey(0)
#画像を保存する
cv2.imwrite("img/gray.jpg",gray)
