import numpy as np
import cv2

img1=100*np.ones((300,300),np.uint8)
img2=100*np.ones((300,300),np.uint8)
img1=cv2.rectangle(img1,(150,0),(300,300),(255,0,255),-1)
img1=cv2.line(img1,(100,0),(200,200),(255,0,255),1)
img2=cv2.line(img2,(100,0),(200,200),(255,0,255),1)

img2=cv2.rectangle(img2,(0,150),(300,300),(255,0,255),-1)
# cv2.imshow("imshow",img2)
cv2.waitKey(0)