# encoding=utf-8
__author__ = 'vvliebe'

# 加载图像

import cv2

# 读取图像
img = cv2.imread('imgs/SAM_0961.jpg')

cv2.namedWindow('Image')

# 显示图像
cv2.imshow('Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()