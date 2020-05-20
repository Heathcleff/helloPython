# -*- coding:utf-8 -*-
# function.py
# author @zeshen
# function - Demonstrating how to define a function and call to reuse it.

import matplotlib.pyplot as plt
import numpy as np
import math as m

def fx(x):
    f=(2.7**x+2.7**(-x))/(2.7**x-2.7**(-x))
    return f

res=fx(2.0)
print(res)

x=np.linspace(-2,2,1000)
y=fx(x)
plt.figure(figsize=(10.8,10.8))
plt.plot(x,y)
plt.savefig('plotexample1.png')
plt.show()

x1=np.random.random(50)
x2=-1*np.random.random(50)
print(x1)
plt.figure(figsize=(10.8,10.8))
plt.plot(x1,(2.7**x1+2.7**(-x1))/(2.7**x1-2.7**(-x1)),'rx')
plt.plot(x2,(2.7**x2+2.7**(-x2))/(2.7**x2-2.7**(-x2)),'bo')
plt.savefig('plotexample2.png')
plt.show()
