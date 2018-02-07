'''
Assignment 9 - Benchmarking Algorithms
Ketty, 2018/2/6, Benchmarking Algorithms
purpose: to check how long the program should run

Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

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

'''
#import module
import time
import matplotlib.pyplot as plt
#set lists and some basic variable
t = []
ti = []
tim = []
tal = []
tal1 = []
tal2 = []
prime = []
primes = [2]
num = [10000,20000,30000,40000,50000]
i = 2
#define the first prime function
def prime1(n):
#print(primes[0])
#n = int(input("How many numbers do you want to check?"))
    for i in range(2,n):
        for j in range (0, len(primes)):
            if i % primes[j] == 0:
                break
            if j == len(primes) - 1:
                primes.append(i)
    #print(primes)
#set the intial time and put it into the list t
t.append(time.time()) 
#store each time when finishing the function prime1 once
for p in range(0,len(num)):
    prime1(num[p])
    t.append(time.time())
#making a table of prime1
print("First algorithm:")
print("number","      ","time")
for q in range(0,len(num)):
    total = t[q + 1]-t[q]
    tal.append(total)
    print(num[q],"       ",total)
#making a plot of prime1
plt.figure()

plt.plot(num,tal)  
plt.xlabel('numeber')  
plt.ylabel('time')  

plt.show()
#define the second prime function
def prime2(m):
     primes = [2]
     for i in range(2,m):
         isPrime = True
         for item in primes:
             if i % item == 0:
                 isPrime = False
         if isPrime == True:
             primes.append(i)
#set the intial time and put it into the list ti
ti.append(time.time()) 
#store each time when finishing the function prime1 once
for o in range(0,len(num)):
    prime2(num[o])
    ti.append(time.time())
#making a table of prime2
print("Second algorithm:")
print("number","      ","time")
for u in range(0,len(num)):
    total1 = ti[u + 1]-ti[u]
    tal1.append(total1)
    print(num[u],"       ",total1)

#making a plot of prime2
plt.figure()

plt.plot(num,tal1)  
plt.xlabel('numeber')  
plt.ylabel('time')  

plt.show()

def prime3(n):
    prime3 = [1] * (n + 1)
    for i in range (2,len(prime3)):
        j = i
        while j < len(prime3):
            if j > i:
                prime3[j] = 0
            j += i
    for i in range (2,len(prime3)):
        if prime3[i] != 0:
            prime.append(i)
            
#set the intial time and put it into the list ti
tim.append(time.time()) 
#store each time when finishing the function prime1 once
for w in range(0,len(num)):
    prime3(num[w])
    tim.append(time.time())
#making a table of prime2
print("Third algorithm:")
print("number","      ","time")
for e in range(0,len(num)):
    total2 = tim[e + 1]-tim[e]
    tal2.append(total2)
    print(num[e],"       ",total2)

#making a plot of prime2
plt.figure()

plt.plot(num,tal2)  
plt.xlabel('numeber')  
plt.ylabel('time')  

plt.show()





 

























































