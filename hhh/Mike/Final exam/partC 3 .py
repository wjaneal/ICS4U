# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:48:50 2018
Part C 3(a)
@author: xuyin
"""

class recursive_algorithms: 
    
    def find (self,n): 
        if n == 0:
            return 2
        if n >0 : 
            return 3*self.find(n-1)
        
    def checkIt (self,x): 
        if x in f:
            print(True)
            return True
        else: 
            print(False)
            return False
        
a =recursive_algorithms()
list1=[]

for n in range (0,100):
    if a.find(n) <40000000:
        list1.append(n)
print(len(list1))

f = []
for i in range (0,len(list1)):
    f.append(a.find(i))
    
a.checkIt(2)