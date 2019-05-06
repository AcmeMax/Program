#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
class Dog():
    # 一次模拟小狗的简单尝试
    def __init__(self, name, age):
        # 初始化属性
        self.name = name
        self.age = age

    def sit(self):
        # 模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # 模拟小狗在命令时打滚
        print(self.name.title() + " rolled over")


my_dog = Dog("acac", "50")
my_dog.sit()
my_dog.roll_over()
