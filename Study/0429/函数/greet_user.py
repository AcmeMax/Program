#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title()
        print(msg)
usernamas = ["dnisd0", "chaica", "ascbac"]
greet_users(usernamas)
