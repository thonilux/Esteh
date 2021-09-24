import numpy as np
import cv2 as cv
import cv2
from matplotlib import pyplot as plt
frame = cv2.imread("laser.jpeg", 1)
scale_percent = 60
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)




red = resized[:,:,2]
img = 255-red


cv2.imshow("red", img)
# cv2.imshow("kontur", mask)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()