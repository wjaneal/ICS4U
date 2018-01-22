'''
Assignment 6 - Program in a Class

Coding convention:
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names


Option A - Make a more complete quiz program using a class structure
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name,
the score on the quiz and the percentage achieved. The name of each file should be asfollows:
QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.


Option B - Write the Stock Ticker program in a class structure.
(a) Store the results of each game in a file. The results should include the date and time, the
names of each player and the total networth achieved at the end. The playersshould be listed in
the order of their networth. The name of each file should be as follows: STyyyymmddhhmmss.txt
where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.

'''

#import windows
import datetime

class Quiz():
    def inName(self):
    #Input the users name
    ##########################
        self.firstName = input("Input your first name:")
        self.lastName = input("Input your last name:") 

    def quiz(self):
    #run the quiz and give feedback or score
    ##########################
        self.Rem = {"Who is the best girl in the world?":"Rem", \
               "Who is the champion in the 2016 bmoe?":"Rem",\
               "Who is the most popular girl in 2016?":"Rem",\
               "When is Rem's birthday?":"2.2",\
               "Who is Rem's favourate person?":"bmt"}
        print("Here are the questions about Rem:")
        self.Rk = list(self.Rem.keys())
        self.Rv = list(self.Rem.values())
        self.score = 0
        for i in range(0,len(self.Rk)):
            print(self.Rk[i])
            self.ans = input("")
            if self.ans == self.Rv[i]:
                self.score += 1
                print("Correct!")
            else:
                self.score = self.score
                print("Incorrect!")

    def dateTime(self):
    #yyyymmddhhmmss
    #put the datetime into a turple and show part of them
    ##########################
        self.list1 = []
        self.list2 = []
        self.list1 = datetime.datetime.now().timetuple()
        for i in range(0,len(self.list1)):
            self.list2.append(str(self.list1[i]))
        if len(self.list2[1])==1:
            self.date = self.list2[0]+"0"+self.list2[1]+self.list2[2]
        else:
            self.date = self.list2[0]+self.list2[1]+self.list2[2]

        if len(self.list2[3])==1:
            self.hour = "0"+self.list2[3]
        else:
            self.hour = self.list2[3]
        
        if len(self.list2[4])==1:
            self.mini = "0"+self.list2[4]
        else:
            self.mini = self.list2[4]
    
        if len(self.list2[5])==1:
            self.seco = "0"+self.list2[5]
        else:
            self.seco = self.list2[5]
            
    def saveFile(self):
    #save the data as a file
    ##########################
        self.stringToSave = self.firstName +" " + self.lastName + " " + str(self.score) +" " + str(self.score/len(self.Rk)*100) + "%"
        self.fileName = "Quiz"+self.date+self.hour+self.mini+self.seco+self.firstName[0]+self.lastName[0]+".txt"
        self.myFile = open(self.fileName, 'w')
        self.myFile.write(self.stringToSave)
        self.myFile.close()
    
#windows.startfile(fileName)

#run the program
Q = Quiz()
Q.inName()
Q.quiz()
Q.dateTime()
Q.saveFile()

