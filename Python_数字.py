# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:11:13 2018

@author: xujia
"""

"""
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
"""

# Ask the age

print('What is your age?') 
myAge = input()
print('I see. You will be ' + str(int(myAge) + 1) + ' in a year.')
