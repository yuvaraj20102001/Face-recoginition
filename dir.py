import os
import cv2

# cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
# haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
#print(haar_model)
img=cv2.imread("programingfiles/filter/1.jpg")
cv2.imshow("abc",img)
