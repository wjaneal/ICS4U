'''
Assignment 10 - Benchmarking Sorting Algorithms


Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

(1) Create a class with functions for three sorting algorithms - bubble sort, selection sort and insertion sort. 
(2) Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[10000,20000,30000,40000,50000]
(3) Output of the program:
Bubble sort algorithm:
n	time
10000	2.23
20000	4.67
30000 	7.88
40000	11.34
50000	14.44

Insertion sort algorithm:
n	time
10000	2.23
20000	14.67
30000 	117.88
40000	211.34
50000	11214.44

Selection Sort algorithm:
n	time
10000	1.4
20000 	4.5
30000	10.4
40000	29.3
50000	100.2

(4) Have Python graph the results using pyplot / matplotlib
'''

import time #import module
import random
import matplotlib.pyplot as plt

time1 = [] #create empty lists for time spent
time2 = []
time3 = []
class sorting_algorithm(): #put the algorithms into a class
        
    def bubble_sort(self,list1):  #define bubble sort algorithm
        for i in range (0, len(list1)-1): #compare each two
            for j in range(0, len(list1)-1-i):
                if list1[j] > list1[j+1]:
                    list1[j], list1[j+1] = list1[j+1],list1[j]
                    j = j+1
        return list1
            #time_spent.append(self.acurate_time)
        
    def insertion_sort(self,list1):  #define insertion sort algorithm
        for i in range (1, len(list1)): #put the first number out of the list into the correct position of the list
            j = i - 1
            while list1[j]>= list1[j+1] and j >= 0:
                list1[j], list1[j+1] = list1[j+1],list1[j]
                j -= 1
        return list1
    
    def selection_sort(self,list1):  #define selection sort algorithm
        for i in range (0, len(list1)): #define a smallest one firstly and replace it with smaller number I may find later
            mi = i
            for j in range (i+1, len(list1)):
                if list1[j] <= list1[mi]:
                    mi =j
            if mi != i:
                list1[i], list1[mi] = list1[mi], list1[i]
        return list1
'''   
    def random(self,list1,range1):
        list1 = random.sample(range(5000), k = self.range1)
        return list1
'''            
s = sorting_algorithm() #use a simple name for the class
        
        #time_spent.append(self.acurate_time)
#s = sorting_algorithm(list1)

list1 = [1000,2000,3000,4000,5000] #Create a list consisting of designated number.

for i in range (0, len(list1)): #call the function and record the time spent
    lis = random.sample(range(list1[i]), k = list1[i])
    start_time = time.time()
    s.bubble_sort(lis)
    acurate_time1 = time.time() - start_time
    time1.append(acurate_time1)

for i in range (0, len(list1)): #call the function and record the time spent
    lis = random.sample(range(list1[i]), k = list1[i])
    start_time = time.time()
    s.insertion_sort(lis)
    acurate_time2 = time.time() - start_time
    time2.append(acurate_time2)
    
for i in range (0, len(list1)): #call the function and record the time spent
    lis = random.sample(range(list1[i]), k = list1[i])
    start_time = time.time()
    s.selection_sort(lis)
    acurate_time3 = time.time() - start_time
    time3.append(acurate_time3)




print ("Bubble sort algorithm:") #print the outcome
for i in range (5):
    #haha = decimal.Decimal(time1[i])
    #haha = round(time1[i],2)
    print(str(list1[i]), "      ", str(time1[i]))
print ("insertion sort algorithm:")
for i in range (5):
    #haha = decimal.Decimal(time1[i])
    #haha = round(time1[i],2)
    print(str(list1[i]), "      ", str(time2[i]))
print("selection sort algorithm:")
for i in range (5):
    #haha = decimal.Decimal(time1[i])
    #haha = round(time1[i],2)
    print(str(list1[i]), "      ", str(time3[i]))

plt.scatter(list1,time1) #plot out the graph!! with scatter points!!
plt.title('Relationship Between Times of Repetition and Time spent-Bubble Sort Algorithm ')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
plt.scatter(list1,time2) #can also use plt.plot() to chart a graph with points connected by lines
plt.title('Relationship Between Times of Repetition and Time spent-Insertion Sort Algorithm ')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()
plt.scatter(list1,time3)
plt.title('Relationship Between Times of Repetition and Time spent-Selection Sort Algorithm ')
plt.xlabel('Repetition')
plt.ylabel('Time Spent')
plt.show()


plt.plot(list1,time1,color='red') #This generates the graph for the Bubble sort algorithm.
plt.plot(list1,time2,color='blue') #This generates the graph for the Insertion sort algorithm.
plt.plot(list1,time3,color='green') #This generates the graph for the Selection sort algorithm.
plt.title('Benchmarking Sorting Algorithms') #This creates a title for the graph.
plt.ylabel('Time') #This creates the y label for the graph.
plt.xlabel('n Value') #This creates the x label for the graph.
plt.show()

#print ("Insertion sort algorithm:")
#print ("Selection Sort algorithm:")
    
'''
list4 = random.sample(range(5000), k = 3000)
list5 = random.sample(range(5000), k = 4000)
list6 = random.sample(range(5000), k = 5000)
start_time = time.time()
s.bubble_sort(list2)

s.bubble_sort(list3)
acurate_time3 = time.time() - start_time
start_time = time.time()
s.bubble_sort(list4)
acurate_time4 = time.time() - start_time
start_time = time.time()
s.bubble_sort(list5)
acurate_time5 = time.time() - start_time
start_time = time.time()
s.bubble_sort(list6)
acurate_time6 = time.time() - start_time
yy = [acurate_time2,acurate_time3,acurate_time4,acurate_time5,acurate_time6]
print (yy)
'''
'''
def function1():
    for index in range (0, len(list1))
        list_used = random.sample(range(5000), k = 5000)
        return list_used
    list_used = sorting_algorithm(list_used)
    list_used.bubble_sort()
    list_used.insertion_soracurate_time
'''
'''
def function1():
    lotteryNumbers = []
    for i in range(0,len(list1)):
        for index in range (0,list1[i]):
            lotteryNumbers.append(random.randrange(0,list1[i]))
        lotteryNumbers = sorting_algorithm(lotteryNumbers)
        lotteryNumbers.bubble_sort()
        lotteryNumbers.insertion_sort()
'''

'''
list__=[10000,20000,30000,40000,50000]
for i in range (0,len(list__)):
    list1= random.sample(range(50000), list__[i])
    outcome = sorting_algorithm(list1)
    outcome.bubble_sort()
    outcome.insertion_sort()

print (time_spent)
'''





 

























































