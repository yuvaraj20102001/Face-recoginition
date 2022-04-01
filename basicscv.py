import cv2
from cv2 import MORPH_ELLIPSE
from cv2 import MORPH_RECT
import numpy as np
from matplotlib import pyplot as plt


'''the imread() function in opencv reads the image in the BGR format i.e,reverse of RGB'''

img=cv2.imread("programingfiles/filter/input.jpg")
grayimg1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



''' matrix representation of the image
each matrix line or the array has the bgr value of the pixel '''

print(img[0][0])

'''  width,height of the image , total number of pixel '''

print("width:",img.shape[0])
print("height:",img.shape[1])
print("Total number of pixels:",img.shape[0]*img.shape[1])

'''different color scales of the image , the basic color scheme that everyone familiar is the RGB format the RED GREEN BLUE ,
the 3rd elemnt in the shape decides the number of color channel of the image
 there are other color channels in an image that ca be represented or converted into some color channels are '''

print("Width,Height,Color Channels",img.shape)
cv2.imshow("Grayscale image",grayimg1)

'''Grayscale image is an single channel image and converting the image back to 3 channel image is simple,
similar to conversion of the grayscale image'''

print("The Color Channel of the Grayscale image",grayimg1.shape)
grayimg1=cv2.cvtColor(grayimg1,cv2.COLOR_GRAY2BGR)
print("The Changed color channel of grayscale image",grayimg1.shape)


# cv2.imshow("Hue Saturation Value",cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
# cv2.imshow("Lightness channel A and channel B",cv2.cvtColor(img,cv2.COLOR_BGR2LAB))
'''Three different Color channel of the Rgb image is shown below ,the splitted color channel can also be merged back into 3 color channels'''
B,G,R=cv2.split(img)

# cv2.imshow("Blue",B)
# cv2.imshow("Green",G)
# cv2.imshow("Red",R)


merged=cv2.merge([B,G,R])
#cv2.imshow("merged",merged)
''' 
graphical representation of the image .  
since the each pixel value is read inthe BGR format the BGR pixel value is converted to RGB'''


# plt.subplot(211)
# plt.imshow(img)
# plt.title('Input',loc='left')

# img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# plt.subplot(212)
# plt.imshow(img1)
# plt.title('Output',loc='right')

# plt.show()

''' scaling of image.
by mentioning the desired pixel lengths
or by mentioning the desired multiple of the x axis and y axis'''

img2=cv2.resize(img,(640,480))
img3=cv2.resize(img,(0,0),fx=1.5,fy=1.5)
# cv2.imshow("resized image",img2)
# cv2.imshow("resized image 2",img3)
print("Total number of pixels of resized image:",img3.shape[0]*img3.shape[1])


''' Translation of image ,Translation of image is done using the Transformation matrix which is a 
2*3 matrtix that helps to transform the image with respect to the image that is given as input.
first we will create a transformation matrix,then with respect to the transformation matrix we will translate the 
image.'''

transmat=np.float32([[1,0,100],[0,1,100]])
transimage=cv2.warpAffine(img,transmat,(img.shape[1],img.shape[0]))
transimage2=cv2.warpAffine(img3,transmat,(img3.shape[1],img3.shape[0]))
# cv2.imshow("translated image",transimage)
# cv2.imshow("resized and translated image",transimage2)

''' Rotation of Image . similar to translation of image the transformation matrix for rotation is also calculated 
and with respect to the rotation matrix the image is warped to rotate. As we made the transformation matrix for translation
on our own the rotation matrix will be returned by getRotationMatrix2D() where center,angle,scale is passed as input. here also 
2*3 matrix will be returned the matrtix will be vector multiplied by [[cosB -sinB 0],[sinB cosB,0]]'''

rotationmatrix=cv2.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),45,1.0)
rotatedimage=cv2.warpAffine(img,rotationmatrix,(img.shape[1],img.shape[0]))
# cv2.imwrite("rotatedimage.jpg",rotatedimage)
# cv2.imshow("rotated image",rotatedimage)
# print(rotationmatrix)

''' Now we have rotated the image and as a next step we are going to calculate the translation matrix for the rotated image 
then we will translate the rotated image'''

# rotatedimage=cv2.imread("rotatedimage.jpg")
# rotationmatrix=cv2.getRotationMatrix2D((rotatedimage.shape[1]//2,rotatedimage.shape[0]//2),45,1.0)

transrotatemat=np.float32([[1,0,100],[0,1,100]])
transrotatedimage=cv2.warpAffine(rotatedimage,transrotatemat,(rotatedimage.shape[1],rotatedimage.shape[0]))
# cv2.imshow("translated rotated image",transrotatedimage)

