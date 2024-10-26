import cv2
import numpy as np
'''绘图'''
image = np.zeros((300, 300, 3), np.uint8)
cv2.imshow('image', image)
cv2.waitKey(0)
#画直线
cv2.line(image, (100,200), (250,250), (255,0,0), 2)
cv2.imshow('image', image)
cv2.waitKey(0)
#画矩形
cv2.rectangle(image, (30, 100), (60, 150), (0, 255, 0), 3)
cv2.imshow('image', image)
cv2.waitKey(0)
#画圆
cv2.circle(image, (150,100), 20, (0, 0, 255), 3)
cv2.imshow('image', image)
cv2.waitKey(0)
#绘制字符串
cv2.putText(image, 'hello', (100, 50), 0, 1, (255, 255, 255),2, 3)
cv2.imshow('image', image)
cv2.waitKey(0)

exit()
img = cv2.imread('./img/OpenCV_Logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255)
contours, hierarchy = cv2.findContours(thresh)
cnt = contours[0]
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x, y), ())
cv2.imshow('image')

