import cv2
import mediapipe as mp
import numpy as np

#drawing utilitty
mp_drawing = mp.solutions.drawing_utils

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
    cap=cv2.VideoCapture(0)
while True:
  flag,frame=cap.read()
  if not flag:
    print("COULD NOT ACCESS CAMERA")
    break

  results=face_detection.process(frame)

  # for landmark in results.detections:    
  #   mp_drawing.draw_detection(frame,landmark)

  # print(results.detections)

  #cv2.putText(frame,"GOKU",(261,157),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0))
  cv2.imshow('frame',frame)

  if(cv2.waitKey(0) & 0xff ==ord('x')):
    break

cap.release()	
cv2.destroyAllWindows()