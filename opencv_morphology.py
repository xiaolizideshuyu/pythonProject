import cv2
import numpy as np
"""腐蚀和膨胀，可以交替使用"""

gray = cv2.imread('img/OpenCV_Logo.png',cv2.IMREAD_GRAYSCALE)
_,binary = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.imshow('binary',binary)
cv2.waitKey(0)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(binary,kernel) #腐蚀
cv2.imshow('erosion',erosion)
cv2.waitKey(0)

dilation = cv2.dilate(binary,kernel) #膨胀
cv2.imshow('dilation',dilation)
cv2.waitKey(0)