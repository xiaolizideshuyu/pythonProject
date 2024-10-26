import cv2

'''梯度算法：常用来检测边缘  '''

gray = cv2.imread('./img/OpenCV_Logo.png', cv2.IMREAD_GRAYSCALE) #梯度算法接收灰度图

laplacian = cv2.Laplacian(gray, cv2.CV_64F) #拉普拉斯算子
canny = cv2.Canny(gray,100,200)#卡尼算法

cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)
cv2.imshow('canny',canny)
cv2.waitKey(0)
