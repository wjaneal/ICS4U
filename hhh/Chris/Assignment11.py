# -*- coding: utf-8 -*-
"""
Assignment 11 - Linear, Random and Binary Searching - Benchmarking
Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names
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
    def linearsearch(n):
        a = []
        print('Linear Search Algorithm:')
        print('trial	time')
        for i in n: # compare the num one by one 
            if i > 0.7 and i <0.8: # put the nums between 0.7 and 0.8 in a list
                a.append(i)
                a.sort() # pick out the smallest one by sorting
        ##print(a[0])
    def binarysearch(n):
        lowest = 0
        print('Binary Search Algorithm:')
        print('trial	time')
        highest = 10000
       
        while True:
            mid = (lowest + highest - 1) // 2  # 2 keep zooming in the limit
            if highest - lowest == 2: # 3 when finally you have three nums left 
                if n[highest-1] > 0.7:
                    ##print(n[highest-1])
                    pass
                    
                else:
                    ##print(n[highest])
                    pass
                    
                break
            elif highest - lowest == 1: # 3 when finally younhave two nums left
                if n[highest-1] > 0.7:
                    ##print(n[highest-1])
                    pass
                else:
                    ##print(n[highest])
                    pass
                break
    
            else: # 1 compare the num in the middle with 0.7
                if n[mid] > 0.7: #zoom in the limit
                    highest = mid
                    
                elif n[mid] < 0.7: #zoom in the limit
                    lowest = mid

Search=searching
Search.randomsearch()
Search.linearsearch()
Search.binarysearch()