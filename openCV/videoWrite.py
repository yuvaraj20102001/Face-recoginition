import cv2 


def rotate(img,ang,rotpoint=None):
    height,width=img.shape[:2]
    if(rotpoint is None):
        rotpoint=(width//2,height//2)
    rotMat=cv2.getRotationMatrix2D(rotpoint,ang,1.0)
    dimensions=(width,height)
    return cv2.warpAffine(img,rotMat,dimensions)

    
cap=cv2.VideoCapture(0)

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("Sample.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==True):
        #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=rotate(frame,45)
        out.write(frame)
        cv2.imshow("IMG",frame)
        if(cv2.waitKey(1) & 0xff ==ord('x')):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()