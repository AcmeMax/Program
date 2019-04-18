#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax

# 用for循环去打印列表里面的元素
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + " that was a great trick!")


# 创建数值列表
# python 使用range()可以创建一系列数字
for i in range(1, 9):
    print(i)

# 使用range()生成一个列表
List = list(range(1, 9))
print(List)

# range()的第三个参数是指出每次增长多少个数
list1 = list(range(1, 20, 3))
print(list1)


# 创建一个列表,将1到10的平方加上去
sqls = []
for value in range(1, 11):
    sql = value**2
    sqls.append(sql)
print(sqls)


# 练习
for value in range(1, 21):
    print(value)

sqles = list(range(1, 1000000))
for value in sqles:
    print(value, "\n")
