# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:34:35 2018
Name: Jaune
Date: Jan 15
Program Tiltle: Area Calculator
Propose: Calculates the area under curves
@author: CTL
"""

from math import *

x = 1.0
x1 = pi
n = 9999
area = 0.0
def f(x):
    return sin(x)

for i in range (1,n):
    xi = 0.0
    ai = f(x+(x1-x)*i/n) * (x1-x)/n
    area += ai
print (area)

from math import *

x = 1.0
x1 = 10.0
n = 9999
area = 0.0
def f(x):
    return 2**x

for i in range (1,n):
    xi = 0.0
    ai = f(x+(x1-x)*i/n) * (x1-x)/n
    area += ai
print (area)


from math import *

x = 1.0
x1 = 10.0
n = 9999
area = 0.0
def f(x):
    return x*x

for i in range (1,n):
    xi = 0.0
    ai = f(x+(x1-x)*i/n) * (x1-x)/n
    area += ai
print (area)
