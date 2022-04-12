import numpy as np
import cv2

img=cv2.imread("filter/rect3 copy.jpg")
#img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
# print(img.shape)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#grayimg=cv2.GaussianBlur(grayimg,(7,7),1)
_,threshimg=cv2.threshold(grayimg,220,255,cv2.THRESH_BINARY)
grayimg=cv2.cvtColor(grayimg,cv2.COLOR_GRAY2BGR)

contours,hierarchy=cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(list(contours))
for contour in contours:
  arclen1=cv2.arcLength(contour, True)
  arclen2=cv2.arcLength(contour, True)
  print("Arclength::",arclen1,arclen2)
  approx = cv2.approxPolyDP(contour, 0.01 * arclen1,True)
  cv2.drawContours(img,[contour],0,(255,0,0),3)
  # cv2.drawContours(img,[contour],0,(255,0,0),1)
  # print(contour[0])
  #print(contour[0])
  # print(contour)
  
  x,y,w,h=cv2.boundingRect(approx)
  print("contours ::::",contour)
  print("approximation ::::",approx)
  print("Length of approximated contours and length of contours ::::",len(approx),len(contour))
  # print(approx[len(approx)-1])

  if(len(approx)==4):
    if(w==h):
      cv2.putText(img,'SQUARE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
      
    else:
      cv2.putText(img,'RECTANGLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
  
  elif(len(approx)==2):
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