#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
file_name = "programming.txt"
with open(file_name, 'w') as file_object:
    file_object.write("I Love programming!\n")
# 打印多行
    file_object.write("I Love creating new games\n")


with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
