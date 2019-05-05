#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
def greet_user(username):
    print("Hello " + username.title())
greet_user("acmemax")

# 使用函数和while循环 给程序加上退出代码
def get_formutted_name(frist_name, last_name):
    full_name = frist_name + " " + last_name
    return full_name.title()

while True:
    print("/nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("Frist Name:")
    if f_name == "q":
        break
    l_name = input("Last Name:")
    if l_name == "q":
        break
    formutted_name = get_formutted_name(f_name, l_name)
    print("Hello " + formutted_name + "!")
