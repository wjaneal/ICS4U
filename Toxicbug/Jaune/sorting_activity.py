# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:49:01 2018
Name: Jaune
Date: April 18 2018
Purpose: Final test 
Title: Sorting
@author: CTL
"""

import random
import time

randomnumber=[]
bubbletime=[]
insertiontime=[]
selectiontime=[]

#This line is to create a function class
class sorting():
    
    def bubble_sort(self,seq): #This line is to define the bubble sort.
        changed = True
        while changed: #This line is to create a loop to keep caomparing the numbers in the list.
            changed = False
            for self.i in range(len(seq) - 1):
                if seq[self.i] > seq[self.i+1]: #This line is to compare the two numbers.
                    seq[self.i], seq[self.i+1] = seq[self.i+1], seq[self.i] #This line is to swap the two numbers.
                    changed = True
        return None
    
    def insertion_sort(self,l): #This line is to define the insertion sort.
        for self.i in range(1, len(l)):
            self.j = self.i-1 
            self.key = l[self.i] #This line is to make a vacany.
            while (l[self.j] > self.key) and (self.j >= 0): #This line is to create a loop to keep comparing the numbers in the list.
                l[self.j+1] = l[self.j]
                self.j -= 1
            l[self.j+1] = self.key #This is to insert the number in that position.
   
    def selection_sort(self,lst): #This line is to define the selection sort.
        for self.i, self.e in enumerate(lst): #The enumerate command allows people to loop over something and have an automatic counter.
            self.mn = min(range(self.i,len(lst)), key=lst.__getitem__)
            lst[self.i], lst[self.mn] = lst[self.mn], self.e
        return lst

    def benchmarking(self):
        self.n = [10000]
        self.a = int(random.randient(10000)) #This line is to make the range of the random numbers equeals to the numbers in the n list.
        randomnumber.append(self.a) #This line is to put the random numbers in the list.
        return randomnumber
    
        print("Bubble sort time:") #This line is to make a table of the two figures.
        print("length"," ", "time")
        for i in range(0,len(self.n)):
            for j in range(0,self.n[i]):
                s.randomnum(i)
        self.t0=time.time() #This line is to calculate the starting time.
        s.bubble_sort(randomnumber)
        self.t1=time.time() #This line is to calculate the ending time.
        self.bubbletime.append(self.t1-self.t0) #This line is to calculate the total time to run the program.
        for i in range(0,len(self.n)):
            print(self.n[i]," ",self.bubbletime[i]) #This line is to put the numbers in the table.
            
        print("insertion sort time:")#This line is to make a table of the two figures.
        print("length"," ", "time")
        for i in range(0,len(self.n)):
            for j in range(0,self.n[i]):
                s.randomnum(i)
        self.t0=time.time() #This line is to calculate the starting time.
        s.insertion_sort(randomnumber)
        self.t1=time.time() #This line is to calculate the ending time.
        self.insertiontime.append(self.t1-self.t0) #This line is to calculate the total time to run the program.
        for i in range(0,len(self.n)):
            print(self.n[i]," ",self.insertiontime[i])#This line is to put the numbers in the table.
            
        print("selection sort time:")#This line is to make a table of the two figures.
        print("length"," ", "time")
        for i in range(0,len(self.n)):
            for j in range(0,self.n[i]):
                s.randomnum(i)
        self.t0=time.time() #This line is to calculate the starting time.
        s.selection_sort(randomnumber)
        self.t1=time.time() #This line is to calculate the ending time.
        self.selectiontime.append(self.t1-self.t0) #This line is to calculate the total time to run the program.
        for i in range(0,len(self.n)):
            print(self.n[i]," ",self.selectiontime[i]) #This line is to put the numbers in the table.

#This two lines are to run the program
s=sorting()
s.benchmarking()

