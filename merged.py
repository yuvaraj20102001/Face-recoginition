import cv2
img= cv2.imread("filter/input.jpg")
B,G,R=cv2.split(img)

cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)

I=cv2.threshold(img,90,255,cv2.THRESH_BINARY)
B=cv2.threshold(B,90,255,cv2.THRESH_BINARY)
G=cv2.threshold(G,90,255,cv2.THRESH_BINARY)
R=cv2.threshold(R,90,255,cv2.THRESH_BINARY)

print(B)
merged1=cv2.merge([B[1],G[1],R[1]])
cv2.imshow("merged1",merged1)
cv2.imshow("merged",I[1])
cv2.waitKey(0)