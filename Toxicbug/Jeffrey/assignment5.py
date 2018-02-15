# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:55:07 2018

@author: Jeffrey

purpose:
(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.
"""
# Create a dictionary with at least five key:value pairs to store the questions and answers.
AnswerBox = {"What is 2 + 2? ": "4", "What is the capital of the United States? ": "Washington", "What is the earth's natural satellite? ": "moon", "What is 2*3? ": "6", "What is 9/3? ": " 3"}
AnswerBoxK = list(AnswerBox.keys()) # Using a list to get all the questions
AnswerBoxV = list(AnswerBox.values()) # Using a list to get all the answers 
UserAnswer = [] # Using a empty list to restore answers
score = 0
current_start = 0 # using a variable to keep in trace of rounds 
# Loop through all the questions
for i in AnswerBox.keys():
    UserAnswer.append(input(i))
    if AnswerBoxV[current_start] == UserAnswer[current_start]: # Compare answers 
        score +=1
        print("You are correct")
    else:
        print("Wrong Answer")
    current_start += 1

print("\nYour score is ", score) # printing results
























