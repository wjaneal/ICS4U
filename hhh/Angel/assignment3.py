#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:47:18 2018
@author: hailankan
compare and check letters
output something according to the decisions made using six comparison operators; check if each letter in the alphabet is in a string
"""

input1 = float(input("please enter a number"))
input2 = float(input("please enter a number"))
int1 = int(input1)
int2 = int(input2)
def Equal():
    if int1 == int2:
        print("equal")
    else:
        print("not equal!")
def Notequal():
    if int1 != int2:
        print("not equal")
    else:
        print("equal")
def Bigger():
    if int1 > int2:
        print(int1," is larger than ",int2)
    else:
        print(int1," is not larger than ",int2)
def Smaller():        
    if int1 < int2:
        print(int1," is smaller than ",int2)
    else:
        print(int1," is not smaller than ",int2)
def Boe():
    if int1 >= int2:
        print(int1," is not smaller than ",int2)
    else:
        print(int1," is smaller than ",int2)
def Soe():
    if int1 <= int2:
        print(int1," is not larger than ",int2)
    else:
        print(int1," is larger than ",int2)
Equal()
Notequal()
Bigger()
Smaller()
Boe()
Soe()

string1 = str(input("please enter something:"))
def Check(string1):
    if "a" in string1:
        print("a is in "+string1)
    if "b" in string1:
        print("b is in "+string1)
    if "c" in string1:
        print("c is in "+string1)
    if "d" in string1:
        print("d is in "+string1)
    if "e" in string1:
        print("e is in "+string1)
Check(string1)
for i in range(65,91):
    if chr(i) in string1:
        print(chr(i)+" is in "+string1)
for i in range(97,123):
    if chr(i) in string1:
        print(chr(i)+" is in "+string1)















   