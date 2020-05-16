# -*- coding: utf-8 -*-
# factorial.py
# author @zeshen
# function - Calculate factorial

# while循环
n1 = int(input("请输入任意整数n: \n"))
i1= 1
fac1 = 1
while i1 <= n1:
    fac1 *= i1
    i1 += 1
print("n! = ", fac1)


# for循环
n2=int(input("请输入任意整数：\n"))
i2=1
fac2=1
for temp in range(n2):
    fac2*=i2
    i2+=1
print("n! = ",fac2)