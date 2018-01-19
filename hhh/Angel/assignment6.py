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
    def Name(self):    
        self.first_name=input("first name:")
        self.last_name=input("last name:")
        self.full_name=self.first_name+" "+self.last_name
        self.first_initial=list(self.first_name)[0]
        self.last_initial=list(self.last_name)[0]
    def Questions(self):
        self.score=0
        self.amount=int(input("how many questions:"))
        for i in range(0,self.amount):
            number1= int(random()*100)
            number2= int(random()*100)
            answer = input("what is "+str(number1)+"*"+str(number2)+"?")
            if int(answer) == number1*number2:
                print("correct")
                self.score+=1
            else:
                print("incorrect")
        print("your score is "+str(self.score))
        
    def Result(self):
        self.percentage = str(self.score/self.amount*100) + "%"
        print(self.percentage)
        
    def File(self):
        self.Name()
        self.Questions()
        self.Result()
        self.time= datetime.now().strftime('%Y%m%d%H%M%S')
        file = open("Quiz"+self.time+str(self.first_initial)+str(self.last_initial)+".txt","w")
        file.write(self.full_name)
        file.write("score:"+str(self.score))
        file.write("percentage:"+str(self.percentage))
        file.close()
    
run=Quiz()
run.File()
