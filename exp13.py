# 将Python的sys标准库中的argv引入脚本
from sys import argv

# 调试用代码：
# print(">>>>>解包前的argv",repr(argv))

# read the WYSS section for how to run this
script, first, second, third = argv

# 调试用代码：
# print(">>>>>>>argv[repr]:",repr(argv))
# print(">>>>>>>argv[str]:",str(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
