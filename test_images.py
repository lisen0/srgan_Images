# -*- coding: utf8 -*-

#from utils import *
from tensorlayer.prepro import *
import numpy as np
import scipy
import os
from PIL import Image
import cv2

def crop_sub_imgs(x, is_random=False):
    x = crop(x, wrg=384, hrg=384, is_random=is_random)
    return x

def downsample(x):
    x = imresize(x, size=[96, 96], interp='bicubic', mode='L')
    return x

j = 0

for i in os.listdir('finger_imgs/finger_HR/'):
    print i
    x = scipy.misc.imread('finger_imgs/finger_HR/' + i, mode='L')
    #x = cv2.imread('finger_imgs/finger_HR/' + i, 0)
    print x.shape
    x = crop_sub_imgs(x)
    print type(x)
    print x.shape
    print x[1][1]
    scipy.misc.imsave('finger_imgs/finger_HR_crop/{}.bmp'.format(j), x)
    #x = x.resize([x.shape[0], x.shape[1], 1])
    x = list(x)
    x = np.resize(x, [np.shape(x)[0], np.shape(x)[1], 1])
    print x.shape
    x = downsample(x)
    #x = scipy.misc.imresize(x[:,:,0], [96, 96], interp='bicubic', mode='L')
    cv2.imwrite('finger_imgs/finger_LR/{}.bmp'.format(j), x)
    j = j + 1
'''
x = scipy.misc.imread('data2017/DIV2K_train_HR/0001.png')
print x.shape
'''
