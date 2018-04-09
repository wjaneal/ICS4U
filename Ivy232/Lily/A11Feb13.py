'''
Assignment 11 - Linear, Random and Binary Searching - Benchmarking


Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

(1) Create a class with functions for three search algorithms - random, linear and binary. 
(2) Write a program that determines the amount of time taken to search lists of 1000000 random numbers.
(3) Sample output of the program:
Random search algorithm:
trial#	time
1	2.23
2	2.67
3 	2.88
4  2.92
5	2.11
Average: 2.56


Linear Search Algorithm:
trial#	time
1	3.45
2	3.97
3 	3.21
4	1.23
5	2.23
Average ...


Binary Search algorithm:
trial#	time
1	0.56
2 	0.87
3	0.23
4	0.34
5	0.12
Average ....


<<<<<<< HEAD
'''

import random  #This is to form random list
import decimal #This is to convert 'e' into part of the number
#import matplotlib.pyplot as plt
#wxh = 0
n = [] #This is to create a empty list for random number to fit in.
for i in range (100001): #This is a for loop to select certain amount of random numbers.
        r = random.random()*1
        n.append(r)
good = sorted(n) #Sort the list into sequence from the smallest to the biggest.

import time #import module

#import matplotlib.pyplot as plt

time1 = [] #create empty lists for time spent
time2 = []
time3 = []
class sorting_algorithm(): #put the algorithms into a class
        
    def randomSearch(self,n): #Randomsearch function when random number is chosen in a certain range.
        self.maximum = len(n) #This is the first and the biggest range.
        self.minimum = 0
        self.number = random.randint(self.minimum,self.maximum-1) #This is to choose a random number in the range given.
        while self.maximum - self.minimum != 1: #This is to form a loop only end when the start and the end
            if good[self.number] < 0.7:         #have the difference of "1"
                self.minimum = self.number #This is to condense the range into smaller ones according to the outcome we get.
                self.number = random.randint(self.minimum,self.maximum)
            if good[self.number] > 0.7: 
                self.maximum = self.number
                self.number = random.randint(self.minimum,self.maximum)
        if good[self.minimum] > 0.7: #This is to make a choice: which one should we choose between the two?
            self.number = self.minimum
        elif good[self.minimum] < 0.7 and good[self.maximum] > 0.7:
            self.number = self.maximum
        return good[self.number] 
    
        #time_spent.append(self.acurate_time)
        
    def linearSearch(self,n): #This is to look through the numbers from the smallest to the biggest
        for i in range (0, len(n)): #Whenever we get a number bigger than 0.7, we end the loop.
            if n[i]<=0.7:
                i += 1
            else:
                break
        return n[i]

    
    def binarySearch(self,array): #This is to devide the whole range into two again and again, till we find the
        self.lower = 0            #number we want
        self.upper = len(array)
        while self.lower < self.upper:   # use < instead of <=, creating a loop
            x = self.lower + (self.upper - self.lower) // 2 
            self.val = array[x]
            self.lval = array[x-1]
            if self.val > 0.7 and self.lval < 0.7:
                return self.val
            elif 0.7 > self.val: #This is to keep looking for the number just bigger than 0.7 through repeating the loop.
                self.lower = x
            elif 0.7 < self.val:
                self.upper = x

#print(binary_search(good))
'''   
    def random(self,list1,range1):
        list1 = random.sample(range(5000), k = self.range1)
        return list1
'''            
s = sorting_algorithm() #use a simple name for the class
        
        #time_spent.append(self.acurate_time)
#s = sorting_algorithm(list1)
'''
list1 = [1000,2000,3000,4000,5000] #Create a list consisting of designated number.
'''



for i in range (0, 5): #call the function and record the time spent
    #lis = random.sample(range(list1[i]), k = list1[i])
    start_time = time.time()
    s.randomSearch(good)
    acurate_time1 = decimal.Decimal(time.time() - start_time)
    time1.append(acurate_time1) #This is to put each of the record into a list for printing afterwards.

for i in range (0, 5): #call the function and record the time spent
    start_time = time.time()
    s.linearSearch(good)
    acurate_time2 = decimal.Decimal(time.time() - start_time)
    time2.append(acurate_time2)
    
for i in range (0, 5): #call the function and record the time spent
    start_time = time.time()
    s.binarySearch(good)
    acurate_time3 = decimal.Decimal(time.time() - start_time)
    time3.append(acurate_time3)




print ("Random search algorithm:") #print the outcome
for i in range (5):
    #haha = decimal.Decimal(time1[i])
    #haha = round(time1[i],2)
    print("      ", str(time1[i]))
print ("Linear search algorithm:")
for i in range (5):
    #haha = decimal.Decimal(time1[i])
    #haha = round(time1[i],2)
    print( "      ", str(time2[i]))
print("Binary search algorithm:")
for i in range (5):
    #haha = decimal.Decimal(time1[i])
    #haha = round(time1[i],2)
    print( "      ", str(time3[i]))
    
'''
plt.scatter(list1,time1) #plot out the graph!! with scatter points!!
plt.title('Relationship Between Times of Repetition and Time spent-Random Search Algorithm ')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
plt.scatter(list1,time2) #can also use plt.plot() to chart a graph with points connected by lines
plt.title('Relationship Between Times of Repetition and Time spent-Linear Search Algorithm ')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
plt.scatter(list1,time3)
plt.title('Relationship Between Times of Repetition and Time spent-Bianry Search Algorithm ')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
'''


































'''
=======
>>>>>>> 81e8aa76a02d1c71b464c2e0e4b35300b428e514
'''
