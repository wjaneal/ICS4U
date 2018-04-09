# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:53:58 2018

@author: 11256
"""
import random
class account():

    
    def create_account(self):
        self.username = input("Please create a username:")
        self.code = input("Please create your code:")
        self.email = input("Please enter your email address:")
        file = open('C:/Users/11256/Desktop/a/expandtion.txt','a')
        file.write(self.username+'\n'+self.code+'\n')
        file.write(self.email)
        file.close()
        difference = open('C:/Users/11256/Desktop/a/difference.txt','a')
        difference.write(self.username + '0')
        print ("Sucess!", self.username)
        H.showmenu()
        
    def login(self):

        self.name = input("Enter your username：")
        user_file = open('C:/Users/11256/Desktop/a/expandtion.txt','r')
        user_list = user_file.readlines()

            
        if self.name in user_list:
            self.passwd = input('Enter your code：')

            if self.passwd in user_list:
                print("Welcome",self.name)
                #Set the logged in variable to true...
                q = ("Do you want to log out or find more information?")
                print(q)
                ques = input("""
                             1.log out
                             2.information
                             """)

                if ques == "1":
                    print ("Successfully logged off!")
                    H.showmenu()
                if ques == "2":
                    print ("What do you want to know?")
                    print ("""
                           1.difference
                           2.temp key
                           3.transaction record
                           """)
                    choice =  input("please choose in 1, 2, 3:")
                    if choice == "1":
                        difference = open('C:/Users/11256/Desktop/a/difference.txt','r')
                        for line in difference.readlines():                          
                            line = line.strip()                             
                            print ("Your difference is: %s" % (line))
                    if choice == "2":
                        key = open('C:/Users/11256/Desktop/a/key.txt','w')
                        key1 = random.randint(1,10000)
                        print ("Your time key is",key1)
                        key2 = str(key1)
                        key.write(key2)
                        key.close
                    if choice == "3":
                        print("Haimeizuox")
            else:
                print("Wrong code")
                print("Please try again")
                H.login()
        else:
            print (" Username not found")
            print("please try again")
            H.login()

        user_file.close()
        
    
    def exit(self):
        print("See you next time!")
        
    def showmenu(self):
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
