# -*- coding: utf-8 -*-
'''
Created on Mon Jan 22 23:11:16 2018
Name:Khan
Date: January 22, 2018
Title:assignment6
Purpose :Option A - Make a more complete quiz program using a class structure
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time
    A and B are the first and last initials of the user.
Variable:FirstName,LastName,Dic1,Score,i,answer,Quiz,quiz,Filename,File,Content,percentage
'''
import time# import a module
class Quiz:#create a class
    def name(self):#this is to record the name
        self.FirstName = input('What is your first name') #this is to get the first name
        self.LastName = input('What is your last name')#this is to get the last name
        self.F=self.FirstName[0]#this is to get the initial of user's first name
        self.L=self.LastName[0]#this is to get the initial of user's last name
    def quiz(self):#this is to operate the quiz programe
        self.Dic1={'When was the first U.S.consititution made out?':'1787' ,'When did Bismarck pass away':'1898','When was Napolean crowned':'1804','When did Kutuzov pass away':'1813','When did USSR fall apart':'1991'}
        #this is the question list
        self.Score = 0#this is to initialize the score
        print('Each question worth 1 mark in the quiz.') #this is to give some information about the quiz
        for i in range (0,5):#this is to start a loop
            print('Question number '+str(i + 1)+' :')#this is to tell the question number
            print(list(self.Dic1.keys())[i])#this is to show the questions
            answer = input('Please write your answer here: ')#this is to record the answer
            if answer == list(self.Dic1.values())[i]:#this is to judge the answer
                print('  correct')
                self.Score = self.Score + 1#this is to accumulate the scores
            else:
                print('  wrong')
            print('Your current score is: '+str(self.Score))#this is to inform the current score
        print ('Your final score is: '+str(self.Score))#this is to inform the final score
    def file(self):#this is to create the file
        self.percentage = int(self.Score)/5*100#this is to calculate the percentage
        self.Content = 'Score ='+ str(self.Score)+'      Percentage ='+str(self.percentage)+'%'#this is to decide the content
        self.Filename = time.strftime("%Y%m%d%H%M%S")+self.F+self.L#this is to decide the file name
        self.File = open('Quiz'+self.Filename+'.txt','w')#this is to create a blank file
        self.File.write(self.Content)#this is to write the content
        self.File.close( )#this is to close the file
#run the file
Q = Quiz()
Q.name()
Q.quiz()
Q.file()
