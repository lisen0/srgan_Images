# -*- coding: utf8 -*-

import numpy
import cv2
import scipy

x = cv2.imread('HR_upsample/evaluate/valid_hr_0_0.bmp')
#x = (x + 1) * 127.5
x = x / 4
cv2.imwrite('HR_upsample/evaluate/modified_hr_0_0.bmp', x)
