# 导入函数的方法
* ##### import module_name
    >"导入指定模块"
* ##### from module_name import function_name
    >"导入特定的函数"
* ##### from module_name import function_name as mp
    >"使用as 给函数指定别名"
    
* ##### import module_name as mn
    >"使用as给模块指定别名"
* ##### from module_name import *
    >"导入模块中的所有函数"
# 函数编写指南
###### (应给函数指定描述性名称，且只在其中使用小写字母和下划线。)
* ##### def function_name(parameter_0, parameter_1='default value')
    >"给形参指定默认值时，等号两边不要有空格"
* ##### functionname(value0, parameter1='value')
    >"对于函数调用中的关键字实参，也应遵循这种约定"