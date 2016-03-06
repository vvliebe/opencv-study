# encoding=utf-8
__author__ = 'vvliebe'

# 连线

import cv2
import numpy as np

img = cv2.imread('imgs/SAM_1048.jpg')

h = np.zeros((256, 256, 3))

bins = np.arange(256).reshape(256, 1)

color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

for index, col in enumerate(color):
    originHist = cv2.calcHist([img], [index], None, [256], [0, 256])
    cv2.normalize(originHist, originHist, 0, 255 * 0.9, cv2.NORM_MINMAX)
    hist = np.int32(np.around(originHist))
    pts = np.column_stack((bins, hist))
    cv2.polylines(h, [pts], False, col)

h1 = np.flipud(h)



cv2.imshow('colorhist', h)
cv2.imshow('colorhist1', h1)

cv2.waitKey(0)
cv2.destroyAllWindows()
