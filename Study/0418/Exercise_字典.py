#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax

# 在Python中, 字典就是一系列的键值对
alian_1 = {'color': 'green', 'points': '5'}
print(alian_1['color'])
print(alian_1['points'])
print(alian_1)

# 给外星人加一个随机出现的坐标
alian_1['x_position'] = 0
alian_1['y_position'] = 25
print(alian_1)
# python字典只关系键值对的关联关系,不关心键值对的排列顺序

# 有时候我们会先添加字典,然后在加键值对进去
alian_1 = {}
alian_1["color"] = 'red'
alian_1['points'] = 5
print(alian_1)


# 改变字典里面定义的值
alian_1 = {'color': 'red'}
print(alian_1)
alian_1["color"] = 'green'
print(alian_1)

alian_1 = {'x_position': '1', 'y_position': '25', 'speed': 'medium'}
print("old x = position :" + str(alian_1["x_position"]))

if alian_1['speed'] == 'slow':
    x_increment = 1
elif alian_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
print(type(x_increment))
print(type(alian_1['x_position']))
alian_1['x_position'] = int(alian_1['x_position']) + x_increment
print("new x = position:" + str(alian_1['x_position']))
print(type(alian_1['x_position']))


# 可以通过del来删除来将一个键删除同时删除他的值
alian_1 = {'color': 'red', 'points': '5'}
del alian_1['points']
print(alian_1)


#  遍历字典
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print('KEY: ' + key)
    print('value: ' + value)


