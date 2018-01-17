# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-16
Program Title: assignment5
Purpose: 
(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.
Variable names: dirt1, score
"""

dict1 = {'When did the Beijing Olympics held?':'2008', 'What is the answer of 1+1 ?': '2', 'What is the area of a square with the side length of 4':'16','Which city is the Capital of China':'beijing','Who wrote the book \'The hunger games\' ?':'Suzanne Collins'}
score = 0
print('Welcome to this quiz!')
print('Each question worth 1 mark in the quiz.')
for i in range (0,len(dict.keys())):
    print('Question number '+str(i + 1)+' :')
    print(list(dict1.keys())[i])
    answer = input('Please write your answer here: ')
    if answer == list(dict1.values())[i]:
        print('correct!!!')
        score = score + 1
    else:
        print('wrong!!!')
    print('Your current score is: '+str(score))
print ('Your final score is: '+str(score))