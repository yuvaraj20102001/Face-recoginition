import numpy as np
import cv2

img=cv2.imread("filter/shapes2.png")
# cap=cv2.VideoCapture(0)
# while(True):
#   flag,img=cap.read()
#   cv2.imshow("Result",img)
#   if(cv2.waitKey(1) & 0xff == ord('q')):
#     break
# cv2.destroyAllWindows()
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#grayimg=cv2.GaussianBlur(grayimg,(7,7),1)
_,threshimg=cv2.threshold(grayimg,220,255,cv2.THRESH_BINARY)
grayimg=cv2.cvtColor(grayimg,cv2.COLOR_GRAY2BGR)

contours,hierarchy=cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(list(contours))
for contour in contours:
  arclen=cv2.arcLength(contour, True)
  approx = cv2.approxPolyDP(contour, 0.01 * arclen, True)
  cv2.drawContours(img,[contour],0,(0,255,0),3)
  print( )
  x,y,w,h=cv2.boundingRect(contour)
  sum_sq = np.sqrt(np.sum(np.square([w,h])))
  print(sum_sq)
  print(arclen//4)

cv2.waitKey(0)




# def empty():
#   return 1
# cv2.namedWindow("THRESHOLD")
# cv2.resizeWindow("THRESHOLD",640,480)
# cv2.createTrackbar("threshold1","THRESHOLD",100,255,empty)
# cv2.createTrackbar("threshold2","THRESHOLD",100,255,empty)
# t1=cv2.getTrackbarPos("threshold1","THRESHOLD")
# t2=cv2.getTrackbarPos("threshold2","THRESHOLD")
# print(t1,t2)
