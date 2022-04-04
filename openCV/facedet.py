
import cv2
import numpy as np 


haar_path = 'C:/Users/test/AppData/Local/Programs/Python/Python310/lib/site-packages/cv2/data/'

img = cv2.imread('programingfiles/filter/4faces.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(haar_path +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(haar_path +'haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(gray, 1.3)


for (x,y,w,h) in faces:
    #draw rectangle around face
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #select face as region of interest 
    roi_g = gray[y:y+h,x:x+h]
    roi_c = img[y:y+h,x:x+h]
    
    eyes = eye_cascade.detectMultiScale(roi_g)
    
    for (ex,ey,ew,eh) in eyes:
        
        cv2.rectangle(roi_c, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
img=cv2.resize(img,(480,600))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()