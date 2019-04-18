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


squers = [value**2 for value in range(1, 11)]
print(squers)


# 切片 使用列表的一部分
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 复制列表 切片只是暂时的复制列表 后面加上元素输出不会改变原来列表的值
my_foods = ['pizza', 'falafel', 'carrot cake']
my_foods_new = my_foods[:]
print(my_foods_new)
my_foods.append("ica")
print(my_foods)
my_foods_new.append("can")
print(my_foods_new)

my_foods1 = ['pizza', 'falafel', 'carrot cake']
my_foods1_new = my_foods1
print(my_foods1)
print(my_foods1_new)
my_foods1.append("ica")
my_foods1_new.append("can")
print(my_foods1_new)
print(my_foods1)


# 元组  元组定义了在一个周期类不能改变他的值  如果要改变需重新定义他的值
foods = ('sz', 'xhz', 'r', 'bc', 'nr')
for food in foods:
    print(food)

foods = ('sz', "ad", "e", "bc", "nr")
for food in foods:
    print(food)
