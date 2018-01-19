import time
#ask for user's name
class quiz():
    def func(self):
        self.name = (input("what is your name?"))
        print(self.name)
        self.question={"Are you happy?":"yes!","How r u today?":"good!", "Want to chat?":"of course!","I am sad...":"chins up!","What's the weather?":"sunny!"}
        self.key1=list(self.question.keys())
        self.value1=list(self.question.values())
        self.score = 0
        self.i = 0
        for i in range (0,len(self.key1)):
            self.questionprint = self.key1[i]
            print (self.questionprint)
            self.answer = input("")
            self.answerprint = self.value1[i]
            if self.answer == self.answerprint:
                self.score = self.score +1
                self.stringName = str(self.score) + " " + str(self.score/5 * 100) + "%"

#make name for the file
    def saveFile(self):
        self.filename = "quiz"+str(time.strftime("%Y%m%d%H%M%S")) + ".txt"
        self.myfile = open(self.filename, 'w')
        self.myfile.write(self.stringName)
        self.myfile.close()


Q = quiz()
Q.func()
Q.saveFile()

