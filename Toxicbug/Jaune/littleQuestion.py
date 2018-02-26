# -*- coding: utf-8 -*-
"""
Spyder Editor
Name: Jaune
Date: Jan 16
Title: dictionary and tuple
Purpose: studying
This is a temporary script file.
"""
#This line is to define the questions and anwsers.
D = {"what is the most popular country in the world?":"China","what is the capital city of China?":"Beijing","what is life,the universe and everything?":"42","what is 2*3?":"6","what is chemistry?":"everything"}

trace = 0 #This is to trace where you are in the list.
Dk = list(D.keys())
Dv = list(D.values())
score = 0
YourAnswer = []
for i in Dk:
    Question = input(i) #This line is to show the question.
    YourAnswer.append(Question) #This line is to put your answer into the list YourAnswer.
    if YourAnswer[trace] == Dv[trace]: #This line is to judge whether your answer is right.
        print("You are right")
        score += 1 #This line is to calculate the socres.
    else:
        print("You are wrong")
    #This line is to make sure that you are on the right spot.
    trace += 1

print("\nYour final score is: ", score)




















