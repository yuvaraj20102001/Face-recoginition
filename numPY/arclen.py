import cv2
import numpy as np

a=np.array([[1,1,1],[2,2,2],[3,3,3]])
print(a)
arc=cv2.arcLength(a,True)
print(arc)