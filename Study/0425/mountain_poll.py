#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
# 使用用户的输入来填充列表
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == "no":
        polling_active = False
print("\n=== Poll Rrsults ===")
for name, response in responses.items():
    print(name + "would like to climb" + response + ".")
