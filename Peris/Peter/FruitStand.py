# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:06:20 2018

@author: 84999
"""
print("Welcome to our fruit shop!\n")
#set the class of fruit that have basic 
class fruit:
    #basic intiate for name, quantity, and price
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def getName(self):
        return(self.name)#it will return, when we print getName(),for the names of fruits

    def getQuantity(self):
        return(self.quantity)#it will return, when we print getQuantity(), for the quantities of fruits

    def getPrice(self):
        return(self.price)#it will return, when we print getPrice(), for the prices of fruits


#set a class with fruitstand, for the function purchase and display
class fruitstand:
    def __init__(self):#set 6 fruits for  __init__
        self.fruitList = [fruit("Rambutans", 15, 6), fruit("Mangoes", 20, 3), fruit("Coconuts", 12, 5), 
                          fruit("Bananas", 30, 2), fruit("Pitayas", 17, 4), fruit("Durians", 8, 8)]

    #define the purchase function 
    def purchase(self,fruits_shopper, moneyAvailable,fruits_names,quantity):
        for p in self.fruitList: 
            if p.getName() == fruits_names:#make the Name and fruits_names euqal,it is the variable that the fruits from store
                fruits_numbers = 0 #set it for 0
                while True: #use while True will break some special situation that will encounter with a infinite loop, and never goes to end
                    moneyAvailable -= p.getPrice() #the shopper's money minus(-) the fruit pirce
                    if moneyAvailable >= 0 and quantity >= 0: 
                        fruits_numbers += 1 #shopper's fruits will add one aftter this function
                    else:
                        break #break the loop
                return (p.getName(), fruits_numbers) #it will return in display, after caculating how many fruits are available for shopper to buy                  

    def display(self):
        print("\nThe fruit store have(food available): ")
        for i in range (0,len(self.fruitList)):#it will show the fruit's names and quantities from the fruitstand
            print(self.fruitList[i].name,self.fruitList[i].quantity)

#set a shopper class for the function update and display
class shopper:
     #intiate for name and money
    def __init__(self, name, money):
        self.name = name
        self.money = money 
        self.F = fruitstand()#set F that connect to the fruitstand
        self.I = [fruit("Rambutans", 0, 6), fruit("Mangoes", 0, 3), fruit("Coconuts", 0, 5), fruit("Bananas", 0, 2),
                  fruit("Pitayas", 0, 4), fruit("Durians", 0, 8)]#it shows the shopper's fruits quantity and its fruit names, and it set 0 as the beggining of purchasing
#set the function of updating the situation of the shopper's fruits
    def update(self, fruits_names, quantity):
        benefit = self.F.purchase(self.name, self.money, fruits_names, quantity)#it makes a connection between update and purchase function
        for i in self.I:
            if i.getName() == benefit[0]:#the benifi is showing that the quantities of fruits that add in 
                i.quantity += benefit[1]
    
    def display(self):
        print(self.name, self.money)#it shows the shopper's name and his money
        print("\nThe fruits you have: ")
        for i in range (0,len(self.I)):#it shows a list of fruit names, and the quantity of fruits that what you have
            print(self.I[i].name,self.I[i].quantity)
            
            
#The final part of starting print for the display, shopper's name, and the money that shopper have
print("Name: ","money: ")
s = shopper("Bansen ", 50) #50 dollars and shopper's name:Bansen
s.update("Durians", 8) #it set an update for buying eight Durians, but it actually can only buy 6,so it will automatically buy 6 Durians
s.display()
s.F.display()