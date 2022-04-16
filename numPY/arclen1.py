import cv2
import numpy as np

# Generate 5 x 5 black image
img = np.zeros((9, 9), np.uint8)

# Draw 3 x 1 white line
img = cv2.rectangle(img, (1, 1), (5, 5), 255,cv2.FILLED)

# Find contours
cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

# Outputs
print(img, '\n')                                    
print(np.squeeze(cnts[0]), '\n')                    
print('Contour points:', cnts[0].shape[0], '\n')   
arclen=cv2.arcLength(cnts[0], True) 
print('arcLength:', arclen, '\n')
print('approx points',cv2.approxPolyDP(cnts[0],0.001*arclen,True))