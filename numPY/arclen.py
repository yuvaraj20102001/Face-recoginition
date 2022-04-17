import numpy as np
import cv2


font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.imread('newimg.jpg', cv2.IMREAD_COLOR)
#img2=cv2.resize(img2,(0,0),fx=1.5,fy=1.5)

img = cv2.imread('newimg.jpg', cv2.IMREAD_GRAYSCALE)
#img=cv2.resize(img,(0,0),fx=1.5,fy=1.5)

_, threshold = cv2.threshold(img,200, 255, cv2.THRESH_BINARY)

contours, _= cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours :

	approx = cv2.approxPolyDP(cnt, 0.009* cv2.arcLength(cnt, True), True)
	print("arclength for false openloop",cv2.arcLength(cnt, True))
	print("arc length for true closed surve",cv2.arcLength(cnt, True))
	x,y,w,h=cv2.boundingRect(approx)
	print("WIDTH HEIGHT :::",w,h)

	cv2.drawContours(img2, [approx], 0, (0, 0, 255), 2)
	print("approx",np.squeeze(approx))

	n = approx.ravel()
	i = 0

	for j in n :
		if(i % 2 == 0):
			x = n[i]
			y = n[i + 1]

			# String containing the co-ordinates.
			string = str(x) + " " + str(y)

			#if(i == 0):
				# text on topmost co-ordinate.
			# cv2.putText(img2, "Arrow tip", (x, y),
			# 					font, 0.5, (255, 0, 0))
			#else:
				# text on remaining co-ordinates.
			cv2.putText(img2, string, (x, y),font, 0.5, (0, 255, 0))
			print(i,string)
		i = i + 1

# Showing the final image.
cv2.imwrite("coordinate.jpg",img2)
cv2.imshow('image2', img2)
cv2.waitKey(0)
