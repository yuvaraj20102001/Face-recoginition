
import cv2 
import numpy as np 

haar_path = 'C:/Users/test/AppData/Local/Programs/Python/Python310/lib/site-packages/cv2/data/'

filt = cv2.imread("programingfiles/filter/dog2.png")


face_cascade = cv2.CascadeClassifier(haar_path +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(haar_path +'haarcascade_eye.xml')


original_filt_h,original_filt_w,filt_channels = filt.shape

filt_gray = cv2.cvtColor(filt, cv2.COLOR_BGR2GRAY)


ret, original_mask = cv2.threshold(filt_gray, 50, 255, cv2.THRESH_BINARY_INV)
original_mask_inv = cv2.bitwise_not(original_mask)



cap = cv2.VideoCapture(0)
ret, img = cap.read()
img_h, img_w = img.shape[:2]

while True:

    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=4)

    for (x,y,w,h) in faces:
        
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

        
        face_w = w
        face_h = h
        face_x1 = x
        face_x2 = face_x1 + face_w
        face_y1 = y
        face_y2 = face_y1 + face_h

        filt_width = int(1.5 * face_w)
        filt_height = int(filt_width * original_filt_h / original_filt_w)
        
        
        filt_x1 = face_x2 - int(face_w/2) - int(filt_width/2)
        filt_x2 = filt_x1 + filt_width
        filt_y1 = face_y1 - int(face_h)
        filt_y2 = filt_y1 + filt_height 

        #check to see if out of frame
        if filt_x1 < 0:
            filt_x1 = 0
        if filt_y1 < 0:
            filt_y1 = 0
        if filt_x2 > img_w:
            filt_x2 = img_w
        if filt_y2 > img_h:
            filt_y2 = img_h

        
        filt_width = filt_x2 - filt_x1
        filt_height = filt_y2 - filt_y1

        #resize filt to fit on face
        filt = cv2.resize(filt, (filt_width,filt_height), interpolation = cv2.INTER_AREA)
        mask = cv2.resize(original_mask, (filt_width,filt_height), interpolation = cv2.INTER_AREA)
        mask_inv = cv2.resize(original_mask_inv, (filt_width,filt_height), interpolation = cv2.INTER_AREA)

        #take ROI for filt from background that is equal to size of filt image
        roi = img[filt_y1:filt_y2, filt_x1:filt_x2]

        #original image in background (bg) where filt is not
        roi_bg = cv2.bitwise_and(roi,roi,mask = mask)
        roi_fg = cv2.bitwise_and(filt,filt,mask=mask_inv)
        dst = cv2.addWeighted(roi_bg,0.3,roi_fg,0.7,gamma=0.2)

        #put back in original image
        img[filt_y1:filt_y2, filt_x1:filt_x2] = dst

        break
        
    cv2.imshow('img',img) 

    
    if cv2.waitKey(1) == ord('x'):
        break;

cap.release()
cv2.destroyAllWindows()