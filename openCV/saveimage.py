import numpy as np
import cv2

img=cv2.imread('filter/rect.png')
img1=np.full((700,1400,3),(255,255,255),dtype=np.uint8)
# img1=cv2.cvtColor(img, cv2.COLOR_BIN)
# img2=100*np.ones((300,300),np.uint8)
print(img.shape)
img2=cv2.rectangle(img1,(100,500),(300,550),(255,0,255),-1)

img2=cv2.circle(img1,(350,100),50,(100,0,100),-1)

img2=cv2.line(img1,(50,100),(250,100),(0,0,0),1)

pts = [(830 ,52),(772,95),( 794,167),(867,167),(889 ,95)]
cv2.fillPoly(img1, np.array([pts]),(0,100,255))

pts = [(1067 ,52),(994 ,52),(972,110),( 994,167),(1067,167),(1089 ,110)]
cv2.fillPoly(img1, np.array([pts]),(0,100,255))

pts = [(1067 ,552),(994 ,552),(972,610),( 994,667),(1067,667),(1039 ,615)]
cv2.fillPoly(img1, np.array([pts]),(0,100,255))

pts = [(531 ,152),(422,225),( 444,307),(617,307),(639 ,225)]
cv2.fillPoly(img1, np.array([pts]),(0,100,255))

pts = [(1031 ,222),(922,325),( 944,457),(1117,457),(1140 ,325)]
cv2.fillPoly(img1, np.array([pts]),(100,100,255))

pts = [(580,350), (500, 420),(600,500)]
cv2.fillPoly(img1, np.array([pts]),(0,0,255))

pts = [(1100,180), (1200, 180),(1150,250)]
cv2.fillPoly(img1, np.array([pts]),(0,0,255))

pts = [(1192,300), (1308, 300),(1250,200)]
cv2.fillPoly(img1, np.array([pts]),(0,0,255))

pts = [(830 ,452),(772,495),( 794,567),(867,557),(889 ,495)]
cv2.fillPoly(img1, np.array([pts]),(0,100,255))

img2=cv2.rectangle(img1,(400,550),(600,650),(255,0,255),-1)

pts = [(830 ,252),(772,295),( 794,367),(867,357)]
cv2.fillPoly(img1, np.array([pts]),(0,0,255))

pts = [(41,600), (170, 600),(120,650)]
cv2.fillPoly(img1, np.array([pts]),(0,0,255))

img2=cv2.rectangle(img1,(100,250),(300,450),(0,100,255),-1)

img2=cv2.line(img1,(450,100),(600,100),(0,0,0),1)
cv2.imwrite("newimg.jpg",img1)

# img2=cv2.rectangle(img2,(0,150),(300,300),(255,0,255),-1)
cv2.imshow("imshow",img2)
cv2.waitKey(0)