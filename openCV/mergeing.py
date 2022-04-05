import numpy as np
import cv2

img1=cv2.imread("horizontal.jpg")
img2= cv2.imread("vertical.jpg")
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

merged=np.hstack((img1,img2))
cv2.imshow("merged",merged)
img=(img1+img2)
cv2.imshow("Averaged",img)
cv2.waitKey(0)