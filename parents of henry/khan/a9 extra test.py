# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:49:31 2018

@author: simet
"""
import time
p=[2,3,5,7]
start=time.clock()
n=10000000
for i in range (1,n,2):
    if i%3!=0:
        if i%5!=0:
            if i%7!=0:
                prime =0
                a=int(p[-1])
                for j in range (a,int(i+1),2):
                    if i%j ==0:
                        prime+=1
                        
                    if prime == 1:
                        p.append(i)


print(p)
elapsed = (time.clock() - start)
Text=str(n)+' '+str(elapsed)
print(Text)

