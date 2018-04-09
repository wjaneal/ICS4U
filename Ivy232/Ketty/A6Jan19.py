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

#The users name
##########################
FN = input("Input your first name:")
LN = input("Input your last name:") 

#quiz
##########################
Rem = {"Who is the best girl in the world?":"Rem", \
       "Who is the champion in the 2016 bmoe?":"Rem",\
       "Who is the most popular girl in 2016?":"Rem",\
       "When is Rem's birthday?":"2.2",\
       "Who is Rem's favourate person?":"bmt"}

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

#yyyymmddhhmmss
##########################
list1 = []
list2 = []
list1 = datetime.datetime.now().timetuple()
for i in range(0,len(list1)):
	list2.append(str(list1[i]))
if len(list2[1])==1:
	date = list2[0]+"0"+list2[1]+list2[2]
else:
	date = list2[0]+list2[1]+list2[2]

if len(list2[3])==1:
	hour = "0"+list2[3]
else:
	hour = list2[3]

if len(list2[4])==1:
	mini = "0"+list2[4]
else:
	mini = list2[4]

if len(list2[5])==1:
	seco = "0"+list2[5]
else:
	seco = list2[5]

#save the data as a file
##########################
stringToSave = FN +" " + LN + " " + str(score) +" " + str(score/len(Rk)*100) + "%"
fileName = "Quiz"+date+hour+mini+seco+FN[0]+LN[0]+".txt"
myFile = open(fileName, 'w')
myFile.write(stringToSave)
myFile.close()

#windows.startfile(fileName)
