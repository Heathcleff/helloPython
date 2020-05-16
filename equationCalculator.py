# -*- coding: utf-8 -*-
# equationCalculator.py
# author @zeshen
# function - Calculate the quadratic equation of one variable

print("方程模板：Ax^2+Bx+C=D\n")

# 输入参数
'''
以下程序将input函数和float函数进行嵌套。
input函数获取用户输入，然后将用户输入作为<字符类型>传递，
此例中，字符值被传递给了float函数，
float函数将传入参数由字符类型转换为浮点类型后赋值给变量
-*-注意，字符型型参数无法参与数值计算，需要进行格式转换-*-
'''
a = float(input("请输入A：\n"))
b = float(input("请输入B：\n"))
c = float(input("请输入C：\n"))
d = float(input("请输入D：\n"))

# 标准化方程
c = c - d  # 注意，这里对c变量进行了迭代，相当于c'=c-d，c'为过程后的变量

# 计算delta
delta = b ** 2 - 4 * a * c

# 求解并输出
'''
以下程序将使用一种名为“判断结构”的机制，其基础组分为if，else，elif。
运行思路为自上而下，若逻辑判断为真，则执行该判断结构内的语句，然后向下继续遍历；
若逻辑判断为伪，则跳转至下一个判断结构，直至遍历完全部逻辑判断语句。
书写判断语句以及后面将引入的循环语句时，要注意语句的缩进，缩进是区分语句层次的唯一依据，
若缩进出现错误，Python解释器将报错或执行异常。
判断语句有时也可以是直接的True和False，这样也可以使判断结构正常运行。
特殊的，我们将非0值定义为真，将0定义为伪，如果发现判断语句不是表达式而是任一非0值时，
我们也认为该逻辑判断为真，反之为伪。
'''
if delta > 0:
    print('x1 = ', (-b - delta ** 0.5) / 2 / a, '\nx2 = ', (-b + delta ** 0.5) / 2 / a)
elif delta == 0:
    print('x1 = x2 = ', (-b - delta ** 0.5) / 2 / a)
elif delta < 0:
    print('该方程没有实数解！')
# 排错部分：若出现意外的状况，输出字符进行报错
else:
    print('程序错误！\n请检查源代码和输入是否有误！\n')
