#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:31:34 2018
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
@author: haichunkan
"""
import random
import time   
def randomR(list1):# this is random search
    lowest=0#identify the max and min number's index
    highest=999999
    #index=int(random.random()*1000000)
    while  highest-lowest!=1:
        index=int(random.uniform(lowest+1,highest))
        if list1[index]<num:
            lowest=index
        if list1[index]>num:
            highest=index #make the range smaller until the difference is 1
    print(list1[highest],"is just greater than",num)        
def linear(list1):#linear search
    for i in range(0,len(list1)):
        if list1[i]>num:#start from beginning, until it find the number just greater 
            print(list1[i],"is just greater than",num)
            break
def binary(list1):#binary search
    lowest=0
    highest=999999
    while  highest-lowest!=1:
        index=(highest+lowest)//2#make it half
        if list1[index]<num:
            lowest=index
        if list1[index]>num:
            highest=index
    print(list1[highest],"is just greater than",num)   
def countTime():
    global ar,al,ab
    list1=[]
    for i in range(0,1000000):
        list1.append(int(random.random()*10000000)) 
    list1.sort()     
    starttime=time.time()#count the time for each
    randomR(list1)#random searching
    e=time.time()-starttime
    rt.append(e)
    ar+=e#add to toyal time
    starttime=time.time()#linear searching
    linear(list1)
    e=time.time()-starttime
    lt.append(e)
    al+=e
    starttime=time.time()#binary searching
    binary(list1)
    e=time.time()-starttime
    bt.append(e)
    ab+=e       


rt=[]#store the time for each searching funtion in
lt=[]
bt=[]
ar=0#a represents total time
al=0
ab=0         
for i in range(0,5):
    num=int(random.random()*10000000)# create a random number we need to search
    print("what is just greater than",num)
    countTime()#run the programme
print("Random search algorithm:")
print("trial#	time") # output of random search    
for i in range(0,5):
    print(i+1, rt[i])     
print("Average:", ar/5)
print("Linear search algorithm:")#output of linear search
print("trial#	time")      
for i in range(0,5):
    print(i+1, lt[i])     
print("Average:", al/5)
print("Binary search algorithm:")#output of binary search
print("trial#	time")      
for i in range(0,5):
    print(i+1, bt[i])     
print("Average:", ab/5)      