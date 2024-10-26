import cv2

'''滤波'''
image = cv2.imread('./img//噪点图1.png')
gauss = cv2.GaussianBlur(image, (5, 5), 0 ) #高斯滤波
median = cv2.medianBlur(image,5) #中值滤波
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.imshow('gaussian',gauss)
cv2.waitKey(0)
cv2.imshow('median', median)
cv2.waitKey(0)
