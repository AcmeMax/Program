#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:acmemax
# 首先创建一个列表，其中包括一些要打印的设计
unprinted_designs = ['cgsacasu', 'aycvasc', 'ahcas']
completed_modles = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("Printing modles:" + current_design)
    completed_modles.append(current_design)

# 显示打印好了的所以模型
print("\nThe following models have been printed")
for completed_modle in completed_modles:
    print(completed_modle)


# 使用函数处理以上的代码
def print_models(unprinted_designs, completed_modles):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing models: " + current_design)
        completed_modles.append(current_design)

def show_completed_models(completed_models):
    # 显示已经打印好了的所有模型
    