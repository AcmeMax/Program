#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
# 删除一个列表里面的特定值
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove("cat")
print(pets)
