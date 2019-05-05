#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something , and i will repeat it back yo you!"
prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)


# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

citys = "\nplease enter the name of a city you have visited:"
citys += "\n(Enter 'quit'when you are finished.)"
while True:
    city = input(citys)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 1:
        continue
    print(current_number)
