import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
frame = cv2.imread("mask.png")

    # Capture frame-by-frame
#    ret, frame = cap.read()

    # Our operations on the frame come here
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
blur = cv2.GaussianBlur(hsv,(9,9),0)
#treshlod
lower=np.array([170,30,90])
upper=np.array([190,50,110])

mask=cv2.inRange(blur,lower,upper)
result=cv2.bitwise_and(frame,frame,mask=mask)
gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
canny= cv2.Canny(thresh1,1,100)
    # Display the resulting frame

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
a = []
b = 0
for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 255))
        a.append([x, y])
cv2.imshow('frame1', canny)
cv2.imshow('frame',frame)
cv2.waitKey()
cv2.destroyAllWindows()