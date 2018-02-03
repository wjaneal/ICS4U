# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-01-15
Program Title: Area Under Curves
Purpose:
(1) Find the area under y = sin(x) from x=0 to x = PI.
(2) Find the area under y = 2^x from x = 1 to x = 10
(3) Find the area under a curve of your choice on a range of your choice.
"""

import math
print('Question 1')
a = 0
b = math.pi
n = 1000000
Area1 = 0.0
def f(x):
    return math.sin(x)

for i in range(1,1+n):
    xi = a + i*(b-a)/n
    Ai = (b-a)/n*f(xi)
    Area1 += Ai
print(Area1)

print()

print('Question 2')
c = 1
d = 10
n= 1000000
Area2 = 0.0
def g(x):
    return 2**x
 
for j in range(1,1+n):
    xj = c + j*(d-c)/n
    Aj = (d-c)/n*g(xj)
    Area2 += Aj
print(Area2)

print()

print('Question 3')
e = int(eval(input('please tell me the beginning of the interval: ')))
f = int(eval(input('please tell me the end of the interval: ')))
n = 1000000
Area3 = 0.0
def h(x):
    return abs(math.tan(x))

for k in range(1,1+n):
    xk = e + k*(f-e)/n
    Ak = (f-e)/n*h(xk)
    Area3 += Ak
print(Area3)



