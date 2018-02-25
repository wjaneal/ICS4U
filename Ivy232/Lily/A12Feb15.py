'''
Assignment 12 - Recursive Algorithms - Towers of Hanoi


Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

(1) Create a class with functions for three recursive algorithms.  Include factorials, the Towers of Hanoi and any other recursive function.  Allow the user to choose any of the three functions and then interact with the function.  The program should provide adequate instructions and output to be useful.
'''
#1: factorial


def func(x):
    if x == 1: #define a number when x = 1, allowing the function to recur.
        return 1
    else:
        return x *func(x-1) #This is to calculate the factorial.


#2:Move loops

def func(x):
    if x == 1: #define a number when x = 1, allowing the function to recur.
        return 1
    else:
        return 2**(x-1) + func(x-1) #This is to calculate the steps required.

def func2(x)
    print("It requires "+ str(func(x)) + " steps to move " + str(x) + " loops.")
    #This is to print the answer




#3:snowflake

from turtle import *

def f(length, depth):
    if depth == 0:
        forward(length) #This is to go forward for 1 unit
    else:
        f(length/3, depth-1) #This is the start of the loop
        right(60) #This step is to connect the end of every loop
        f(length/3, depth-1) #second loop
        left(120)
        f(length/3, depth-1) #third loop
        right(60)
        f(length/3, depth-1) #forth loop
        
        
def f1(length,repeat,spe):
    speed(spe)
    for i in range(3): #There are mainly three parts in a flake
        f(length,repeat)
        left(120) #This is to make a turn when finish one part out of the three.








 

























































'''
=======
>>>>>>> 81e8aa76a02d1c71b464c2e0e4b35300b428e514
'''
