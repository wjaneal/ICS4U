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
        self.inventory = [["rusty Crowbar"],["health potion"],["shovel"],["key"],["Keepsake ring"],["master sword"]["nightmare"]["bloody ape"]]
        
class player:
    
    def _init_(self,name):
        self.name = name
        self.inventory = []
        self.location = 0
        self.alive = True
        self.gothrough = True
        self.map = map
        self.victory = False
        self.commandWords = []
        print(name)
    
    def command(self):
        print("Please enter a command: (up to two words)")
        self.commandWords = input()
        self.commandList = self.commandWords.split(" ") #split the command by spaces
        if len(self.commandList) == 0 or len(self.commandList) >2:
            print("Please enter a valid action") #ensure correct length of command - 1 or 2 words
        if self.commandList[0] in ["N", "E", "S", "W"]:
            self.move(self.commandList[0]) #move if the command is a cardinal direction

        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy"]: #check for valid attack situation:
            if self.commandList[1] == "monster" and "monster" in self.map.inventory[self.location] and "rusty Crowbar" in self.inventory:
                print("You have defeated the monster!")
                self.map.inventory[self.location].remove("monster")
            else: #otherwise, the player will die:
                print("You swing your sword wildly and....")
                self.alive = False

        #Checking for valid commands to 'get' an item
        if self.commandList[0] in ["get", "take", "obtain", "grab", "acquire"]:
            if self.commandList[1] in self.map.inventory[self.location]:
                 print("You have taken the ", self.commandList[1])
                 self.inventory.append(self.commandList[1])
                 self.map.inventory[self.location].remove(self.commandList[1])
                 #If the player gets the monster, death results
                 if "monster" or "boss" in self.inventory:
                     print("That was not a good idea. The monster decides to have you for breakfast.")
                     self.alive = False
            else:
                 print("Are you hallucinating? There is no such item here.")

        if self.commandList[0] in ["use","drink"]:
            if self.commandList[1] == "health" and "health potion" in self.inventory:
                print("You have used the health potion!")

        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "shovel" and "obstacle" in self.map.inventory[self.location] and "shovel" in self.inventory:
                print("You have removed the obstacle!")
                self.map.inventory[self.location].remove("obstacle")
          
        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy"]: #check for valid attack situation:
            if self.commandList[1] == "boss" and "boss" in self.map.inventory[self.location] and "master sword" in self.inventory and "Keepsake ring" in self.inventory:
                print("You have defeated the boss!!")
                self.map.inventory[self.location].remove("boss")
 
        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "key" and "locked door" in self.map.inventory[self.location] and "key" in self.inventory:
                print("You have opened the door to the 5th room!")
                self.map.inventory[self.location].remove("locked door")
        
    def showinstrctions():
        #print a main menu and the commands
        print("Adventure game")
        print("===============")
        print("commands:")
        print("'go[direction]'")
        
    def showstatus(self):
        #print the player's current status
        print("---------------------")
        print("You are in the "+self.map.roomNames[self.location])
        print("---------------------")
        
#a dictionary linking a room to other positions
    rooms = {
                0 : { "names" : "Dungeon",
                     "north" : 1} ,
                 
                1 : { "names" : "OldLibrary",
                     "south" : 0,
                     "east"  : 2} ,
                 
                2 : { "names" : "Courtyard",
                     "west"  : 1,
                     "north" : 3,
                     "east"  : 5} , 
            
                3 : { "names" : "Hallway",
                     "south" : 3,
                     "east"  : 4} ,
                 
                4:  { "names" : "StarRoom",
                     "west"  : 3} ,
            
                5:  { "names" : "Hallway1",
                     "west"  : 2,
                     "east"  : 6} ,
                 
                6:  { "names" : "Courtyard2",
                     "west"  : 5,
                     "east"  : 7,
                     "south" : 8} ,
                                                 }

P = player("Baron")
while P.victory == False and P.alive == True: #check for whether the player is alive and whether the player has won.
    P.description() #Show a description
    P.showInventory() #Show player inventory
    P.showRoomInventory() #Show the items in the room
    P.showDirections() #Show the available directions
    P.command() #Allow player to enter commands
    P.checkVictory() #Check for whether the player has won

#Set the final message depending on whether the player is alive or die:
if P.alive == False:
    print("Bloody hand slowly close Baron's eyes.Everything is futile......")
else:
    print("Baron pay his effort, and finally Beat the monster down!")
        
        
