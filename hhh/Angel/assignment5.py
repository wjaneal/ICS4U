#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:13:14 2018
@author: hailankan
Program Title: quiz program
Function:(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.
"""
#questions and answers
D={"what is 1 + 1?":"2","what is the capital city of China?":"Beijing","which city held the 2012 Summer Olympics?":"London","which liquid has the highest heat capacity?":"water","which country occupied the most area?":"Russia"}
answer= []
Dk = D.keys()
Dv = list(D.values())
score=0#initial score is 0
for i in D.keys():#put correct answers in a list
    answer.append(input(i))
for i in range(0, len(Dk)):
    if answer[i] == Dv[i]:
        score+=1#for every correct answer, +1 score
        print("You are correct!")#tell the user the answer is correct
    else:
        print("You are wrong!")#tell the user the answer is wrong
print ("You get a score of", score)#print final score