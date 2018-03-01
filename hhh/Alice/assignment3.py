#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:10:15 2018

@author: haichunkan

"""

#let the user enter 2 numbers and convert them into integers.
a=int(input("Please enter a number:"))
b=int(input("Please enter another number:"))
#Compare a and b.
if a==b:
    print("a=b is",True)
else:
    print("a=b is",False)
if a!=b:
    print("a!=b is",True)
else:
    print("a!=b is",False)    
if a<b:
    print("a<b is",True)
else:
    print("a<b is",False)
if a<=b:
    print("a<=b is",True)
else:
    print("a<=b is",False)
if a>b:
    print("a>b is",True)
else:
    print("a>b is",False)
if a>=b:
    print("a>=b is",True)
else:
    print("a>=b is",False)    
#let the user enter a string.    
word=input("Please enter a word:")
#find out whether a letter(from a to e) is in the string.
if "a" in word:
    print ("a is in",word)
if "b" in word:
    print ("b is in",word)
if "c" in word:
    print ("c is in",word)
if "d" in word:
    print ("d is in",word)
if "e" in word:
    print ("e is in",word)
#Use a loop to find out what letter in the alphabet is in the string.    
for i in range (97,123):
    if chr(i) in word:#lower case letters from a to z is 97 to 122 
        print("lower case",chr(i),"is in",word)
for ii in range (65,91):#upper case letters from A to Z is 65 to 90
    if chr(ii) in word:
        print("upper case",chr(ii),"is in",word)
#Here is another solution.       
for i in word:#First, find each letter in the string.
    if ord(i)>=97 and ord(i)<=123:
#Then, locate them in the alphabet and decide their type.
#Lower case:        
       print(i,"is lower case") 
for ii in word:
#upper case:    
    if ord(i)>=65 and ord(i)<=91:
       print(i,"is upper case")        