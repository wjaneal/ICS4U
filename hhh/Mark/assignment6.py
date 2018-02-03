# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-01-19
Program Title: Program in a Class
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
"""
import time
class Quiz:
    def quizStart(self): #Start the quiz. 
        self.score = 0 #This variable is used to record the score of the user.
        self.fn = str (input('Please write down your first name: '))#This is used to record the first name of the user.
        self.ln = str (input('Please write down your last name: '))#This is used to record the last name of the user.
        self.quiz = {'When did Beijing Olympics hold?' : '2008' , 'When did Bismarck pass away?' : '1898' , 'When was Napolean crowned' : '1804' , 'When was the founding of new China' : '1949', 'When was the first U.S.consitution made out?' : '1787' , 'When did London Olympics hold?' : '2012'}
        print('Welcome to this quiz!')#This is used to let users know the quiz is starting.
        print('Each question worth 1 mark in the quiz.')
        for i in range (0,5): 
            print('Question number '+str(i + 1)+' :')#This is used to let users know the current question number.
            print(list(self.quiz.keys())[i])
            self.answer = input('Please write your answer here: ')
            if self.answer == list(self.quiz.values())[i]:#The decision structure is used to determine whether the user's answer is correct or not.
                print('correct!!')
                self.score = self.score + 1
            else:
                print('wrong!!')
            print('Your current score is: '+str(self.score))#This is used to help users know their current score.
        print ('Your final score is: '+str(self.score))#This is used to help users know their final score.
        self.percentage=self.score/5*100#This is used to determine users' percentage of the question.
        self.saveFile()#This is used to save a file
        
    def saveFile(self):#This is used to save a txt. file.
        self.str1 = 'Quiz'+ time.strftime('%Y%m%d%H%M%S') + self.fn[0] + self.ln[0] #This is the file name.
        self.File = open (self.str1+'.txt','w') #This is used to creat a file
        self.str2 = 'Result of the quiz!!!'+'\nName of the user: '+self.name+'\nScore of the quiz: '+str(self.score)+'\nPercentage of the quiz: '+str(self.score/5*100)+''#This is used to record the user's percentage, name and the score of the quiz.
        self.File.write (self.str2)
        self.File.close()
        
a = Quiz()
a.quizStart        
        