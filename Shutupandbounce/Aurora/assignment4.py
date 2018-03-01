#Name: Aurora Hou
#Date: January 15, 2018
#Program Title: Area Calculator
#Program Function: This program calcuates the area under curves (mathematical functions)
from math import *
#Variables:
pi = 4*atan(1)
Areaf1 = 0.0
Areaf2 = 0.0
Areaf3 = 0.0
n = 1000000
#This is the function to use in the area calculation
def f1(x):
    return sin(x)
def f2(x):
    return 2 ** x
def f3(x):
    return 6*x-7

for i in range(1, n+1):#Find xi, the current x value
    a = 0.0 #This is the starting x value
    b = pi #This is the ending x valu
    xi = a+((b-a)/n)*i#find the function value
    Aif1 = f1(xi)*(b-a)/n
    Areaf1 += Aif1
print(Areaf1)

for i in range(1,n+1):
    a = 1.0 #This is the starting x value
    b = 10.0 #This is the ending x value
    xi = a+((b-a)/n)*i
    Aif2 = f2(xi)*(b-a)/n
    Areaf2 += Aif2
print(Areaf2)

for i in range(1, n+1):#Find xi, the current x value
    a = 5.0 #This is the starting x value
    b = 10.0 #This is the ending x value
    xi = a+((b-a)/n)*i#find the funcion value
    Aif3 = f3(xi)*(b-a)/n
    Areaf3 += Aif3
print(Areaf3)