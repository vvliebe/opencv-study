# encoding=utf-8
__author__ = 'vvliebe'

# Canny 算子

import cv2

img = cv2.imread('imgs/SAM_0961.jpg',0)

gaussImg = cv2.GaussianBlur(img, (3, 3), 0)

canny = cv2.Canny(img, 50, 150)

cv2.imshow('origin', img)
cv2.imshow('gauss', gaussImg)
cv2.imshow('canny', canny)

while True:
    if cv2.waitKey(0) != 99:
        break

cv2.destroyAllWindows()