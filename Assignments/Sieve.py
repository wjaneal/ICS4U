#Sieve of Erastothenes

n = 1000000
primes = [1]*(n+1)

for i in range(2,len(primes)):
    j = i
    while j < len(primes):
        if j>i:
            primes[j]=0
        j+=i
for i in range(2,len(primes)):
    if primes[i] != 0:
        print(i)

