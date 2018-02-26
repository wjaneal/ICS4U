# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-02-11
Program Title: assignment10 (sorting)
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

class sort():
    
    #This is to define a new function for select sorting
    def select(self):
        List=[]
        for i in range(0,self):#This loop is used to create the list
            List.append(random.randint(0,i+1))
            
        start=time.clock()#This is to record the start time
        for j in range(len(List)-1,0,-1):#This is to start the loop to make a select sort
            maxValue=0
            for l in range(1,j+1):#This is to start a loop
                if List[l]>List[maxValue]:#This is to make a judgement
                    maxValue = l 
            tmp = List[j]#This could swap values
            List[j] = List[maxValue]
            List[maxValue] = tmp
        sort.t3.append(time.clock() - start)#This is to record the time of the project

    #This is to define a new function for insert sorting
    def insert(self):
        List=[]
        for i in range(0,self):#This loop is used to create the list
            List.append(random.randint(0,i+1))
            
        start=time.clock()#This is to record the start time
        for index in range(1,len(List)):#This is to start a loop to make an insert sort           
            value = List[index]#This is to get the current value
            p = index#This is to get the position number            
            while p>0 and List[p-1]>value:#This is to make a judgement
                List[p]=List[p-1]#This is to mchange the value
                p = p-1              
            List[p]=value#This is to move the right one into the position           
        sort.t2.append(time.clock() - start)#This is to record the time of the project

    #This is to define a new function for bubble sorting        
    def bubble(self):
        List=[]
        for i in range(0,self):#This loop is used to create the list
            List.append(random.randint(0,i+1))
        
        start=time.clock()#This is to record the start time
        for Num in range(len(List)-1,0,-1):#This is to start a loop to make a bubble sort
            for i in range(Num):#This is to move one number 
                if List[i]>List[i+1]:#This is to make a judgement
                    Temp = List[i]
                    List[i] = List[i+1]#This is to switch them
                    List[i+1] = Temp#
        sort.t1.append(time.clock() - start)#This is to record the time of the project
        
    #This could print and start the whole program.
    def start_sorting():
        sort.t1=[]#This is to make new lists
        sort.t2=[]
        sort.t3=[]
        #This is to start the loops
        for i in range (1000,5001,1000):
            sort.select(i)
            sort.bubble(i)
            sort.insert(i)
       
    #This could print out all the data.
    def print_out():
        print('The time for select sort')
        for i in range (5):
            print(str((i+1)*1000)+' '+str(sort.t3[i]))
        print()
        print('The time for insert sort')
        for i in range (5):
            print(str((i+1)*1000)+' '+str(sort.t2[i]))
        print()
        print('The time for bubble sort')
        for i in range (5):
            print(str((i+1)*1000)+' '+str(sort.t1[i]))
            
    # This could draw the graph.
    def draw_graph():
        x=[1000,2000,3000,4000,5000]#This is to set the N list
        draw.plot(x,sort.t1,color='red') #This is to draw the lines
        draw.plot(x,sort.t2,color='green') 
        draw.plot(x,sort.t3,color='blue') 
        draw.title('Relationship between t and n') #This is to define the title
        draw.ylabel('t') #This is to name the axises
        draw.xlabel('n') #This is to name the axises
        draw.show()#This is to show the graph
        
sort.start_sorting()
sort.print_out()
sort.draw_graph()




