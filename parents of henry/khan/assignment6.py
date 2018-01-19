'''
Name:Khan
Date: January 15, 2018
Title:assignment6
Purpose :Option A - Make a more complete quiz program using a class structure
(a) Have the program ask for the user's name.
(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    A and B are the first and last initials of the user.
Variable:FirstName,LastName,Dic1,Score,i,answer,Quiz,quiz,Filename,File,Content,percentage
'''
import time
FirstName = input('What is your first name')
LastName = input('What is your last name')
Dic1={'When was the first U.S.consititution made out?':'1787' ,'When did Bismarck pass away':'1898','When was Napolean crowned':'1804','When did Kutuzov pass away':'1813','When did USSR fall apart':'1991'}
Score = 0
print('Each question worth 1 mark in the quiz.')
for i in range (0,5):
    print('Question number '+str(i + 1)+' :')
    print(list(Dic1.keys())[i])
    answer = input('Please write your answer here: ')
    if answer == list(Dic1.values())[i]:
        print('  correct')
        Score = Score + 1
    else:
        print('  wrong')
    print('Your current score is: '+str(Score))
print ('Your final score is: '+str(Score))
class Quiz:
    def __init__ (self,score,f,l):
        self.score = Score
        self.f = FirstName[0]
        self.l = LastName[0]
quiz = Quiz(Score,FirstName,LastName)
percentage = int(Score)/5*100
Content = 'Score ='+ str(Score)+'      Percentage ='+str(percentage)+'%'
Filename = time.strftime("%Y%m%d%H%M%S")+quiz.f+quiz.l
File = open('quiz'+Filename+'.txt','w')
File.write(Content)
File.close( )
'''


Option B - Write the Stock Ticker program in a class structure.
(a) Store the results of each game in a file. The results should include the date and time, the names of each player and the total networth achieved at the end. The players should be listed in the order of their networth. The name of each file should be as follows: STyyyymmddhhmmss.txt where:
    yyyymmdd is the current date. January 16 would be 20180116 for example
    hhmmss is the current hour, minute and time.
    '''





