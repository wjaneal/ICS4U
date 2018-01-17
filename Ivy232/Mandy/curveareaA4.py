#Name:Mandy
#Date: January 15, 2018
#Program Title: Area Calculator
#Program Function: This program calcuates the area under curves (mathematical functions)

'''
(1) Find the area under y = sin(x) from x=0 to x = PI.
(2) Find the area under y = 2^x from x = 1 to x = 10
(3) Find the area under a curve of your choice on a range of your choice.
'''
from math import *
#part1
a1 = 0.0 #This is the starting x value
b1 = pi #This is the ending x value
n = 1000000
Area1 = 0.0 #This is the total area
def g(x):
    return sin(x)

for i in range(1,n+1):
    #Find xi, the current x value
    xi1 = (b1-a1)/n + a1   
    #Find the area of the rectangle, Ai, using the function
    Ai1 =g((b1-a1)/n*i+a1) * (b1-a1)/n
    #Add it to the total area, "Area"
    Area1 += Ai1
#Print the area here
print (Area1)

#part2
a = 1.0 #This is the starting x value
b = 10.0 #This is the ending x value
n = 1000000 #This is the number of rectangles
Area = 0.0 #This is the total area
#This is the function to use in the area calculation
def f(x):
    return 2**x

for i in range(1,n+1):
    #Find xi, the current x value
    xi = (b-a)/n + a  
    #Find the area of the rectangle, Ai, using the function
    Ai =f((b-a)/n*i+a) * ((b-a)/n)
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)

#part3
a3 = 1.0 #This is the starting x value
b3 = 100.0 #This is the ending x value
n = 1000000 #This is the number of rectangles
Area3 = 0.0 #This is the total area
#This is the function to use in the area calculation
def h(x):
    return x**4

for i in range(1,n+1):
    #Find xi, the current x value
    xi3 = (b3-a3)/n + a3   
    #Find the area of the rectangle, Ai, using the function
    Ai3 =h((b3-a3)/n*i+a3) * (b3-a3)/n
    #Add it to the total area, "Area"
    Area3 += Ai3
#Print the area here
print (Area3)

