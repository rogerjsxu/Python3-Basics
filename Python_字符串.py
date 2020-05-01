# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:11:13 2018

@author: xujia
"""


##字符串(String)

#python中单引号和双引号使用完全相同。
#使用三引号('''或""")可以指定一个多行字符串。
#转义符:反斜杠 '\'可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
#字符串可以用 + 运算符连接在一起，用 * 运算符重复。
#Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
#Python中的字符串不能改变。



# Ask the name
print('Hello! What\'s your name?') #内含转义符
myname = input()
print('It is good to meet you, ' + myname + '.')

