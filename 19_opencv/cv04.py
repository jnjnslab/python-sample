import numpy as np
import cv2

#文字を表示する
img = np.zeros((500,500,3),np.uint8)
img[:,:] = [255,255,255]
#cv3.putText(img,text,文字の左下座標,フォントの種類,フォントのスケールファクター,文字の色,線を描画するアルゴリズム,画像データの原点が左上か)
img = cv2.putText(img,'ABCDE',(100,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)

cv2.imwrite("img/text.jpg",img)
