# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 01:56:10 2018

@author: 11256
"""
import time
n = [10000,20000,30000,40000,50000]
a1times = []
a2times = []

start = time.time()
def primes1(n):
    for p in n:
        primes= [1] * (p + 1)
        for i in range(2,len(primes)):
            j = i
            while j<len(primes):
                if j >i:
                    primes[j] = 0
                    j+=i
            for i in range(2,len(primes)):
                if primes[i] != 0:
                    return(i)
primes1(n)
end = time.time()
elapsed = end - start
a1times.append(elapsed)
print (a1times)

start2 = time.time()
def primes2(n):
    for p in n:
        primes = [2]
#Look for other primes starting at 3:
        for i in range(3,p):
    #Assume each new number is prime:
            isPrime = True
    #print("Testing " +str(i))
            for j in primes:
        #If it divides evenly into a lower number, it is not prime:
                if i % j  == 0:
            #print(str(j)+" divides "+str(i)+"..."+str(i)+" is not prime")
                    isPrime = False
    #If it is prime, append it to the list of primes
        if isPrime == True:
	#print(str(i)+" is a prime number - add to the list")
            primes.append(i)
#Print out the primes:
primes2(n)
end2 = time.time()
elapsed2 = end2 - start2
a2times.append(elapsed2)
print (a2times)