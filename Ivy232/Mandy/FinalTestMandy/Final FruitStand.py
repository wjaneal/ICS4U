#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:15:26 2018

@author: xuwentong
"""
        
class fruit():

    def __init__(self, fruitName, quantity, price):
        self.fruitName = fruitName
        self.quantity = quantity
        self.price = price
        
    def getName(self):
        print ('%s' % (self.fruitName))
    def getQuantity(self):
        print ('%s: %s' % (self.fruitName,self.quantity))
    def getPrice(self):
        print ('%s: %s' % (self.fruitName,self.price))

class fruitstand():

    def __init__(self, List):
        self.List = []
        F = self.List
        F.append(fruit("apple",10,1))
        F.append(fruit("banana",50,2))
        F.append(fruit("grape",10,5))
        F.append(fruit("avocado",510,2))
        F.append(fruit("strawberry",60,5))
        '''
        self.F.append(fruit("apple",10,1))
        self.F.append(fruit("banana",50,2))
        self.F.append(fruit("grape",10,5))
        self.F.append(fruit("avocado",510,2))
        self.F.append(fruit("strawberry",60,5))
        '''
    def purchase(self,fruitName, shopperName, quantity):
    
        if shopperName.cash >= (fruitName.price*int(quantity)):
            if quantity <= fruitName.quantity:
                for j in range (0,len(self.List)):
                    if self.List[j].fruitName == fruitName.fruitName:
                        
                        F.List[j].quantity -= quantity
                        shopperName.I[j].quantity += quantity
                        shopperName.cash = shopperName.cash - fruitName.price * quantity
                        #print ("You have bought:")
                        return(fruitName.fruitName,str(quantity))

      
            
            
            else:
                quantity = fruitName.quantity
                return (fruitName.fruitName,str(quantity))
        else:
            quantity = str(shopperName.cash / fruit.price)
            return (fruitName.fruitName, str(quantity))
        #def buy(a,b,c,d):
           #fruit(apple)=fruit(apple)-a
        
    def sell(self,fruitName, shopperName,quantity): # B5 sell the fruit
        for j in range (0,len(shopperName.I)):
            if shopperName.I[j].fruitName == fruitName.fruitName:
                F.List[j].quantity += quantity
                shopperName.I[j].quantity -= quantity
                shopperName.cash = shopperName.cash + fruitName.price * quantity

                
            
    '''
    def get(self):
        return F.purchase.quantity
    '''
class shopper():
    def __init__(self,shopperName,cash):
        self.shopperName = shopperName
        self.cash = cash
        # Check....self.FS = fruitstand()
        '''
        self.FS = fruitstand([])
        fruitstand.F.append(fruit("apple",10,1))
        fruitstand.F.append(fruit("banana",50,2))
        fruitstand.F.append(fruit("grape",10,5))
        fruitstand.F.append(fruit("avocado",510,2))
        fruitstand.F.append(fruit("strawberry",60,5))
        '''
        #self.FS.F[2].name
        #self.I=[("apple", 0,1),("banana",0,2),("grape",0,5),("avocado",0,2),("strawberry",0,5)]
        self.I = []
        self.I.append(fruit("apple", 0,1))
        self.I.append(fruit("banana",0,2))
        self.I.append(fruit("grape",0,5))
        self.I.append(fruit("avocado",0,2))
        self.I.append(fruit("strawberry",0,5))
        
    def update(self,fruitName):
        print(self.shopperName,self.cash)
        print("")
        for j in range (0,5):
            if self.I[j].fruitName == fruitName.fruitName:
                print ("Customer:",self.shopperName)
                print ("Cash:",self.cash)
                print ("Your Order:",self.I[j].quantity,self.I[j].fruitName)
    def fruitindex(self,fruitName): # B1 return index
        for j in range (0,len(F.List)):
            if F.List[j].fruitName == fruitName.fruitName:
                return (j)
    

        #use a loop to iterate through I until you find the index of Fruitname；
        #update the I using that index value：
        #self.I[index].quantity -= ...
        #self.cash += ...
        #self.FS.F[3].getPrice()
        '''
        for index in (0,len(I)):
            if self.I[index].fruitName == fruitName:
                self.FS.F[index].quantity -= fruitstand.get().quantity
                self.I[index].quantity += quantity
                self.cash = self.cash - fruitName.price * quantity
        '''
        #self.I = fruitstand([])
        '''
        for j in (0,5):
            if self.I[j].fruitName == fruitName.fruitName:
                
                F.List[j].quantity -= F.get()
                self.I[j].quantity += F.get()
                self.cash = self.cash - fruitName.price * F.get()
            else:
                j += 1
        '''
                
    def display(self):
        print(self.shopperName,self.cash)
        print("")
        
        for i in range(0,len(self.I)):
            print(self.I[i].fruitName)
            print("Inventory: Quantity", self.I[i].quantity)
            print("Fruit Stand: Quantity", F.List[i].quantity)
            print("Price:", F.List[i].price)
            print("")
            i += 1
        
S = shopper("simon",100)

apple = fruit("apple", 45, 1)
banana = fruit("banana",50,2)
grape = fruit("grape",10,5)
avocado = fruit("avocado",510,2)
strawberry = fruit("strawberry",60,5)

F=[]

F.append(fruit("apple",10,1))
F.append(fruit("banana",50,2))
F.append(fruit("grape",10,5))
F.append(fruit("avocado",510,2))
F.append(fruit("strawberry",60,5))
F = fruitstand([])

##################Start From Here#############

# Part A
while True: #mian loop
    S.display()
    x = input("What fruit would you like?")
    if x == "apple":
        y = apple
    if x == "banana":
        y = banana
    if x == "grape":
        y = grape
    if x == "avocado":
        y = avocado
    if x == "strawberry":
        y = strawberry
    
    n = int(input("Quantity:"))
    F.purchase(y,S,n)
    S.update(y)
    print ("Would you like to continue?")
    ans = str(input ("Please type Yes/No." ))
    if ans == "Yes":
        
        continue
    else:
        S.display()
        print ("Thank You!")        
        break

# Part B
# B1 in "shopper" class
# B2
print(S.I[(S.fruitindex(apple))].quantity)# print the num of apple S has

# B3 conditional statement
if S.cash >= 5 * banana.price :
    print ("You have enough money to buy 5 bananas")
else:
    print ("Sorry! You don't have enough money to buy 5 bananas")

# B4
S.I.append(fruit("pear",5,3))
F.List.append(fruit("pear",500,3))
S.display()

# B5 in the fruitstand class

