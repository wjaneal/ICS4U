# -*- coding: utf-8 -*-
"""
Jan 12, 2018
assignment 1
ChrisLi
puepose: write a short program that loops through 1000 numbers.
for each number that is divisible by 3, print "divisible by 3"
for each number that is divisible by 19, print "is a multiple of 19"
variable number : i
"""

for i in range(0,1000):
    if i % 3 ==0:
        print(str(i),"is divisible by 3")
    elif i % 19 ==0:
        print(str(i),"is a multiple of 19")
    else:
        print(i)
        