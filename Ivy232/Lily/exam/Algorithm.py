

import time #import module
import random


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
        for i in range (1, len(list1)): #This is to increase the range each time we complete a round of comparison, until the whole list is included in the comparison.
            j = i - 1 #This is to let j start from the outmost number of each range.
            while list1[j]>= list1[j+1] and j >= 0: #When the outmost number is bigger than the number we want to insert,
                list1[j], list1[j+1] = list1[j+1],list1[j] #We exchange their positions
                j -= 1 #This is to endow j with the number to the left, and the next left, and so on...
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

s = sorting_algorithm() #use a simple name for the class
        
        #time_spent.append(self.acurate_time)
#s = sorting_algorithm(list1)


list1 = [] #This is to create a empty list for random number to fit in.
for i in range (10001): #This is a for loop to select certain amount of random numbers.
        r = random.random()*1
        list1.append(r)

list2 = list1
list2.sort()
list2[34], list2[99] = list2[99], list2[34]



start_time = time.time()
s.bubble_sort(list1)
acurate_time1 = time.time() - start_time


start_time = time.time()
s.insertion_sort(list1)
acurate_time2 = time.time() - start_time

start_time = time.time()
s.selection_sort(list1)
acurate_time3 = time.time() - start_time  

x = [acurate_time1,acurate_time2, acurate_time3]
print(x)
print("Insertion algorithm is the most efficient")





start_time = time.time()
s.bubble_sort(list2)
acurate_time1 = time.time() - start_time


start_time = time.time()
s.insertion_sort(list2)
acurate_time2 = time.time() - start_time

start_time = time.time()
s.selection_sort(list2)
acurate_time3 = time.time() - start_time  

x = [acurate_time1,acurate_time2, acurate_time3]
print(x) 
#[12.807415008544922, 0.0017731189727783203, 4.646894216537476]
























































