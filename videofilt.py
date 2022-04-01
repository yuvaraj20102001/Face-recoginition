
import cv2


capture=cv2.VideoCapture(0)

frame_width=int(capture.get(3))
frame_height=int(capture.get(4))



#out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 20, (frame_width,frame_height))

while True:
  success,frame=capture.read()
  width=int(frame.shape[1]*0.5)
  height=int(frame.shape[0]*0.5)
  frame=cv2.resize(frame,(width,height))

  if success==True:
    #out.write(frame)
    cv2.imshow("FRAME",frame)

  if cv2.waitKey(20) & 0xff== ord('x'):
    break

#out.release()
capture.release()  
	
cv2.destroyAllWindows()