import cv2
import numpy as np
'''读取图像和显示图像'''
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    print(cv2.__version__)
    # print(cv2.getVersionInfo())
    image = cv2.imread('./img/opencv-logo.png')
    # print(image.shape)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    # print(cv2.getWindowProperty('image'))
    print(image[:, :, 0])
    print(image[:, :, 1])
    print(image[:, :, 2])
    cv2.imshow('blue', image[:, :, 0])
    cv2.waitKey(0)
    cv2.imshow('green', image[:, :, 1])
    cv2.waitKey(0)
    cv2.imshow('red', image[:, :, 2])
    cv2.waitKey(0)
    # 灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    cv2.waitKey(0)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
