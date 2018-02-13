# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:39:56 2018
Name:Jaune 
Date:Feb. 6
Title: Benchmarking
Purpose:Studying
@author: CTL
"""

import time
import pylab as pl

n=[10000,20000,30000,40000,50000]
p1time=[]
p2time=[]

#To define two functions that can help find prime number
#This method is to use the sieve method to find the primes.
def prime1(n):
    primes=[1]*(n+1)

    for i in range(2,len(primes)):
        j=i
        while j<len(primes):
            if j>i:
                primes[j]=0 #This line is to make the numbers that have already been searched 0.
            j+=i
    for i in range(2,len(primes)):
        if primes[i] !=0:
            return(i)

#This method is to use the normal method to find primes.            
def prime2(n):
    primes = [2]
    for i in range(3,n):
        isPrime = True
        for j in primes:
            if i%j == 0: #This line is to exam whether the numbers we find have other factors. 
                isPrime = False
                break
        if isPrime == True:
            primes.append(i) #This line is to add the numbers we find to the list primes
    return(primes)

#To make the figures form tables
print("First Algorithm")
print("n"," ","time")
for i in n:
    t0=time.time()
    prime1(i)
    t1=time.time()
    t=t1-t0 #This line is to calculate the total time that the program needs to execute
    p1time.append(t)
    print(i," ",t)
pl.plot(n, p1time) #This line is to show the figures in diagram.
pl.xlabel('Numbers') #This line is to add x-axis name.
pl.ylabel('Time') #This line is to add y-axis name.
pl.show() #This line is to show the diagram.

print("              ")
print("Second Algorithm")
print("n"," ","time")
for a in n:
    t0=time.time()
    prime2(a)
    t1=time.time()
    t=t1-t0 #This line is to calculate the total time that the program needs to execute
    p2time.append(t)
    print(a," ",t)
pl.plot(n, p2time) #This line is to show the figures in diagram.
pl.xlabel('Numbers') #This line is to add x-axis name.
pl.ylabel('Time') #This line is to add y-axis name.
pl.show() #This line is to show the diagram.
