# -*- coding: utf-8 -*-
"""
Assignment 3
Chris Jan 14th 
purpose: compare two different numbers and check letters
variable number: a b c 
"""

 #    (a)
print("(a)")                         
a=input("a:")                       
b=input("b:")           
print("\n")              
                         #    (b)
print("(b)")                         
a=int(float(a))          
b=int(float(b))          
print("a=",a)           
print("b=",b)            
print("\n")
                         #   (c)
print("(c)")
if a==b:
    print("a=b ture")
else:
    print("a=b false")
if a!=b:
    print("a!= ture")
else:
    print("a!= false")
if a>b:
    print("a>b ture")
else:
    print("a>b false")
if a<b:
    print("a<b ture")
else:
    print("a<b false")
if a<=b:
    print("a<=b ture")
else:
    print("a<=b false")
if a>=b:
    print("a>=b ture")
else:
    print("a>=b false")
print("\n")
                        #    (d）
print("(d)")
c=input("c:")
print("c=",c)
print("\n")
                        #    (e)
print("(e)")                       
if "a" in c:
    print("a is in c")
else:
        print("a is not in c")
if "b" in c:
    print("b is in c")
else:
    print("b is not in c")
if "c" in c:
    print("c is in c")
else:
    print("c is not in c")    
if "d" in c:
    print("d is in c")
else:
    print("d is not in c")   
if "e" in c:
    print("e is in c")
else:
    print("e is not in c")   
print("\n")
                        #    (f)
print("(f)")    
for i in range(97,123):             
 if (chr(i)) in c:
    print(chr(i) +  "is in" + c)
 else:
    print(chr(i) +  "is not in" + c)
        


















     