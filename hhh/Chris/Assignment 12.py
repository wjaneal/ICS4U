# -*- coding: utf-8 -*-
"""
Assignment 12 - Recursive Algorithms - Towers of Hanoi
Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names
(1) Create a class with functions for three recursive algorithms.  
Include factorials, the Towers of Hanoi and any other recursive 
function.  Allow the user to choose any of the three functions 
and then interact with the function.  The program should provide 
adequate instructions and output to be useful.
"""

def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
    if source:
        target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print(source, helper, target)

def fib(n):#The Fibonacci numbers are defined by: 
#Fn = Fn-1 + Fn-2 
#with F0 = 0 and F1 = 1 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n=int(input("input a number to compute the fibonacci:"))
print(fib(n))