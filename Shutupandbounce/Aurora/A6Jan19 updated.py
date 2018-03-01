'''
Assignment 6 - Program in a Class
#Name：Aurora Hou
#Date:Jan,19,2018
#Revised date:Feb,25,2018
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
#now = datetime.now()#this is the current time
class quiz():  
    def Property(self):
        self.Fname = input("Please input your first name here: \n")
        self.Lname = input("Please input your last name here: \n") 
        now = datetime.now()#this is the current time
        print("This is the current time:"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second),"\n")
    #This function is known as a class instantiation function
    #It is also known as a constructor
    #constructor is to make a new instance of a class
    def Quiz(self):#This uses self as a parameter
        self.score = 0 #gives the initial value of player's score
        D = {"What's the capital of Japan?":"Tokyo",
             "What is my favourite subject in school?":"After school",
             "What's the best thing in winter?":"Home",
             "What's the name of the polymer of carbonate?":"Polycarbonate",
             "Who is the most popular singer in 2017 universally?":"Ed Sheeran"}#Writes the questions and answers of the quiz
        Dk = list(D.keys())#Arrange the questions into a list
        Dv = list(D.values())#Arrange the answers into a list
        for i in range(0,len(D.keys())):#(1b) In a loop, ask questions based on the key values. 
            print(Dk[i])
            Answer = input("Please input your answer:")#(1c) Allow the user to input the answers.
            if Answer == Dv[i]:
                print("Correct answer!You win a score!")
                self.score += 1 #Keep track of the score
            else:
                print("Sorry!You are wrong.")
            self.score = str(self.score) #Adjust to fit the following steps
        print("Hello!Dear "+self.Lname + self.Fname+", your total quiz score is: "+self.score)
    def Percent(self):
        self.score = len(self.score)#(1d) Keep track of the score and when all of the questions have been asked, tell print the final quiz score
        self.percentage=self.score/5*100 #This calculates the percentage
    def Date(self):
        T = datetime.now()#to simplify the following steps
        self.year = str(T.year)
        self.month = str(T.month)
        self.day = str(T.day)
        self.hour = str(T.hour)
        self.minute = str(T.minute)
        self.second = str(T.second)
        self.DATE = self.year+self.month+self.day+self.hour+self.minute+self.second#Combine all the time pieces together
    def File(self):
        self.score = str(self.score)
        self.percentage = str(self.percentage)            
        self.Name="Quiz"+self.DATE+self.Fname[0]+self.Lname[0] #This creates a new file and the file name.
        f = open("{0}.txt".format(self.Name), 'w')
        f.write("Date:"+self.DATE)
        f.write("Player:"+self.Fname[0]+self.Lname[0]+"\n")
        f.write("Score:{0}\n"+self.score)
        f.write("Percentage:{0}%\n"+self.percentage)#Writes the file
        f.close()#Save and close the file
Q = quiz()#This is used to run the object
Q.Property()
Q.Quiz()
Q.Percent()
Q.Date()
Q.File()
  





































