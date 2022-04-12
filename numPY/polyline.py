''' import numpy as np
import cv2

# read input
img = cv2.imread('filter/open.jpg')
hh, ww = img.shape[:2]

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

# get points
points = np.column_stack(np.where(thresh.transpose() != 0))

# list points
# for pt in points:
#     ptx = pt[0]
#     pty = pt[1]
#     print(ptx,pty)

# approximate polygon
poly = cv2.approxPolyDP(points, 0.02 * ww, False)

# list polygon points
# for p in poly:
#     px = p[0]
#     py = p[0]
#     #print(px,py)

# draw polygon on copy of input
result = img.copy()
cv2.polylines(result, [poly], False, (0,0,255), 1)

# save results
cv2.imwrite('curve_polygon.png', result)

cv2.imshow("thresh", thresh)
cv2.imshow("result", result)
cv2.waitKey(0) '''



import cv2

img = cv2.imread('filter/open.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)


_,binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# cv2.imshow("binary", binary)
# cv2.waitKey(0)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.009 * cv2.arcLength(contour, False)
    approx = cv2.approxPolyDP(contour, epsilon, closed=False)
    cv2.drawContours(img, [approx], -1, (0, 255, 255), 1)

cv2.imshow("approx", img)
cv2.waitKey(0)

cv2.destroyAllWindows()