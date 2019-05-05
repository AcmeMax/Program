#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
musician = get_formatted_name("acme", "casa")
print(musician)