# -*- coding: utf-8 -*-
"""
Spyder Editor
Name: Jaune
Date: Jan 16
Title: dictionary and tuple
Purpose: studying
This is a temporary script file.
"""
D = {"what is the most popular country in the world?":"China","what is the capital city of China?":"Beijing","what is life,the universe and everything?":"42","what is 2*3?":"6","what is chemistry?":"everything"}

trace = 0
Dk = list(D.keys())
Dv = list(D.values())
score = 0
YourAnswer = []
for i in Dk:
    Question = input(i)
    YourAnswer.append(Question)
    if YourAnswer[trace] == Dv[trace]:
        print("You are right")
        score += 1
    else:
        print("You are wrong")
    
    trace += 1

print("\nYour final score is: ", score)



"""
youranswear = input ("type your answear here")   
for i in range (0,len(D.keys())):
    print (Dk[i]) 
    if youranswear == D.values[i]:
        print ("your answear is correct")
        score += 1
    else:
        print ("your answear is wrong")
print ("This is your final socre:",score)

"""

















