# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 25/Tan/2018
Program Title: Assignment9: Benchmarkig Algorithms

Purpose:
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

import math
import time#import time and math modelu
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True#This is to judge whether the number is n

def Primes1(n):
    primes = [2]
    for i in range(3, n + 1, 2):
        if isPrime(i):
            primes.append(i)
    return primes#This is to find the list for prime numbers

def runTime():
    for n in range (10000,50001,10000):
        start=time.clock()
        Primes1(n)    
        elapsed = (time.clock() - start)
        Result1=str(n)+' '+str(elapsed)
        print(Result1)#TFind the elapsed
        

def Primes2():
    for n in range (10000,50001,10000):
        p=[2,3,5,7]
        start=time.clock()
        for i in range (1,n,2):
            if i%3!=0:
                if i%5!=0:
                    if i%7!=0:
                        prime =0
                        a=int(p[-1])
                        for j in range (a,int(i+1),2):
                            if i%j ==0:
                                prime+=1
                                
                            if prime == 1:
                                p.append(i)
        elapsed = (time.clock() - start)
        Result2=str(n)+' '+str(elapsed)
        print(Result2)#Another program
        
def End():
        print('n time')
        runTime()
        print('')
        print('n time')
        Primes2()#This is to get everything ready
End()
                        
            
        
        
            
            

  
          