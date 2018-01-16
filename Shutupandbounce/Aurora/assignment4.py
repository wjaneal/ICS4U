#Name: Aurora Hou
#Date: January 15, 2018
#Program Title: Area Calculator
#Program Function: This program calcuates the area under curves (mathematical functions)
from math import *
#Variables:
pi = 4*atan(1)
a = 0.0 #This is the starting x value
b = pi #This is the ending x value
n = 1000000 #This is the number of rectangles
Areaf1 = 0.0
Areaf2 = 0.0
Areaf3 = 0.0
#This is the function to use in the area calculation
def f1(x):
    return sin(x)
def f2(x):
    return 2 ** x
def f3(x):
    return 6*x-7

for i in range(n, n+1):
    #Find xi, the current x value
    xi = a+((b-a)/n)*i
    for x in range(0,int(pi)):
        #find the function value
        Aif1 = f1(xi)*(b-a)/n
        Areaf1 += Aif1
    #Find xi, the current x value
    for x in range(1,10):
        #find the function value
        Aif2 = f2(xi)*(a-b)/n
        Areaf2 += Aif2
    #Find the area of the rectangle, Ai, using the function
    for x in range(240,245):
        #find the funcion value
        Aif3 = f3(xi)*(a-b)/n
        Areaf3 += Aif3
    print("x =",x,"\n(1)",Areaf1,"\n(2)",Areaf2,"\n(3)",Areaf3)