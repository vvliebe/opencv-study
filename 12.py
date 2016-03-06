# encoding=utf-8
__author__ = 'vvliebe'

# Laplacian 算子

import cv2

img = cv2.imread('imgs/SAM_0961.jpg')

qray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=5)

result = cv2.convertScaleAbs(qray_lap)

cv2.imshow('origin', img)
cv2.imshow('laplacian', result)

while True:
    if cv2.waitKey(0) != 99:
        break

cv2.destroyAllWindows()