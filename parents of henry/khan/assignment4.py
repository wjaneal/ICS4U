#Name:Khan
#Date: January 15, 2018
#Program Title: Area Calculator
'''Program Function:
(1) Find the area under y = sin(x) from x=0 to x = PI.
(2) Find the area under y = 2^x from x = 1 to x = 10
(3) Find the area under y = x from x = 1 to x = 2.
variables:a,b,n,Area'''
import math
n = int(1000000) 
Area = 0.0
def f(x):
    return math.sin(x)

a = 0.0 #This is the starting x value
b = math.pi #This is the ending x value
for i in range(1,n+1):
    #Find xi, the current x value
    xi =  float(a+(i-1)*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = float(((b-a)/n))*float(f(xi))#i made some change here
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)

Area=0.0
a = 1.0 #This is the starting x value
b = 10.0 #This is the ending x value

def g(x):
    return 2**x


for i in range(1,n+1):
    #Find xi, the current x value
    xi =  float(a+(i-1)*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = float(((b-a)/n))*float((g(xi+(b-a)/n)+g(xi))/2)#i made some change here
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)

Area=0.0
a = 1.0 #This is the starting x value
b = 2.0 #This is the ending x value

def h(x):
    return x


for i in range(1,n+1):
    #Find xi, the current x value
    xi =  float(a+(i-1)*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = float(((b-a)/n))*float((h(xi+(b-a)/n)+h(xi))/2)#i made some change here
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)



