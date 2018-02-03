'''
Assignment 5 - Lists, Tuples, Dictionaries, Compound Data Types

Coding convention: 
(a) lower case file name
(b) LilyTao, Jan.16th, list_dictionary, Purpose in multiline comment at the beginning
(c) mixedCase variable names

(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.

'''
'''
List1 = ["red", "orange", "green"]
Tuple1 = ("blue", "yellow", "purple")

print(List1[0])
print(Tuple1[0])
#List1[0] = "white" - This command is ok.
#Tuple1[0] = "brown" - This command is not ok.
#Tuples do not support assignment
#Lists are mutable; tuples are not mutable
List1[0] = "white"
List1.append("pink")
print(List1)
List1.pop(1)
print(List1)
List1.reverse()
print(List1)

#Dictionaries

D1 = {0:"Red", 1:"Green", 2:"Blue"}
D = {"What is the capital city of France?":"Paris", "What is the capital city of Japan?":"Beijing!", "What is the capital city of Greece?":"Buzhidao","What is the capital city of Brazil":"Brazilia","How cold is absolute 0?":"-273.15 degrees celcius"}

print("Here are the values in D1:")
print(D1[0],D1[1],D1[2])
Dk = D.keys()
Dv = D.values()
print(D.keys(), D.values())
for i in range(0,len(D.keys())):
    print(Dk[i], Dv[i])
'''
score=0
i=0
dictionary1={"Are you happy?":"yes!","How r u today?":"good!", "Want to chat?":"of course!","I am sad...":"chins up!","What's the weather?":"sunny!"}
Dk = list(dictionary1.keys())    #split the dictionary into lists
Dv = list(dictionary1.values())
for i in range (len(Dk)):
    print(Dk[i])                 #question and input can be seperate
    x = input()
    y = Dv[i]
    if x == y:
        score =score +1
    #else:
    #    score=score

print(score)
            










































