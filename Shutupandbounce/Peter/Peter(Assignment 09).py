#Assignment 9 - Benchmarking Algorithms
#Name:Peter Zeng
#Date: January 25, 2018
#Program Title: Benchmarking Algorithms
#Program Function:(1) Create two functions: prime1(n) and prime2(n) that take a number
#that represents the set of integers from which to find prime numbers.
#For example, n=1000 specifies that the function will look for primes up to 1000.
#(2) Find out how to measure elapsed time in Python
#(3) Write a program that determines the amount of time taken to find primes up to the following values: 
#n=[10000,20000,30000,40000,50000]
#(4) Output of the program:
import time
import matplotlib.pyplot as plt

def prime1(n):
    primes = [2]*(n+1)
    for i in range(3,100000):
        isPrime = False
        print("Testing number of "+str(i))
    for j in primes:
        if i % j == 0:
            isPrime = False
        if isPrime == True:
            primes.append(i)
            print (primes)

def prime2(n):
    P = []
    f = []
    for i in range(n+10):
        if i > 2 and i%2 == 0:
            f.append(1)
        else:
            f.append(0)
    i = 3
    while i*i <= n:
        if f[i] == 0:
            j = i*i
            while j <= n:
                f[j] = 1
                j += i+i
        i += 2
 
    P.append(2)
    for x in range(3,n+1,2):
        if f[x] == 0:
            P.append(x)
 
    return P
 
n = 100000
P = prime2(n)
print (P)
        
 
#Time，Data
t = [10000,20000,30000,40000,50000]
prime1Times = []
prime2Times = []

for p in t:
    start = time.time()
    prime1(p)
    period = time.time() - start
    prime1Times.append(period)

for e in t:
    start = time.time()
    prime2(e)
    period = time.time() - start
    prime2Times.append(period)  

print("The First Algorism:")
print("n    ", "Time")
for r in range(0,5):
    print(t[r], prime1Times[r])
plt.plot(t, prime1Times)
plt.ylabel('Running Time For Algorithm 1')
plt.xlabel('Numbers')
plt.show()
print("The Second Algorism:")
print("n    ", "Time")

for a in range(0,5):
    print(t[a], prime2Times[a])
plt.plot(t, prime2Times)
plt.ylabel('Running Time For Algorithm 2')
plt.xlabel('Numbers')
plt.show()