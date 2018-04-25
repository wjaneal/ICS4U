<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:53:58 2018

@author: 11256
"""
import random
class account():
    #class the acount to severl parts

    
    def create_account(self):
        self.username = input("Please create a username:")
        self.code = input("Please create your code:")
        self.email = input("Please enter your email address:")
        #The creat part ask the user to create the username, code, and email
        file = open('C:/Users/11256/Desktop/a/expandtion.txt','a')
        #create a text to store the data
        file.write(self.username+' '+self.code+' ')
        #write the date in the text
        file.write(self.email)
        file.close()
        #clolse the file
        difference = open('C:/Users/11256/Desktop/a/difference.txt','a')
        #creat a text to store the difference
        difference.write(self.username + '0')
        print ("Sucess!", self.username)
        H.showmenu()
        #after all the step, show the menu again
        
    def login(self):
        # this is a function to detect if the username and code in the database
        self.name = input("Enter your username：")
        user_file = open('C:/Users/11256/Desktop/a/expandtion.txt','r')
        #read the text
        user_list = user_file.readlines()
        #readlines to combine the data in one line 
        
        if self.name in user_list:
            #check the name in the list
            self.passwd = input('Enter your code：')
            # if the name in the list, ask the user to input the code

            if self.passwd in user_list:
                print("Welcome",self.name)
                #success login
                q = ("Do you want to log out or find more information?")
                print(q)
                
                ques = input("""
                             1.log out
                             2.information
                             """)
                # ask the user to choose the next step

                if ques == "1":
                    print ("Successfully logged off!")
                    H.showmenu()
                # success log off
                if ques == "2":
                    print ("What do you want to know?")
                    print ("""
                           1.difference
                           2.temp key
                           3.transaction record
                           """)
                    choice =  input("please choose in 1, 2, 3:")
                    #three choices for user to know the information
                    if choice == "1":
                        difference = open('C:/Users/11256/Desktop/a/difference.txt','r')
                        for line in difference.readlines():           
                            #read the lines in the text
                            line = line.strip()                             
                            print ("Your difference is: %s" % (line))
                    if choice == "2":
                        key = open('C:/Users/11256/Desktop/a/key.txt','w')
                        #create and open a new text 
                        key1 = random.randint(1,10000)
                        print ("Your time key is",key1)
                        key2 = str(key1)
                        #create a random key
                        key.write(key2)
                        #store the key in the text
                        key.close
                        #close the text
                    if choice == "3":
                        print("Sorry, no transaction record.")
            else:
                print("Wrong code")
                print("Please try again")
                H.login()
                #if the code are not in the list, print wrong code
        else:
            print (" Username not found")
            print("please try again")
            H.login()
            #if the username nor in the list, print not find the username

        user_file.close()
            
    def exit(self):
        # define the function for user to exit
        print("See you next time!")
        
    def showmenu(self):
        #create a menu for user to choose
        print ("""
        1.create account
        2.login
        3.exit
        """)
        num = input("please choose in 1, 2 ,3:")
        if num == "1":
            H.create_account()
        if num == "2":
            H.login()
        if num == "3":
            H.exit()
                            
H = account()
H.showmenu()
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:53:58 2018

@author: 11256
"""
import random
class account():
    #class the acount to severl parts

    
    def create_account(self):
        self.username = input("Please create a username:")
        self.code = input("Please create your code:")
        self.email = input("Please enter your email address:")
        #The creat part ask the user to create the username, code, and email
        file = open('C:/Users/11256/Desktop/a/expandtion.txt','a')
        #create a text to store the data
        file.write(self.username+' '+self.code+' ')
        #write the date in the text
        file.write(self.email)
        file.close()
        #clolse the file
        difference = open('C:/Users/11256/Desktop/a/difference.txt','a')
        #creat a text to store the difference
        difference.write(self.username + '0')
        print ("Sucess!", self.username)
        H.showmenu()
        #after all the step, show the menu again
        
    def login(self):
        # this is a function to detect if the username and code in the database
        self.name = input("Enter your username：")
        user_file = open('C:/Users/11256/Desktop/a/expandtion.txt','r')
        #read the text
        user_list = user_file.readlines()
        #readlines to combine the data in one line 
        
        if self.name in user_list:
            #check the name in the list
            self.passwd = input('Enter your code：')
            # if the name in the list, ask the user to input the code

            if self.passwd in user_list:
                print("Welcome",self.name)
                #success login
                q = ("Do you want to log out or find more information?")
                print(q)
                
                ques = input("""
                             1.log out
                             2.information
                             """)
                # ask the user to choose the next step

                if ques == "1":
                    print ("Successfully logged off!")
                    H.showmenu()
                # success log off
                if ques == "2":
                    print ("What do you want to know?")
                    print ("""
                           1.difference
                           2.temp key
                           3.transaction record
                           """)
                    choice =  input("please choose in 1, 2, 3:")
                    #three choices for user to know the information
                    if choice == "1":
                        difference = open('C:/Users/11256/Desktop/a/difference.txt','r')
                        for line in difference.readlines():           
                            #read the lines in the text
                            line = line.strip()                             
                            print ("Your difference is: %s" % (line))
                    if choice == "2":
                        key = open('C:/Users/11256/Desktop/a/key.txt','w')
                        #create and open a new text 
                        key1 = random.randint(1,10000)
                        print ("Your time key is",key1)
                        key2 = str(key1)
                        #create a random key
                        key.write(key2)
                        #store the key in the text
                        key.close
                        #close the text
                    if choice == "3":
                        print("Sorry, no transaction record.")
            else:
                print("Wrong code")
                print("Please try again")
                H.login()
                #if the code are not in the list, print wrong code
        else:
            print (" Username not found")
            print("please try again")
            H.login()
            #if the username nor in the list, print not find the username

        user_file.close()
            
    def exit(self):
        # define the function for user to exit
        print("See you next time!")
        
    def showmenu(self):
        #create a menu for user to choose
        print ("""
        1.create account
        2.login
        3.exit
        """)
        num = input("please choose in 1, 2 ,3:")
        if num == "1":
            H.create_account()
        if num == "2":
            H.login()
        if num == "3":
            H.exit()
                            
H = account()
H.showmenu()
>>>>>>> ketty
