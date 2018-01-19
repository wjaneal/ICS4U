# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 16/Tan/2018
Program Title: Lists, Tuples, Dictionaries, Compound Data Types

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
import time 
First_Name = str(input('First name :'))
Last_Name = str(input('Last name :'))
dict1 = {'what is the capital city of China': 'Beijing' ,'what is the capital city of France': 'Paris','what is the capital city of Japan': 'Tokyo','what is the capital city of Australia': 'Canberra','what is the capital city of Russia': 'Moscow'}
print("Each question worth 1 score")
score = 0

for i in range (0,5):
    print (list(dict1.keys())[i])
    answer = input('please give me the answer:')
    if answer == list(dict1.values())[i]:
        print ('correct')
        score +=1
    else:
        print('wrong')
print('Your final score is : ' + str(score))

class Quiz:
    def __init__(self,score,First_Name, Last_Name):
        self.score = score
        self.First_Name = First_Name
        self.Last_Name = Last_Name


quiz = Quiz(score,First_Name,Last_Name)
str1 = 'Quiz'+ time.strftime('%Y%m%d%H%M%S') + quiz.First_Name[0] + quiz.Last_Name[0]
File = open (str1+'.txt','w')
str2 = 'Result of the quiz:'+'\nName of the user: '+quiz.First_Name + quiz.Last_Name +'\nScore of the quiz: '+str(score)+'\nPercentage of the quiz: '+str(score/5*100)+''
File.write (str2)
File.close()

    
    

