# -*- coding: utf8 -*-

from utils import *
import scipy
import cv2
import tensorlayer as tl

#x = get_imgs_fn('0_6.bmp', 'finger_imgs/finger_HR_split/')
#print x.shape
#print type(x)

x = cv2.imread('finger_imgs/finger_HR_split/0_0.bmp')
x = (x / 127.5) - 1
print x.shape
print x[45][45]
cv2.imwrite('finger_imgs/finger_HR_split/0_0_rgb_rescale.bmp', x)

#x = get_imgs_fn('0_0.bmp', 'finger_imgs/finger_HR_split/')
#x = (x / 127.5) - 1
#print x.shape
#print x[53][53]
#tl.vis.save_image(x, 'finger_imgs/finger_HR_split/0_0_tl_rescale.bmp')
