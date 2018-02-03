'''
Assignment 6 - Program in a Class

Coding convention: 
(a) assignment6
(b) Lily, Jan.18th 2018, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names


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

'''

import time
filename = "quiz"+str(time.strftime("%Y%m%d%H%M%S")) + ".txt"
name = (input("what is your name?"))
print(name)
 
question={"Are you happy?":"yes!","How r u today?":"good!", "Want to chat?":"of course!","I am sad...":"chins up!","What's the weather?":"sunny!"}
key1=list(question.keys())
value1=list(question.values())
score = 0
i = 0
for i in range (0,len(key1)):
    questionprint = key1[i]
    print (questionprint)
    answer = input("")
    answerprint = value1[i]
    if answer == answerprint:
        score = score +1

stringName = str(score) + " " + str(score/5 * 100) + "%"

myfile = open(filename, 'w')
myfile.write(stringName)
myfile.close()

























































