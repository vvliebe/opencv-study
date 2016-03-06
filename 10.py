# encoding=utf-8
__author__ = 'vvliebe'

# 中值滤波器 去除椒盐

import cv2

img = cv2.imread('imgs/2.jpg')

result = cv2.medianBlur(img, 5)

cv2.imshow('origin', img)

cv2.imshow('result', result)

while True:
    if cv2.waitKey(0) != 99:
        break
cv2.destroyAllWindows()










