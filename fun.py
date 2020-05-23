# -*- coding:utf-8 -*-
# function.py
# author @zeshen
# function - Demonstrating how to define a function and call to reuse it.

import matplotlib.pyplot as plt
import numpy as np
import math as m

def fx(x):
    f= ((np.exp(x) + np.exp(-x)) / (np.exp(x) - np.exp(-x)))
    return f

plt.figure(figsize=(10.8, 10.8))
x1=np.linspace(-5,0,30)
y1=fx(x1)
x2=np.linspace(0,5,30)
y2=fx(x2)
plt.plot(x1,y1,'bx-',x2,y2,'rx-')
plt.show()