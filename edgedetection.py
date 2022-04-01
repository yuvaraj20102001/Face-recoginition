import cv2
import sys
import numpy as np
# vimg=cv2.imread("programingfiles/filter/input.jpg")
vimg=cv2.imread("vertical.jpg")
himg=cv2.imread("horizontal.jpg")
cv2.imshow("Vimg",vimg)
cv2.imshow("Himg",himg)

# # img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# # blur=cv2.GaussianBlur(img1,(3,3),sigmaX=0,sigmaY=0)
# '''PREWITT OPERATOR'''
Dx=np.array([[-1,0,1],[-5,0,5],[-1,0,1]])
Dy=np.array([[-1,-5,-1],[0,0,0],[1,5,1]])
prewitt1=cv2.filter2D(vimg,-1,Dx)
prewitt2=cv2.filter2D(himg,-1,Dy)
final=(np.square(prewitt1)+np.square(prewitt2))
cv2.imshow("Prewitt operator1",prewitt1)
cv2.imshow("Prewitt operator2",prewitt2)
'''CANNY operator'''
# canny=cv2.Canny(img,100,200)
# blurcanny=cv2.Canny(blur,50,200)
# cv2.imshow("Canny",canny)
# cv2.imshow("bCanny",blurcanny)
'''SOBEL OPERATOR'''
# sobelx=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
# sobely=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5)
# cv2.imshow("HElllo",sobelx)
# cv2.imshow("HElllOOO",sobely)
cv2.waitKey(0)