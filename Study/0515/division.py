#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
print("Give me two numbers, and i'll divide on")
print("Enter 'q' to quit." )
while True:
    first_number = input("\nFirst Name: ")
    if first_number == "q":
        break
    last_number = input('\nLast name: ')
    if last_number == "q":
        break
    try:
        answer = int(first_number)/int(last_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by 0!")

