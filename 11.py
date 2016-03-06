# encoding=utf-8
__author__ = 'vvliebe'

# sobel算子实现边缘检测

import cv2

img = cv2.imread('imgs/SAM_0961.jpg')

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow('origin', img)
cv2.imshow('absX', absX)
cv2.imshow('absY', absY)
cv2.imshow('result', dst)


while True:
    if cv2.waitKey(0) != 99:
        break

cv2.destroyAllWindows()
