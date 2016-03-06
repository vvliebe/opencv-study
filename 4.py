# encoding=utf-8
__author__ = 'vvliebe'

# 分离通道

import cv2

img = cv2.imread('imgs/SAM_0994.jpg')
b, g, r = cv2.split(img)

cv2.imshow('img', img)
cv2.imshow('red', r)
cv2.imshow('green', g)
cv2.imshow('blue', b)

cv2.waitKey(0)
cv2.destroyAllWindows()