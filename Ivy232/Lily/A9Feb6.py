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
import time #import module recording time
import decimal 
import matplotlib.pyplot as plt #import module ploting graph
time_spent1 = [] #two lists including amount of time spent by two algorithms
time_spent2 = []
#start_time = time.time()
def function_(n): #define function in order to exert the first algorithm
    start_time = time.time()
    prime = [2] #the initial list of prime numbers
    for i in range (3, n): #loop meant to create list of prime numbers
        isPrime = True #make judgement
        for j in prime:
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            prime.append(i)
    #print(prime)  this is not necessary becaust it takes too much time
    acurate_time = decimal.Decimal(time.time() - start_time) #calculate the amount of time used by the algorithm
    #a.quantize(decimal.Decimal('0.00000'))
    time_spent1.append(acurate_time.quantize(decimal.Decimal('0.00000'))) #round the decimal
    #return time_spent1


#print("--- %s seconds ---" % (time.time() - start_time))
def function__(n): #define function to exert algorithm 2
    list_of_prime = [] #define an empty list
#n = 100
    start_time = time.time()
    number = [1] * (n+1) #create a list with  a lot of number "1"
    for i in range (2, len(number)): #This loop make use of sequence number of the list to express the prime numbers
        j = i 
        while j < len(number): #In this loop the "if" part is skipped when i is equal to j
            if j > i:
                number[j] = 0
            j += i #change all of the multiple sequences, which are not prime numbers, into "0"
    for i in range (2, len(number)):
        if number[i] != 0: #judgement
            list_of_prime.append(i) #fill the empty list with all of the prime numbers.
            #print(list_of_prime)
    acurate_time = decimal.Decimal(time.time() - start_time) #calculate the time spent
    #a.quantize(decimal.Decimal('0.00000'))
    time_spent2.append(acurate_time.quantize(decimal.Decimal('0.00000'))) #round the decimals
    #return time_spent2

repeat = [10000, 20000, 30000, 40000, 50000] #create a list with the tested number
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
plt.scatter(repeat,time_spent1) #plot out the graph!! with scatter points!!
plt.title('Relationship Between Times of Repetition and Time spent-Algorithm 1')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
plt.scatter(repeat,time_spent2) #can also use plt.plot() to chart a graph with points connected by lines
plt.title('Relationship Between Times of Repetition and Time spent-Algorithm 2')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
