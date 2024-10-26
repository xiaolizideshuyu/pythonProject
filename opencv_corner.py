import cv2

'''提取特征点'''

image = cv2.imread('./img/OpenCV_Logo.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.1,10)
for corner in corners:
    x,y= corner.ravel()
    cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)

cv2.imshow('corners', image)
cv2.waitKey()