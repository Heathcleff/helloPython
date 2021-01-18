# 将sys中的argv模块引入脚本
from sys import argv

# 将argv解包到script和filename两个变量中
script, filename = argv

# 打开filename所指的文件，赋值对象给txt
txt = open(filename)

# 输出1
print(f"Here's your file {filename}:")
# 读取txt对象内容，将读取的信息输出
print(txt.read())

# 引导用户输入文件名
print("Type the file name again:")
# 使用input获取用户输入的文件名
file_again = input(">")

# 打开file_again所指的文件，并将对象赋值给txt_again
txt_again = open(file_again)

# 使用read方法读取对象txt_again的内容，并将内容输出
print(txt_again.read())

