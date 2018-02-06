#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:20:18 2018
Prime Number
@author: Mandy
"""

import time
 
n = int(input("n="))
#1#############################
t0 = time.time()

#code_block

primes = [2]
for i in range (3,n):
    for j in primes:
        if i % j == 0:
            break
        if j == primes[-1]:
            primes.append(i)
            #print(primes)
print(primes)

#code_block

t1 = time.time()
total = t1-t0
print(total)

#2##################################
t0 = time.time()
primes1 = [2]
for i in range (3,n):
    for j in range(0,len(primes1)):
        if i % primes1[j] == 0:
            break
        if j == len(primes1)-1:
            primes1.append(i)      
print(primes1)

t1 = time.time()
total1 = t1-t0
print(total1)

#3###################################
t0 = time.time()
prime2 = [2]
for i in range (2,n):
    isPrime = True
    for  item in prime2:
        if i % item == 0:
             isPrime = False
    if isPrime == True:
            prime2.append(i)
print(prime2)
t1 = time.time()
total2 = t1-t0
print(total2)
#4####################################
t0 = time.time()
#n = int(input("n="))
number = [1] * (n+1)
for i in range (2, len(number)):
    j = i
    while j < len(number):
        if j > i:
            number[j] = 0
        j += i
for i in range (2, len(number)):
    if number[i] != 0:
        print(i)
t1 = time.time()
total3 = t1-t0
print(total3)
#####################################
print("n:",n)
print("#1:",total)
print("#2:",total1)
print("#3:",total2)
print("#4:",total3)