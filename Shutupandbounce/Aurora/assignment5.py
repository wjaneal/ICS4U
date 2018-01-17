#Name: Aurora Hou
#Date: January 16, 2018
#Program Title: Lists, Tuples, Dictionaries, Compound Data Types

#(1) Make a short quiz program that uses a dictionary for its questions and answers.
#(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
#Dictionaries
score = 0
D = {"Why is John Snow so charming?":"Not so charming as you !","What is my favourite subject in school?":"After school.","Do I like the winter here?":"It's killing me.","Why is it that everyone in Canada likes baseball?":"Totally no idea.","What is my favourite fruit?":"Something you cannot find in North America."}
Dk = list(D.keys())
Dv = list(D.values())
#(1b) In a loop, ask questions based on the key values. 
for i in range(0,len(D.keys())):
    print(Dk[i])
#(1c) Allow the user to input the answers.
    Answer = input("Please input your answer:")
    if Answer == Dv[i]:
        print("Correct answer!You win a score!")
        score += 1
    else:
        print("Sorry!You are wrong.")
#(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score
print("Your total score is:"+str(score))