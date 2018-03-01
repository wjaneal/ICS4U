# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:19:23 2018

@author: Halley
Assignment 5 - Lists, Tuples, Dictionaries, Compound Data Types
Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names
(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.

"""
score = 0
quiz = {"What is the answer of 23+5?":"28","What is the answer of the 12+2?":"14","What is the answer of 33-7?":"26","What is the answer of 18-80?":"-62","What is the answer of 12^2?":"144"}
qKeys = list(quiz.keys())
qValues = list(quiz.values())
print("Quize is Begining!")
for i in range(len(qKeys)):
    print(qKeys[i])
    answer=input("The answer is:")
    if answer == qValues[i]:
        score += 1
        print("Correct!")
    else:
        print("You are wrong!")
print("You score is "+ str(score)+"out of 5")