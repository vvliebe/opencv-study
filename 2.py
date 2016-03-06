# encoding=utf-8
__author__ = 'vvliebe'

# 保存图像 imwrite

import numpy as np
import cv2

img = cv2.imread('imgs/SAM_0965.jpg')

print img.shape

# 初始化图片
emptyImage = np.zeros(img.shape, np.uint8)

# 复制图片
emptyImage2 = img.copy()

# 转为灰度图
emptyImage3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('img1', emptyImage)
cv2.imshow('img2', emptyImage2)
cv2.imshow('img3', emptyImage3)

cv2.imwrite('build/imgs/1.jpg', emptyImage3)

cv2.waitKey(0)

cv2.destroyAllWindows()