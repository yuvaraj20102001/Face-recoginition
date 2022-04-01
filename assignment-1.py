import cv2
import numpy as np


capture=cv2.VideoCapture(0)
#video-gesture positions of successive frames
back1=cv2.imread("filter/1.jpg")
back2=cv2.imread("filter/2.jpg")

while capture.isOpened():
	success,frame=capture.read()
	if not success:
		print("could not access the webcam")
		break
	

	print(frame.shape)
	k=cv2.waitKey(50)
	
	if k & 0xff ==ord('1'):
			
		back1=cv2.resize(back1,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back1,0.3,gamma=0.4)
			
	if k & 0xff ==ord('2'):
			
		back2=cv2.resize(back2,(frame.shape[1],frame.shape[0]))
		frame=cv2.addWeighted(frame,0.9,back2,0.3,gamma=0.4)
		#cv2.imshow("frame",blended_image)

	cv2.imshow("frame",frame)

		
	if k & 0xff ==ord('x'):
		break
		
capture.release()
cv2.destroyAllWindows()