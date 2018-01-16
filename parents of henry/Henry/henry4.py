# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 15/Tan/2018
Program Title:Area Calculater
Purpose:
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning

(1) Find the area under y = sin(x) from x=0 to x = PI.
(2) Find the area under y = 2^x from x = 1 to x = 10
(3) Find the area under a curve of your choice on a range of your choice.


""" 
from math import *
import math
a = 0
b = math.pi
n = 100000
Area1 = 0.0
def f(x):
    return math.sin(x)
for i in range (1,n+1):
    xi = a + (b-a)/n * i
    Ai = (b-a)/n * f(xi)
    Area1 += Ai
print(Area1)

c = 1
d = 10
n = 100000
Area2 = 0.0
def g(x):
    return 2 ** x
for j in range (1,n+1):
    xj = c + (d-c)/n * j
    Aj = (d-c)/n * g(xj)
    Area2 += Aj
print (Area2)


e = int(eval(input('starting x value:')))
f = int(eval(input('ending x value:')))
n = 100000
Area3 = 0.0
def h(x):
    return 2**x + x**2
for k in range (1,n+1):
    xk = e + (f-e)/n * k
    Ak = (f-e)/n * h(xk)
    Area3 += Ak
print (Area3)

    



    
    
    
    
    

    
