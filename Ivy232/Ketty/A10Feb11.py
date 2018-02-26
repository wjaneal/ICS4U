'''
Assignment 10 - Benchmarking Sorting Algorithms
Ketty
2018/2/6
Sorting Algorithms
purpose: Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[10000,20000,30000,40000,50000]


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
import random
import time
import matplotlib.pyplot as plt

#set lists to prepare
leng = [100,200,300,400,500]
num = []
t = []
ta = []
tb = []
t1 = []
t2 = []
t3 = []
#create a class
class sorting():
    #define function of bubble sorting
    def bubble_sort(self,seq):
        changed = True
        while changed:
            changed = False
            for self.i in range(len(seq) - 1):
                if seq[self.i] > seq[self.i+1]:
                    seq[self.i], seq[self.i+1] = seq[self.i+1], seq[self.i]
                    changed = True
        return seq
    #define function of insertion sorting
    def insertion_sort(self,l):
        for self.i in range(1, len(l)):
            self.j = self.i-1 
            self.key = l[self.i]
            while (l[self.j] > self.key) and (self.j >= 0):
                l[self.j+1] = l[self.j]
                self.j -= 1
            l[self.j+1] = self.key
    #define function of selection sorting
    def selection_sort(self,lst):
        for self.i, self.e in enumerate(lst):
            self.mn = min(range(self.i,len(lst)), key=lst.__getitem__)
            lst[self.i], lst[self.mn] = lst[self.mn], self.e
        return lst
    #define function of make a list of random numbers
    def random(self,u):
        self.a = int(random.random()*leng[u])
        num.append(self.a)
        return u


#class
s = sorting()
#run the class and function, and input time each time in list t
for i in range(0,len(leng)):
    for j in range(0,leng[i]):
        s.random(i)
    t.append(time.time())
    s.bubble_sort(num)
    num = []
#the time of endding
t.append(time.time())
#the difference of time and put them into a list
for m in range(0,len(t)-1):
    b = t[m+1]-t[m]
    t1.append(b)
#print the table of time and number
print("Bubble sort algorithm:")
print("n     time")
for i in range(0,len(leng)):
    print(leng[i],"    ",t1[i])

#making a plot of prime1
plt.figure()

plt.plot(leng,t1)  
plt.xlabel('numeber')  
plt.ylabel('time')  

plt.show()




#run the class and function, and input time each time in list t
for i in range(0,len(leng)):
    for j in range(0,leng[i]):
        s.random(i)
    ta.append(time.time())
    s.insertion_sort(num)
    num = []
#the time of endding
ta.append(time.time())
#the difference of time and put them into a list
for m in range(0,len(ta)-1):
    b = ta[m+1]-ta[m]
    t2.append(b)
#print the table of time and number
print("Insertion sort algorithm:")
print("n     time")
for i in range(0,len(leng)):
    print(leng[i],"    ", t2[i])
#making a plot of prime1
plt.figure()

plt.plot(leng,t2)  
plt.xlabel('numeber')  
plt.ylabel('time')  

plt.show()




#run the class and function, and input time each time in list t
for i in range(0,len(leng)):
    for j in range(0,leng[i]):
        s.random(i)
    tb.append(time.time())
    s.selection_sort(num)
    num = []
#the time of endding
tb.append(time.time())
#the difference of time and put them into a list
for m in range(0,len(tb)-1):
    b = tb[m+1]-tb[m]
    t3.append(b)
#print the table of time and number
print("Selection sort algorithm:")
print("n     time")
for i in range(0,len(leng)):
    print(i + 1,"    ",t3[i])
#making a plot of prime1
plt.figure()

plt.plot(leng,t2)  
plt.xlabel('numeber')  
plt.ylabel('time')  

plt.show()



 

























































