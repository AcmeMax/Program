#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
# 你调用函数时,python必须将函数调用中的每一个实参都关联到函数定义中的一个形参,
# 因此,最简单的关联方式是基于实参的循序,这种方法叫做位置实参
# 可以先给形参定义参数
def describe_pet(animal_type, pet_name="dcgahc"):
    # 显示宠物信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())
describe_pet("hamster", "acmemax")

# 你可以根据需要调用函数任意次
describe_pet("pig", "achica")

# 如果定义了形参  位置实参只要传未定义的
describe_pet('dog')

# 关键字实参
describe_pet(pet_name="dcacb", animal_type="dog")

