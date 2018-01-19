# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-19
Program Title: assignment6
Purpose: 
Option A - Make a more complete quiz program using a class structure
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.
Option B - Write the Stock Ticker program in a class structure.
(a) Store the results of each game in a file. The results should include the date and time, the names of each player and the total networth achieved at the end. The players should be listed in the order of their networth. The name of each file should be as follows: STyyyymmddhhmmss.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
I will choose Option A in this assignment.
Variable names: name, dict1, score, quiz.score, quiz.name, quiz.fn, quiz.ln, quiz, File, str1, str2
"""
import time
name = str (input('Please write down your name: '))
dict1 = {'When did the Beijing Olympics held?':'2008', 'What is the answer of 1+1 ?': '2', 'What is the area of a square with the side length of 4':'16','Which city is the Capital of China':'beijing','Who wrote the book \'The hunger games\' ?':'Suzanne Collins'}
score = 0
print('Welcome to this quiz!')
print('Each question worth 1 mark in the quiz.')
for i in range (0,5):
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

class Quiz:
    def __init__(self,score,full_name):
        self.score = score
        self.name = full_name
        name_pieces = full_name.split(' ')
        self.fn = name_pieces[0]
        self.ln = name_pieces[-1]

quiz = Quiz(score,name)
str1 = 'Quiz'+ time.strftime('%Y%m%d%H%M%S') + quiz.fn[0] + quiz.ln[0]
File = open (str1+'.txt','w')
str2 = 'Result of the quiz!!!'+'\nName of the user: '+quiz.name+'\nScore of the quiz: '+str(score)+'\nPercentage of the quiz: '+str(score/5*100)+''
File.write (str2)
File.close()
