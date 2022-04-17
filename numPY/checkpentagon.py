import numpy as np
import cv2


def distance(p1,p2):
  dis=pow(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2),0.5)
  return dis

def verify_opposides(a):
  d1=distance(a[0],a[1])
  d2=distance(a[2],a[3])
  d3=distance(a[0],a[3])
  d4=distance(a[1],a[2])
  print(d1,d2,d3,d4)
  if((d2<=(d1+1) and d2>=(d1-1)) and (d4<=(d3+1) and d4>=(d3-1))):
    return 1
  else:
    return 0


img=cv2.imread("filter/shapes3.png")

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,threshimg=cv2.threshold(grayimg,200,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours[1:]:
  arclen=cv2.arcLength(contour, True)
  approx = cv2.approxPolyDP(contour, 0.009 * arclen, True)
  cv2.drawContours(img,[approx],0,(0,255,0),2)

  x,y,w,h=cv2.boundingRect(approx)

  print(approx)

  if(len(approx)==5):
    dis=[]
    count=0
    approx=np.squeeze(approx)
    for i in range(0,4):
      print(approx[i],approx[i+1])
      dis.append(distance(approx[i],approx[i+1]))
    dis.append(distance(approx[4],approx[0]))
    dis.sort()
    print(dis)

    for i in range(0,5):
      for j in range(i+1,5):
        if(dis[j]<=dis[i]+1 and dis[j]>=dis[i]-1):
          count+=1
    print(count)
    if(count>=2):
      cv2.putText(img,'PENTAGON',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    else:
      dis=[]
      count=0
      cv2.putText(img,'irregular polygon',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("img1",img)

cv2.waitKey(0)