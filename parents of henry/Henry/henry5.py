# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 16/Tan/2018
Program Title: Lists, Tuples, Dictionaries, Compound Data Types

Purpose

(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.

"""

dict1 = {'what is the capital city of China': 'Beijing' ,'what is the capital city of France': 'Paris','what is the capital city of Japan': 'Tokyo','what is the capital city of Australia': 'Canberra','what is the capital city of Russia': 'Moscow'}
print("Each question worth 1 score")
score = 0

for i in range (0,5):
    print (list(dict1.keys())[i])
    answer = input('please give me the answer:')
    if answer == list(dict1.values())[i]:
        print ('correct')
        score +=1
    else:
        print('wrong')
print('Your final score is : ' + str(score))

    
    

