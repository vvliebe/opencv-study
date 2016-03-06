# encoding=utf-8
__author__ = 'vvliebe'

# 模糊

import cv2

img = cv2.imread('imgs/background3.jpg')

result = cv2.blur(img, (15, 15))

cv2.imshow('src', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()






