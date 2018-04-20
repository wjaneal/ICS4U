
class fruit:
    def __init__(self,fname,price,quantity):
        self.name=str(fname)#fruit name
        self.price=price#fruit price
        self.quantity=int(quantity)#fruit quantity
    def getName(self):
        return self.name 
    def getPrice(self):
        return self.price 
    def getQuantity(self):
        return self.quantity
    
class fruitstand:
    def __init__(self):
        self.fa =[fruit("apple",4,40),fruit("banana",3,50),
                  fruit("watermelon",20,10),fruit("pear",5,30),
                  fruit("grape",10,20)]#start with 5 fruits
    def FA(self):
        return self.fa

    def purchase(self,sname,smoney,ftobuy,fnrequest):
        for fruits in self.fa:#find its position in the list
            if fruits.getName()==ftobuy:
               position=self.fa.index(fruits) 
        fprice=self.fa[position].getPrice()#get the price
        fquantity=self.fa[position].getQuantity()#get the quantity in fruitstand

        faffordable=int(smoney/fprice)#max fruit quantity that shopper can buy with his cash
        ftrade=min(faffordable,fnrequest,fquantity)#max quantity the stand can provide with shopper's cash
        fquantity-=ftrade#update fruit quantity in the fruitstand
        self.fa[position]=fruit(ftobuy,fprice,fquantity)
        return[ftobuy,ftrade,position]
                  
    def display(self):
        print("fruit in fruitstand: ")#list all the fruit
        for i in range(0,5):
            print(self.fa[i].getName(),self.fa[i].getQuantity())

class shopper():
    def __init__(self,sname,smoney):
        self.name=sname
        self.money=smoney
        self.F=fruitstand()#shopper is at fruitstand
        self.I=[fruit("apple", 4, 0), fruit("banana", 3, 0), 
            fruit("watermelon", 20, 0), fruit("pear",5,0),
            fruit("grape",10,0) ]#start with quantity 0
        

    def update(self,ftobuy,fnrequest):
        shopping=self.F.purchase(self.name,self.money,ftobuy,fnrequest)
        position=shopping[2]#position is the same
        ftrade=shopping[1]#call 
        price=self.I[position].getPrice()
        fnbuy=self.I[position].getQuantity()+ftrade#all the fruit has bought
        self.I[position]=fruit(ftobuy,price,fnbuy)
        self.moneyspend=ftrade*price
        self.money-=self.moneyspend#update available money
        
    def display(self):
        print("shopper name: ",self.name)
        print("shopper cash: ",self.money)
        print("shopper has: ")#list the inventory
        for i in range(0,5):
            print(self.I[i].getName(),self.I[i].getQuantity())
        self.F.display()
s=shopper("alice",100)
s.update("apple",5)
s.update("banana",1)
s.display()
shopper_name=input("Your name: ")
shopper_cash=int(input("Your cash: "))
s=shopper(shopper_name,shopper_cash)
s.display()
state="initiate"
while state!="E":
    print("input C to buy fruit or to continue")
    print("input E to end")#choose continue or end
    fruit_wanted=""
    while fruit_wanted!="apple" or !="banana" or !="watermelon"or !="pear" or !="grape":#loop until the fruit chosen is available
        fruit_wanted=input("fruit You want: ")
        
    fruitquantity_wanted=-1
    while fruitquantity_wanted<=0:#loop until the quantity is a positive integer
        fruitquantity_wanted=int(input("quantity you want: "))
    s.update(fruit_wanted,fruitquantity_wanted)
    state=input("now input :")
s.display()
print("Thank you for shopping in our fruitstand!")
        
    

s.display()


        
        
