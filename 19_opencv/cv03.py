import numpy as np
import cv2

#円を描画する
img1 = np.zeros((500,500,3),np.uint8)
img1[:,:] = [255,255,255]
#cv2.circle(img,centeer,radius,color,thickness,lineType,shift)
cv2.circle(img1,(200,200),50,(255,0,0),1)
cv2.imwrite("img/circle1.jpg",img1)

img2 = np.zeros((500,500,3),np.uint8)
img2[:,:] = [255,255,255]
cv2.circle(img2,(200,200),50,(0,255,0),3)
cv2.imwrite("img/circle2.jpg",img2)

img3 = np.zeros((500,500,3),np.uint8)
img3[:,:] = [255,255,255]
#塗りつぶし
cv2.circle(img3,(200,200),50,(0,0,255),-1)
cv2.imwrite("img/circle3.jpg",img3)

