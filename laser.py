import numpy as np
import cv2

frame = cv2.imread("laser.jpeg", 1)
red = frame[:,:,2]
#hsv = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
#gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
img = 100 - red
#canny=cv2.Canny(img,1,100)
#(thresh, im_bw) = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, th1 = cv2.threshold(img, 10, 0, cv2.THRESH_BINARY)

canny=cv2.Canny(th1,1,100)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
canny2=cv2.Canny(opening,1,100)
contours, hierarchy = cv2.findContours(canny2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
a = []
b = 0
for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        if w<40 and h<10:
            continue
        cv2.drawContours(canny2, [box], 0, (0, 0, 255))
        a.append([x, y])

cv2.imshow("kontur", red)
cv2.imshow("kontur1", img)
# cv2.imshow("th1", th1)
# cv2.imshow("th2", canny2)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()