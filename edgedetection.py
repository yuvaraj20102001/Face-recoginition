import cv2
import sys

img=cv2.imread("programingfiles/filter/input.jpg")

print(sys.getsizeof(img))

img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blur=cv2.GaussianBlur(img1,(3,3),sigmaX=0,sigmaY=0)
canny=cv2.Canny(img,100,200)
blurcanny=cv2.Canny(blur,50,200)
cv2.imshow("Canny",canny)
cv2.imshow("bCanny",blurcanny)
sobelx=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
sobely=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5)
cv2.imshow("HElllo",sobelx)
cv2.imshow("HElllOOO",sobely)
cv2.waitKey(0)