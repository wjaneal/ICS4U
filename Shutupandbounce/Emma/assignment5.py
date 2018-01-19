# -*- coding: utf-8 -*-
"""
(b) Name:Emma, 
Date:Created on Tue Jan 16 13:17:06 2018,
Title:Assignment 5 - Lists, Tuples, Dictionaries, Compound Data Types, 
Purpose:(1) Make a short quiz program that uses a dictionary for its questions and answers.

"""
#(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
D={"What is life, universe and everything?":"42", 
   "If there are 6 apples and you take away 4, how many do you have?":"4", 
   "What goes up and never comes down?":"age", 
   "What has a head and a tail but no body?":"a coin",
   "If there are 12 fish and half of them drown, how many are there? ":"12"}
score = 0#This is the total score.
Dk = list(D.keys())
Dv = list(D.values())
for i in range(0, len(D.keys())):#(1b) In a loop, ask questions based on the key values. 
    answer = input(Dk[i])#(1c) Allow the user to input the answers.
    if answer == Dv[i]:
        score += 1#Keep track of the score.
        print("Correct!")
    else:
        print("Sorry... It isn't.")
print("Your score is", score,"out of 5")#When all of the questions have been asked, tell print the final quiz score.