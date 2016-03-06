# encoding=utf-8
__author__ = 'vvliebe'

# 滤波实际上是信号处理里的一个概念,而图像本身也可以看成是一个二维的信号.其中的像素点灰度值高低代表信号的强弱
# 高频: 图像中灰度变化剧烈的点
# 低频: 图像中平坦的,灰度变化不大的点

# 根据图像的高频与低频的特征,我们可以设计相应的高通与低通滤波器,高通滤波器可以检测出图像中尖锐,变化明显的地方;
# 低通滤波器可以让图像变得光滑,滤波图像中的噪声

# 常见的低通滤波器 blur 函数, 高斯模糊, 中值滤波
# 高通滤波器  Sobel算子  Laplacian 算子 Canny 算子

# blur函数

import cv2

img = cv2.imread('imgs/background3.jpg')

result = cv2.blur(img, (15, 15))

cv2.imshow('src', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()






