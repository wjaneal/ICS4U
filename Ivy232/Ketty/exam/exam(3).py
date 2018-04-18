m = [10,100,1000,10000]
#,10000,100000
n1 = []
t = []
import random
import time
#define a class 
class search():
    #define a function to use binary algorithm to search
    def Binary(self,n,high):
        self.low = 0
        self.high = high
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
for i in m:
    for j in range(0,i):
        n1.append(random.random())
    n1.sort()
    #print(n1)
    a = time.time()
    s.Binary(n1,i-1)
    b = time.time()
    t.append(b-a)
    
print(t)
