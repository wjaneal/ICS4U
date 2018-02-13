# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:04:12 2018
Name: Jaune
Date: Jan 12
Ttitle: Oprator
Purpose: Studying
Varable names:
@author: CTL
"""
#This two lines tell the users to input their numbers.
a = input ("enter your number:")
b = input ("enter another number:")
x = int (a) #This is to make the numbesrs become integers
y = int (b)

#This is to make comparison between these two numbers
if x == y:
    print (x, "is eaqual to" ,y)
elif x<y:
    print (x, "is less than" ,y)
elif x>y:
    print (x, "is greater than", y)
elif x!=y:
    print (x, "is not eaquel to", y)
elif x<=y:
    print (x, "is less then and eaqual to", y)
elif x>=y:
    print (x, "is greater than and eaquel to", y)
    

a = input ("enter your word:") #This line is to ask the operator to input numbers
xstring = str(a) #This is to make the word a string.
if "a" in xstring:
    print ("a is in your word.")
elif "b" in xstring:
    print ("b is in your word.")
elif "c" in xstring:
    print ("c is in your word.")
elif "d" in xstring:
    print ("d is in your word.")
elif "e" in xstring:
    print ("e is in your word.")

d=input("enter your word:")#This line is to ask the operator to input numbers
string1 = str(d)#This is to make the word a string.
for i in range(97,123): #The range in this line represents the alphabet.
    if chr(i) in string1:
        print(chr(i), " is in the string")
for ii in range(65,91):
    if chr(ii) in string1:
        print(chr(ii), " is in the string")




 








