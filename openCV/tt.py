import numpy as np
import cv2
black=np.ones((300,300),dtype=np.uint8)
cv2.circle(black,(75,75),30,(255,255,255),-1)
cv2.circle(black,(117,117),30,(255,255,255),-1)
cv2.line(black,(200,200),(300,300),(255,255,255),1)
kernel=np.ones((5,5),np.uint8)
#OPENING
eroded=cv2.erode(black,kernel,iterations=2)
dilate=cv2.dilate(eroded,kernel,iterations=1)
cv2.imshow("eroded",eroded)
cv2.imshow("dilate",dilate)
cv2.imshow("OPENING",black)

#CLOSING
dilate=cv2.dilate(black,kernel,iterations=2)
eroded=cv2.erode(dilate,kernel,iterations=1)
cv2.imshow("eroded",eroded)
cv2.imshow("dilate",dilate)

cv2.imshow("CLOSING",black)
cv2.waitKey(0)