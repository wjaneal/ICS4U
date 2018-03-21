#Final Project:Adventure Game
#Date:2018.03.10 - 2018.03.31
#Group Name:Peris
#Group Members:Peter, Chris ,Janue

#Map class - keeps all of the general game information organized
#directions - list of dictionaries about the structure of the map - organized by room number
#roomNames - names of the "rooms" on the map
#inventory - list of items located in the map - organized by room number
class map:
    def _init_(self):
        self.directions = [{"N":1},{"S":0, "E":2},{"N":3,"W":1,"E":5},{"S":2,"E":4},{"W":3},{"W":2,"E":6},{"S":8,"E":7,"W":5},{"W":6},{"N":6,"W":9,"S":10},{"E":8},{"N":8,"S":11},{"S":12},{"W":13}]
        self.roomNames = ["MysteriousRoom","OldLibrary","Courtyard","Hallway","StarRoom","Hallway1","Courtyard2","WonderRoom","Hallway2","Ruins","BloodZone","Hallway3","Hallway4","Balcony"]
        self.inventory = [[],["rusty crowbar"],["health potion","locked door"],["nightmare"],["key"],[],[],["shovel"],["health potion"],["master sword","keepsake ring"],["bloody ape"],[],[],[]]

class player:

    def _init_(self):
        self.rpg = True
        self.Bnhp = 200
        self.Nmhp = 100
        self.Bahp = 500
        self.inventory = []
        self.location = 0
        self.alive == True
        self.map = map
        self.victory == False
        self.commandWords = []
        print("A boy who is called Baron went to a place of interest with his classmates and teachers.")
        print("He sat beside Alley who was his best friend. Baron fell asleep on the bus because this journey did not reach his expected.")
        print("When he was wakened up, He suddenly realized that he was locked in the castle alone.")
        print("He saw a big rotten room around him with niff, he was looking outside that it had full of dark around the castle.")
        print("This is not Earth!!” he shouted. It forced Baron to find the way out, in order to go back to the world he lived.")


    def command(self):
        print("Please enter a command: (up to two words)")
        self.commandWords = input()
        self.commandList = self.commandWords.split(" ") #split the command by spaces
        if len(self.commandList) == 0 or len(self.commandList) >2:
            print("Please enter a valid action") #ensure correct length of command - 1 or 2 words
        if self.commandList[0] in ["N", "E", "S", "W"]:
            self.move(self.commandList[0]) #move if the command is a cardinal direction

        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy","hit"]: #check for valid attack situation:
            if self.commandList[1] == "nightmare" and "nightmare" in self.map.inventory[self.location] and "rusty crowbar" in self.inventory:
                print("You have defeated the nightmare!")
                self.map.inventory[self.location].remove("nightmare")
            else: #otherwise, the player will die:
                print("You attack on the air, bad luck! maybe you can do your best at your next life... ")
                self.alive = False

        #Checking for valid commands to 'get' an item
        if self.commandList[0] in ["get", "take", "obtain", "grab", "acquire"]:
            if self.commandList[1] in self.map.inventory[self.location]:
                 print("You have taken the ", self.commandList[1])
                 self.inventory.append(self.commandList[1])
                 self.map.inventory[self.location].remove(self.commandList[1])
                 #If the player gets the monster, death results
                 if "nightmare" or "bloody ape" in self.inventory:
                     print("A bloody hand slowly close Baron's eyes.Everything is futile......")
                     self.alive = False
            else:
                 print("Are you hallucinating? There is no such item here.")

        if self.commandList[0] in ["use","drink"]:
            if self.commandList[1] == "health" and "health potion" in self.inventory:
                print("You have used the health potion!")

        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "shovel" and "barrier" in self.map.inventory[self.location] and "shovel" in self.inventory:
                print("You have removed the barrier!")
                self.map.inventory[self.location].remove("barrier")
          
        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy"]: #check for valid attack situation:
            if self.commandList[1] == "bloody ape" and "bloody ape" in self.map.inventory[self.location] and "master sword" in self.inventory and "keepsake ring" in self.inventory:
                print("You have defeated the bloody ape!!")
                self.map.inventory[self.location].remove("bloody ape")
 
        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "key" and "locked door" in self.map.inventory[self.location] and "key" in self.inventory:
                print("You have opened the door to the Hallway1")
                self.map.inventory[self.location].remove("locked door")


    def movement(directions,self):
        if self.location == 3 and "nightmare" in self.map.inventory[self.location]:
            print("Nightmare drag you into the darkness...")
            self.alive = False
            return
        
        if self.location == 10 and "bloody ape" in self.map.inventory[self.location]:
            print("Baron's whole body begin to bleed. After a few minutes, he fall into a pool of blood, and never wake up......")
            self.alive = False
            return
    
    
    def checkVictory(self):
        if self.location == 10 and "bloody ape" in self.inventory:
            self.victory == False
        else:
            self.victory == True
            
    def showstatus(self):
        #print the player's current status
        print("---------------------")
        print("You are in the "+self.map.roomNames[self.location])
        print("---------------------")
    
    def showItems(self):
        print("Items: ")
        for i in self.inventory:
            print (i)
    
    def showRoomItems(self):
        print("You see the items here: ")
        for i in self.map.inventory[self.location]:
            print(i)
    
    def showDirections(self):
        print("You may move in the following directions:")
        item = self.map.directions[self.location]
        z = item.keys()
        for x in z:
            print(x)

    def health(self):
        self.Bn = input("what does Baron do?")
        if self.Bn == ("fight","attack", "slice", "hack", "destroy"):
            print("Baron use physical attack!")
            self.Nmhp-50
            self.Bahp-250
        if self.Nmhp == 0:
            print("you defeated the nightmare!!")
        if self.Bahp == 0:
            print("youd defeated the bloody ape!!")
            
#Run the game
P = player#set a player who called Baron, he is our main character , and intialize the game
while P.victory == False and P.alive == True: #check for whether the player is alive and whether the player has won.
    P.command() #Allow player to enter commands
    P.checkVictory() #Check for whether the player has won
    P.showstatus() #Show a description
    P.showItems() #Show player items
    P.showRoomItems() #Show the items in the room
    P.showDirections() #Show the available directions


#End of game
#Set the final message depending on whether the player is alive or die:
if P.alive == False:
    print("A bloody hand slowly close Baron's eyes.Everything is futile......")
else:
    print("Baron pay his effort and finally win his round! ")
        
        





