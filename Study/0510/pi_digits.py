#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())
