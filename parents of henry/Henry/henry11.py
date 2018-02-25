# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 13/Feb/2018
Program Title: Linear, Random and Binary Searching - Benchmarking

Purpose:

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

import random#This is to import modules
import time
class searching():#This is to set up a class 

    def randomSearching(self):#This is to define a function
        Guess = 0#initilize the guessing
        Max=1000000#This is to set the original range of guessing
        Min=0
        judge= False # This is to set the original judgement
        start =time.clock()#This is to start the timer
        while judge == False:#This is to start a loop
            Guess = random.randint(Min,Max)#This is to get a random numbern
            if Guess   == self:#This is to stop the loop
                judge = True
            if Guess > self:#This is to judge
                Max = Guess#This is to change the range
            if Guess < self:#This is to judge
                Min = Guess#This is to change the range
            
        elapsed = (time.clock() - start)#This is to stop the timer
        return elapsed#This is to return the value for the function
    
    def linearSearching(self):#This is to define a functionn
        start =time.clock()#This is to start a timer
        for i in range (0,1000001):#This is to start a loop
            if i != self:#This is to judge the number one by one
                i+=1#This is to add one
            else:
                elapsed = (time.clock() - start)#This is to stop the timer
                break#This is to end the loop
        return elapsed#This is to return the time value
    
    def binarySearching(self):#This is to define a new function
        start = time.clock()#This is to start the timer
        Max=1000000#This is to set the original range
        Min=0
        judge=False#This is to set a original judgement
        
        while judge == False:#This is to start a loop
            Guess = int((Max+Min)/2)#This is to get the number right between the max and the min
            if Guess   == self:#This is to stop the loop
                judge = True#This is to stop the judgement
            if Guess > self:#This is to judge
                Max = Guess#This is to change the range
            if Guess < self:#This is to judge
                Min = Guess#This is to change the range

        elapsed = (time.clock() - start)#This is to stop the timer
        return elapsed#This is to return the time value
    def start():#This is to define a new function to put all the functions all together
        print ('Random Searching')#This is to divide the section
        Average=0#This is to set up a variable, initilize the average
        for i in range (0,5):#This is to start a loop
            N=random.randint(0,1000000)#This is to get a N to guess
            Time1=searching.randomSearching(N)#This is to operate the function
            TextR='Trial'+ str(i)+' '+str(Time1)#This is to get the print content
            print(TextR)#This is to print
            Average=Average + Time1#This is to get the value for average
        print('Average '+str(Average/5))#This is to get the value for average
        print('')#This is to change line

        print ('Linear Searching')#This is to divide the section
        for i in range (0,5):#This is to start a loop
            N=random.randint(0,1000000)#This is to get a N to guess
            Time2=searching.linearSearching(N)#This is to operate the function
            TextL='Trial'+ str(i)+' '+str(Time2)#This is to get the print content
            print(TextL)#This is to print
            Average=Average + Time2#This is to get the value for average
        print('Average '+str(Average/5))#This is to get the value for average
        print('')#This is to change line

        print ('Binary Searching')#This is to divide the section 
        for i in range (0,5):#This is to start a loop
            N=random.randint(0,1000000)#This is to get a N to guess
            Time3=searching.binarySearching(N)#This is to operate the function
            TextB='Trial'+ str(i)+' '+str(Time3)#This is to get the print content
            print(TextB)#This is to print
            Average=Average + Time3#This is to the value for average
        print('Average '+str(Average/5))#This is to get the value for average

searching.start()#This is to start the managing function


        
        
        
        
        
        