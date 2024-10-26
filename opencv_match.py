import cv2
import numpy as np

'''匹配算法'''
'''想要匹配不同大小的菱形的图像，可以放大缩小图像'''

image = cv2.imread('./img/poker.png')
cv2.imshow('image', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度化处理
cv2.imshow('image', gray)
cv2.waitKey(0)
template = gray[61:108, 250:285]  # 提取模板图片
cv2.imshow('image', template)
cv2.waitKey(0)
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)  # 模版匹配算法
print(match)
locations = np.where(match >= 0.9)  # 找出匹配系数大于0.9的匹配点

w, h = template.shape[0:2]  # 求出模版图案的长和宽

# 循环遍历每一个匹配点，在原始图像上画出相应的矩形框
for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2,y2),(0,255,0),2)

cv2.imshow('image', image)
cv2.waitKey(0)