# encoding=utf-8
__author__ = 'vvliebe'

# 直方图

import cv2
import numpy as np


# hist = cv2.calcHist([img],
#                     [0], # 使用的通道
#                     None, # 没有使用mask
#                     [256], # HistSize
#                     [0.0, 255.0] # 直方图的范围
#                     )

def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])  # 计算直方图的数据
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)

    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color, )

    return histImg


img = cv2.imread('imgs/SAM_0974.jpg')

b, g, r = cv2.split(img)

histImgB = calcAndDrawHist(b, [255, 0, 0])
histImgG = calcAndDrawHist(g, [0, 255, 0])
histImgR = calcAndDrawHist(r, [0, 0, 255])

cv2.imshow('histImageB', histImgB)
cv2.imshow('histImageG', histImgG)
cv2.imshow('histImageR', histImgR)

cv2.waitKey(0)
cv2.destroyAllWindows()
