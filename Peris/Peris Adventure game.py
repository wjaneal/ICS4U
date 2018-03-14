# -*- coding: utf-8 -*-
"""
#Adventure game -Baron's Adventure
#Get away from the castle
#Enter commands by keyboard to play
#By: 
#Date: March 9, 2018
"""

#Map class - keeps all of the general game information organized
#directions - list of dictionaries about the structure of the map - organized by room number
#roomNames - names of the "rooms" on the map
#inventory - list of items located in the map - organized by room number
class map:
    
    def _init_(self):      
       self.directions = [{"N":1},{"S":0, "E":2},{"N":3,"W":1,"E":5},{"S":2,"E":4},
                           {"W":3},{"W":2,"E":6},{"S":8,"E":7,"W":5},{"W":6},{"N":6,"W":9,"S":10},
                           {"E":8},{"N":8,"S":11},{"S":12},{"W":13},{}]
       self.roomNames = ["MysteriousRoom","OldLibrary","Courtyard","Hallway","StarRoom",
                          "Hallway1","Courtyard2","WonderRoom","Hallway2","Ruins",
                          "BloodZone","Hallway3","Hallway4","Balcony"]
       self.inventory = [["rusty Crowbar"],["health potion"],["shovel"],["key"],["Keepsake ring"],["master sword"],[]]
      
    def showinstrctions():
        #print a main menu and the commands
        print("Adventure game")
        print("===============")
        print("commands:")
        print("'go[direction]'")
        
    def showstatus():
        #print the player's current status
        print("---------------------")
        print("You are in the" + rooms[location]["names"])
        print("---------------------")
        
#a dictionary linking a room to other positions
rooms = {
            0 : { "names" : "MysteriousRoom",
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
                 
            4 : { "names" : "StarRoom",
                  "west"  : 3} ,
            
            5 : { "names" : "Hallway1",
                  "west"  : 2,
                  "east"  : 6} ,
                 
            6 : { "names" : "Courtyard2",
                  "west"  : 5,
                  "east"  : 7,
                  "south" : 8} ,
                 
            7 : { "names" : "WonderRoom",
                  "west"  : 6} ,
            
            8 : { "names" : "Hallway2",
                  "west"  : 9,
                  "south" : 10} ,
                 
            9 : { "names" : "Ruins",
                  "east"  : 8} ,
                 
            10 : { "names" : "BloodZone",
                   "south" : 11} ,
                  
            11 : { "names" : "Hallway3",
                   "south" : 12} ,
                  
            12 : { "names" : "Hallway4",
                   "north" : 11,
                   "west"  : 13} ,
                  
            13 : { "names" : "Balcony",
                   "east"  : 12} 
            }
            
#an inventory, which is initally empty
inventory = []
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  