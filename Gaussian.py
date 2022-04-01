
# Python OpenCV - getgaussiankernel() Function
  
# import cv2
import cv2
import numpy as np
# read image
img = cv2.imread('programingfiles/filter/input.jpg')
  
# Creates a 1-D Gaussian kernel

a = cv2.getGaussianKernel(7,1)

b=np.array([[1,2,1],[2,4,2],[1,2,1]])
print(a)
  
# print Gaussian filter coefficients matrix