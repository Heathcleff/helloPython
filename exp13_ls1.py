# 错误的调用方式：
# import sys.argv
from sys import argv

script, x, y = argv
print("Sum of x and y is:", int(x) + int(y))
# 不进行转化的后果：
print("If you do not transform string to numeric, it will be:", x + y)
