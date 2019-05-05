#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# name = input("Please enter your name: ")
# print("Hello " + name)



# 求模运算符%
number = input("Enter a number, and i'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")


# 练习
car = input("What kind of car would you like to rent? :")
print("Let me see if can find you a " + str(car))


food = input("How many people are coming to dinner, please? :")
food = int(food)
if food >= 8:
    print("Sorry, we don't have any vacant tables")
else:
    print("we have a table free")
