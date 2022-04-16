import numpy as np
import math
def distance(p1,p2):
  dis=pow(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2),0.5)
  # if(dis-int(dis)<=0.1):
  #   dis=math.floor(dis)
  # else:
  #   dis=math.ceil(dis)  
  return dis

def verify_opposides(a):
  if(distance(a[0],a[1])==distance(a[2],a[3]) and distance(a[0],a[3])==distance(a[1],a[2])):
    return 1
  else:
    return 0
def calculate_centroid(a):
  x=a[:,0]
  y=a[:,1]
  x=np.average(x)
  y=np.average(y)
  centroid=[x,y]
  for i in a:
    print(distance(centroid,i))
  return(centroid)



#a=np.array([[ 91,31],[159,80],[133,160],[ 51,160],[24,80]])
#a=np.array([[130,52],[ 72,95],[ 94,167],[167,167],[189,95]])
#a=np.array([[137,47],[239,120],[200,240],[77,240],[37,120]])
a=np.array([[166,17],[278 ,16],
 [280 ,127],
 [167 ,129]])
print(a[0],a[1],a[2],a[3])
dis=[]
count=0
# for i in range(0,4):
#   print(a[i],a[i+1])
#   dis.append(distance(a[i],a[i+1]))
# dis.append(distance(a[4],a[0]))

# for i in range(3):
#   if(int(dis[i])==int(dis[4-i])):
#     count+=1
  
print(count) 
print(distance(a[0],a[1]))
print(distance(a[2],a[3]))
print(verify_opposides(a))
# print(calculate_centroid(a))