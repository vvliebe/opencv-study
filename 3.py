# encoding=utf-8
__author__ = 'vvliebe'

# 访问像素 生成椒盐图

import cv2
import numpy as np


def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])  # img.shape = [width, height, (2 | 3)]
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i] = [255, 255, 255]
    return img


img = cv2.imread('imgs/SAM_0978.jpg')

saltImg = salt(img, 1000)

cv2.imshow('Salt', img)

cv2.imwrite('build/imgs/2.jpg', saltImg)

cv2.waitKey(0)

cv2.destroyAllWindows()