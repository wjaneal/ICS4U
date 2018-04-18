import time
import random


class sorting:
    def bubble_sort(self):#definethe bubble sorting
        start=time.time()#To record the start time
        self.changed = True
        while self.changed:
            self.changed = False
            for i in range(len(self.a) - 1):
                if self.a[i] > self.a[i+1]:
                    self.a[i], self.a[i+1] = self.a[i+1], self.a[i]
                    self.changed = True
        self.time1.append((self.x,time.time()-start))#calculate to the elapsed time
        

    def insertion_sort(self):#difind the insertion sorting
        start=time.time()
        for i in range(1, len(self.a)):
            j = i-1
            key = self.a[i]
            while (self.a[j] > key) and (j >= 0):
                self.a[j+1] = self.a[j]
                j -= 1
                self.a[j+1] = key
        self.time2.append((self.x,time.time()-start))
  
    def selection_sort(self):#define the selection sorting time
        start=time.time()
        for i, e in enumerate(self.a):
            mn = min(range(i,len(self.a)), key=self.a.__getitem__)
            self.a[i], self.a[mn] = self.a[mn], e

        self.time3.append((self.x,time.time()-start))
    

    
    def excute(self):#Mix them together to excute it
        self.time1 = []
        self.time2 = []
        self.time3 = []
        self.n = [10000]#It shows the range of the numbers
        for i in self.n:
            self.a=[] #creat a new list to include the numbers
            for j in range(0,i): 
                self.a.append(int(random.random()*(i+1)))
            self.x=i
            H.bubble_sort() #excute the function
            H.insertion_sort() 
            H.selection_sort()
        print("Bubble sort algorithm:")#print the label
        print("n"+"         "+"time")
        for i in range(0,len(self.time1)):
            print(str(self.time1[i][0])+"     "+str(self.time1[i][1]))
        print("Insertion sort algorithm:")
        print("n"+"         "+"time")
        for i in range(0,len(self.time2)):
            print(str(self.time2[i][0])+"     "+str(self.time2[i][1]))
        print("Selection sort algorithm:") 
        print("n"+"         "+"time")
        for i in range(0,len(self.time3)):
            print(str(self.time3[i][0])+"     "+str(self.time3[i][1]))


H = sorting()
H.excute()






































