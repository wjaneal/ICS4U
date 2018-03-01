# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
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
class search():#This is to set up a class 

    
    def Linear(self):#This is to define a function
        start =time.clock()#This is to start a timer
        for i in range (0,1000001):#This is to start a loop
            if i != self:#This is to judge the number one by one
                i+=1#This is to add one
            else:
                elapsed = (time.clock() - start)#This is to stop the timer
                break#This is to end the loop
        return elapsed#This is to return the time value
   
    def Random(self):#This is to define a function
        Guess = 0#This is to set a variable
        Max=1000000#This is to set the original range of guessing
        Min=0
        x= False#This is to set up the variable for judgement
        start =time.clock()#This is to start the timer
        while x == False:#This is to start a loop
            Guess = random.randint(Min,Max)#This is to get a random number
            if Guess   == self:#This is to stop the loop
                x = True
            if Guess > self:#This is to judge
                Max = Guess#This is to change the range
            if Guess < self:#This is to judge
                Min = Guess#This is to change the range
            
        elapsed = (time.clock() - start)#This is to stop the timer
        return elapsed#This is to return the value for the function
   
    def Binary(self):#This is to define a new function
        start = time.clock()#This is to start the timer
        Max=1000000#This is to set the original range
        Min=0
        x=False#This is to set a original judgement
        
        while x == False:#This is to start a loop
            Guess = int((Max+Min)/2)#This is to get the number right between the max and the min
            if Guess   == self:#This is to stop the loop
                x = True#This is to stop the judgement
            if Guess > self:#This is to judge
                Max = Guess#This is to change the range
            if Guess < self:#This is to judge
                Min = Guess#This is to change the range
        elapsed = (time.clock() - start)#This is to stop the timer
        return elapsed#This is to return the time value
    
    def start():#This is to define a new function to put all the functions all together
        print ('Linear search')#This is to divide the section
        Average=0#This is to set up a variable
        for i in range (0,5):#This is to start a loop
            N=random.randint(0,1000000)#This is to get a N to guess
            Time=search.Linear(N)#This is to operate the function
            L='Trial'+ str(i)+' '+str(Time)#This is to get the print content
            print(L)#This is to print
            Average=Average + Time#This is to get the value for average
        print('Average'+str(Average/5))#This is to get the value for average
        
        print ('Random search')#This is to divide the section
        
        for i in range (0,5):#This is to start a loop
            N=random.randint(0,1000000)#This is to get a N to guess
            Time=search.Random(N)#This is to operate the function
            R='Trial'+ str(i)+' '+str(Time)#This is to get the print content
            print(R)#This is to print
            Average=Average + Time#This is to get the value for average
        print('Average '+str(Average/5))#This is to get the value for average
        
        print ('Binary search')#This is to divide the section 
        for i in range (0,5):#This is to start a loop
            
            N=random.randint(0,1000000)#This is to get a N to guess
            Time=search.Binary(N)#This is to operate the function
            B='Trial'+ str(i)+' '+str(Time)#This is to get the print content
            print(B)#This is to print
            Average=Average + Time#This is to the value for average
        print('Average '+str(Average/5))#This is to get the value for average

search.start()#This is to start the managing function
