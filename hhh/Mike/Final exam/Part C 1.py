# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:39:49 2018

@author: xuyingjie
"""

import random
import time

class sort():
    
    #This is to define a new function for select sorting
    def select(self):
        List=[]
        for i in range(0,10000):#This loop is used to create the list
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
        selectTime = time.clock() - start#This is to record the time of the project
        print(selectTime)

    #This is to define a new function for insert sorting
    def insert(self):
        List=[]
        for i in range(0,10000):#This loop is used to create the list
            List.append(random.randint(0,i+1))
            
        start=time.clock()#This is to record the start time
        for index in range(1,len(List)):#This is to start a loop to make an insert sort           
            value = List[index]#This is to get the current value
            p = index#This is to get the position number            
            while p>0 and List[p-1]>value:#This is to make a judgement
                List[p]=List[p-1]#This is to mchange the value
                p = p-1              
            List[p]=value#This is to move the right one into the position           
        insertTime = time.clock() - start#This is to record the time of the project
        print(insertTime)

    #This is to define a new function for bubble sorting        
    def bubble(self):
        List=[]
        for i in range(0,10000):#This loop is used to create the list
            List.append(random.randint(0,i+1))
        
        start=time.clock()#This is to record the start time
        for Num in range(len(List)-1,0,-1):#This is to start a loop to make a bubble sort
            for i in range(Num):#This is to move one number 
                if List[i]>List[i+1]:#This is to make a judgement
                    Temp = List[i]
                    List[i] = List[i+1]#This is to switch them
                    List[i+1] = Temp#
        bubbleTime = time.clock() - start#This is to record the time of the project
        print(bubbleTime)
        
a = sort()
a.select()
a.bubble()
a.insert()


class change_list_sort():
    
    #This is to define a new function for select sorting
    def select(self):
        List=[]
        for i in range(0,9998):#This loop is used to create the list
            List.append(i)
        List.append(9999)
        List.append(9998)
            
        start=time.clock()#This is to record the start time
        for j in range(len(List)-1,0,-1):#This is to start the loop to make a select sort
            maxValue=0
            for l in range(1,j+1):#This is to start a loop
                if List[l]>List[maxValue]:#This is to make a judgement
                    maxValue = l 
            tmp = List[j]#This could swap values
            List[j] = List[maxValue]
            List[maxValue] = tmp
        selectTime = time.clock() - start#This is to record the time of the project
        print(selectTime)

    #This is to define a new function for insert sorting
    def insert(self):
        List=[]
        for i in range(0,9998):#This loop is used to create the list
            List.append(i)
        List.append(9999)
        List.append(9998)
            
        start=time.clock()#This is to record the start time
        for index in range(1,len(List)):#This is to start a loop to make an insert sort           
            value = List[index]#This is to get the current value
            p = index#This is to get the position number            
            while p>0 and List[p-1]>value:#This is to make a judgement
                List[p]=List[p-1]#This is to mchange the value
                p = p-1              
            List[p]=value#This is to move the right one into the position           
        insertTime = time.clock() - start#This is to record the time of the project
        print(insertTime)

    #This is to define a new function for bubble sorting        
    def bubble(self):
        List=[]
        for i in range(0,9998):#This loop is used to create the list
            List.append(i)
        List.append(9999)
        List.append(9998)
        
        start=time.clock()#This is to record the start time
        for Num in range(len(List)-1,0,-1):#This is to start a loop to make a bubble sort
            for i in range(Num):#This is to move one number 
                if List[i]>List[i+1]:#This is to make a judgement
                    Temp = List[i]
                    List[i] = List[i+1]#This is to switch them
                    List[i+1] = Temp#
        bubbleTime = time.clock() - start#This is to record the time of the project
        print(bubbleTime)
    
b = change_list_sort()
b.select()
b.bubble()
b.insert()
       
        