#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax


# 使用sort对列表进行永久性的排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# 给sort()加上参数reverse = True 输出的数组和正序的相反
cars.sort(reverse=True)
print(cars)

# 使用sorted()对列表进行临时性的排序, 同样他也有reverse = True
cars1 = ['bmw', 'audi', 'toyota', 'subaru']
print("这是原来的列表:")
print(cars1)
print("这是临时修改的列表:")
print(sorted(cars1))
print(sorted(cars1, reverse=True))
print("这个是经历了sorted()之后的列表:")
print(cars1)


# reverse()方法可以是列表倒序打印
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print(cars2)
cars2.reverse()
print(cars2)


# len()可以确定列表的长度
cars3 = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars3))

# 练习
citys = ["sanya", "changshang", "beijing", "shanghai", "nanjing"]
print(citys)

print(sorted(citys))

print(citys)

print(sorted(citys, reverse=True))

print(citys)

citys.reverse()
print(citys)

citys.reverse()
print(citys)

citys.sort()
print(citys)

citys.sort(reverse=True)
print(citys)
