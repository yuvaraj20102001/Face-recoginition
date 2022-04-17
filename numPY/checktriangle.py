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


img=cv2.imread("newimg.jpg")
#img=cv2.resize(img,(0,0),fx=1.5,fy=1.5)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,threshimg=cv2.threshold(grayimg,200,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours[1:]:
  arclen=cv2.arcLength(contour, True)
  approx = cv2.approxPolyDP(contour, 0.009 * arclen, True)
  cv2.drawContours(img,[approx],0,(100,100,0),2)

  x,y,w,h=cv2.boundingRect(approx)

  print(approx)

  if(len(approx)==3):
    dis=[]
    count=0
    approx=np.squeeze(approx)
    for i in range(0,2):
      print(approx[i],approx[i+1])
      dis.append(distance(approx[i],approx[i+1]))
    dis.append(distance(approx[2],approx[0]))
    #dis.sort()
    print(dis)

    for i in range(0,3):
      for j in range(i+1,3):
        if(dis[j]<=(dis[i]+1) and dis[j]>=(dis[i]-1)):
          count+=1
    print(count)
    if(count==3):
      cv2.putText(img,'equilateral',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    elif(count==1):
      cv2.putText(img,'isosceles',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    else:
      dis=[]
      count=0
      cv2.putText(img,'Scalene',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("img1",img)

cv2.waitKey(0)