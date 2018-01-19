#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: chenquancheng
Date: Created on Wed Jan 17 13:12:19 2018
Title: Developed Quiz
Purpose: To make a more complete quiz program using a class structure and to save a file after the quiz
"""
import datetime
import random
#This is a class structure.
class Quiz:
    def quizOp(self):
        #This is a function that operates the quiz.
        self.score=0 #This initializes the user's score as 0.
        self.firstName=input("What's your first name?")#This lets the user input his first name.
        self.lastName=input("What's your last name?")#This lets the user input his last name.
        self.A=self.firstName[0]#This gets the first initial of the user.
        self.B=self.lastName[0]#This gets the last initial of the user.
        self.mathGenerator()#This generates some random math problems.
        #This creates some quiz problems.
        self.quiz={"What is "+str(self.a)+"+"+str(self.b)+"?":str(self.answer),"What is the capital city of China?":"Beijing","Which city is LIA in?":"London","How many items are there in a dozen?":"12","What planet are we on?":"Earth"}
        self.qKeys=list(self.quiz.keys())#This gets the keys.
        self.qValues=list(self.quiz.values())#This gets the values.
        print("Are you ready?Let's start the quiz!")
        for i in range(len(self.qKeys)):
            print(self.qKeys[i])
            self.userAnswer=input("Please input your answer here.")
            if self.userAnswer == self.qValues[i]:
                print("You are correct!")
                self.score+=1
            else:
                print("You are wrong!")
        print("Your score is "+str(self.score)+" out of 5")
        self.percentage=self.score/5*100
        self.saveFile()
        
    def mathGenerator(self):
        #This generates some math problems.
        self.a=random.randint(1,100)
        self.b=random.randint(1,100)
        self.answer=self.a+self.b
    
    def getDate(self):
        #This gets the date and time.
        i = datetime.datetime.now()
        self.year=str(i.year)
        self.month=str(i.month)
        self.day=str(i.day)
        self.hour=str(i.hour)
        self.minute=str(i.minute)
        self.second=str(i.second)
        if len(self.month)==1:
            self.month="0"+self.month
        if len(self.day)==1:
            self.day="0"+self.day
        if len(self.hour)==1:
            self.day="0"+self.day
        if len(self.minute)==1:
            self.minute="0"+self.minute
        if len(self.second)==1:
            self.second="0"+self.second
        self.timeTotal=self.year+self.month+self.day+self.hour+self.minute+self.second 
    
    def saveFile(self):
        #This saves the file.
        self.getDate()
        self.fileName="Quiz"+self.timeTotal+self.A+self.B
        fw = open("{0}.txt".format(self.fileName), 'w')
        fw.write("Username:"+self.firstName+" "+self.lastName+"\n")
        fw.write("Score:{0}\n".format(str(self.score)))
        fw.write("Percentage:{0}%\n".format(str(self.percentage)))
        fw.close()
        self.readFile()
    
    def readFile(self):
        #This reads the file.
        self.fileName="Quiz"+self.timeTotal+self.A+self.B
        fr = open("{0}.txt".format(self.fileName), 'r')
        self.result=fr.read()
        print(self.result)
        fr.close()
        
a=Quiz()
a.quizOp()


