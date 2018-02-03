#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hailankan
Jan 19, 2018
Program Title: Quiz quiz
Function:
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.
"""

from random import random
from datetime import datetime


class Quiz():
    def Name(self):#ask the user to input their name    
        self.first_name=input("first name:")
        self.last_name=input("last name:")
        self.full_name=self.first_name+" "+self.last_name
        self.first_initial=list(self.first_name)[0]#get the first name initial
        self.last_initial=list(self.last_name)[0]#...last...
    def Questions(self):
        self.score=0
        self.amount=int(input("how many questions:"))#ask how many questions they want
        #get two random numbers 
        for i in range(0,self.amount):
            number1= int(random()*100)
            number2= int(random()*100)
            answer = input("what is "+str(number1)+"*"+str(number2)+"?")
            if int(answer) == number1*number2:
                print("correct")
                self.score+=1#add score for each correct answer
            else:
                print("incorrect")
        print("your score is "+str(self.score))#print score
        
    def Result(self):#print correct percentage
        self.percentage = str(self.score/self.amount*100) + "%"
        print(self.percentage)
        
    def File(self):
        self.Name()
        self.Questions()
        self.Result()
        self.time= datetime.now().strftime('%Y%m%d%H%M%S')#get current time
        file = open("Quiz"+self.time+str(self.first_initial)+str(self.last_initial)+".txt","w")#set file name
        #writte name,score, and percentage
        file.write(self.full_name)
        file.write("score:"+str(self.score))
        file.write("percentage:"+str(self.percentage))
        file.close()
    
run=Quiz()
run.File()#run program
