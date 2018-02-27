import random
import time
import matplotlib.pyplot as plt
import numpy as np

class Sorting():   
    def Arrangement(self):
        self.x = []
        self.Time1 = []#This creates an empty list to store the time
        self.Time2 = []
        self.Time3 = []
        self.list1 = [] #This creates an empty list to store the numbers
        self.list2 = []
        self.Range=[100,200,300,400,500] #This defines the length of the list of random numbers.
        for self.i in self.Range: #This loop iterates through all the integer ranges
            for x in range(0,self.i): #This loop appends a certain number of random numbers to the list.
                self.list1.append(int(random.random()*(self.i+1)))

    def BubbleSort(self):      
        for self.NUmber in range(len(self.list1)-1,0,-1):       
            Start1 = time.time()#This starts recording time
            for i in range(self.NUmber):
                if self.list1[i] > self.list1[i+1]:
                    self.Last = self.list1[i]
                    self.list1[i] = self.list1[i+1]
                    self.list1[i+1] = self.Last 
                else:
                    self.list1 = self.list1
            End1 = time.time()#This ends recording time
            self.Time1.append(End1 - Start1)
        print("   n       BubbleSorting Time")
        for A,B in zip(self.Range,self.Time1):
            print(" ",A,"   ",B,"   ")
            
    def SelectionSort(self):
        for self.i in range(len(self.x)-1,0,-1):
            Start2 = time.time()
            Max=0
            for location in range(1,self.i+1):
                if self.x[location]>self.x[Max]:
                    Max = location
                    Temp = self.x[self.i]
                    self.x[self.i] = self.x[Max]
                    self.x[Max] = Temp
            End2 = time.time()
            self.Time2.append(End2-Start2)
        print("   n       SelectionSorting Time")
        for A,B in zip(self.Range,self.Time2):
            print(" ",A,"   ",B,"   ")
        
    def InsertionSort(self): #This defines a function for Insertion sort algorithm.
        for i in range(1,len(self.list1)): #This loop iterates through the list,starting from the second element.
            Start3 = time.time() #This gets the start time.
            curNum=self.list1[i] #This initializes curNum as the element in the list with index i.
            for j in range(i-1,-1,-1): #This loop iterates through the prior numbers of the element with index i.
                if self.list1[j]>curNum: #If the number is larger than the number with index i, its value is set to the next element in the list.
                    self.list1[j+1]=self.list1[j]
                else:
                    self.list1[j+1]=curNum #If the number is not larger than the number with index i, nothing happens.
                    break #This exits from the inner loop and proceeds to the next element.
            if self.list1[0]>curNum: #If the first element in the list is bigger than the current number tested, the value of the current number is set to the first element.
                self.list1[0]=curNum
            End3 = time.time()
        self.Time3.append(End3-Start3)
        print("   n       InsertionSorting Time")
        for A,B in zip(self.Range,self.Time3):
            print(" ",A,"   ",B,"   ")
              

S = Sorting()
S.Arrangement()
S.BubbleSort()
S.SelectionSort()
S.InsertionSort()
#S.Graphing()
