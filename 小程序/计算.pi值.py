# pi.py
from random import *
from math import sqrt
from time import clock
DARTS = 120
hits = 0
seed(1)
clock ()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print ("Pi的 值是%s" % pi)
print ("程序运行时间是%-8.6ss" % clock())
