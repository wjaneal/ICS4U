# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-01-16
Program Title: Lists, Tuples, Dictionaries, Compound Data Types
Purpose:
(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.
"""

dict1={"What is the capital city in China?" : "Beijing" , "What is the capital city in France?" : "Paries" , "What is the capital city in Japen?" : "Tokyo" , "What is the capital city in Canada" : "Ottawa" , "What is the capital city in Australia?" : "Camberra"}
score=0
print('Each question worth 1 mark')
for i in range (0,len(dict1.keys())):
    print('Question number' + str(i + 1)+' :')
    print(list(dict1.keys())[i])
    answer = input('Please write your answer here: ')
    if answer == list(dict1.values())[i]:
        print('correct!!')
        score = score + 1
    else:
        print('wrong!!')
print ('Your final score is: ' +str(score))
