# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:57:49 2018

@author: xuyin
"""

originString = 'sdlfsldfhsdjh'
binaryString = ' '.join(format(ord(x),'b')for x in originString)
print(binaryString)

listB = []
listB = binaryString.split(' ')
print(listB)

for i in range (len(listB)):
    a = listB[i][1:4]
    listB[i][1:4] = listB[i][4:6]
    listB[i] = listB[i] + a

print(listB)
