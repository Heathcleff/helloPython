# -*- coding:utf-8 -*-
# function.py
# author @zeshen
# function - Demonstrating how to define a function and call to reuse it.

import matplotlib.pyplot as plt
import numpy as np


def fx(x):
    f = ((np.exp(x) + np.exp(-x)) / 2 / (np.exp(x) - np.exp(-x))) + np.sinh(x)
    return f


print(fx(3))
x1 = np.linspace(-5, 0, 100)
y1 = fx(x1)
x2 = np.linspace(0, 5, 100)
y2 = fx(x2)
plt.figure(figsize=(10.8, 10.8))
plt.grid()
plt.plot(x1, y1, 'b-', x2, y2, 'r-')
plt.yscale('linear')
plt.savefig("plotexample.png",dpi=600)
plt.show()