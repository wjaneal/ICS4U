# -*- coding: utf-8 -*-
'''
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
'''
#import mutiple module
import random
import time


class Search():  # This defines a class for three searching method

    # This method won't work because of the Recursion Limitation of python.

    '''
    def randomSearch(self,Num):
        if int(Num) == random.randint(0,1000000):
            return Num
        else:
            return self.randomSearch(Num)
    
    '''

    def randomSearch(self):  # This defines a function for random Searching
        compareNum = random.randint(0, 1000000)
        randomNumber = random.randint(0, 1000000)
        startTime = time.clock()
        while compareNum != randomNumber:
            randomNumber = random.randint(0, 1000000)

        return time.clock() - startTime

    def linearSearch(self):  # This defines a function for linear Searching
        startTime = time.clock()
        for i in range(1, 1000001):
            if i != self:
                i += 1  # Search the next number
            else:
                stop = (time.clock() - startTime)  # It means the timer is stop
                break  # It means that the loop has stopped
        return stop  # It means to return the timer value

    def binarySearch(self):
        low = 0
        height = 1000000
        startTime = time.clock()
        while low < height:
            mid = int((low + height) / 2)
            if mid < self:
                low = mid

            elif mid > self:
                height = mid

            else:
                stop = (time.clock() - startTime)

                return stop

    def start(): # This defines a function for start
        # For random searching algorithm:
        print ('Random search algorithm:')
        print ('Trial #    ' + 'Time ')
        Average1 = 0
        for i in range(1, 6):
            Num = random.randint(0, 1000000)
            Time1 = Search.randomSearch(Num)
            Output =  str(i) + ' ' + str(Time1)
            print(Output)
            Average1 = Average1 + Time1
        print('Average1: ' + str(Average1 / 5))
        print(' ')

        Average2 = 0
        # For linear search algorithm:
        print('Linear search algorithm:')
        print('Trial #    ' + 'Time ')
        for i in range(1, 6):
            Num = random.randint(0, 1000000)
            Time2 = Search.linearSearch(Num)
            Output = str(i) + ' ' + str(Time2)
            print(Output)
            Average2 = Average2 + Time2
        print('Average2: ' + str(Average2 / 5))
        print(' ')

        Average3 = 0
        # For binary searching algorithm:
        print('Binary search algorithm:')
        print('Trial #    ' + 'Time ')
        for i in range(1, 6):
            Num = random.randint(0, 1000000)
            Time3 = Search.binarySearch(Num)
            Output = str(i) + ' ' + str(Time3)
            print(Output)
            Average3 = Average3 + Time3
        print('Average3: ' + str(Average3 / 5))
        print(' ')

Search.start() # It means to start the function

'''

       
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
'''
