#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
# 返回字典
def build_person(frist_name, last_name):
    person = {"frist": frist_name, "last": last_name}
    return person
musician = build_person("acme", "max")
print(musician)

def build_person_copy(frist_name, last_name, age = ""):
    person = {"frist": frist_name, "last": last_name}
    if age:
        person["age"] = age
    return person
musician = build_person_copy("acme", "max", "27")
print(musician)
