# -*- coding: utf8 -*-

import numpy as np
import scipy
import cv2
import os

path = 'finger_imgs/finger_HR_crop/'
first = 100
for file in sorted(os.listdir(path)):
    second = 10
    x = cv2.imread(path + file, 0)
    #file_name_list = (path+file).split('/')
    #file_name = file_name_list[-1].split('.')[0]
    i = 0
    for count in range(4):
        j = 0
        for count_1 in range(4):
            _x = x[i:i+96, j:j+96]
            cv2.imwrite('finger_imgs/finger_HR_split/{}_{}.bmp'.format(first, second), _x)
            second += 1
            j += 96
        i += 96
    first += 1

