#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:49:44 2018

@author: Charlotte
"""

def f(n): #Define a function.
    if n == 0: #f(0) = 2
        return 2
    if n >= 1:
        return f(n-1)*3 + 2 #Define f(n) when n >= 1.

n = 0
while(f(n)<40000000): #Thw value of f(n) should be less than 40000000.
    print(f(n)) #
    n+=1 #The number of n increases by 1.
print("The number of n is",n)
