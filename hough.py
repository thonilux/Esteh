import sys
import math
import cv2 as cv
import cv2
import numpy as np


def main(argv, csdt=None):
    laser = cv.imread("laser.jpeg",1)
    src = laser.copy()
    red = laser[:, :, 1]
    red1 = 255-red
    dst = cv.Canny(red1, 50, 200, None, 3)

    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    cv.line(laser, (0,540), (1200,540), (0, 0, 255), 3, cv.LINE_AA)
    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            if  a<0 and a>(-0.001) :
                x0 = a * rho
                y0 = b * rho
                y1 = int(y0 + 1000 * (a))
                y2 = int(y0 - 1000 * (a))
                selisih=540-y1
                pt1 = (0,y1)
                pt2 = (1200, y2)
                if y1>10 or y2>10:
                    cv.putText(laser, 'Selisih='+str(selisih)+'Px', (50,y1-10), cv.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 1, cv.LINE_AA)
                    cv.line(laser, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)
                print(pt1)
                print(pt2)
##################################################

    src[:, :, 2] = np.zeros([src.shape[0], src.shape[1]])
    grey = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (9, 9), 0)
    canny = cv2.Canny(blur, 1, 100)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        tinggi = 10
        area1 = cv2.contourArea(c) / 1000
        area = w * h / 1000
        are = str(area)
        xway = w * tinggi
        yway = h * tinggi
        surface = (2 * area) + (2 * xway) + (2 * yway)
        volume = w * h * tinggi
        print("%.2f" % surface)
        position = (x + 10, y - 10)
        # draw the biggest contour (c) in green
        #cv2.rectangle(laser, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.drawContours(laser, contours, -1, 255, 3)
        cv2.putText(laser, "Area = " + "%.2f"%area1 +'Px', position, cv.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 1,cv.LINE_AA)
        # cv2.putText(canny, "Area = " + "%.2f" % area1, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 2)

    cv.imshow("Source", laser)


    cv.waitKey()
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])