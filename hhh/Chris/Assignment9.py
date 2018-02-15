# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 01:59:38 2018
ChrisLi
(1) Create two functions: prime1(n) and prime2(n) that take a number that represents the set of integers from which to find prime numbers.  For example, n=1000 specifies that the function will look for primes up to 1000.
(2) Find out how to measure elapsed time in Python
(3) Write a program that determines the amount of time taken to find primes up to the following values: n=[10000,20000,30000,40000,50000]
(4) Output of the program:
First algorithm:
n	time
10000	2.23
20000	4.67
30000 	7.88
40000	11.34
50000	14.44
Second algorithm:
n	time
10000	2.23
20000	14.67
30000 	117.88
40000	211.34
50000	11214.44
(5) Bonus:  Have Python graph the results using pyplot / matplotlib

"""
import time#import module recording time
import matplotlib.pyplot as plt#import module ploting graph
n=[10000,20000,30000,40000,50000]

def primesone(x1):#the first fuction
   prime = [2] #the initial list of prime numbers
   for i in range (3, x1): #loop meant to create list of prime numbers
        for j in prime:
            if i % j == 0:
                break
        if j== prime[-1]:
                prime.append(i) 
   return()
def primestwo(x2):#the second function
    newprime=[]
    prime = [1]*(x2+1)
    for i in range(2,len(prime)):
        j=i
        while j<len(prime):
            if j>i:
                prime[j]=0
            j+=i
    for i in range(2,len(prime)):
        if prime[i]!=0:
            newprime.append(prime[i])
    return()
def countTime():#Measure the time that function primeOne() takes.
    k1=[]
    e1=[]
    print("First algorithm:")
    print("n    time")
    for i in range(0,len(n)):
        x1=n[i]
        k1.append(x1)
        start_time1 = time.time()#start the time
        primesone(x1)
        elapsed_time1 = time.time() - start_time1#end the timer
        e1.append(elapsed_time1)
        print(x1,elapsed_time1)
        
    k2=[]
    e2=[]
    print("Second algorithm:")
    print("n    time")
    for i in range(0,len(n)):
        x2=n[i]
        k2.append(x2)
        start_time2 = time.time()
        primestwo(x2)
        elapsed_time2 = time.time() - start_time2
        e2.append(elapsed_time2)
        print(x2,elapsed_time2)
        plt.plot(k1, e1, color='red')
        plt.plot(k2, e2, color='yellow')
        plt.xlabel('Repetition')
        plt.ylabel('Time Spent')
        plt.title('The speed of the calculating the primes')
        plt.show()
countTime() 