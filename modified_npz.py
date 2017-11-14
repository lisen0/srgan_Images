# -*- coding: utf8 -*-

import numpy as np

net = np.load('checkpoint/g_srgan.npz')
x = net['params']
print type(x)
print x[0].shape
print x[2].shape
