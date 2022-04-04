
import cv2
import numpy as np
from matplotlib import pyplot as plt
  
  
img = cv2.imread('programingfiles/filter/cards.jpg')
width,height=250,350
  
pts1 = np.float32([[225,100],[425,140],[160,380],[365,420]])
  
pts2 = np.float32([[0,0],
                   [width,0 ], 
                   [0,height],[width,height]])
  
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (width, height))
  
plt.subplot(211)
plt.imshow(img)
plt.title('Input')
  
plt.subplot(212)
plt.imshow(dst)
plt.title('Output')
  
plt.show()
  
# Displaying the image

      
cv2.imshow('image', img)
cv2.imshow("out",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()