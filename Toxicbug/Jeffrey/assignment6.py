# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:31:01 2018

@author: Jeffrey

Option A - Make a more complete quiz program using a class structure
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz 
    and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.

"""


import random 
import datetime

# Make a class to organize the quiz program:
class Quiz():
    # Prompt the user to enter the name
    def AskName(self):
        self.first_name = input("What is your first name? ")
        self.last_name = input("What is your last name? ")
        self.full_name = self.first_name + self.last_name
        return(self.full_name)
    # Generate questions and restore the data
    def Question(self):
        self.first_number = random.randrange(0,10)
        self.second_number = random.randrange(0,20)
        self.string_prompt = "What is " + str(self.first_number) + " X " + str(self.second_number) + " ? "
        self.user_answer = input(self.string_prompt)
        self.answer = self.first_number * self.second_number
    # Check the answer and add scores
    def AddScore(self):
        self.score = 0
        self.n = 5
        for i in range(self.n):
            self.Question()
            if int(self.user_answer) == int(self.answer):
                print("You are right")
                self.score += 1
            else:
                print("You are wrong")
            print("Your score is now: ", self.score, " out of ", i+1)
        self.correct_percentage = (str(self.score/self.n*100) + "%")
    # Get the date in a format and the file names
    def Dates(self):
        self.string_time = str(datetime.datetime.now())
        self.format_time = []
        for characters in self.string_time:
            if ord(characters)<58 and ord(characters)>47:
                self.format_time.append(characters)
        self.format_time = self.format_time[:12]
        self.AskName()
        self.initials = self.first_name[0] + self.last_name[0]
        self.file_name = ''.join(self.format_time) + self.initials + ".txt"
    # Read and wirte the file for date of test takers  
    def Files(self):
        self.Dates()
        self.file = open(self.file_name, "w")
        self.file.write("\nFirst Name: " + str(self.first_name))
        self.file.write("\nLast Name: " + str(self.last_name))
        self.AddScore()
        self.file.write("\nScore: " + str(self.score))
        self.file.write("\nPercentage Achieved: " + self.correct_percentage)
        self.file.close()

#Run the program
a = Quiz()
a.Files()