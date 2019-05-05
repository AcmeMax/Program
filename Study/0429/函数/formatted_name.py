#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
def get_formatted_name(first_name , last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
musicion = get_formatted_name("acme", "max")
print(musicion)

def get_formatted_name_copy(first_name, middle_name, last_name):
    full_name = first_name + " " + middle_name + " " +last_name
    return full_name.title()
musicion = get_formatted_name_copy("acme", "biao", "max")
print(musicion)

def get_formatted_name_copy_copy(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
musicion = get_formatted_name_copy_copy("acme", "max")
print(musicion)
musicion = get_formatted_name_copy_copy("acme", "wang", "max")
print(musicion)
