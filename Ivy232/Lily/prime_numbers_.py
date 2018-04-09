#The sieve of Erastothenes
'''
Assignment 9 - Benchmarking Algorithms


Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

(1) Create two functions: prime1(n) and prime2(n) that take a number that represents the set of integers from which to find prime numbers.  For example, n=1000 specifies that the function will look for primes up to 1000.
(2) Find out how to measure elapsed time in Python
(3) Write a program that determines the amount of time taken to find primes up to the following values: n=[10000,20000,30000,40000,50000]
(4) Output of the program:
'''
'''
prime  =  1
num = 2
while prime <= 2000000:
    if prime % 2 = 0 or prime % 3 = or prime % 5 = 0
    
    for num in range (1, prime):
        if prime % num == 0:
            break
        else:
            print (prime)
        num = num + 1
    prime = prime + 1
'''
'''
primes = [2]
i = 2
for i in range (2, 1000):
    for j in range (0, len(primes)):
        if i % primes[j] == 0:
            break
        if j == len(primes)-1:
            primes.append(i)
print(primes)
'''
import time
import decimal
import matplotlib.pyplot as plt
time_spent1 = []
time_spent2 = []
#start_time = time.time()
def function_(n):
    start_time = time.time()
    prime = [2]
    for i in range (3, n):
        isPrime = True
        for j in prime:
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            prime.append(i)
    #print(prime)
    acurate_time = decimal.Decimal(time.time() - start_time)
    #a.quantize(decimal.Decimal('0.00000'))
    time_spent1.append(acurate_time.quantize(decimal.Decimal('0.00000')))
    #return time_spent1
'''
repeat = [10000, 20000, 30000, 40000, 50000]
for i in range (0, len(repeat)):
    function_(repeat[i])
print (time_spent1)
'''   


#print("--- %s seconds ---" % (time.time() - start_time))
def function__(n):
    list_of_prime = []
#n = 100
    start_time = time.time()
    number = [1] * (n+1)
    for i in range (2, len(number)):
        j = i
        while j < len(number):
            if j > i:
                number[j] = 0
            j += i
    for i in range (2, len(number)):
        if number[i] != 0:
            list_of_prime.append(i)
            #print(list_of_prime)
    acurate_time = decimal.Decimal(time.time() - start_time)
    #a.quantize(decimal.Decimal('0.00000'))
    time_spent2.append(acurate_time.quantize(decimal.Decimal('0.00000')))
    #return time_spent2

repeat = [10000, 20000, 30000, 40000, 50000]
for i in range (0, len(repeat)):
    function_(repeat[i])
    function__(repeat[i])
    
print (" time spent on algorithm 1: "+"\nrange          time spent")

for i in range (0, len(repeat)):
    print(str(repeat[i])+"          "+str(time_spent1[i]))
print (" time spent on algorithm 2: "+"\nrange          time spent")
for i in range (0, len(repeat)):
    print(str(repeat[i])+"          "+str(time_spent2[i]))
#print (time_spent1)
#print (time_spent2)
plt.scatter(repeat,time_spent1)
plt.title('Relationship Between Times of Repetition and Time spent-Algorithm 1')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
plt.scatter(repeat,time_spent2)
plt.title('Relationship Between Times of Repetition and Time spent-Algorithm 2')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
