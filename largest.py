import numpy as np
import cv2
cap = cv2.VideoCapture(0)

# load the image
frame = cv2.imread("1.png", 1)
#while(True):
#    ret, fram = cap.read()
#    frame=cv2.flip(fram,1)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
blur = cv2.GaussianBlur(frame,(9,9),0)
canny= cv2.Canny(blur,1,100)
    # red color boundaries [B, G, R]
lower = [1, 0, 20]
upper = [220, 220, 220]

    # create NumPy arrays from the boundaries
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
mask = cv2.inRange(frame, lower, upper)
output = cv2.bitwise_and(frame, frame, mask=mask)

ret,thresh = cv2.threshold(mask, 40, 255, 0)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(output, contours, -1, 255, 3)
        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        #int k = v
        #print(w/100)
        #print(h/100)
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
 #       cv2.putText(frame, "Surface = " + "%.2f" % surface, position1, cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 2)
#        cv2.putText(frame, "Area = " + "%.2f" % volume, position2, cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 2)

    # show the images

cv2.imshow("kontur", canny)
cv2.imshow("Result", frame)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()