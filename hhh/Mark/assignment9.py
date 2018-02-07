# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-02-06
Program Title: Benchmarking Algorithms
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
import time
n=[10000,20000,30000,40000,50000]
a1times = []
a2times = []
for x in range (0,5):
    print(n[x])
    start1 = time.time()
    prime1 = [1]*(n[x]+1)
    for i in range(2,len(prime1)):
        j = i
        while j < len(prime1):
            if j>i:
                prime1[j]=0
            j+=i
    for i in range(2,len(prime1)):
        if prime1[i] != 0:
            print(i)
    end1 = time.time()
    elapsed1 = end1 - start1
    a1times.append(elapsed1)
    
    start2 = time.time()
    prime2 = [2]
    maxj = 2
    for i in range(3,n[x]+1):
        isPrime = True
        for j in prime2:
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            prime2.append(i)
    print(prime2)
    end2= time.time()
    elapsed2 = end2 - start2
    a2times.append(elapsed2)
    
print()
    
print('First Algorithm time(n=[10000,20000,30000,40000,50000]):')
for k in range (0,5):
    print(str(n[k])+'   '+str(a1times[k]))
    
print()

print('Second Algorithm time(n=[10000,20000,30000,40000,50000]):')
for k in range (0,5):
    print(str(n[k])+'   '+str(a2times[k]))
    
    

    
    














        
        
        
        
        
