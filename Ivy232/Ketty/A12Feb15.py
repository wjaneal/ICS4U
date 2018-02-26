'''
Assignment 12 - Recursive Algorithms - Towers of Hanoi

Ketty
2018.2.24
Recursive Algorithms

Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

(1) Create a class with functions for three recursive algorithms.  
Include factorials, the Towers of Hanoi and any other recursive 
function.  Allow the user to choose any of the three functions 
and then interact with the function.  The program should provide 
adequate instructions and output to be useful.
'''

#define the class of recursive algorithms
class rec():
    #factorial
    def fac(self,n):
        if n > 1:
            return n * self.fac(n-1)
        else:
            return 1
    #hanoi tower
    def hanoi(self,n,p1,p2):
        if n == 1:
            return("Move 1 from p1 to p3")
        if n != 1:
            posts = [p1,p2]
            if 1 not in posts:
                p3 = 1
            if 2 not in posts:
                p3 = 2
            if 3 not in posts:
                p3 = 3
            self.hanoi(n-1,p1,p3)
            #print steps
            print ("move one from", p1 ,"to", p2) 
            self.hanoi(n-1,p3,p2)
    #calculate the sum
    def sum(self,n):
        if n > 1:
            return n + self.sum(n-1)
        else:
            return 1
    #function of choosing one to run
    def inter(self):
        cho = ""
        while cho != "4":
            print("Please choose a function to run.1.factorial 2.hanoi tower 3.calculate the sum 4.quit")
            cho = input("Your choice:")
            if cho == "1":
                num = int(input("Which number do you want to calculate the factorial of it?"))
                print(self.fac(num))
            if cho == "2":
                how = int(input("How many rings do you want to move?"))+1
                now = int(input("Which one do you want to start?"))
                end = int(input("Which one do you want to end?"))
                self.hanoi(how,now,end)
            if cho == "3":
                num = int(input("Which number do you want to calculate the sum of it with numbers less than it?"))
                print(self.fac(num))
            
        
#run the class     
r = rec()
r.inter()        
'''    
r = rec()
num = int(input("How many ?"))
print(r.sum(num))
print(r.fac(num))
how = int(input("How many rings do you want to move?"))+1
now = int(input("Which one do you want to start?"))
end = int(input("Which one do you want to end?"))
r.hanoi(how,now,end)


'''




 













































