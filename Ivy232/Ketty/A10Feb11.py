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
leng = [1000,2000,3000,4000,5000]
num = []
t = []
ta = []
tb = []
t1 = []
t2 = []
t3 = []
class sorting():
    def bubble_sort(self,seq):
        changed = True
        while changed:
            changed = False
            for self.i in range(len(seq) - 1):
                if seq[self.i] > seq[self.i+1]:
                    seq[self.i], seq[self.i+1] = seq[self.i+1], seq[self.i]
                    changed = True
        return None
    def insertion_sort(self,l):
        for self.i in range(1, len(l)):
            self.j = self.i-1 
            self.key = l[self.i]
            while (l[self.j] > self.key) and (self.j >= 0):
                l[self.j+1] = l[self.j]
                self.j -= 1
            l[self.j+1] = self.key
    def selection_sort(self,lst):
        for self.i, self.e in enumerate(lst):
            self.mn = min(range(self.i,len(lst)), key=lst.__getitem__)
            lst[self.i], lst[self.mn] = lst[self.mn], self.e
        return lst
    def random(self,u):
        self.a = int(random.random()*leng[u])
        num.append(self.a)
        return num
s = sorting()
for i in range(0,len(leng)):
    for j in range(0,leng[i]):
        s.random(i)
    t.append(time.time())
    s.bubble_sort(num)
t.append(time.time())
#print(t)

for m in range(0,len(t)-1):
    b = t[m+1]-t[m]
    t1.append(b)
print(t1)


for i in range(0,len(leng)):
    for j in range(0,leng[i]):
        s.random(i)
    ta.append(time.time())
    s.insertion_sort(num)
ta.append(time.time())
for m in range(0,len(ta)-1):
    b = ta[m+1]-ta[m]
    t2.append(b)
print(t2)






 

























































