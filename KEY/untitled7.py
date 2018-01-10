#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:48:55 2018
@author: haichunkan
ICS4UAssignment1: Find the multiples of 3 and 19 from 1 to 1000.

"""

for i in range (1,1001):#It runs 1000 times.
    if i % 3 == 0:#Judge if the number is divisible by 3.
        print(i,"is divisible by 3!")#Print the number if it is.
    if i % 19 == 0:#udge if the number is divisible by 3.
        print(i,"is a multiple of 19")#Print the number if it is.