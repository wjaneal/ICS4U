# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 01:39:05 2018

@author: 11256
"""
'''
Purpose:
(1) Create a class with functions for three search algorithms - random, linear and binary.
(2) Write a program that determines the amount of time taken to search lists of 10000 random numbers.
(3) Print the results.
'''
import time
import random
list = []
#create a list to fill the numbers
for x in range (0, 10000):
    list.append(random.randint(0, 100))
    #create 1000 numbers
a = int(input("Enter number to search: "))
    #ask user to input a number
t1 = []
t2 = []
t3 = []
#create 3 lists to hold the time
class search_algorithms():
    def random(n):
        #definde the random algorithm
        maxNumber = 10000
        minNumber = 0
        
        while maxNumber - minNumber != 1: 
            index = random.randint(0,n-1) 
            if list[index] > n and index < maxNumber: 
                maxNumber = index
            if list[index] < n and index > minNumber: 
                minNumber = index                           
        return(list[maxNumber])
    

    
    def linear(n):
        #define linear algorithm
        found = False

        for i in range(len(list)):
            if(list[i] == a):
                found = True
                print("%d found at %dth position"%(a,i))
                break
 
            if(found == False):
                print("%d is not in list"%a)
        
    def binary(alist, item):
        #define binary algorithm
        first = 0
        last = len(alist)-1
        found = False
        while first<=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
	            found = True
            else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
        return found
    def time():
        start = time.time()
        s.random
        end = time. time()
        t1.append(start-end)   
        #use the list to calculate the time
        
        start = time.time()
        s.linear
        end = time. time()
        t1.append(start-end)
        
        start = time.time()
        s.binary(list, a)
        end = time. time()
        t1.append(start-end)
    
s = search_algorithms()
s.time()
        
        

