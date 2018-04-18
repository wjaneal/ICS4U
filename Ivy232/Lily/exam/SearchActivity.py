
import random  
import decimal 
import matplotlib.pyplot as plt
import time



n1 = []
n2 = []
n3 = []
n4 = []
n5 = []

for j in range (11):
    r = random.random()*1
    n1.append(r)
n1 = sorted(n1)



for j in range (101):
    r = random.random()*1
    n2.append(r)
n2 = sorted(n2)

for j in range (1001):
    r = random.random()*1
    n3.append(r)
n3 = sorted(n3)

for j in range (10001):
    r = random.random()*1
    n4.append(r)
n4 = sorted(n4)

for j in range (100001):
    r = random.random()*1
    n5.append(r)
n5 = sorted(n5)

def binarySearch(array): 
    lower = 0           
    upper = len(array)
    while lower < upper: 
        x = lower + (upper - lower) // 2 
        val = array[x]
        lval = array[x-1]
        if val > 0.7 and lval < 0.7:
            return val
        elif 0.7 > val: 
            lower = x
        elif 0.7 < val:
            upper = x
    

print(binarySearch(n1))
print(binarySearch(n2))
print(binarySearch(n3))
print(binarySearch(n4))
print(binarySearch(n5))

n6 = []
for j in range (1000001):
    r = random.random()*1
    n6.append(r)
n6 = sorted(n6)






def function(x):
    start_time = time.time()
    binarySearch(n6)
    time_spent = decimal.Decimal(time.time() - start_time)
    print(time_spent)
    plt.scatter(len(x),time_spent) 
    plt.title('Relationship Between Times of Repetition and Time spent-Binary Search Algorithm ')
    plt.xlabel('Repetition')
    plt.ylabel('Time Spent')
    plt.show()

function(n6)
#The time spent is very little, much less than I expected. I think binary search is a very efficient search algorithm. It only compares the values, but doesn't swap the numbers, and always decrease the range within which it is searching, which allows the search to go fast and efficient enough.
#This reminds me of the comparison among bubblesorting, insertion sorting and selection sorting. Among these sorting algorithm, the insertion sorting is the most efficient one.
#The reason is similar, but also a little different. For insertion algorithm, the range is expanding gradually, but the beginning point is very specific.
#The other two algorithm always repeat the process of go through the whole list time after time, which is very time-consuming.
#Choosing the most efficient algorithm is very important. We want to reach the goal as soon as possible. Therefore, how to take short cut in computer programming is a significant topic.

'''
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

'''            
s = sorting_algorithm() #use a simple name for the class
        
        #time_spent.append(self.acurate_time)
#s = sorting_algorithm(list1)
'''

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







































