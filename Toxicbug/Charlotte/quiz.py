#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: chenquancheng
Date: Created on Tue Jan 16 12:51:17 2018
Title: short quiz
Purpose: makes a short quiz program that uses a dictionary for its questions and answers
"""
score=0
quiz={"What is 2+3?":"5","What is the capital city of China?":"Beijing","Which city is LIA in?":"London","How many items are there in a dozen?":"12","What planet are we on?":"Earth"}
qKeys=list(quiz.keys())
qValues=list(quiz.values())
print("Are you ready?Let's start the quiz!")
for i in range(len(qKeys)):
    print(qKeys[i])
    userAnswer=input("Please input your answer here.")
    if userAnswer == qValues[i]:
        print("You are correct!")
        score+=1
    else:
        print("You are wrong!")
print("Your score is "+str(score)+" out of 5")