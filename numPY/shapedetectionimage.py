import numpy as np
import cv2

img=cv2.imread("filter/shapes1.png")
#img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
# print(img.shape)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#grayimg=cv2.GaussianBlur(grayimg,(7,7),1)
_,threshimg=cv2.threshold(grayimg,220,255,cv2.THRESH_BINARY)
grayimg=cv2.cvtColor(grayimg,cv2.COLOR_GRAY2BGR)

contours,hierarchy=cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours[0].shape)
#print(list(contours))
for contour in contours:
  arclen=cv2.arcLength(contour, True)
  approx = cv2.approxPolyDP(contour, 0.01 * arclen, True)
  cv2.drawContours(img,[contour],0,(0,255,0),2)
  # print(contour[0])
  # print(contour)
  x,y,w,h=cv2.boundingRect(approx)
  print(len(approx))

  if(len(approx)==4): 
    if(w==h):
      cv2.putText(img,'SQUARE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
      
    else:
      cv2.putText(img,'RECTANGLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
  
  elif(len(approx)==2):
    print(contour)
    cv2.putText(img,'LINE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

  elif(len(approx)==3):
    cv2.putText(img,'TRIANGLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
  elif(len(approx)==5):
    cv2.putText(img,'PENTAGON',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
  elif(len(approx)==6):
    cv2.putText(img,'HEXAGON',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
  else:
    cv2.putText(img,'CIRCLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
#threshimg=cv2.cvtColor(threshimg,cv2.COLOR_GRAY2BGR)
#stimg=np.hstack((img,grayimg,threshimg))

cv2.imshow("img1",img)

cv2.waitKey(0)