#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:AcmeMax
# 打印出pi_digits.txt文件中的字符,打印之前要使用open打开文件
with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)
# 打印的文件会比原来增加后面的空格,我们使用rstrip()来删除后面的空格
    print('-'*50)
    print(content.rstrip())
print('-'*50)
# 单行输出
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for link in file_object:
        print(link)
print("-"*50)
# 单行输出去空格
with open(filename) as file_object:
    for link in file_object:
        print(link.rstrip())
print('^'*50)
# open()返回的对象只能在with模块中使用,如果要在with外使用的话要将它储存在一个列表中

filename = 'pi_digits.txt'
with open(filename) as file_object:
    links = file_object.readlines()
for link in links:
    print(link.rstrip())

# 使用文件中的内容
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
print('*'*100)
# 千位文件
filename = "pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
pi_million_string = ''
for line in lines:
    pi_million_string += line.strip()
print(pi_million_string[:54] + "......")
print(len(pi_million_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_million_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")