#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
def make_pizza(size, *toppings):
    print("\nMakeing a " + str(size) + "-inch pizza with the followingn toppings:")
    for topping in toppings:
        print("-" + topping)