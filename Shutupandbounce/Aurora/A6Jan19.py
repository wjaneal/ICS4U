'''
Assignment 6 - Program in a Class
#Name：Aurora Hou
#Date:Jan,19,2018
Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names


Option A - Make a more complete quiz program using a class structure
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.
'''

from datetime import *
now = datetime.now()#this is the current time
print("This is the current time:"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second))
Fname = input("Please input your first name here: \n")
Lname = input("Please input your last name here: \n")
class quiz():
    
    #This function is known as a class instantiation function
    #It is also known as a constructor
    #constructor is to make a new instance of a class
    D= {"Why is John Snow so charming?":"The beard",
    "What is my favourite subject in school?":"After school",
    "Do I like the winter here?":"It's killing me",
    "Why is it that everyone in Canada likes baseball?":"Totally no idea",
    "What is my favourite fruit?":"Something you cannot find in North America"}
    Dk = list(D.keys())
    Dv = list(D.values())
    for i in range(0,len(D.keys())):
        #(1b) In a loop, ask questions based on the key values. 
        print(Dk[i])
        Answer = input("Please input your answer:")#(1c) Allow the user to input the answers.
        if Answer == Dv[i]:
            print("Correct answer!You win a score!")
            score += 1
        else:
            print("Sorry!You are wrong.")
score = str(score)
print("Hello!Dear "+Lname+ Fname+", your total quiz score is: "+score)
def Score(self): #Use self as a parameter
    self.score = score
    self.score = 0
def Percent(self):
    self.percentage=self.score/5*100 #This calculates the percentage
def Date(self):
    self.now.year = str(now.year)
    self.now.month = str(now.month)
    self.now.day = str(now.day)
    self.now.hour = str(now.hour)
    self.now.minute = str(now.minute)
    self.now.second = str(now.second)
    self.DATE = self.now.year+self.now.month+self.now.day+self.now.hour+self.now.minute+self.now.second
#(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score
    f = open(self.DATE+Fname[0]+Lname[0].txt,'w')
    f.write = ('"at"+self.DATE+ ", " +"the score of the player "+Fname[0]+Lname[0]+ "is "+self.percentage')
    f = close()






















































