  #Name: William Neal
#Date: January 19, 2018
#Title: Fruit Stand
#Demonstrate Use of Classes

#Define fruit class:
#Defines name, price and quantity for a type of fruit
class fruit:
    #This function is known as a class instantiation function
    #It is also known as a constructor
    #The job of a constructor is to make a new instance of a class
    def __init__(self,name, price, quantity): #Use self as a parameter
    	#Here are some class attributes or instance variables
    	self.name = name #The self. indicates that the variable
	#belongs to the class
        self.price = price  
        self.quantity = quantity
#Define fruitstand class
#Defines a list of instances of the fruit class
class fruitstand:

    def __init__(self, fruitList, fruitPrices, fruitQuantities):
    	#Set up an empty list of fruit
        self.fruitAvailable = []
	#Populate the list with data.
        for i in range(0,len(fruitList)):
	    self.fruitAvailable.append(fruit(fruitList[i],fruitPrices[i],fruitQuantities[i]))

#Data for the fruit stand:
fL = ["Apples", "Pears", "Bananas", "Oranges", "Mangoes"]
fP = [1.56,2.33,3.97,4.99,5.99]
fQ = [45,65,76,56,45]

#Declaration of the fruit stance instance, F
F = fruitstand(fL, fP, fQ)
#Populate the fruit stand with fruit using the data lists.
for i in range(0,len(F.fruitAvailable)):
	print(F.fruitAvailable[i].name+" "+str(F.fruitAvailable[i].price)+" "+str(F.fruitAvailable[i].quantity))

#Declare a new instance of the class 'fruit'
T = fruit("Tamarind", 14.44, 1000)
#Print out the class attributes (class variables)
print(T.name)
print(T.price)
print(T.quantity)


