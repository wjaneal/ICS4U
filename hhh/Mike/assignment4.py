# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-15
Program Title: assignment4
Purpose: 
(1) Find the area under y = sin(x) from x=0 to x = PI.
(2) Find the area under y = 2^x from x = 1 to x = 10
(3) Find the area under a curve of your choice on a range of your choice.
Variable names: a, b, c, d, e, f, n, Area1, Area2, Area3, xi, Ai, xj, Aj, xk, Ak, i, j, k
"""
import math
print ('Part 1')
a = 0
b = math.pi
n = 1000000
Area1 = 0.0
def f(x):
    return math.sin(x)
for i in range (1,n+1):
    xi = a + (b-a)/n * i
    Ai = (b-a)/n * f(xi)
    Area1 += Ai
print(Area1)

print()
print('Part 2')
c = 1
d = 10
n = 1000000
Area2 = 0.0
def g(x):
    return 2 ** x
for j in range (1,n+1):
    xj = c + (d-c)/n * j 
    Aj = (d-c)/n * g(xj)
    Area2 += Aj
print (Area2)

print ()
print ('Part 3')
e = int(eval(input('please tell me the beginning of the interval: ')))
f = int(eval(input('please tell me the end of the interval: ')))
n = 1000000
Area3 = 0.0
def h(x):
    return 4**x + x**2
for k in range (1,n+1):
    xk = e + (f-e)/n * k
    Ak = (f-e)/n * h(xk)
    Area3 += Ak
print (Area3)

