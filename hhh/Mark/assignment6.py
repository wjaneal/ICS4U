# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-01-19
Program Title: Program in a Class
Purpose:
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.
"""

import time
FirstName = input('What is your first name?')
LastName = input('What is your last name?')
dict1={'When did Beijing Olympics hold?' : '2008' , 'When did Bismarck pass away?' : '1898' , 'When was Napolean crowned' : '1804' , 'When was the founding of new China' : '1949', 'When was the first U.S.consitution made out?' : '1787' , 'When did London Olympics hold?' : '2012'}
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
class Quiz:
    def __init__ (self,score,first_name,last_name):
        self.score = score
        self.f = FirstName[0]
        self.l = LastName[0]
quiz = Quiz(score,FirstName,LastName)
percentage = int(score)/5*100
Content = 'score =' + str(score)+'Percentage =' + str(percentage) + '%'
Filename = time.strftime('%Y%m%d%H%M%S')+quiz.f+quiz.l
File = open('quiz'+Filename+'.txt','w')
File.write(Content)
File.close( )

        