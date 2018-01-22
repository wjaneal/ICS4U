#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:35:32 2018
Option A - Make a more complete quiz program using a class structure
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.
@author: haichunkan
"""
import time
class Quiz():
    def playerInformation(self):#Ask the user's name.
        self.first_name=input("Your first name:")
        self.last_name=input("Your last name:") 
        fn=list(self.first_name)
        ln=list(self.last_name)
        if ord(fn[0])>=97 and ord(fn[0])<=122:#Convert the initials into upper case.
            fn[0]=chr(ord(fn[0])-32)
        if ord(ln[0])>=97 and ord(ln[0])<=122:
            ln[0]=chr(ord(ln[0])-32)
        self.initials=fn[0]+ln[0]#Combine the initials of first and last name together.    
    def quizQuestions(self):#Here are the quiz problems.
        self.score=0
        print("Start the quiz!")
        D={"What is as fast as a cheetah and as slow as a tortoise?":"shadow","What belongs to you but others use it more than yourself?":"name","How long do you need to finish reading a book":"one second","What is the largest ant in the world?":"elephant","What kind of tables do not have legs?":"vegetables"}
        Dk=list(D.keys())
        Dv=list(D.values())
        for i in range (0,len(Dk)): 
            print(Dk[i])
            answer=input("Your answer:")
            if answer==Dv[i]:
                print ("True")
                self.score+=1#Add scores.
            else:
                print("False")
                print("The true answer is",Dv[i])
            self.c= str((i+1)*100/len(Dk))+"%"  
            print("You have completed",self.c)#This is how many questions have been finished.
        print("Your score is:",self.score)#Show the final score.    
    def date(self):
        self.time=time.strftime('%Y%m%d%H%M%S')#Get the time now,year,month,day,hour,minute,second.
           
    def file(self):#Name the file.
        self.name="quiz"+self.time+self.initials+".txt"
        File = open(self.name,'w')
        File.write(self.name)
        File.write("Name: "+self.first_name+self.last_name)
        File.write("Completeness: "+self.c)#This is the percentage of completeness.
        File.write("Score: "+str(self.score))#This shows the correct 
        File.close()
q=Quiz()  #Run the program.      
q.playerInformation()
q.quizQuestions()
q.date()
q.file()

                   