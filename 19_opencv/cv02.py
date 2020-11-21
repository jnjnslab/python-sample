import numpy as np
import cv2

#新規に画像を生成する
img1 = np.zeros((500,500,3),np.uint8)
img1[:,:] = [255,0,0]
cv2.imwrite("img/blue_img.jpg",img1)

img2 = np.zeros((500,500,3),np.uint8)
img2[:,:] = [0,255,0]
cv2.imwrite("img/green_img.jpg",img2)

img3 = np.zeros((500,500,3),np.uint8)
img3[:,:] = [0,0,255]
cv2.imwrite("img/red_img.jpg",img3)

img4 = np.zeros((500,500,3),np.uint8)
img4[:,:] = [255,255,255]
cv2.imwrite("img/white_img.jpg",img4)
