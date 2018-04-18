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
import matplotlib.pyplot as plt
# If you have a problem, please re-run the program!

class Guess():
    
    def Ran(n): 
        n.sort()
        lowest = 0
        highest = 10000
        while True:
            num = random.randint(lowest,highest) # guess the index of the list
            if n[num] > 0.7: #zoom in the limit
                highest = num + 1
                #print("index",num)
                if highest - lowest == 1:
                    ##print(n[highest])
                    break
                elif highest - lowest == 2:
                    ##print(n[lowest+1])
                    break
                
            elif n[num] < 0.7: #zoom in the limit
                lowest = num
                if highest+1 - lowest == 1:
                    ##print(n[highest])
                    break
                elif highest+1 - lowest == 2:
                    ##print(n[lowest+1])
                    break
        
           
             
            
    def Linear(n):
        a = []
        for i in n: # compare the num one by one 
            if i > 0.7 and i <0.8: # put the nums between 0.7 and 0.8 in a list
                a.append(i)
                a.sort() # pick out the smallest one by sorting
        ##print(a[0])

    #Here
    def Binary(n):
        lowest = 0
        highest = len(n)
       
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

#draw diagrams
    def drawing(n):
        plt.plot(a1times ,n,color='red') # Bubble sort algorithm
        plt.title('Binary') # title ofthe graph
        plt.ylabel('num of items') # y label for the graph
        plt.xlabel('Time') # x label for the graph
        plt.show()
    #Ran(n)
    #Linear(n)        
    #Binary(n)  
    

############################Part C2 abc######################
print("Binary Search:")
    #sum = 0
while True:
    n1 = []
    for i in range(0,10):
        n1.append(random.random()) # print a list with 10000 terms between 0-1
        
        t0 = time.time()
        Guess.Binary(n1)
        t1 = time.time()
        total1 = t1-t0
    print("      ",total1)
    n2 = []
    for i in range(0,100):
        n2.append(random.random()) # print a list with 10000 terms between 0-1
        
        t0 = time.time()
        Guess.Binary(n2)
        t1 = time.time()
        total2 = t1-t0
    print("      ",total2)            
        #sum += total
        
    n3 = []
    for i in range(0,1000):
        n3.append(random.random()) # print a list with 10000 terms between 0-1
        
        t0 = time.time()
        Guess.Binary(n3)
        t1 = time.time()
        total3 = t1-t0
    print("      ",total3)            
   
    n4 = []
    for i in range(0,10000):
        n4.append(random.random()) # print a list with 10000 terms between 0-1
        
        t0 = time.time()
        Guess.Binary(n4)
        t1 = time.time()
        total4 = t1-t0
    print("      ",total4)            
  
    n5 = []
    for i in range(0,100000):
        n5.append(random.random()) # print a list with 10000 terms between 0-1
        
        t0 = time.time()
        Guess.Binary(n5)
        t1 = time.time()
        total5 = t1-t0
    print("      ",total5)
    n6 = [] 
    a1times = [] 
    for i in range(0,1000000):
        n6.append(random.random()) # print a list with 10000 terms between 0-1
        
        t0 = time.time()
        Guess.Binary(n6)
        t1 = time.time()
        total6 = t1-t0
        a1times.append(total6)
    print("      ",total6)
    
   

    Guess.drawing(n6)
    break