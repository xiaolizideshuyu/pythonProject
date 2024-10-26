import cv2

"""图像阈值处理,二分法"""

grap = cv2.imread('img/yuzhi.png', cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(grap, 10, 255, cv2.THRESH_BINARY)
binary_adaptive = cv2.adaptiveThreshold(grap, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
ret1,binary_otsu=cv2.threshold(grap,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #日本大金算法,聚类分析算法，不需要人为定义阈值是多少
cv2.imshow('grap', grap)
cv2.waitKey(0)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.imshow('binary_adaptive', binary_adaptive)
cv2.waitKey(0)
cv2.imshow('binary_adaptive', binary_otsu)
cv2.waitKey(0)

