#Name: Ketty
#Date: January 16, 2018
#Program Title: 
#Program Function:

'''
Assignment 5 - Lists, Tuples, Dictionaries, Compound Data Types

(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.

'''
Rem = {"Who is the best girl in the world?":"Rem", "Who is the champion in the 2016 bmoe?":"Rem", "Who is the most popular girl in 2016?":"Rem","When is Rem's birthday?":"2.2","Who is Rem's favourate person?":"bmt"}

print("Here are the values in Rem:")
Rk = list(Rem.keys())
Rv = list(Rem.values())
score = 0
for i in range(0,len(Rk)):
    print(Rk[i])
    ans = input("")
    if ans == Rv[i]:
        score += 1
    else:
        score = score

print("This is your quiz score:",score)
