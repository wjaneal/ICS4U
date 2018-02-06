#The sieve of Erastothenes
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
'''
prime = [2]
for i in range (3, 1000):
    isPrime = True
    for j in prime:
        if i % j == 0:
            isPrime = False
    if isPrime == True:
        prime.append(i)
print(prime)
'''
n = 100
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
        
    
        