''' Atlast here we have done three operations at a time with help of the below transformation matrix that we have dervied 
approximately for rotation about  45 degree and scaling to 0.5 time and translation from 100 pixel'''

scalingmat=np.float32([[0.35355339,-0.35355339,100],[0.35355339,0.35355339,100]])
scaledimage=cv2.warpAffine(img,scalingmat,(img.shape[1],img.shape[0]))
# cv2.imshow("scaled image",scaledimage)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# print(grayimg)
''' Thresholding of image - threesholding is an type of object segmentaion that helps in 
seperating the different levels of objects in the image. The process of thresholding involves
 comparing the pixel value wit that of the given threshold value , if the pixel value greater than threshold value the pixel value is set to '0',
 else the pixel value is set to max value that is mentioned in the function'''
ret,thresh_1=cv2.threshold(grayimg,90,255,cv2.THRESH_BINARY)# if(src(x,y)>thresh) then dst(x,y)=maxValue else dst(x,y)=0
ret,thresh_2=cv2.threshold(grayimg,90,255,cv2.THRESH_BINARY_INV)# if(src(x,y)>thresh) then dst(x,y)=0 else dst(x,y)=maxValue
ret,thresh_3=cv2.threshold(grayimg,90,255,cv2.THRESH_TOZERO)# if(src(x,y)>thresh) then dst(x,y)=src(x,y) else dst(x,y)=0
ret,thresh_4=cv2.threshold(grayimg,90,255,cv2.THRESH_TOZERO_INV)# if(src(x,y)>thresh) then dst(x,y)=0 else dst(x,y)=src(x,y)
ret,thresh_5=cv2.threshold(grayimg,90,255,cv2.THRESH_TRUNC)# if(src(x,y)>thresh) then dst(x,y)=threshold else dst(x,y)=src(x,y)

# cv2.imshow("Thresh_1",thresh_1)
# cv2.imshow("Thresh_2",thresh_2)
# cv2.imshow("Thresh_3",thresh_3)
# cv2.imshow("Thresh_4",thresh_4)
# cv2.imshow("Thresh_5",thresh_5)

''' Adaptive thresholding - unlike simple thresholding the adaptive thresholding calculates its own thresholding value 
for a small region with respeect to blocksize given.'''

Athresh_1=cv2.adaptiveThreshold(grayimg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)
Athresh_2=cv2.adaptiveThreshold(grayimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)
# cv2.imshow("adaptiveThreshold Mean",Athresh_1)
# cv2.imshow("adaptiveThreshold Gaussian",Athresh_2)

''' Mathematical Morphology - set of processes that can be performed on the image based on the shapes , 
the commonly used morphological operations are : dilation,erosion. dialtion is used to reduce the noise of the image ,
increases the object area and prominent/clear it is the xor operation . eroding it is the dual of dilation it erodes away the 
boundaries of the object and it is used to diminsh the features of the image.'''

ker=np.ones((6,6),np.uint8)
erodedimg=cv2.erode(img,ker,iterations=1)


dilatedimg=cv2.dilate(img,ker,iterations=1)
# erodedimg=cv2.erode(img,ker,iterations=5)
# dilatedimg=cv2.dilate(img,ker,iterations=5)
cv2.imshow("eroded image",erodedimg)
cv2.imshow("dilated image",dilatedimg)

''' opening and closing of the image- the combinations of dialtion and erosion is the opening and closing of image 
opening is nothing but erosion followed dilation,closing is noting but dilation followed by erosion ,
the structural element or thee kernel can be derived from the function getStructurElement() this returns the 
numpy array of type uint8,there are few types of strutural elements like MORPH_ELLIPSE,MORPH_RECT,MORPH_CIRCLE,etc'''

kernel=cv2.getStructuringElement(MORPH_ELLIPSE,(5,5))
kernel1=cv2.getStructuringElement(MORPH_RECT,(5,5))
# print(kernel,kernel1,sep="\n")

opening=cv2.morphologyEx(grayimg,cv2.MORPH_OPEN,ker)
closing=cv2.morphologyEx(grayimg,cv2.MORPH_CLOSE,ker)
morphgradient=cv2.morphologyEx(grayimg,cv2.MORPH_GRADIENT,ker)
tophat=cv2.morphologyEx(grayimg,cv2.MORPH_TOPHAT,ker)
blackhat=cv2.morphologyEx(grayimg,cv2.MORPH_BLACKHAT,ker)
# cv2.imshow("opening image",opening)
# cv2.imshow("closing image",closing)
# cv2.imshow("gradient image",morphgradient)
# cv2.imshow("tophat image",tophat)
# cv2.imshow("blackhat image",blackhat)

cv2.waitKey(0)
