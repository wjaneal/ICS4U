# -*- coding: utf-8 -*-
"""
Assignment 6 
Jan 19
ChrisLi
Variable names: users' names answers
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.
"""
import time
class quiz:
    def __init__(self, full_name):
        self.name = full_name
        
user1=input("user's name:")

    #Dictionaries
D = {"Is tokyo belongs to Japan?":"yes","Is pineapple belongs to fruits?":"yes","Who is the current president of USA?":"Trump","Is the car's speed faster than plane?":"no","Is frog belongs to human being?":"no"}
answer=[]
point=0
Dk = list(D.keys())
Dv = list(D.values())
for i in D.keys():
    answer.append(input(i))
for i in range(0, len(Dk)):
    if answer[i] == Dv[i]:
        point+=20
print (user1,"You get a score of", point,time.strftime("%y%m%d %H:%M:%S"))
