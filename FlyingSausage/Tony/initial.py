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
        self.email = input("Please enter your email adress:")
        file = open('C:/Users/11256/Desktop/a/expandtion.txt','w')
        file.write(self.username+'\n'+self.code+'\n')
        file.write(self.email)
        file.close()
        difference = open('C:/Users/11256/Desktop/a/difference.txt','w')
        difference.write(self.username + '0')
        difference.close()
        
    def login(self):

        self.name = input("Enter your username：")
        user_file = open('C:/Users/11256/Desktop/a/expandtion.txt','r')
        user_list = user_file.readlines()

            
        if self.name in user_list:
            self.passwd = input('Enter your code：')

            if self.passwd in user_list:
                print("sucess",self.name)
            else:
                print("Wrong code")
        else:
            print ("Wrong username")

        user_file.close()
    
    def information(self):
        if H.login == True:
            print("Information, Showmenu")

        else:
            print ("Please login")
            H.login
            difference = open('C:/Users/11256/Desktop/a/difference.txt','r')
            print ("What do you want to know?")
            choice =  input("1.difference 2.the temp key")
            if choice == 1:
                difference = open('C:/Users/11256/Desktop/a/expandtion.txt','w')
                line = difference.readlines()
                print ("Your difference is",line)
            if choice == 2:
                key = open('C:/Users/11256/Desktop/a/key.txt','w')
                key1 = random.randint(1,10000)
                print (key1)
                key.write(key1)
                key.close
    
    def showmenu(self):
        print ("""
        1.create account
        2.login
        3.information""")
        num = input("please choose in 1, 2 ,3:")
        if num == 1:
            H.create_account
        if num == 2:
            H.login
        if num == 3:
            H.information
                
            
H = account()
H.showmenu()
