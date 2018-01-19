#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:21:13 2018
Program:A short quiz.
The users can enter their answers.
The program will keep track of the score.
@author: haichunkan
"""
#Set the qustions and answers.
D={"What is as fast as a cheetah and as slow as a tortoise?":"shadow","What belongs to you but others use it more than yourself?":"name","How long do you need to finish reading a book":"one second","What is the largest ant in the world?":"elephant","What kind of tables never do not have legs?":"vegetables"}
#Set the original score to 0.
point=0
#Covert the keys and valuses into list objects.
Dk=list(D.keys())
Dv=list(D.values())
for i in range (0,len(Dk)): 
    print(Dk[i])#Show the riddle.
    answer=input("Your answer:")#Input answer here.
    if answer==Dv[i]:
        print ("True")
        point+=1#if the anwer is true,add 1 score.
    else:
        print("False")
print ("Your total score is",point)  #output the final score.      