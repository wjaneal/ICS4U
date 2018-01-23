# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 19/Tan/2018
Program Title: Assignment6

PPurpose: 
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
import time # import a module
#create a class
class Quiz: 
    def __init__(self): #This is a function that operates the quiz   
        self.score = 0   #First, initialize the score as 0
        self.name = str(input("please give your name :")) #Let the user input the name
        name_pieces = self.name.split(' ')#This split the name of the user.
        self.fn = name_pieces[0]#This could record the first name of the user
        self.ln = name_pieces[-1]#This could record the last name of the user
        self.quiz = {'what is the capital city of China': 'Beijing' ,'what is the capital city of France': 'Paris','what is the capital city of Japan': 'Tokyo','what is the capital city of Australia': 'Canberra','what is the capital city of Russia': 'Moscow'}  #create a dict
        print("Welcome to the quiz!")  #This give a mention that quiz starts
        print("Each question worth 1 score")    # This give the information of this quiz
        for i in range (0,5):       # create a loop that print the question and let user input the answer
            print ("question number " + str(i+1) + ":")       # Let user know the current question number
            print (list(self.quiz.keys())[i])                  # print the question
            self.answer = input('please give me the answer:')    # input the answer
            if self.answer == list(self.quiz.values())[i]:      # The decision structure is used to judge if the answer is correct
                print ('correct')   # give a feedback about particular question
                self.score +=1           # if the answer is correct, get  1 score
            else:
                print('wrong')      # give a feedback about particular question
            print('your current score is :' + str(self.score))      # give a feedback of their current score
        print('Your final score is : ' + str(self.score))        # give the final score
        self.percentage = self.score/5*100 #This is used to calculate the percentage of the user
        self.saveFile()  #This will save a txt file
    
   
    def saveFile(self):#This could create a txt file and record the score of the user.
        self.str1 = 'Quiz'+ time.strftime('%Y%m%d%H%M%S') + self.fn[0] + self.ln[0] #This is the file name.
        self.File = open (self.str1+'.txt','w') #This is used to creat a file
        self.str2 = 'Result of the quiz!!!'+'\nName of the user: '+self.name+'\nScore of the quiz: '+str(self.score)+'\nPercentage of the quiz: '+str(self.score/5*100)+''#This is used to record the user's percentage, name and the score of the quiz.
        self.File.write (self.str2)
        self.File.close()


Quiz()



    
    

