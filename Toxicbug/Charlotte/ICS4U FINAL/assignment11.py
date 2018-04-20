#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Charlotte Chen
Date: Created on Tue Feb 13 13:00:00 2018
Title: Benchmarking search algorithms
Purpose:
(1) Create a class with functions for three search algorithms - random, linear and binary.
(2) Write a program that determines the amount of time taken to search lists of 1000000 random numbers.
(3) Print the results.
"""
import time 
import random
import matplotlib.pyplot as plt

class searching: #This creates a class for these three searching algorithms. 
    
    def randomSearch(self): #This defines a function for the random search algorithm.
        startTime=time.time() #This gets the start time.
        self.lIndex=0 #This sets the lowest index to 0.
        self.hIndex=self.n2-1 #This sets the highest index to 999999.
        self.guess=False #This initializes self.guess to False.
        while self.guess==False: #This loop continues if the number has not been guessed.
            self.index=random.randint(self.lIndex,self.hIndex) #This guesses a random index from the lowest index to the highest index.
            if self.n[self.index]>self.num: #If the number at the index is greater than the set number, the current index is set to the highest index. 
                self.highest=self.n[self.index] #This sets the current number to the highest number.
                self.hIndex=self.index
            elif self.n[self.index]<self.num: #If the number at the index is smaller than the set number, the current index is set to the lowest index.
                self.lowest=self.n[self.index] #This sets the current number to the lowest number.
                self.lIndex=self.index
            if self.hIndex-self.lIndex==2 and self.n[self.hIndex-1]>self.num: #If the difference between the highest and the lowest index is 2 and the number before the number at the highest index,            
                self.guess=True #the number required is found.
            elif self.hIndex-self.lIndex==1: #If the difference between the highest and the lowest index is 1,
                self.guess=True #the number required is found, which is just the number at the highest index.
        self.timeR.append((self.trial,time.time()-startTime)) 
        #This calculates the time for the random search algorithm and appends the trial number and time to a list.
        
    def linearSearch(self): #This defines a function for the linear search algorithm.
        startTime=time.time() #This gets the start time.
        for i in range(0,self.n2): #This loop iterates through the list.
            if self.n[i]<self.num and self.n[i+1]>self.num: #If the number at the current index is smaller than the set number and the next number is larger than the set number,
                break #the number required is found.
        self.timeL.append((self.trial,time.time()-startTime))
        #This calculates the time for the linear search algorithm and appends the trial number and time to a list.
    
    def binarySearch(self): #This defines a function for the binary search algorithm.
        startTime=time.time() #This gets the start time.
        self.lIndex=0 #This sets the lowest index to 0.
        self.hIndex=self.n2-1 #This sets the highest index to 999999.
        self.guess=False #This initializes self.guess to False.
        while self.guess==False: #This loop continues if the number has not been guessed.
            self.index=int((self.lIndex+self.hIndex)/2) #This sets the current index to the integer average of the lowest and highest index.
            if self.n[self.index]>self.num: #If the number at the index is greater than the set number, the current index is set to the highest index. 
                self.highest=self.n[self.index] #This sets the current number to the highest number.
                self.hIndex=self.index
            elif self.n[self.index]<self.num: #If the number at the index is smaller than the set number, the current index is set to the lowest index.
                self.lowest=self.n[self.index] #This sets the current number to the lowest number.
                self.lIndex=self.index
            if self.hIndex-self.lIndex==2 and self.n[self.hIndex-1]>self.num:
                self.guess=True
            elif self.hIndex-self.lIndex==1:
                self.guess=True  
        #self.timeB.append((self.trial,time.time()-startTime))
        self.timeB.append(time.time()-startTime)
        #This calculates the time for the binary search algorithm and appends the trial number and time to a list.
    
    def benchmarking(self):
        self.averageT = []
        self.timeR=[] #This creates an empty list to store trial numbers and time for the Random sort algorithm.
        self.timeL=[] #This creates an empty list to store trial numbers and time for the Linear sort algorithm.
        self.timeB=[] #This creates an empty list to store trial numbers and time for the Binary sort algorithm.
        self.num=0.7 #This sets the number    
        #for x in range(0,5): #This creates five trials.
        #self.trial=x+1 #This gets the trial number.
        self.n=[]
        self.n1 = [10,100,1000,10000,20000,100000]
        for x in range(0,len(self.n1)):
            self.n2 = self.n1[x]
            for i in range(0,self.n2): #This appends 1000000 numbers between 0 and 1 to the list.
                self.n.append(random.randint(0,1000000))
            self.n.sort() #This lets the numbers in the list go from smallest to largest.
            #a.randomSearch() #This uses random search algorithm to search for the number.
                #a.linearSearch() #This uses linear search algorithm to search for the number.
            a.binarySearch() #This uses binary search algorithm to search for the number.
        for i in self.timeB:
            print(i)
            
            
        '''
        totalTimeL=0
        totalTimeB=0
        print("Random search algorithm:")#This prints the trial number and corresponding execution time for the Random search algorithm.
        print("trial#"+"         "+"time")
        for i in range(0,len(self.timeR)):
            print(str(self.timeR[i][0])+"     "+str(self.timeR[i][1]))
        for i in range(0,len(self.timeR)):
            totalTimeR+=self.timeR[i][1]
            AverageR=totalTimeR/len(self.timeR)
        print("Average: ",AverageR,"\n")
        print("Linear search algorithm:")#This prints the trial number and corresponding execution time for the Linear search algorithm.
        print("trial#"+"         "+"time")
        for i in range(0,len(self.timeL)):
            print(str(self.timeL[i][0])+"     "+str(self.timeL[i][1]))
        for i in range(0,len(self.timeL)):
            totalTimeL+=self.timeL[i][1]
            AverageL=totalTimeL/len(self.timeL)
        print("Average: ",AverageL,"\n")
        print("Binary search algorithm:") #This prints the trial number and corresponding execution time for the Binary search algorithm.
        print("trial#"+"         "+"time")
        for i in range(0,len(self.timeB)):
            print(str(self.timeB[i][0])+"     "+str(self.timeB[i][1]))  
        for i in range(0,len(self.timeB)):
            totalTimeB+=self.timeB[i][1]
            AverageB=totalTimeB/len(self.timeB)
        print("Average: ",AverageB)
        '''
        plt.plot(self.n1,self.timeB,color='red') #This generates the graph for the Bubble sort algorithm.
        plt.title('Benchmarking Binary Searching') #This creates a title for the graph.
        plt.ylabel('Time') #This creates the y label for the graph.
        plt.xlabel('n Value') #This creates the x label for the graph.
        plt.show()
     
    

a=searching() #This creates an instance of the searching class.
a.benchmarking() #This starts the program.
