#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:48:22 2018

@author: xuwentong
"""

def f(n):
    if n > 1:
        return n * f(n-1)
    else:
        return 1
    
print(f(10))
print(f(100))
print(f(1000))
#print(f(10000))