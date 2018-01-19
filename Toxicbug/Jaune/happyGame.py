# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:02:07 2018
Name: Jaune
Date: Jan 19
Title: python class
Purpose: studying
@author: CTL
"""

import datetime

class happyGame():
    
    def time(self):
        self.now = datetime.datetime.now()
        self.name()
        self.grade = "Quize" + (now.strftime("%Y%m%d%H%M%S")) + str(self.your_name) + ".txt"
        self.grade.strip(' ')
        self.grade.strip(':')
    
    def name(self): 
        self.first_name = input ("what is your first name? :" )
        self.last_name = input ("what is your last name? :" )
        self.your_name = self.first_name + self.last_name
        return (self.your_name)

    def quize(self):
        self.D = {"what is the most popular country in the world?":"China","what is the capital city of China?":"Beijing","what is life,the universe and everything?":"42","what is 2*3?":"6","what is chemistry?":"everything"}
        self.trace = 0
        self.Dk = list(self.D.keys())
        self.Dv = list(self.D.values())
        self.score = 0
        self.YourAnswer = []
        for i in self.Dk:
            self.Question = input(i)
            self.YourAnswer.append(self.Question)
            if self.YourAnswer[self.trace] == self.Dv[self.trace]:
                print("You are right")
                self.score += 1
            else:
                print("You are wrong")
    
            self.trace += 1
        print("\nYour final score is: ", self.score)

    def store(self):
        self.time()
        self.file = open(self.grade, 'w')
        self.file.write(str(self.your_name))
        self.quize()
        self.file.write(str(self.score))
        self.file.close()

H = happyGame()
H.name()
H.quize()
H.store()











