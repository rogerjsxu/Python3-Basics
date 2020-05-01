# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:31:57 2020

@author: xujia
"""
import numpy as np
import matplotlib.pyplot as plt
import random
'''
x = []
y = []
for i in range(50):
    x.append(random.uniform(1,90))
    y.append(random.uniform(0,10))
b = 0
sum_min = 10000
b_found = 0
while b<10:
    sum=0
    for i in range(50):
        sum+=(y[i]-b)**2
    if sum<sum_min:
        sum_min = sum
        b_found = b
    #print(b,sum)
    b = b + 0.01

plt.scatter(x,y)
plt.plot([0,100],[b_found,b_found])
plt.ylim(-20,40)
plt.show()
'''

def generate():
    x = []
    y = []
    for i in range(50):
        x.append(random.uniform(1,90))
        y.append(random.uniform(0,10))
    return x,y

def find_b(y):
    b = 0
    sum_min = 10000
    b_found = 0
    while b<10:
        sum=0
        for i in range(50):
            sum+=(y[i]-b)**2
        if sum<sum_min:
            sum_min = sum
            b_found = b
        #print(b,sum)
        b = b + 0.01
    return b_found

def plots(x,y,b_found):
    plt.scatter(x,y)
    plt.plot([0,100],[b_found,b_found])
    plt.ylim(-20,40)
    
m1,n1 = generate()
b1 = find_b(n1)

m2,n2 = generate()
b2 = find_b(n2)

plots(m1,n1,b1)
plots(m2,n2,b2)
plt.show()


