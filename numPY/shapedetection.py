from dis import dis
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
  
def calculate_centroid(a):
  x=a[:,0]
  y=a[:,1]
  x=np.average(x)
  y=np.average(y)
  return([x,y])

# img2=cv2.imread("filter/shapes.jpg")
img=cv2.imread("newimg.jpg")
#img=cv2.resize(img,(0,0),fx=1.5,fy=1.5)
# img=np.stack((img,img2))
# print(img.shape)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#grayimg=cv2.GaussianBlur(grayimg,(7,7),1)

_,threshimg=cv2.threshold(grayimg,170,255,cv2.THRESH_BINARY)
#cv2.imshow("gray",threshimg)

contours,hierarchy=cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(list(contours))



for contour in contours[1:]:
  arclen=cv2.arcLength(contour, True)
  approx = cv2.approxPolyDP(contour, 0.01 * arclen, True)
  cv2.drawContours(img,[approx],0,(0,255,0),2)
  #print(contour[0])
  # print(contour)
  x,y,w,h=cv2.boundingRect(approx)
  # print(len(approx))
  print(approx)

  if(len(approx)==4): 
    approx=np.squeeze(approx)
    #print(approx)

    print(w,h)
    if(verify_opposides(np.array(approx))):
      if((w<=h+1 and w>=h-1) or (h>=w-1 and h<=w+1)):
        cv2.putText(img,'SQUARE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.circle(img,(500,450),3,(0,0,0),-1)
      else:
        cv2.putText(img,'RECTANGLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    else:
      cv2.putText(img,'irregular polygon',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
      
  
  elif(len(approx)==2):
    cv2.putText(img,'LINE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

  elif(len(approx)==3):
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


  elif(len(approx)==5):
    dis=[]
    count=0
    approx=np.squeeze(approx)
    for i in range(0,4):
      print(approx[i],approx[i+1])
      dis.append(distance(approx[i],approx[i+1]))
    dis.append(distance(approx[4],approx[0]))
    #dis.sort()
    print(dis)

    for i in range(0,5):
      for j in range(i+1,5):
        if(dis[j]<=(dis[i]+1) and dis[j]>=(dis[i]-1)):
          count+=1
    print(count)
    if(count>=2):
      cv2.putText(img,'PENTAGON',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    else:
      dis=[]
      count=0
      cv2.putText(img,'irregular polygon',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


  elif(len(approx)==6):
    dis=[]
    count=0
    approx=np.squeeze(approx)
    for i in range(0,5):
      print(approx[i],approx[i+1])
      dis.append(distance(approx[i],approx[i+1]))
    dis.append(distance(approx[5],approx[0]))
    #dis.sort()
    print(dis)

    for i in range(0,6):
      for j in range(i+1,6):
        if(dis[j]<=(dis[i]+1) and dis[j]>=(dis[i]-1)):
          count+=1
    print(count)
    if(count>=3):
      cv2.putText(img,'HEXAGON',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    else:
      dis=[]
      count=0
      cv2.putText(img,'irregular polygon',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
  else:
    cv2.putText(img,'CIRCLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
#threshimg=cv2.cvtColor(threshimg,cv2.COLOR_GRAY2BGR)
#stimg=np.hstack((img,grayimg,threshimg))

cv2.imshow("img1",img)

cv2.waitKey(0)