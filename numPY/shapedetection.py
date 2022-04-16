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
  print(int(d1),int(d2),int(d3),int(d4))
  if(d1==d2 and d3==d4):
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
# img=cv2.resize(img2,(img.shape[1],img.shape[0]))
# img=np.stack((img,img2))
# print(img.shape)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#grayimg=cv2.GaussianBlur(grayimg,(7,7),1)

_,threshimg=cv2.threshold(grayimg,150,255,cv2.THRESH_BINARY)
#cv2.imshow("gray",threshimg)

contours,hierarchy=cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(list(contours))



for contour in contours[1:]:
  arclen=cv2.arcLength(contour, True)
  approx = cv2.approxPolyDP(contour, 0.009 * arclen, True)
  cv2.drawContours(img,[approx],0,(0,255,0),2)
  #print(contour[0])
  # print(contour)
  x,y,w,h=cv2.boundingRect(approx)
  # print(len(approx))
  print(approx)

  if(len(approx)==4): 
    approx=np.squeeze(approx)
    print(approx)

    #print(w,h)
    if(verify_opposides(np.array(approx))):
      if(w==h):
        cv2.putText(img,'SQUARE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.circle(img,(500,450),3,(0,0,0),-1)
      else:
        cv2.putText(img,'RECTANGLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    else:
      cv2.putText(img,'irregular polygon',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
      
  
  elif(len(approx)==2):
    cv2.putText(img,'LINE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

  elif(len(approx)==3):
    cv2.putText(img,'TRIANGLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)


  elif(len(approx)==5):
    dis=[]
    count=0
    approx=np.squeeze(approx)
    for i in range(0,4):
      print(approx[i],approx[i+1])
      dis.append(int(distance(approx[i],approx[i+1])))
    dis.append(int(distance(approx[4],approx[0])))
    print(dis)

    for i in range(5):
      if(int(dis[i]) in dis[i+1:]):
        count+=1
    print(count)
    if(count==2 or count==3):
      cv2.putText(img,'PENTAGON',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    else:
      dis=[]
      count=0
      cv2.putText(img,'irregular polygon',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)


  elif(len(approx)==6):
    cv2.putText(img,'HEXAGON',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
  else:
    cv2.putText(img,'CIRCLE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
#threshimg=cv2.cvtColor(threshimg,cv2.COLOR_GRAY2BGR)
#stimg=np.hstack((img,grayimg,threshimg))

cv2.imshow("img1",img)

cv2.waitKey(0)