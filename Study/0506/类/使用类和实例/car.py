#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")


my_new_car = Car("asc", "aas", "12")
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(-1)
my_new_car.read_odometer()

