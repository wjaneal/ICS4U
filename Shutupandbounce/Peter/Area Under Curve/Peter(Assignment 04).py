#Name:Peter Zeng
#Date: January 15, 2018
#Program Title: Area Under Curve
#Program Function: (1) Find the area under y = sin(x) from x=0 to x = PI.
#(2) Find the area under y = 2^x from x = 1 to x = 10
#(3) Find the area under a curve of your choice on a range of your choice.

from math import*

                                                            #(1)
#Variables
q = 0 #This is the starting x value
w = pi  #This is the ending x value
e = 10000000  #This is the number of rectangles
Area1= 0.0  #This is the total area

#This is the function to use in the area calculation
def f1(x):
    return sin(x)

for i in range (1,e+1):
    #Find xi, the current x value
    xi = q+(w-q)/e*i
     #Find the area of the rectangle, Ai, using the function
    Ai = (q-w)/e*f1(xi)
     #Add it to the total area, "Area1"
    Area1 += Ai
    #Print the area here
print(Area1)
    
        
                                                            #(2)
#Variables
r = 1.0  #This is the starting x value
t = 10 #This is the ending x value
y = 1000000  #This is the number of rectangles
Area2= 0.0  #This is the total area

#This is the function to use in the area calculation
def f2(x):
        return 2**x

for n in range (1,y+1):
    #Find xn, the current x value
    xn = r+(t-r)/y*n
     #Find the area of the rectangle, An, using the function
    An = (r-t)/y*f2(xn)
     #Add it to the total area, "Area2"
    Area2 += An
    #Print the area here
print(Area2)
    
                                                            #(3)
#Variables
u = 1.0 #This is the starting x value
i = 900  #This is the ending x value
p = 50000  #This is the number of rectangles
Area3= 0.0  #This is the total area

#This is the function to use in the area calculation
def f3(x):
    return cos(x)+x/3+x*2

for m in range (1,p+1):
    #Find xm, the current x value
    xm = u+(u-i)/p*m
     #Find the area of the rectangle, Am, using the function
    Am = (u-i)/p*f3(xm)
     #Add it to the total area, "Area3"
    Area3 += Am
    #Print the area here
print(Area3)

    
    