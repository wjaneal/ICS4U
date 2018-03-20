# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:10:49 2018
Name:Aurora Hou
Propose:
(1) Create a class with functions for three sorting algorithms - bubble sort, selection sort and insertion sort.
(2) Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[10000,20000,30000,40000,50000]
(3) Output of the program
"""
#import time#Import time module
#import random
from random import shuffle#Import random module
import matplotlib.pyplot as plt
import numpy as np
import time

class Sorting():
    
    def Arrangement(self):
        self.alist= [] #This creates an empty list to store the numbers.
        self.Range=[10,20,30,40,50] #This defines the length of the list of random numbers.
        for self.i in self.Range: #This loop iterates through all the integer ranges
            for x in range(0,self.i): #This loop appends a certain number of random numbers to the list.
                self.alist.append(int(random.random()*(self.i+1)))
        print("Here's the orginal list:\n",self.alist)    
        
    def BubbleSort(self):
        Start1 = time.time()
        for self.NUmber in range(len(self.alist)-1,0,-1):
            for self.x in range(self.NUmber):
                if self.alist[self.x] > self.alist[self.x+1]:
                    self.Last = self.alist[self.x]
                    self.alist[self.x] = self.alist[self.x+1]
                    self.alist[self.x+1] = self.Last 
        print("The current list using bubble sort is: ",self.alist," .")        
        End1 = time.time()
        self.time1.append(self.alist,End1-Start1)
        
    def SelectionSort(self):
       Start2 = time.time()
       for self.i in range(len(self.x)-1,0,-1):
            positionOfMax=0
            for location in range(1,self.i+1):
                if self.x[location]>self.x[positionOfMax]:
                    positionOfMax = location
            temp = self.x[self.i]
            self.x[self.i] = self.x[positionOfMax]
            self.x[positionOfMax] = temp
       print("Here's the SelectionSorted list:\n",self.x," .") 
       End2 = time.time()
       self.time2.append(self.alist,End2-Start2)
        
    def InsertionSort(self): #This defines a function for Insertion sort algorithm.
        startTime=time.time() #This gets the start time.
        for i in range(1,len(self.list1)): #This loop iterates through the list,starting from the second element.
            curNum=self.list1[i] #This initializes curNum as the element in the list with index i.
            for j in range(i-1,-1,-1): #This loop iterates through the prior numbers of the element with index i.
                if self.list1[j]>curNum: #If the number is larger than the number with index i, its value is set to the next element in the list.
                    self.list1[j+1]=self.list1[j]
                else:
                    self.list1[j+1]=curNum #If the number is not larger than the number with index i, nothing happens.
                    break #This exits from the inner loop and proceeds to the next element.
            if self.list1[0]>curNum: #If the first element in the list is bigger than the current number tested, the value of the current number is set to the first element.
                self.list1[0]=curNum
        self.timeI.append((self.n,time.time()-startTime)) #This appends the n value and the execution time to a list.
        End3 = time.time()
        self.time3.append(self.alist,End-Start3)
        
    def Graphing(self):
        plt.style.use('fivethirtyeight')
        plt.title('Sorting Algorithms')
        plt.xlabel('Numbers')
        plt.ylabel('Time(Seconds)')
        plt.plot(self.alist,self.time1,color='red') #This generates the graph for the Bubble sort algorithm.
#       plt.plot(x,self.time2,color='blue') #This generates the graph for the Insertion sort algorithm.
#        plt.plot(x,self.time3,color='green') #This generates the graph for the Selection sort algorithm.
        plt.show()

S = Sorting()
S.BubbleSort()
#S.InsertionSort()
#S.SectionSort()
S.Arrangement()
S.Graphing()