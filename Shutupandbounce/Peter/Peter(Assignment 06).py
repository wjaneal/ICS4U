#Name:Peter Zeng
#Date: January 19, 2018
#Program Title: Make a more complete quiz program using a class structure
#Program Function:(a) Have the program ask for the user's name.
#(b) Record the results of each quiz in a file. The results should include the user's name, the score on the quiz and the percentage achieved. The name of each file should be as follows: QuizyyyymmddhhmmssAB.txt where:
    #yyyymmdd is the current date. January 16 would be 20180116 for example
    #hhmmss is the current hour, minute and time.
    #A and B are the first and last initials of the user.
class Question:
    def __init__(self, name):
        self.name = name
    def quiz(self):
        print ("your quiz score is"), self.name
        q = Question('')
        q.quiz()

import datetime
import time

i = datetime.datetime.now()
print("Time: %s/%s/%s %s:%s:%s" % (i.day,i.month,i.year,i.hour,i.minute,i.second))

date = '%y.%m.%d %H.%M.%S '
first_name = input("Enter the User's first name:")
last_name = input("Enter the User's last name:")
name_initial = (first_name[0]+last_name[0])
score = 0
numbers_of_questions = 5
print("---------------------------------------------------------------------")
#Fun quiz/Dictionary
D = {"1+2+3+4+.......+100?":"5050",
    "what type of function the f(x)=cos(x)+10 is?":"trigonometric function",
    "1+1=2,is it correct?if not,write your answer(probably not according to math\￣▽￣/)":"no,11",
    "987654321/123456789(remain the integer)?":"8",
    "1+10**5/2+3?":"50004"}
Dk = list(D.keys())
Dv = list(D.values())
percentage = 100
for x in range(0, len(D.keys())):
    respond = input(Dk[x])
    if respond == Dv[x]:
        score += 1
        print('right,（。＾▽＾）')
    else:
        print ('wrong!😝')
print("------------------------------------------------------------------------------------")
print ("The answer for the first one is'+(1+100)*100/2)=5050(you only need to write the answer)")
print ("The answer for the second one is trigonometric function")
print ("The answer for the third one is no，11")
print ("The answer for the forth one is 8")
print ("your final score is "+str(score))

q = open("quiz "+str(time.strftime(date))+name_initial+'fire.txt','w')
q.write("Date: "+time.strftime(date)+first_name+" "+last_name+"'s fun quiz result:"+str(score)+" with "+str((score/numbers_of_questions)*percentage)+"% of success rate")
q.close()











