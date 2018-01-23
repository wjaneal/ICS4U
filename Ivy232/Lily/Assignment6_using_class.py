import time
#ask for user's name

#What does this class do?
class quiz(object):
    #What does this function do?
    def func(self):
        self.name = (input("what is your name?")) #ask about the user's name
        print("Welcome, "+self.name)
        self.question={"Are you happy?":"yes!","How r u today?":"good!", "Want to chat?":"of course!","I am sad...":"chins up!","What's the weather?":"sunny!"} #set up questions and answers in a dictionary
        self.key1=list(self.question.keys()) #split the dictionary into two lists
        self.value1=list(self.question.values()) #the two lists include keys and values respectively.
        self.score = 0
        self.i = 0 #give values to "score" and "i"
        for i in range (0,len(self.key1)): 
            self.questionprint = self.key1[i] #put each of the values and keys in a loop
            print (self.questionprint)
            self.answer = input("") #leave blank space for user to type in answers
            self.answerprint = self.value1[i]  
            if self.answer == self.answerprint: #make decision and ask the computer answer differently
                self.score = self.score +1 #accumulate the score
                print ("Congrats! You are right!")
            else:
                print ("Wrong answer...But keep trying!") #respondence
        print("Your result of this strange quiz is:" +str(self.score))
        self.stringName = "Your score is:"+str(self.score) + " " + str(self.score/5 * 100) + "%" #use a variable to substitute the whole long thing...very useful! Because some function does not allow multiple terms.
        
#make name for the file
    def saveFile(self):
        self.filename = "quiz"+str(time.strftime("%Y%m%d%H%M%S")) + ".txt" #create a file, and simultaneously give the file a certain name including the instant when user finishes the quiz
        self.myfile = open(self.filename, 'w') 
        self.myfile.write(self.stringName) #magic of subtitute
        self.myfile.close()


Q = quiz()
Q.func()
Q.saveFile()

