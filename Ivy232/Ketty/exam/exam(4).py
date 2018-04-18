
n1 = []
import random
import time
#define a class 
class search():
    #define a function to use binary algorithm to search
    def Binary(self,n):
        self.low = 0
        self.high = 999999
        while True:
            self.mid = (self.low + self.high) // 2
            if self.high - self.low == 2:
                if n[self.high-1] > 0.7:
                    return(n[self.high-1])
                else:
                    return(n[self.high])
                break
            else:
                if n[self.mid] > 0.7: 
                    self.high = self.mid
                if n[self.mid] < 0.7: 
                    self.low = self.mid
#class
s = search()
#get 1000000 numbers
for j in range(0,1000000):
    n1.append(random.random())
#algorithm
print(n1)
'''
a = time.time()
s.Binary(n1)
b = time.time()
t = b-a
print(t)
'''
