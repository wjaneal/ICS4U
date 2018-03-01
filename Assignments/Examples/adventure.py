'''
##################
# Adventure Game - Njall's Adventure
# Escape the dungeon using your wits and reasoning!
#Enter commands by keypboard to play
#By: William Neal
#Date: March 1, 2018
##################
'''


#Map class - keeps all of the general game information organized
#directions - list of dictionaries about the structure of the map - organized by room number
#roomNames - names of the "rooms" on the map
#inventory - list of items located in the map - organized by room number
class map:

    def __init__(self):
        self.directions = [{"S":1},{"N":0, "E":2},{"N":3,"W":1},{"S":2}]
        self.roomNames = ["dungeon","hallway","courtyard", "countryside"]
        self.inventory = [["gem"], ["sword"], ["monster"],[]]


#Player class - keeps all of the programming about the actions the player can do
#inventory - list of items held by the player
#alive - is the player alive?  Boolean.
#map - a map object to let the player interact with the environment
#victory - Boolean - set to true if the player has met the winning condition.
class player:

    def __init__(self,name):
        self.name = name
        self.inventory = []
        self.location = 0
        self.alive = True
        self.map = map()
        self.victory = False
        self.commandWords = []
        print (name, " has been initiated.")
    #command function - parses player commands

    def command(self):
        print("Please enter a command: (up to two words)")
        self.commandWords = input()
        self.commandList = self.commandWords.split(" ") #split the command by spaces
        if len(self.commandList) == 0 or len(self.commandList) >2:
            print("Please enter a valid action") #ensure correct length of command - 1 or 2 words
        if self.commandList[0] in ["N", "E", "S", "W"]:
            self.move(self.commandList[0]) #move if the command is a cardinal direction
        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy"]: #check for valid attack situation:
            if self.commandList[1] == "monster" and "monster" in self.map.inventory[self.location] and "sword" in self.inventory:
                print("You have defeated the monster!")
                self.map.inventory[self.location].remove("monster")
            else: #otherwise, the player will die:
                print("You swing your sword wildly and....")
                self.alive = False
        #Checking for valid commands to 'get' an item
        if self.commandList[0] in ["get", "take", "obtain", "steal", "acquire"]:
            if self.commandList[1] in self.map.inventory[self.location]:
                 print("You have taken the ", self.commandList[1])
                 self.inventory.append(self.commandList[1])
                 self.map.inventory[self.location].remove(self.commandList[1])
                 #If the player gets the monster, death results
                 if "monster" in self.inventory:
                     print("That was not a good idea. The monster decides to have you for breakfast.")
                     self.alive = False
            else:
                 print("Are you hallucinating? There is no such item here.")


    def move(self, direction):
        if self.location == 2 and "monster" in self.map.inventory[self.location]:
            print("The monster decides it is time for breakfast.  Looks like you are the main course!")
            self.alive = False
            return
        #Try to move to a new room; set the player's new location accordingly
        try:
         if self.map.directions[self.location][direction] != -1:
             print("You have moved to "+self.map.roomNames[self.map.directions[self.location][direction]])
             self.location = self.map.directions[self.location][direction]
         else:
             print("Watch where you are going! You cannot move in that direction.")
        #Indicate if the desired direction is not available
        except:
            print("You cannot move in that direction!")

    def checkVictory(self):
        if self.location == 3 and "gem" in self.inventory:
            self.victory = True

    def description(self):
        print("You are in the "+self.map.roomNames[self.location])

    def showRoomInventory(self):
        print("You see the following:")
        for i in self.map.inventory[self.location]:
            print(i)

    def showInventory(self):
        print("You are carrying the following: ")
        for i in self.inventory:
            print (i)

    def showDirections(self):
        print("You may move in the following directions:")
        item = self.map.directions[self.location]
        k = item.keys()
        for d in k:
            print(d)
#Run the game
P = player("Ted") #Initialize the player with a name
while P.victory == False and P.alive == True: #check for whether the player is alive and whether the player has won.
    P.description() #Show a description
    P.showInventory() #Show player inventory
    P.showRoomInventory() #Show the items in the room
    P.showDirections() #Show the available directions
    P.command() #Allow player to enter commands
    P.checkVictory() #Check for whether the player has won
#End of game:
#Set the final message depending on whether the player is alive:
if P.alive == False:
    print("Better luck next life!")
else:
    print("You have escaped the castle! Congratulations!")


