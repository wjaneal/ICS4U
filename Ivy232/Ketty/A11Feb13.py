# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 02:21:14 2018

@author: sg
Assignment 11 - Linear, Random and Binary Searching - Benchmarking


Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

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

"""
n = []
t = []
t1 = []
t2 = []
import random
import time
#define a class 
class search():
    
    #create numbers into a list
    for i in range(0,100000):
        n.append(random.random())
        #make numbers in order
        n.sort()
    #define a function to use random algorithm to search
    def rand(self,n):
        self.low = 0
        self.high = len(n)
        self.num = random.randint(self.low,self.high-1) 
        while self.high - self.low != 1:
            self.num = random.randint(self.low,self.high-1) 
            if n[self.num] > 0.7: 
                self.high = self.num 
            if n[self.num] < 0.7:
                self.low = self.num
        if n[self.low] > 0.7:
            self.num = self.low
        if n[self.low] < 0.7 and n[self.high]>0.7:
            self.num = self.high
        return n[self.num]
    #define a function to use linear algorithm to search           
    def linear(self,n):
        m = []
        for self.i in n:
            if self.i > 0.7 and self.i <0.8:
                m.append(self.i)
                m.sort()
        return(m[0])
    #define a function to use binary algorithm to search
    def Binary(self,n):
        self.low = 0
        self.high = 1000
        while True:
            self.mid = (self.low + self.high) // 2
            if self.high - self.low == 2:
                if n[self.high-1] > 0.7:
                    return(n[self.high-1])
                else:
                    return(n[self.high])
                break
            else:
                if n[self.mid] > 0.7: 
                    self.high = self.mid
                if n[self.mid] < 0.7: 
                    self.low = self.mid
#class
s = search()


#run the function for 5 times and calculate the difference of time.
for i in range(5):
    a = time.time()
    s.rand(n)
    b = time.time()
    t.append(b-a)
#total time
total = 0
for u in t:
    total += u
#calculate the average time
av = round(total/5,2)

#output the table
print("Random search algorithm:")
print("trial#	time")
for r in range(0,len(t)):
    print(r + 1,"    ",t[r])
print("average:", av)


#run the function for 5 times and calculate the difference of time.
for i in range(5):
    a = time.time()
    s.linear(n)
    b = time.time()
    t1.append(b-a)
#total time
total1 = 0
for u in t1:
    total1 += u
#calculate the average time
av1 = round(total1/5,2)
#output the table
print("Linear search algorithm:")
print("trial#	time")
for r in range(0,len(t1)):
    print(r + 1,"    ",t1[r])
print("average:", av1)

#run the function for 5 times and calculate the difference of time.
for i in range(5):
    a = time.time()
    s.Binary(n)
    b = time.time()
    t2.append(b-a)
#total time
     
total2 = 0
for u in t2:
    total2 += u
#calculate the average time
av2 = round(total2/5,2)
#output the table
print("Binary search algorithm:")
print("trial#	time")
for r in range(0,len(t2)):
    print(r + 1,"    ",t2[r])
print("average:", av2)










        
