
import cv2
import numpy as np

def rotate(img,ang,rotpoint=None):
    height,width=img.shape[:2]
    if(rotpoint is None):
        rotpoint=(width//2,height//2)
    rotMat=cv2.getRotationMatrix2D(rotpoint,ang,1.0)
    dimensions=(width,height)
    return cv2.warpAffine(img,rotMat,dimensions)

def translation(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img,transmat,(img.shape[1],img.shape[0]))

def imagefilter():
    
    dict={0:" :Grayscale",1:" :Blurring",2:" :Sketching",3:" :Flip Horizontal",4:" :Flip Vertical",5:" :Rotate Left",
    6:" :Rotate Right",7:" :Crop",8:" :To Shift"}
    for i in dict:
        print(i,dict[i])

    x=int(input())

    capture=cv2.VideoCapture(0)

    while capture.isOpened():
        success,frame=capture.read()
        if not success:
            print("could not access the webcam")
            break

        print(frame.shape)

        cv2.imshow("ORIGINAL",frame)

        if(x==0):
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #cv2.imshow("GRAYSCALE",gray)
            cv2.imwrite("Grayscaled.jpg",gray)
            

        if(x==1):
            blur=cv2.GaussianBlur(frame,(7,7),cv2.BORDER_DEFAULT)
            #cv2.imshow("BLURRED",blur)
            cv2.imwrite("Blurred.jpg",blur)
        if(x==2):
            sketch=cv2.Canny(frame,125,175)
            #cv2.imshow("SKETCHED",sketch)
            cv2.imwrite("Sketched.jpg",sketch)
        if(x==3):
            flipped=cv2.flip(frame,1)
            #cv2.imshow("SKETCHED",sketch)
            cv2.imwrite("FlippedH.jpg",flipped)
        if(x==4):
            flipped=cv2.flip(frame,0)
            #cv2.imshow("SKETCHED",sketch)
            cv2.imwrite("FlippedV.jpg",flipped)      

        if(x==5):            
            cv2.imwrite("rotatedL.jpg",rotate(frame,45))

        if(x==6):       
            cv2.imwrite("roatedR.jpg",rotate(frame,-45))

        if(x==7):
            cropped=frame[200:400,300:400]
            cv2.imwrite("cropped.jpg",cropped)
        if(x==8):
            cv2.imwrite("Shifted.jpg",translation(frame,100,100))

        


        k=cv2.waitKey(50)
        
        if  k & 0xff ==ord('x'):
            break


    capture.release()
    cv2.destroyAllWindows()
    
    #cv2.imshow("AABC",frame)
    
    #cv2.imshow("AABC",imgorg)

def videofilter():
    

    dict={0:" :Grayscale",1:" :Blurring",2:" :Sketching",3:" :Flip",4:" :Rotate Left",5:" :Rotate Right",6:" :Crop",7:" :To Shift"}
    for i in dict:
        print(i,dict[i])
    x=int(input())

    

    capture=cv2.VideoCapture(0)
    # #video-gesture positions of successive frames
    # back1=cv2.imread("programingfiles/filter/1.jpg")
    # #cv2.imshow("BACK1",back1)
    # back2=cv2.imread("filter/2.jpg")

    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter("Sample.mp4",fourcc,20.0,(640,480))

    while(capture.isOpened()):
        success,frame=capture.read()
        if success==True:
            print(frame.shape)

            cv2.imshow("original",frame)

            if(x==0):
                frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                
                #cv2.imshow("GRAYSCALE",gray)
                if(len(frame.shape)==2):
                    frame=cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                out.write(frame)
            
            if(x==1):
                frame=cv2.GaussianBlur(frame,(7,7),cv2.BORDER_DEFAULT)
                #cv2.imshow("BLURRED",blur)
                out.write(frame)
            
            if(x==2):
                frame=cv2.Canny(frame,125,175)
                print(frame.shape)
                if(len(frame.shape)==2):
                     frame=cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                #cv2.imshow("SKETCHED",sketch)
                out.write(frame)
            if(x==4):            
                frame=rotate(frame,45)
                out.write(frame)

            if(x==5):       
                frame=rotate(frame,-45)
                out.write(frame)

            if(x==6):
                frame=frame[200:400,300:400]
                out.write(frame)
            if(x==7):
                frame=translation(frame,100,100)
                out.write(frame)
            

            cv2.imshow("frame",frame)
            
            
            k=cv2.waitKey(50)
        
            if  k & 0xff ==ord('x'):
                break
        else:
            break
    capture.release()
    cv2.destroyAllWindows()

print("1.IMAGE FILTERING")
print("2.VIDEO FILTERING")
x=int(input())

if(x==1):
    imagefilter()

else:
    videofilter()
cv2.waitKey(0)