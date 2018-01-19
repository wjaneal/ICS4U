#Name:Mandy
#Date: January17, 2018
#Program Title:Option A - Make a more complete quiz program using a class structure 
#Program Function:
'''(a) Have the program ask for the user's name.
   (b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
'''

import os
import time
firstName = input("Your first name:")
lastName = input("Your last name:")
D = {"what does l equal if the orbital shape is s?":"0","what is the orbital shape if l = 3 ":"f","charge of electron = ?":"-1.6*10^-19C","who discovered the electron?":"Thomson","How to spell Br?":"bromine"}
Dk = list(D.keys())
Dv = list(D.values())
scores = 0

for i in range(0,len(D.keys())):
    print (Dk[i])
    a = str(input())
    if a == Dv[i]:
        scores += 1
        print ("You are right!^_^!")
    else:
        scores = scores
        print ("Wrong!>_<!")
print("Your Scores:",scores)
percentage = str(scores/5*100) + "%" 
list1 = str(firstName)
list2 = str(lastName)
date = str(time.strftime("%Y%m%d%H%M%S"))	
stringToSave = "Name:" + str(firstName) + " " + str(lastName) +" " + "scores:" + str(scores) + " " + str(percentage) 

fileName = "Quiz" + date + list1[0] + list2[0] + ".txt"

myFile = open(fileName,'w')
myFile.write(str(stringToSave))
myFile.close()


   
