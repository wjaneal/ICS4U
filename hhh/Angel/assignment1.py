#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:46:34 2018
@author: hailankan
Program Title: multiples of 3 or 19
Purpose: Print 1000 numbers, and find numbers that are divisible by 3 or 19.
"""

for i in range(0,1000):#loop through 1000 numbers
    print(i)#print them
    if i % 3 == 0:#decide whether they are divisivle by 3
        print(i,"is divisible by 3!")#print this message if they are
    if i % 19 == 0:#decide whether they are divisivle by 19
        print(i, "is a multiple of 19!")#print this message if they are