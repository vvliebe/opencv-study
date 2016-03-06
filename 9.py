# encoding=utf-8
__author__ = 'vvliebe'

# 高斯模糊

import cv2

img = cv2.imread('imgs/SAM_0961.jpg')

result1 = cv2.GaussianBlur(img, (5, 5), 1.5)  # 后两个参数为 模糊矩阵 和 标准差
result2 = cv2.GaussianBlur(img, (5, 5), 2.5)  # 模糊矩阵和标准差越大, 图像越模糊
result3 = cv2.GaussianBlur(img, (5, 5), 3.5)

cv2.imshow('origin', img)
cv2.imshow('gaussian 1.5', result1)
cv2.imshow('gaussian 2.5', result2)
cv2.imshow('gaussian 3.5', result3)

while True:
    if cv2.waitKey(0) != 99:
        break
cv2.destroyAllWindows()




