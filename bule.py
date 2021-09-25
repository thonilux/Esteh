import cv2
import numpy as np
frame = cv2.imread("capture.jpg", 1)
hasil= frame.copy()
# frame[:,:,0] = np.zeros([frame.shape[0], frame.shape[1]])
blue=frame[:,:,0]
red=frame[:,:,2]
blur=cv2.GaussianBlur(blue,(3,3),0)
canny=cv2.Canny(blur,100,200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(hasil, contours, -1, 255, 1)
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
        cv2.rectangle(hasil,(x,y),(x+w,y+h),(0,255,0),2)
        # cv2.putText(hasil,"Area = "+are,position, cv2.FONT_HERSHEY_SIMPLEX,  1, (209, 80, 0, 255), 2)
        cv2.putText(hasil, "Area = " + "%.2f" % area1, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 2)



cv2.imshow("Result", blue)
cv2.imshow("Result1", red)
cv2.imshow("Result2", hasil)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()