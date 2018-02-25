# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-02-13
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
class sort():#This is to create the class

    #This is to define a new function for select sorting
    def selectionSort(N):
        List=[]#This is to reset the list
        for i in range(0,N):#This is to start the loop
            List.append(random.randint(0,i+1))#This is to fill the list
            
        start=time.clock()#This is to start the timer
        for k in range(len(List)-1,0,-1):#This is to start the loop
            maxPosition=0#This is to reset the position
            for l in range(1,k+1):#This is to start a loop
                if List[l]>List[maxPosition]:#This is to judge whether the current value is larger than the current max value
                    maxPosition = l #This is to push it as the max value

        temp = List[k]#This is to switch value
        List[k] = List[maxPosition]
        List[maxPosition] = temp
        
        elapsed = (time.clock() - start)#This is to end the timer
        time1=str(N)+' '+str(elapsed)#This is to find the print context
        sort.t1.append(elapsed)#This is to fill the time list
        print(time1)

    #This is to define a new function for insert sorting
    def insertionSort(N):
        List=[]#This is to reset the list
        for i in range(0,N):#This is to start a list
            List.append(random.randint(0,i+1))#This is to fill the list
        
        start =time.clock()#This is to start the timer
        for index in range(1,len(List)):#This is to start a loop
            
            value = List[index]#This is to get the current value
            position = index#This is to get the position number
            
            while position>0 and List[position-1]>value:#This is to judge whether the current value should be there
                List[position]=List[position-1]#This is to move the value
                position = position-1#This is to  change the number of the value
                
            List[position]=value#This is to get the right one into position
        elapsed = (time.clock() - start)#This is to end the timer
        time2=str(N)+' '+str(elapsed)#This is to get the print content
        sort.t2.append(elapsed)#This is to fill the time list
        print(time2)

    #This is to define a new function for bubble sorting        
    def bubbleSort(N):
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
        Time3=str(N)+' '+str(elapsed)#This is to create the name
        sort.t3.append(elapsed)#This is to fill the time list
        print(Time3)#This is to use another algorithm
        
    #This could print and start the whole program.
    def start_sorting():
        sort.t1=[]#This is to make new lists
        sort.t2=[]
        sort.t3=[]
        #This is to start the loops
        print ('Select sort')
        for N in range (1000,5001,1000):
            sort.selectionSort(N)
        print ('Insert sort')
        for N in range (1000,5001,1000):
            sort.insertionSort(N)
        print ('Bubble sort')
        for N in range (1000,5001,1000):
            sort.bubbleSort(N)

    # This could draw the graph.
    def draw_graph():
        nlist=[1000,2000,3000,4000,5000]#This is to set the N list
        draw.plot(nlist,sort.t1,color='red') #This is to draw the lines
        draw.plot(nlist,sort.t2,color='green') 
        draw.plot(nlist,sort.t3,color='blue') 
        draw.title('The relationship between the two variables') #This is to define the title
        draw.ylabel('t') #This is to name the axises
        draw.xlabel('n') #This is to name the axises
        draw.show()#This is to show the graph
        
sort.start_sorting()
sort.draw_graph()

