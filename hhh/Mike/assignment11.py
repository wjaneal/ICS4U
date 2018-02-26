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

import random#This is to import modules
import time
class searching():#This is to set up a class 

    def Linear_searching(self):#This is to define a function
        start =time.clock()#This is to start a timer
        for i in range (0,1000001):#This is to start a loop
            if i != self:#This is to judge the number one by one
                i+=1#This is to add one
            else:
                elapsed = (time.clock() - start)#This is to stop the timer
                break#This is to end the loop
        return elapsed#This is to return the time value

    def Binary_searching(self):#This is to define a new function
        start = time.clock()#This is to start the timer
        Max=1000000#This is to set the original range
        Min=0
        a=False#This is to set a original judgement
        while a == False:#This is to start a loop
            guess = int((Max+Min)/2)#This is to get the number right between the max and the min
            if guess   == self:#This is to stop the loop
                a = True#This is to stop the judgement
            if guess > self:#This is to judge
                Max = guess#This is to change the range
            if guess < self:#This is to judge
                Min = guess#This is to change the range
        elapsed = (time.clock() - start)#This is to stop the timer
        return elapsed#This is to return the time value

    def Random_searching(self):#This is to define a function
        guess = 0#This is to set a variable
        Max=1000000#This is to set the original range of guessing
        Min=0
        a= False#This is to set up the variable for judgement
        start =time.clock()#This is to start the timer
        while a == False:#This is to start a loop
            guess = random.randint(Min,Max)#This is to get a random number
            if guess   == self:#This is to stop the loop
                a = True
            if guess > self:#This is to judge
                Max = guess#This is to change the range
            if guess < self:#This is to judge
                Min = guess#This is to change the range
        elapsed = (time.clock() - start)#This is to stop the timer
        return elapsed#This is to return the value for the function

    def start():#This is to define a new function to put all the functions all together
        print ('Random Searching!')
        avg=0
        for i in range (0,5):#This is to start a loop
            N=random.randint(0,1000000)#This is to get a N to guess
            Time=searching.Random_searching(N)#This is to operate the function
            Random=str(i+1)+' '+str(Time)#This is to get the print content
            print(Random)#This is to print
            avg=avg + Time#This is to get the value for average
        print('Average '+str(avg/5))#This is to get the value for average
        print()#This is to change line
        print ('Linear Searching')#This is to divide the section
        for i in range (0,5):#This is to start a loop
            N=random.randint(0,1000000)#This is to get a N to guess
            Time=searching.Linear_searching(N)#This is to operate the function
            Linear=str(i+1)+' '+str(Time)#This is to get the print content
            print(Linear)#This is to print
            avg=avg + Time#This is to get the value for average
        print('Average '+str(avg/5))#This is to get the value for average
        print()#This is to change line
        print ('Binary Searching')#This is to divide the section 
        for i in range (0,5):#This is to start a loop            
            N=random.randint(0,1000000)#This is to get a N to guess
            Time=searching.Binary_searching(N)#This is to operate the function
            Binary=str(i+1)+' '+str(Time)#This is to get the print content
            print(Binary)#This is to print
            avg=avg + Time#This is to the value for average
        print('Average '+str(avg/5))#This is to get the value for average

searching.start()#This is to start the managing function




