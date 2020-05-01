# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:11:13 2018

@author: xujia
"""
# Ask the name and age
print('Hello! What\'s your name?') #ask for their name
myName = input()
print('It is good to meet you, ' + myName)

print('What is your age?') #ask for their age
myAge = input()
print('I see. You will be ' + str(int(myAge) + 1) + ' in a year.')
