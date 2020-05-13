
# 我的Python大数据学习路线

- Author @Heathcleff
- 参考书籍：余本国 -《基于Python的大数据分析基础及实战》
- 写于2020年5月
---

[TOC]

## Python语法基础

### 你好，Python！

本节Python脚本参见仓库中的*helloPython.py*。

在下面的示例程序中，您将看到以下演示内容：

| 内容 | 行数（范围）|
|:----:|:----:|
|注释与多行注释|line |

```python
# helloPython.py
# Author @Heathcleff
# -*- coding: utf-8 -*-
'''
这是多行注释，注释在执行时并不会对被三个引号（单引号或双引号）包围起来的字段，
或以“#”号开头的行。
上面的“coding”字段为更改程序编码为UTF-8。
'''
"""
 Pycharm中可以显示为加粗字体，可以用来作为程序步的标志说明注释
这也是一种多行注释。
"""
str="Hello, Python!"
print(max(1,2,3,4))
print("a")
print(str)
for i in range(len(str)):
    print(str[i])
print("Python支持一个语句",
      "分多行书写，这样有很多好处。",
      "显而易见，这样书写使代码具有层次感，更加美观",
      "且如果将某函数的各项参数进行分行书写，",
      "也使程序易于修改和阅读。\n",
      "你所看到的是实现分行书写的一种方式。")
print("Python支持一个语句"\
      "分多行书写，这样有很多好处。"\
      "显而易见，这样书写使代码具有层次感，更加美观"\
      "且如果将某函数的各项参数进行分行书写，"\
      "也使程序易于修改和阅读。\n"\
      "你所看到的是实现分行书写的一种方式。")
name=input("Please enter your name:\n")
print("你好，",name,"，看到这种输出效果了吗？\n",
        "这就是标准输入函数和标准输出函数的复合使用效果。")
```
