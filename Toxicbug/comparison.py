# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 01:44:10 2018

@author: 11256
"""

''' 
(a)Name:Tony
(b)Date:January 12th
(c)Program title:comparison
(d)Purpose: comparison the number and check the number in the string
'''
a = input("Enter your first number:")
b = input("Enter your second number:")
x = int(float(a))
y = int(float(b))
if x > y:
    print ("a is larger than b")
elif x == y:
    print ("a is equal to b")
elif x < y:
    print ("a is less than b")
elif x != y:
    print("a is not equal to ")
elif x >= y:
    print("a is larger than and equal to y")
elif x <= y:
    print("a is smaller than and equal to y")
    


a = input("Enter your  word:")
astring = str(a)
if 'a' in astring:
    print ("a is in your word")
else:
    print("a is not in your word")
if 'b' in astring:
    print ("b is in your word")
else:
    print("b is not in your word")
if 'c' in astring:
    print ("c is in your word")
else:
    print("c is not in your word")
if 'd' in astring:
    print ("d is in your word")
else:
    print("d is not in your word")
if 'e' in astring:
    print ("e is in your word")
else:
    print("e is not in your word")
    
b = input("Enter your  word:")
bstring = str(b)
for i in range (97, 123):
    if chr(i) in bstring:
        print (chr(i))
for i in range(65, 91):
    if chr(i) in bstring:
        print (chr(i))
