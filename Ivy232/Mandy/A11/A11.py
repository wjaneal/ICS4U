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
        while True:
            num = random.randint(lowest,highest) # guess the index of the list
            if n[num] > 0.7: #zoom in the limit
                highest = num + 1
                #print("index",num)
                if highest - lowest == 1:
                    print(n[highest])
                    break
                elif highest - lowest == 2:
                    print(n[lowest+1])
                    break
                
            elif n[num] < 0.7: #zoom in the limit
                lowest = num
                if highest+1 - lowest == 1:
                    print(n[highest])
                    break
                elif highest+1 - lowest == 2:
                    print(n[lowest+1])
                    break
        
           
             
            
    def Linear(n):
        a = []
        for i in n:
            if i > 0.7 and i <0.8:
                a.append(i)
                a.sort()
        print(a[0])

    
    def Binary(n):
        lowest = 0
        highest = 1000
       
        while True:
            mid = (lowest + highest) // 2
            if highest - lowest == 2:
                if n[highest-1] > 0.7:
                    print(n[highest-1])
                else:
                    print(n[highest])
                break
    
            else:
                if n[mid] > 0.7: #zoom in the limit
                    highest = mid
                    
                elif n[mid] < 0.7: #zoom in the limit
                    lowest = mid

    #Ran(n)
    #Linear(n)        
    #Binary(n)  
    
####test the time################  
    print("Random Search:")
    t0 = time.time()
    Ran(n)
    t1 = time.time()
    total = t1-t0
    print("Time1:",total)
    print("")
    
    print("Liner Search:")
    t0 = time.time()
    Linear(n)
    t1 = time.time()
    total = t1-t0
    print("Time2:",total)
    print("")
    
    print("Binary Search:")
    t0 = time.time()
    Binary(n)
    t1 = time.time()
    total = t1-t0
    print("Time3:",total)
##################################
#print("Unblock #63,66,72,75(Random),87(linear),97(Binary) to see the number you are looking for! ")    