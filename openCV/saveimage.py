import numpy as np
import cv2

img=cv2.imread('filter/rect.png')
# img1=100*np.ones((300,300),np.uint8)
# img2=100*np.ones((300,300),np.uint8)
print(img.shape)
img2=cv2.rectangle(img,(400,400),(600,500),(255,0,255),-1)
# img1=cv2.circle(img1,(100,0),(200,200),(255,0,255),1)
img2=cv2.line(img,(100,100),(300,100),(0,0,0),1)

img2=cv2.line(img,(350,100),(500,100),(0,0,0),1)
cv2.imwrite("rect3.jpg",img)

# img2=cv2.rectangle(img2,(0,150),(300,300),(255,0,255),-1)
cv2.imshow("imshow",img2)
cv2.waitKey(0)