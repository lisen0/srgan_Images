# -*- coding: utf8 -*-

import cv2
import os
import numpy as np
path = 'HR_upsample/evaluate/'

file_list = []
for file in os.listdir(path):
    print file
    im = cv2.imread(path + file, 0)
    file_list.append(im)

for i in [0, 4, 8, 12]:
    for j in [1, 2, 3]:
        file_list[i] = np.hstack((file_list[i], file_list[i+j]))

i = 0
for j in [4, 8, 12]:
    file_list[i] = np.vstack((file_list[i], file_list[i+j]))

print file_list[0].shape
cv2.imwrite(path + 'final_image.bmp', file_list[0])


