# encoding=utf-8
__author__ = 'vvliebe'

# 中值滤波器

import cv2

img = cv2.imread('imgs/SAM_0961.jpg')


while True:
    if cv2.waitKey(0) != 99:
        break
cv2.destroyAllWindows()










