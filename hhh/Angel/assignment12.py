#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:48:38 2018
@author: hailankan
Create a class with functions for three recursive algorithms.  Include factorials, the Towers of Hanoi and any other recursive function.  Allow the user to choose any of the three functions and then interact with the function.  The program should provide adequate instructions and output to be useful.

"""

class recursive:
    def Factorial(n):
        if n ==1:
            return 1
        else:
            return n * recursive.Factorial(n-1)#ie. 5*F(4)=5*4*F(3)=...=5*4*3*2*1
    
    def TowersOfHanoi(a,b,c,n):#a is start position,c is end position, n is number of towers
        if n == 1:
            print("move 1 from", a," to ",c)
        else:
            #ie.how to move 5 towers from p1 to p3? => how to move 4 towers from p1 to p2 => how to move 3 towers from p2 to p1 => ...
            recursive.TowersOfHanoi(a,c,b,n-1)#move all the other towers except the largest one from position a to b
            # ie.move the 5th from p1 to p3=>move 4th from p2 to p3
            recursive.TowersOfHanoi(a,b,c,1)# move the largest one from start position to end position
            #ie. how to move 4 towers from p2 to p3 => how to move 3 towers from p1 to p3
            recursive.TowersOfHanoi(b,a,c,n-1)# move all the other towers from position b to c
        
    def GuessTheNumber(sta,end,num):#binary search
        mid=(sta+end)//2
        if mid==num:
            print('Found')#find the number
        elif mid>num:
            print('Too Big')#middle is too big
            recursive.GuessTheNumber(sta,mid,num) # use mid as end  
        else:
            print('Too Small')#middle is too small
            recursive.GuessTheNumber(mid,end,num)#use mid as start
             
r=recursive#use the class
answer=''#set a variable
while answer!='4':#if not end
    print('Which one?')
    answer=input("1 factorial; 2 TowersOfHanoi: 3 GuessTheNumber 4 End")#let the user choose a functuon
    if answer=='1':
        n=int(input('of which number'))# the factorial of which number
        r.Factorial (n)
    if answer=='2':
        n=int(input('how many'))#how many towers
        a=input('start position')
        b=input('use position')
        c=input('end position')
        r.TowersOfHanoi(a,b,c,n)
    if answer=='3':
        sta=int(input('start number'))
        end=int(input('end number'))
        num=int(input('choose a number from start to end'))#the number to find
        r.GuessTheNumber(sta,end,num)