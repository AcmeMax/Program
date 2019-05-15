#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
# 使用json.dump来储存这组数字
import json
number = [1, 2, 3, 4, 5, 6, 7]
filename = "number.json"
with open(filename, "w") as f_obj:
    json.dump(number, f_obj)


# 使用json.load()来将这个列表读取到内存中
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
