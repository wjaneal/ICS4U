#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:42:26 2018
@author: hailankan
Fruit Stand
have three classes fruit,fruitstand,shopper
fruit class organizes information for each fruit
fruitstand class is a collection of fruit instances and allows shopper to buy fruit
shopper class has money and is shopping for fruit
"""

class fruit:
    #pass three arguments for each fruit
    def __init__(self,name,quantity,price):
        self.name= name
        self.quantity = quantity
        self.price = price
    #prints the name of the fruit    
    def getName(self,name):
        return self.name
    #prints the price of the fruit    
    def getPrice(self,price):
        return self.price
    #prints the quantity of the fruit    
    def getQuantity(self,quantity):
        return self.quantity
 
#fruit attributes    
fruitList=["apples","pears","oranges","bananas","peaches"]
fruitQuantity=[234,154,164,273,243]
fruitPrice=[2,3,4,3,5]
        
class fruitstand:
    #create a list of five instances of the fruit class
    def __init__(self,fruitList,fruitQuantity,fruitPrice):
       self.fruitAvailable=[]
       for i in range(0,len(fruitList)):#append five instances of fruit to a list, fruit attributes are stored in each instance
           self.fruitAvailable.append(fruit(fruitList[i],fruitQuantity[i],fruitPrice[i]))
    #return fruit name and the quantity purchased       
    def purchase(self,shopperName,cash,fruitName,fruitRequest):
        self.position=fruitList.index(fruitName)#get the index of the fruit purchased
        self.could= cash//self.fruitAvailable[self.position].price#the quantity the shopper can afford
        self.provide=self.fruitAvailable[self.position].quantity#the quantity in the fruitstand
        self.trade= min(self.could,self.provide,fruitRequest)#the quantity requested#find minimum of the three
        self.fruitAvailable[self.position].quantity -= self.trade#substract the quantity from fruitstand
        return [fruitName,self.trade]#return fruit name and quantity
    #display fruit name and fruit quantity            
    def display(self):
        for i in range(0,len(self.fruitAvailable)):
            print(str(self.fruitAvailable[i].name)+' '+ str(self.fruitAvailable[i].quantity))
        
class shopper:
    #F=fruitstand(fruitList,fruitQuantity,fruitPrice)
    #pass two arguments,create a personal inventory
    def __init__(self,name,money):
        self.name= name
        self.money= money
        #self.F=fruitstand(fruitList,fruitQuantity,fruitPrice)
        self.I=[]
        for i in range(0,len(fruitList)):
            self.I.append(fruit(fruitList[i],0,fruitPrice[i]))#how many fruit the shopper has
    #adjust shopper's inventory according to purchase function        
    def update(self,fruitName,fruitRequest, fruitStand):
        self.position=fruitList.index(fruitName)#get index of the fruit
        self.trade = fruitStand.purchase(self.name,self.money,fruitName,fruitRequest)[1]#get quantity traded from purchase function
        #self.trade = shopper.F.purchase(self.name,self.money,fruitName,fruitRequest)[1]
        #self.trade= self.F.purchase(self.name,self.money,fruitName,fruitRequest)[1] 
        self.I[self.position].quantity += self.trade#change fruit quantity in personal inventory
        self.money -= self.trade * self.I[self.position].price#change money the shopper owns
    #list information    
    def display(self,fruitStand):
        print("player info:")
        print(self.name)
        print(self.money)
        for i in range(0,len(self.I)):
            print(str(self.I[i].name)+' '+str(self.I[i].quantity))
        print("fruitstand info:")
        #self.F.display()
        #shopper.F.display()
        fruitStand.display()

        
'''s1=shopper("Bob",2800000)
s1.display()
s2=shopper("Sam",30)
s2.display()
s1.update("pears",3)
s1.update("pears",8000)
s1.display()
s2.update("apples",7)
s2.display()'''

'''S1 = shopper("Bob",2000)
S2 = shopper("Sam",100)
F = fruitstand(fruitList,fruitQuantity,fruitPrice)
S1.update("apples", 200, F)
S1.update("bananas", 500, F)
S1.update("pears", 100, F)
S1.update("peaches", 30000, F)
S1.update("oranges", 20, F)
S1.display(F)
S2.display(F)'''

S= shopper("Bob",1000)#information of the shopper
F = fruitstand(fruitList,fruitQuantity,fruitPrice)#fruitstand instance
run = " "
while run!="Q":
    print(S.name)#print name
    print(S.money)#print money
    fruitName=''
    while fruitName not in fruitList:#enter a fruit name until it is in fruitList
        fruitName = input("What fruit do you want to buy?")
    fruitRequest= -1
    while fruitRequest < 0 or fruitRequest//1 != fruitRequest :# enter a number until it is 0 or a positive integer
        fruitRequest = float(input("How many(an integer not smaller than zero)?"))
    S.update(fruitName,fruitRequest,F)#buy fruit,update information
    print("Do you want to continue?")
    run = input("Q to quit, else to continue")#ask if want to continue
        
    
S.display(F)
print("Thanks for shopping!")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
