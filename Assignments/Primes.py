#Generate Prime numbers using an algoithm:
#A spontaneously designed prime number generator
#Start with 2 as a prime
primes = [2]
maxj = 2
#Look for other primes starting at 3:
for i in range(3,40000):
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
print(primes)
