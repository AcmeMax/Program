#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
def greet_user():
    # 显示简单的问候域
    print("hello!")
greet_user()

# 加上用户名
def greet_user_1(username):
    print("Hello " + username.title() + "!")
greet_user_1("acmemax")