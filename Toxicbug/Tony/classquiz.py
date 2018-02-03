# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 02:15:12 2018

@author: 11256
"""
''' 
(a)Name:Tony
(b)Date:January 16th
(c)Program title: quiz
(d)Purpose: make a quiz for people to answer the question and track the score
'''
import datetime
class Quiz():
    def time(self):
        self.now = datetime.datetime.now()
        self.grade = "Quize" + (self.now.strftime("%Y%m%d%H%M%S")) + str(self.name) + ".txt" 
        self.grade.strip(' ')
        self.grade.strip(':')


    def name(self):#define the name
        self.name = input("What is your name?")
        return (self.name)
    
    def question(self):#define the question
        self.D = {"What is the capital of China?":"Beijing","What is the largerst city in China?":"Hulun Buir","What is the capital city in Canada?":"Ottawa","What is the largerst city in Canada?":"Toronto","What is the capital city in America?":"Washington DC"}
        self.score = a = 0
        self.Dk = list(self.D.keys())
        self.Dv = list(self.D.values())
        for i in range(0,len(self.Dk)):
            self.answer = input(self.Dk[i])
        if self.answer == self.Dv[i]:#use if to check the answer is right
            a=a+1
            print ("You have", a, "score",)
        else:
            print ("You are wrong.")
            print ("You have", a, "score",)
        print("You got",a,"point in the quiz.")
    def store(self):#define the storate
        self.time()
        self.file = open(self.grade, 'w')
        self.file.write(str(self.name))
        self.file.write(str(self.score))
        self.file.close()
#This start the quiz.

H = Quiz()
H.question()
H.store()
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   












