# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:34:35 2018
Name: Jaune
Date: Jan 15
Program Tiltle: Area Calculator
Propose: Calculates the area under curves
@author: CTL
"""
#This is to import math
from math import *

x = 1.0
x1 = pi
n = 9999
area = 0.0
def f(x):
    return sin(x) #This line is to define a function f(x)=sin(x)

#This is to calculate the area under 1-n
for i in range (1,n):
    xi = 0.0
    ai = f(x+(x1-x)*i/n) * (x1-x)/n #This line is to calculate the area of those small rectangles.
    area += ai #This line is to add all the areas of those small rectangles.
print (area)


x = 1.0
x1 = 10.0
n = 9999
area = 0.0
def f(x):
    return 2**x #This line is to define a function f(x)=2^x

#This is to calculate the area under 1-n
for i in range (1,n):
    xi = 0.0
    ai = f(x+(x1-x)*i/n) * (x1-x)/n #This line is to calculate the area of those small rectangles.
    area += ai #This line is to add all the areas of those small rectangles.
print (area)




x = 1.0
x1 = 10.0
n = 9999
area = 0.0
def f(x):
    return x*x #This line is to define a function f(x)=x^2

for i in range (1,n):
    xi = 0.0
    ai = f(x+(x1-x)*i/n) * (x1-x)/n #This line is to calculate the area of those small rectangles.
    area += ai #This line is to add all the areas of those small rectangles.
print (area)
