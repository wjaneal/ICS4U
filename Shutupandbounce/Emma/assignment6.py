# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:38:55 2018
Name:Emma
Title:Assignment 6 - Program in a Class
Purpose:Option A - Make a more complete quiz program using a class structure
(c) mixedCase variable names: quizProgram

"""
#import source required
import time

#(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
class quizProgram:
    def question(D):#Define a function for giving questions to the user to answer.
        D={"What is life, universe and everything?":"42", 
           "If there are 6 apples and you take away 4, how many do you have?":"4", 
           "What goes up and never comes down?":"age", 
           "What has a head and a tail but no body?":"a coin",
           "If there are 12 fish and half of them drown, how many are there? ":"12"}
        score = 0#This is the total score.
        Dk = list(D.keys())
        Dv = list(D.values())
        for i in range(0, len(D.keys())):#(1b) In a loop, ask questions based on the key values. 
            answer = input(Dk[i])#(1c) Allow the user to input the answers.
            if answer == Dv[i]:#Set a if statement for different results.
                score += 1#Keep track of the score.
                print("Correct!")
            else:
                print("Sorry... It isn't.")
        print("Your score is", score,"out of 5")#When all of the questions have been asked, tell print the final quiz score.
        question_number = 5#Convert the number into a string in order to be written in the following setting of the file name.
        percentage = 100
        date = '%Y%m%d%H%M%S'#Set the current time, including date, hour, minute and time.
        first_name = input("Enter the user's first name:")#(a) Have the program ask for the user's name.
        last_name = input("Enter the user's last name:")
        name_initial = (first_name[0]+last_name[0])
        f = open("Quiz"+str(time.strftime(date))+name_initial+".txt", "w")#"f" means "file"
        f.write(first_name+" "+last_name+"'s quiz result:"+str((score/question_number)*percentage)+"% out of 5")#(b) Record the results of each quiz in a file. 
        f.close()
        return D

run = quizProgram()#Create a object based on the class.
run.question()#Run the function.