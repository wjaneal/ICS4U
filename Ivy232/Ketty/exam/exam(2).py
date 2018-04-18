#algorithms
import random
import time
a = []
#to get a list of numbers
for i in range(0,10000):
    a.append(int(random.random()*10000))
a.sort()
b = a[100]
a.pop(100)
c = a[100]
a.pop(100)
a.insert(100,b)
a.insert(100,c)


a1 = []
a2 = []
a3 = []
t = []

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


p = sorting()
#run the class and function, and input time each time in list t
a1 = a
t1 = time.time()
p.bubble_sort(a1)
#the time of endding
t2 = time.time()
t3 = t2 - t1
t.append(t3)

a2 = a
t4 = time.time()
p.insertion_sort(a2)
#the time of endding
t5 = time.time()
t6 = t5 - t4
t.append(t6)

a3 = a
t7 = time.time()
p.selection_sort(a3)
#the time of endding
t8 = time.time()
t9 = t8 - t7
t.append(t9)

t.sort()
if t3 == t[0]:
    print("bubble sort takes the least time.")
    print(t3)

if t6 == t[0]:
    print("intersection sort takes the least time.")
    print(t6)

if t9 == t[0]:
    print("selection sort takes the least time.")
    print(t9)




    
