# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-02-20
Program Title: assignment11
Purpose: 
(1) Create a class with functions for three search algorithms - random, linear and binary. 
(2) Write a program that determines the amount of time taken to search lists of 1000000 random numbers.
(3) Sample output of the program:
Random search algorithm:
trial#	time
1	2.23
2	2.67
3 	2.88
4  2.92
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
class searching():

    #This defines the linear searching
    def Linear_searching(n):
        start =time.time()#This is to record the start time
        for i in range (0,1000001):#This is to start a loop
            if i != n:#This is to judge whether it is the correct number
                i+=1
            else:
                end = time.time()#This is to record the end time
                break
        return (end - start)#This return the time

    #This defines the binary searching
    def Binary_searching(self):
        start =time.clock()#This is to record the start time
        maximum = 1000000
        minimum = 0
        check = False
        while check == False:
            guess = int((maximum+minimum)/2)
            if guess == self:
                check == True
                break
            if guess > self:
                maximum = guess
            if guess <self:
                minimum = guess
        return (time.clock() - start)#This return the time
    
    #This defines the random searching
    def Random_searching(self):
        compareNum = random.randint(0,1000000)
        randomNumber = random.randint(0,1000000)
        startTime = time.clock()
        while compareNum != randomNumber:
            randomNumber = random.randint(0,1000000)
        return time.clock() - startTime

    #This is to define a new function to put all the functions all together
    def Print():
        
    #This is the calculation part
        Linear = []
        for i in range (0,5):#This could record the time for each trail in a list
            n=random.randint(0,1000000)
            Time=searching.Linear_searching(n)
            Linear.append(Time)
        sum1 = 0
        avg1 = 0
        for j in range (0,5):#This loop calculates the sum
            sum1 = sum1 + Linear[j]
        avg1 = sum1 / 5#This calculates the average
        
        Binary = []
        for i in range (0,5):#This could record the time for each trail in a list
            n=random.randint(0,1000000)
            Time=searching.Binary_searching(n)
            Binary.append(Time)
        sum2 = 0
        avg2 = 0
        for j in range (0,5):#This loop calculates the sum
            sum2 = sum2 + Binary[j]
        avg2 = sum2 / 5#This calculates the average

        Random = []
        for i in range (0,5):#This could record the time for each trail in a list
            n=random.randint(0,1000000)
            Time=searching.Random_searching(n)
            Random.append(Time)
        sum3 = 0
        avg3 = 0
        for j in range (0,5):#This loop calculates the sum
            sum3 = sum3 + Random[j]
        avg3 = sum3 / 5#This calculates the average
        
    #This is the print part
        print('Time for linear search: ')#This prints the result for linear search
        for k in range (0,5):
            print(str(k+1)+' '+str(Linear[k]))
        print('average '+str(avg1)+'\n')
        
        print('Time for Binary search: ')#This prints the result for binary search
        for k in range (0,5):
            print(str(k+1)+' '+str(Binary[k]))
        print('average '+str(avg2)+'\n')        

        print('Time for Random search: ')#This prints the result for random search
        for k in range (0,5):
            print(str(k+1)+' '+str(Random[k]))
        print('average '+str(avg3))       
    
searching.Print()#This is to start the managing function



