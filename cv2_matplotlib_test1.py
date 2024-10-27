import cv2
import matplotlib.pyplot as plt

"""matplotlib"""

image = cv2.imread('img/zaodian.png')
print(f'width:    {image.shape[1]}')
print(f'height:   {image.shape[0]}')
print(f'channels: {image.shape[2]}')
cv2.imshow('image', image)
cv2.waitKey(0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.axis('off')
plt.show()

cv2.imwrite('img/zaodian_new.png', image)