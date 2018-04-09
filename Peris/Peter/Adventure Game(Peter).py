#Final Project:Adventure Game
#Date:2018.03.10 - 2018.03.31
#Group Name:Peris
#Peter's part

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
        print(name,"")
        
#Run the game
P = player("Baron") #Initialize the player with a name
while P.victory == False and P.alive == True: #check for whether the player is alive and whether the player has won.
    P.description() #Show a description
    P.showInventory() #Show player inventory
    P.showRoomInventory() #Show the items in the room
    P.showDirections() #Show the available directions
    P.command() #Allow player to enter commands
    P.checkVictory() #Check for whether the player has won

#Set the final message depending on whether the player is alive or die:
if P.alive == False:
    print("A bloody hand slowly close Baron's eyes.Everything is futile......")
else:
    print("Baron pay his effort and finally Beat the monster down!")
        
        
