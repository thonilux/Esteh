import sys
import math
import cv2
import numpy as np
frame = cv2.imread("laser.jpeg", 1)

#########################  HOUGH LINES  #######################
red = frame[:,:,2]
red1 = 255-red

edges = cv2.Canny(red1, 80, 120)
lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1);
for line in lines[0]:
    pt1 = (line[0],line[1])
    pt2 = (line[2],line[3])
    cv2.line(frame, pt1, pt2, (0,0,255), 3)
###############################################################

src=frame.copy()
src[:,:,2] = np.zeros([src.shape[0], src.shape[1]])
grey = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grey,(9,9),0)
canny= cv2.Canny(blur,1,100)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
        cv2.drawContours(frame, contours, -1, 255, 3)
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        tinggi = 10
        area1=cv2.contourArea(c)/1000
        area = w*h/1000
        are=str(area)
        xway=w*tinggi
        yway=h*tinggi
        surface=(2*area)+(2*xway)+(2*yway)
        volume=w*h*tinggi
        print("%.2f" % surface)
        position = (x+10, y + 30)
        position1 = (x + 10, y + 60)
        position2 = (x + 10, y + 90)
        # draw the biggest contour (c) in green
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,"Area = "+are,position, cv2.FONT_HERSHEY_SIMPLEX,  1, (209, 80, 0, 255), 2)
        cv2.putText(canny, "Area = " + "%.2f" % area1, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 2)

cv2.imshow("red",frame)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()