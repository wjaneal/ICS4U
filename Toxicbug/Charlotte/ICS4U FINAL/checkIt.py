#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:53:58 2018

@author: Charlotte
"""
     
def checkIt(x): #Define a function.
    if x < 2: #The value of x cannot be less than 2.
        return False
    if x == 2:
        return True #THe value of x can be equal to 2 and it is the minimum value of x.
    if x > 2:
        x = (x-2)/3 #Use f(n) to get f(n-1)
        return checkIt(x) #Call this function again with f(n-1). Update x.
print(checkIt(80))
        
        
        