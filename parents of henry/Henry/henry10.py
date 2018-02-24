# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 12/Feb/2018
Program Title: Benchmarking Sorting Algorithms

Purpose:

(1) Create a class with functions for three sorting algorithms - bubble sort, selection sort and insertion sort.
(2) Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[10000,20000,30000,40000,50000]
(3) Output of the program:
Bubble sort algorithm:
n	time
10000	2.23
20000	4.67
30000 	7.88
40000	11.34
50000	14.44

Insertion sort algorithm:
n	time
10000	2.23
20000	14.67
30000 	117.88
40000	211.34
50000	11214.44

Selection Sort algorithm:
n	time
10000	1.4
20000 	4.5
30000	10.4
40000	29.3
50000	100.2

(4) Have Python graph the results using pyplot / matplotlib
"""
import random
import time
import matplotlib.pyplot as draw
class sorting():#This is to create the class
    def bubbleSort(N):#This is to define a new function for bubble sorting
        List=[]#This is to make a new list
        for i in range(0,N):#This is to start a loop
            List.append(random.randint(0,i+1))#This is to fill the list
        
        start =time.clock()#This is to start the timer
        for Num in range(len(List)-1,0,-1):#This is to start another loop
            for i in range(Num):#This is to move one number 
                if List[i]>List[i+1]:#This is to judge
                    Temp = List[i]#This is to read the number on that position
                    List[i] = List[i+1]#This is to switch position
                    List[i+1] = Temp#This is to switch position
                elapsed = (time.clock() - start)#This is to end the timer
        Time1=str(N)+' '+str(elapsed)#This is to create the name
        sorting.t1.append(elapsed)#This is to fill the time list
        print(Time1)#This is to use another algorithm
    def insertionSort(N):#This is to define a new function
        List=[]#This is to reset the list
        for i in range(0,N):#This is to start a list
            List.append(random.randint(0,i+1))#This is to fill the list
        
        start =time.clock()#This is to start the timer
        for index in range(1,len(List)):#This is to start a loop
            
            currentvalue = List[index]#This is to get the current value
            position = index#This is to get the position number
            
            while position>0 and List[position-1]>currentvalue:#This is to judge whether the current value should be there
                List[position]=List[position-1]#This is to move the value
                position = position-1#This is to  change the number of the value
                
            List[position]=currentvalue#This is to get the right one into position
        elapsed = (time.clock() - start)#This is to end the timer
        Time2=str(N)+' '+str(elapsed)#This is to get the print content
        sorting.t2.append(elapsed)#This is to fill the time list
        print(Time2)
    def selectionSort(N):
        '''
        list=[]
        for i in range(0,N):
            list.append(random.randint(0,9))
        n=len(list)
        tli=[]
        start =time.clock()
        for i in range (0,n):            
            for j in range (0,n-len(tli)):                
                right = True
                for h in range (0,n-len(tli)):                    
                    if list[j]>list[h]:
                        right = False
                        
                if right == True:
                    tli.append(list[j])
                    list.remove(list[j])
                    break
        elapsed = (time.clock() - start)
        Time3 =str(n)+' '+str(elapsed)
        print(Time3)#This is to use another algorithm
        '''
        List=[]#This is to reset the list
        for i in range(0,N):#This is to start the loop
            List.append(random.randint(0,i+1))#This is to fill the list
        start=time.clock()#This is to start the timer
        for fillslot in range(len(List)-1,0,-1):#This is to start the loop
            
            positionOfMax=0#This is to reset the position
            for location in range(1,fillslot+1):#This is to start a loop
                if List[location]>List[positionOfMax]:#This is to judge whether the current value is larger than the current max value
                    positionOfMax = location#This is to push it as the max value

        temp = List[fillslot]#This is to switch value
        List[fillslot] = List[positionOfMax]
        List[positionOfMax] = temp
        
        elapsed = (time.clock() - start)#This is to end the timer
        Time3=str(N)+' '+str(elapsed)#This is to find the print context
        sorting.t3.append(elapsed)#This is to fill the time list
        print(Time3)
    def Start():
        sorting.t1=[]#This is to make new lists
        sorting.t2=[]
        sorting.t3=[]
        #This is to start the loops
        print ('bubble sort')
        for N in range (1000,5001,1000):

            sorting.bubbleSort(N)
        print ('insertion sort')
        for N in range (1000,5001,1000):
            sorting.insertionSort(N)
        print ('select sort')
        for N in range (1000,5001,1000):
            sorting.selectionSort(N)
        Nlist=[1000,2000,3000,4000,5000]#This is to set the N list


        draw.plot(Nlist,sorting.t1,color='red') #This is to draw the lines
        draw.plot(Nlist,sorting.t2,color='green') 
        draw.plot(Nlist,sorting.t3,color='blue') 
        draw.title('Sorting') #This is to define the title
        draw.ylabel('t') #This is to name the axises
        draw.xlabel('n')
        draw.show()#This is to show the graph
            
        
            
            
            
                
    
sorting.Start()


