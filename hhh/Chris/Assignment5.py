# -*- coding: utf-8 -*-
"""
Assignment 5
ChrisLi Jan 16, 2018
Variable names: a b c d e

(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.

"""

#Dictionaries

D = {"Is tokyo belongs to Japan?":"Yes","Is pineapple belongs to fruits?":"Yes","Who is the current president of USA?":"Trump","Is the car's speed faster than plane?":"No","Is frog belongs to human being?":"No"}

Dk = list(D.keys())
Dv = list(D.values())
for i in range(0,len(D.keys())):
    print(Dk[i])

a=input("a:")
b=input("b:")
c=input("c:")
d=input("d:")
e=input("e:")

