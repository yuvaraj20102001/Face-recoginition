import cv2
from cv2 import THRESH_BINARY 
import numpy as np

def arrange_points(approx):
  approx=approx.reshape(4,2)
  newapprox=np.zeros((4,2),dtype=np.float32)
  print(approx)
  add=approx.sum(1)
  newapprox[0]=approx[np.argmin(add)]
  newapprox[2]=approx[np.argmax(add)]
  print(newapprox)
  print(add)
  diff=np.diff(approx,axis=1)
  newapprox[1]=approx[np.argmin(diff)]
  newapprox[3]=approx[np.argmax(diff)]
  print(diff)
  print(newapprox)
  return newapprox

doc=cv2.imread("filter/docs.jpg")
print(doc.shape)
grayimg=cv2.cvtColor(doc,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(grayimg,(7,7),sigmaX=1)
_,thresh=cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY)
edged=cv2.Canny(thresh,50,150)

contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
max=cv2.contourArea(contours[0])
for contour in contours[1:]:
  if(cv2.contourArea(contour)>max):
    max=cv2.contourArea(contour)

print(max)

for contour in contours:
  #area=cv2.contourArea(contour)
  print(cv2.contourArea(contour))
  arclen=cv2.arcLength(contour,True)
  approx=cv2.approxPolyDP(contour,0.01*arclen,True)
  if(len(approx)==4 and cv2.contourArea(contour)==max):
    #cv2.drawContours(doc,[contour],0,(0,0,255),2)
    (A,B,C,D)=arrange_points(approx)
    AB=pow(((B[0]-A[0])**2)+((B[1]-A[1])**2),0.5)
    CD=pow(((D[0]-C[0])**2)+((D[1]-C[1])**2),0.5)
    print(AB,CD)

    width=(max(int(AB),int(CD)))

    AD=pow(((D[0]-A[0])**2)+((D[1]-A[1])**2),0.5)
    BC=pow(((B[0]-C[0])**2)+((B[1]-C[1])**2),0.5)
    print(AD,BC)

    height=(max(int(AD),int(BC)))
    
    warpimage=np.float32([A,B,C,D])
    finalimage=np.float32([[0,0],[width,0],[width,height],[0,height]])
    print(warpimage,finalimage)
    transmat=cv2.getPerspectiveTransform(warpimage,finalimage)
    print(transmat)
    output=cv2.warpPerspective(doc,transmat,(width, height))
    
    
    #print(approx)
#print(approx.sum(1))

cv2.imshow("contours",doc)
# cv2.drawContours(doc,contour)
cv2.imshow("img",edged)
cv2.imshow("docs",output)
cv2.waitKey(0)