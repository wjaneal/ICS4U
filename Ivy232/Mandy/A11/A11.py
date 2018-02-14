#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:06:24 2018

@author: Mandy

Assignment 11 - Linear, Random and Binary Searching - Benchmarking

(1) Create a class with functions for three search algorithms - random, linear and binary. 
(2) Write a program that determines the amount of time taken to search lists of 1000000 random numbers.
(3) Sample output of the program:
Random search algorithm:
trial#	time
1	2.23
2	2.67
3 	2.88
4       2.92
5	2.11
Average: 2.56


Linear Search Algorithm:
trial#	time
1	3.45
2	3.97
3 	3.21
4	1.23
5	2.23
Average ...


Binary Search algorithm:
trial#	time
1	0.56
2 	0.87
3	0.23
4	0.34
5	0.12
Average ....

"""
import random
import time


class Guess():
    n = []
    for i in range(0,1000):
        n.append(random.random()) # print a list with 1000 terms between 0-1
    #print(n)
    def Ran(n): 
        n.sort()
        lowest = 0
        highest = 1000
        while highest - lowest != 2:
            num = random.randint(lowest,highest) # guess the index of the list
            if n[num] > 0.7: #zoom in the limit
                highest = num
                #print("h",num)
            elif n[num] < 0.7: #zoom in the limit
                lowest = num
                #print("l",num)
            if highest - lowest == 1:
                #print(n[highest])
                break
        #print(n[highest])
           
             
            
    def Linear(n):
        a = []
        for i in n:
            if i > 0.7 and i <0.8:
                a.append(i)
                a.sort()
        #print(a[0])

    
    def Binary(n):
        
        mid = len(n)//2
        LH = []
        RH = []
        
        if n[mid] > 0.7:
            LH = n[:mid+1]
        
            if len(LH) == 2:
            
                print ("Result",LH[1])
                pass
            else:
                Binary(LH)  
           
        elif n[mid] < 0.7:
            RH = n[mid:]
        
            if len(RH) == 2:
            
                print("Result",RH[1])
                pass
            else:
                Binary(RH)
       

    #Ran(n)
    #Linear(n)        
    #Binary(n)  
    
####test the time################  
    
    t0 = time.time()
    Ran(n)
    t1 = time.time()
    total = t1-t0
    print("random:",total)
    t0 = time.time()
    Linear(n)
    t1 = time.time()
    total = t1-t0
    print("Liner:",total)
    t0 = time.time()
    Binary(n)
    t1 = time.time()
    total = t1-t0
    print("Binary:",total)
    