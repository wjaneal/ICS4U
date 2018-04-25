# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:07:30 2018

@author: xuyin
"""

import random
import time
class searching():
    
def findFirstLarger(num, sortedList):

    def binarySearch(self): 
        startTime=time.time() 
        self.low=0
        self.high=999999
        self.guess=False
        while self.guess==False: 
            self.index=int((self.low+self.high)/2) 
            if self.n[self.index]>self.num:  
                self.highest=self.n[self.index] 
                self.high=self.index
            elif self.n[self.index]<self.num: 
                self.lowest=self.n[self.index]
                self.low=self.index
            if self.high-self.low==2 and self.n[self.high-1]>self.num:
                self.guess=True
            elif self.high-self.low==1:
                self.guess=True
        self.timeB.append((self.trial,time.time()-startTime))

    def Print(self):
        self.timeB=[]
        self.num=0.7 #This sets the number    
        self.n=[]
        for i in range(0,100000):
            self.n.append(random.random())
        self.n.sort()
        a.binarySearch()


    def draw_graph(self):
        x=[10,100,1000,10000,100000]#This is to set the N list
        draw.plot(x,self.timeB,color='red') #This is to draw the lines
        draw.title('Relationship between t and n') #This is to define the title
        draw.ylabel('t') #This is to name the axises
        draw.xlabel('n') #This is to name the axises
        draw.show()#This is to show the graph


    
a = searching()
a.Print()
a.draw_graph()


