import cv2
import matplotlib.pyplot as plt

"""matplotlib"""

image = cv2.imread('img/zaodian.png')
h, w, c = image.shape
print(image.shape)

(b, g, r) = image[0, 0]  # 一个像素返回三个通道值
print(image[0, 0])

# 给0像素重新复制
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print(image[0, 0])

cX, cY = (h // 2, w // 2)
t1 = image[0:cX, 0:cY]
plt.imshow(t1)
plt.axis('off')
plt.show()

# cv2.imwrite('img/zaodian_new.png', image)
