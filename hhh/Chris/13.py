# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 01:38:11 2018
Chris
Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names
(1) Create a class with functions for three search algorithms - random, linear and binary. 
(2) Write a program that determines the amount of time taken to search lists of 1000000 random numbers.
(3) Sample output of the program:
"""
import time
import random  #This is to form random list
num=[]
for i in range(1000000):
    num.append(random.randrange(10000000))
num.sort()

class searching:
    def randomsearch():
        total=0#set total time to 0
        print('Random Search Algorithm:')
        print('trial	time')
        for i in range(5):#loop for 5 times
            index=random.randrange(0,999999)
            aim= num[index]
            start_time = time.time()
            search=random.randrange(1000000)#select a number randomly
            end=len(num)-1#initial value
            start=0#initial value
            while num[search]!= aim:
                search=random.randrange(start,end)#select a number randomly in a smaller range
                if num[search]< aim:
                    start=search# let start value equal to search value which is smaller than index
                if num[search]>aim:
                    end=search# let start value equal to search value which is larger than index
            #print (index)            
            elapsed_time = time.time() - start_time#calculate time
            total+=elapsed_time# calculate total time
            print(i+1, elapsed_time)        
        print('average:',total/5)#calculate average
        
    def linearsearch():
        total=0
        print('Linear Search Algorithm:')
        print('trial	time')
        for i in range(5):#loop for 5 times
            index=random.randrange(0,999999)
            aim= num[index]
            start_time = time.time()
            search=0
            while num[search]!= aim:
                search+=1# if not aim, check the next element
            #print (index)            
            elapsed_time = time.time() - start_time#calculate time
            total+=elapsed_time
            print(i+1, elapsed_time)
        print('average:',total/5)
        
    def binarysearch():
        total=0
        print('Binary Search Algorithm:')
        print('trial	time')
        for i in range(5):#loop for 5 times
            index=random.randrange(0,999999)
            aim= num[index]
            start_time = time.time()
            end=len(num)-1
            start=0
            search=len(num)//2# midpoint of the list
            while num[search]!= aim:
                search=(start+end)//2# midpoint of the smaller range
                if num[search]< aim:
                    start=search# omit the range in which the numbers are too small
                elif num[search]>aim:
                    end=search#omit the range in which the numbers are too large
            #print (index)            
            elapsed_time = time.time() - start_time#calculate time
            total+=elapsed_time
            print(i+1, elapsed_time) 
        print('average:',total/5)   

Search=searching
Search.randomsearch()
Search.linearsearch()
Search.binarysearch()


