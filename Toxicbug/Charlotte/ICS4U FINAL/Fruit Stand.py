#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Charlotte Chen
Date: Created on Mon Apr 16 19:42:43 2018
Title: "Fruit Stand" application
Purpose: Design and write a set of classes for a "Fruit Stand" application.
"""
class fruit():
    '''
    This class organizes information for each fruit available at the stand.
    '''
    def __init__(self,name,quantity,price):
        self.name = name #This records the name of the fruit.
        self.quantity = quantity #This records the quantity of the fruit.
        self.price = price #This records the price of the fruit.
    def getName(self):
        print("Name: "+self.name) #This function prints the name of the fruit.
    def getPrice(self):
        print("Price "+str(self.price)) #This function prints the price of the fruit.
    def getQuantity(self):
        print("Quantity: "+str(self.quantity)) #This function prints the quantity of the fruit.

class fruitstand():
    '''
    This class contains a collection of fruit instances and allows the shopper to buy fruit, adjusting quantities of fruit accordingly.
    '''
    def __init__(self):
        self.fruitList = [] #This creates an empty list for five instances of the fruit class.
        #Create five instances of the fruit class.
        self.apples = fruit("apples",5,1.2)
        self.bananas = fruit("bananas",20,2.4)
        self.pears = fruit("pears",18,3.0)
        self.grapes = fruit("grapes",25,3.5)
        self.peaches = fruit("peaches",10,1.6)
        #Append these five instances of the fruit class to a list.
        self.fruitList.append(self.apples)
        self.fruitList.append(self.bananas)
        self.fruitList.append(self.pears)
        self.fruitList.append(self.grapes)
        self.fruitList.append(self.peaches)
    def purchase(self,nameShopper,cash,nameFruit,quantityFruit):
        #This function allows the shopper to purchase fruit and adjusts quantities of fruit at the fruit stand.
        for i in self.fruitList: #Loop through the list containing five instances of the fruit class.
            if (i.name == nameFruit): #Check whether this fruit instance is the fruit the shopper wants.
                self.cashAvailable = cash // i.price #Calculate the maximum number of fruit the shopper can purchase with his money.
                self.available = min(i.quantity,self.cashAvailable,quantityFruit) 
                #Determine the number of fruit the shopper can actually buy, which is the minimum of the quantity of the fruit available at the fruit stand,
                #the number of fruit the shopper can afford and the quantity of fruit the shopper requests.
                i.quantity -= self.available #Adjust the quantity of fruit available at the fruit stand by subtracting the quantity purchased from the original quantity.
                i.quantity = int(i.quantity)
                self.message = [nameFruit,self.available]
                #Create a message containing the name and quantity of fruit to indicate that the customer has successfully purchased the fruit.
                return self.message #Return the message.
    def display(self):
        #This function prints the name and quantity of fruit available at the fruit stand.
        print("Name...Quantity...(available at the fruitstand)")
        for j in self.fruitList:
            print(j.name+"  "+str(j.quantity))

class shopper():
    '''
    This class represents a customer. The customer has money and is shopping for fruit at the fruitstand.
    '''
    def __init__(self,name,money):
        self.name = name #This records the name of the shopper.
        self.money = money #This records the money of the shopper.
        self.F = fruitstand() #This creates an instance of the fruitstand class.
        self.I = [] #Create an empty list for a personal inventory of fruit.
        #Create five instances of the fruit class, each with a quantity of 0.
        self.appleI = fruit("apples",0,1.2)
        self.bananasI = fruit("bananas",0,2.4)
        self.pearsI = fruit("pears",0,3.0)
        self.grapesI = fruit("grapes",0,3.5)
        self.peachesI = fruit("peaches",0,1.6)
        #Append these five instances of the fruit class to the list for the personal inventory.
        self.I.append(self.appleI)
        self.I.append(self.bananasI)
        self.I.append(self.pearsI)
        self.I.append(self.grapesI)
        self.I.append(self.peachesI)
    def update(self,nameShopper,cash,nameFruit,quantityFruit):
        #This function updates the personal inventory according to what the shopper buys.
        self.getMessage = self.F.purchase(nameShopper,cash,nameFruit,quantityFruit) #Get the message from the purchase function in the fruitstand class.
        for k in self.I:
            if k.name == self.getMessage[0]:
                k.quantity += self.getMessage[1] #Add the quantity the shopper purchases to his personal inventory.
                k.quantity = int(k.quantity) #Typecasting: Make quantity of fruit an integer.
                self.money -= self.getMessage[1]*k.price #Update the amount of money the shopper has after purchasing the fruit.
    def display(self):
        #This function prints the shopper's name, his money, the name and quantity of fruit the shopper has, and the name and quantity of fruit available at the fruit stand.
        print("Shopper's Name: "+self.name)
        print("Shopper's Money: "+ "%.2f" % self.money)
        print("Name and Quantity of fruit the shopper has:")
        print("Name...Quantity...")
        for i in self.I:
            print(i.name+"  "+str(i.quantity))
        print("Name and Quantity of fruit available at the fruit stand:")
        print("Name...Quantity...")
        for j in self.F.fruitList:
            print(j.name+"  "+str(j.quantity))

#Main loop
shopper1 = shopper("Charlotte",100) #Create an instance of the shopper class. Initialize the instance with a name and some money. 
shopping = True #Initialize shopping as True.
while shopping == True: 
    checkF = False #Initialize checkF as False.
    checkQ = False #Initialize checkQ as False.
    shopper1.display() #Display the shopper's information.
    choice = input("Would you like to buy some fruit? Type Y to continue and E to exit.")
    #Let the shopper input his choice.
    if choice == "Y":
        while checkF == False:
            nameF = input("Which fruit would you like to purchase?") #Let the shopper input the name of the fruit he wants.
            for i in shopper1.F.fruitList:
                if nameF == i.name: 
                    checkF = True #Check if this fruit is available.
                    while checkQ == False:
                        quantityF = input("How many "+nameF+" would you like to buy?") #Let the user input the quantity he wants.
                        if int(quantityF) >= 0:
                            checkQ = True #Check if this quantity is available.
                            shopper1.update(shopper1.name,shopper1.money,nameF,int(quantityF)) #Process the transaction and Update the information.
                        else:
                            print("Please input a zero or a positive integer for the quantity of the fruit.")
                            continue 
                if checkF == False and i == shopper1.F.fruitList[4]:
                    print("Please input a name of an available fruit.")
                    continue
    if choice == "E":
        shopping = False
    else:
        print("Please input an appropriate statement.") #Check if the choice is available.
        continue
    
    
    
    
    
    
            
        
            
    