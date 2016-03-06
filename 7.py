# encoding=utf-8
__author__ = 'vvliebe'

# 膨胀 和 腐蚀
# 可以检测边缘和拐角

import cv2

img = cv2.imread('imgs/background3.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))

# 腐蚀 高亮减弱, 整体变暗

eroded = cv2.erode(img, kernel)

cv2.imshow('Eroded Image', eroded)

# 膨胀 高亮加强, 整体变亮

dilated = cv2.dilate(img, kernel)

cv2.imshow('dilate image', dilated)

cv2.waitKey(0)

cv2.destroyAllWindows()
