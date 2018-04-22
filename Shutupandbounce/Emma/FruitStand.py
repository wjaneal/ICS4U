# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:27:32 2018
Porject name: Fruit Stand
Purpose: to design a set of classes for a "Fruit Stand" application.
Variables:name, quantity, price
@author: fy
"""
class fruit:
    '''
    This class organizes infomation for each fruit available at the stand.
    '''
    #Pass 3 arguments for each fruit(type: string, integer, and integer)
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)
        
    def getName(self):
        #Prints the name of the fruit.
        return self.name

    def getPrice(self):
        #Prints the price of the fruit.
        return self.price  
        
    def getQuantity(self):
        #Prints the number of fruit.
        return self.quantity
    
class fruitstand:
    '''
    This class contains a collection of fruit instances 
    and allows the shopper to buy fruit, 
    adjusting quantities of fruit accordingly.
    '''
    #This function creates a list of 5 instances of the fruit class complete with names, quantities, 
    #and prices to initialize the stand with those instances. 
    def __init__(self):
        '''
        #The fruit stand has 10 apples, $2/each.
        #The fruit stand has 20 bananas, $0.5/each.
        #The fruit stand has 7 pears, $1.5/each.
        #The fruit stand has 6 avocados, $3/each.
        #The fruit stand has 14 durians, $8/each.
        '''
        self.fruitstand_inventory = [fruit("Apple",10,2),fruit("Banana",20,0.5),
                                     fruit("Pear",7,1.5),fruit("Avocado",6,3),
                                     fruit("Durian",14,8)]
    
    #This function adjusts the number of fruit available in its fruit class
    #according to the number of fruit actually purchased. 
    #Takes the name of the shopper, the shopper's available cash,
    #the name of the fruit, and the quantity of fruit as arguments
    #(type:string,integer,string, integer).
    def purchase(self, shoppername, shoppercash, choice_of_fruit, choice_of_quantity):
        for i in self.fruitstand_inventory:
            if choice_of_fruit == i.getName():
                    #If the shopper can afford the fruit,
                if shoppercash >= choice_of_quantity * float(i.getPrice()):
                    #and if the fruit stand can support the fruit,
                    if i.quantity >= choice_of_quantity:
                        #the shopper succeeds in buying this fruit.
                        i.quantity -= choice_of_quantity
                        shoppercash -= choice_of_quantity * float(i.getPrice())
                    else:
                        i.quantity = choice_of_quantity
                #If the shopper cannot afford the quantity that has to be paid:
                else:
                    choice_of_quantity = shoppercash/choice_of_fruit.getPrice()
                    self.quantity -= choice_of_quantity
        
        #Returns the name and quantity of that fruit to indicate 
        #that the customer has successfully purchased the fruit
        #(up to the number of available fruit)
        return [i.getName(), choice_of_quantity]    
    #This function lists the names and quantities of fruit available at the 
    #fruitstand by iterating through the list and accessing the names of the fruit...
    def display(self):
        print("Available inventory of the fruit stand:","\n",
              "Name     Quantity")
        for i in self.fruitstand_inventory:
            print("{0}       {1}".format(i.getName(), i.getQuantity()))
        

class shopper:
    '''
    This class represents a customer. The customer has money and is shopping
    for fruit at the fruitstand.
    '''
    #This function passes 2 arguments for each shopper(type:string,integer).
    def __init__(self, shoppername, shoppercash):
        self.shoppername = shoppername
        self.shoppercash = shoppercash
        shoppercash = 100
        self.F = fruitstand()#An instance of the fruitstand class.
        #I - a personal inventory of fruit in the form of a list of fruit instances.
        self.I = [fruit("Apple",0,2),fruit("Banana",0,0.5),
                  fruit("Pear",0,1.5),fruit("Avocado",0,3),
                  fruit("Durian",0,8)]
        
    def update(self, choice_of_fruit, choice_of_quantity):
        #new_shopper_inventory = self.F.purchase(self.shoppername, self.shoppercash,
        #                                       self.choice_of_fruit, self.choice_of_quantity)
        gain = self.F.purchase(self.shoppername, self.shoppercash, choice_of_fruit, choice_of_quantity)
        for e in self.I:
            if e.getName() == gain[0]:
                e.quantity += gain[1]
                self.shoppercash -= choice_of_quantity * float(e.getPrice())
            
    def display(self):
        #lists the shopper's name, the amount of money the shopper has,
        #the names and quantities of fruit the shopper has,
        #and available fruit st the fruit stand.
        while True:
            print("Shopper's name:",self.shoppername,"\n"
                  "Money the shopper has($):", self.shoppercash,"\n"
                  "Fruits owned by the shopper(qty,price):")
            for i in self.I:
                print("{0}       {1}".format(i.getName(), i.getQuantity()))
            
            print(self.F.display())
            choice_of_fruit = input("Hi, welcome! Which fruit would you like to have?(Apple/Banana/Pear/Avocado/Durian)")
            for i in self.F.fruitstand_inventory:
                if choice_of_fruit != i.getName():
                    continue
                else:
                    choice_of_quantity = int(input("How many would you like?"))
                    if choice_of_quantity <= 0:
                        continue
                    else:
                        print("Shopper's name:",self.shoppername,"\n"
                              "Money the shopper has($):", self.shoppercash,"\n"
                              "Fruits owned by the shopper(qty,price):")
                        for i in self.I:
                            print("{0}       {1}".format(i.getName(), i.getQuantity()))
                        print(self.F.display())
                        answer = input("Would you like to finish?(y/n)")
                        if answer != "n":
                            print("Shopper's name:",self.shoppername,"\n"
                                  "Money the shopper has($):", self.shoppercash,"\n"
                                  "Fruits owned by the shopper(qty,price):")
                            for i in self.I:
                                print("{0}       {1}".format(i.getName(), i.getQuantity()))
                            print(self.F.display())
                            print("Thanks for shopping! Bye~")
                            return False
            return False
#Start the program.
a = shopper("Neal",100)
a.display()
 

    
