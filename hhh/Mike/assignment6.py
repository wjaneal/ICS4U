# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-19
Program Title: assignment6 (quiz)
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
"""
import time
#The class structure is used here.
class Quiz:
    def __init__(self): #This part is used to start the quiz. 
        self.score = 0 #This variable is used to record the score of the user.
        self.name = str (input('Please write down your name: ')) #This lets user input their name.
        name_pieces = self.name.split(' ')#This split the name of the user.
        self.fn = name_pieces[0]#This could record the first name of the user
        self.ln = name_pieces[-1]#This could recor the last name of the user
        self.quiz = {'When did the Beijing Olympics held?':'2008', 'What is the answer of 1+1 ?': '2', 'What is the area of a square with the side length of 4':'16','Which city is the Capital of China':'beijing','Who wrote the book \'The hunger games\' ?':'Suzanne Collins'}
        print('Welcome to this quiz!')#This will tell the user that the quiz starts
        print('Each question worth 1 mark in the quiz.')
        for i in range (0,5): #The loop structure is used here to print out the quiz questions and let users input their answers.
            print('Question number '+str(i + 1)+' :')#This could let users know what is their current question number.
            print(list(self.quiz.keys())[i])
            self.answer = input('Please write your answer here: ')
            if self.answer == list(self.quiz.values())[i]:#The decision structure here is used to determine whether the answer of the user is correct or not.
                print('correct!!!')
                self.score = self.score + 1
            else:
                print('wrong!!!')
            print('Your current score is: '+str(self.score))#This could help user know their current score.
        print ('Your final score is: '+str(self.score))#This could help user know their final score.
        self.percentage=self.score/5*100#This is used to determine the percentage of the user
        self.saveFile()#This will save a txt file
        
    def saveFile(self):#This could create a txt file and record the score of the user.
        self.str1 = 'Quiz'+ time.strftime('%Y%m%d%H%M%S') + self.fn[0] + self.ln[0] #This is the file name.
        self.File = open (self.str1+'.txt','w') #This is used to creat a file
        self.str2 = 'Result of the quiz!!!'+'\nName of the user: '+self.name+'\nScore of the quiz: '+str(self.score)+'\nPercentage of the quiz: '+str(self.percentage)#This is used to record the user's percentage, name and the score of the quiz.
        self.File.write (self.str2)
        self.File.close()
        
Quiz()        




