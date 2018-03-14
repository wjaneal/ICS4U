# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:55:00 2018

@author: CTL
"""
class map:

    def __init__(self):
        
        #This function is to set up the rooms in the whole game.
        self.directions = [{"N":1},{"S":0, "E":2},{"N":3,"W":1,"E":5},{"S":2,"E":4},
                           {"W":3},{"W":2,"E":6},{"S":8,"E":7,"W":5},{"W":6},{"N":6,"W":9,"S":10},
                           {"E":8},{"N":8,"S":11},{"S":12},{"W":13},{}] 
        #This is to name those rooms.
        self.roomNames = ["Dungeon","OldLibrary","Courtyard","Hallway","StarRoom",
                          "Hallway1","Courtyard2","WonderRoom","Hallway2","Ruins",
                          "BloodZone","Hallway3","Hallway4","Balcony"]
        #This function is to show what objects are in those rooms.
        self.inventory = [["rusty Crowbar"],["health potion"],["shovel"],["key"],
                          ["Keepsake ring"],["master sword"],["monster"],["obstacle"],["boss"],
                          ["locked door"],[]]

class player:
    
    def command(self):
        print("Please enter a command: (up to two words)")
        self.commandWords = input()
        self.commandList = self.commandWords.split(" ") #split the command by spaces
        if len(self.commandList) == 0 or len(self.commandList) >2:
            print("Please enter a valid action") #ensure correct length of command - 1 or 2 words
        if self.commandList[0] in ["N", "E", "S", "W"]:
            self.move(self.commandList[0]) #move if the command is a cardinal direction

        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy"]: #check for valid attack situation:
            if self.commandList[1] == "monster" and "monster" in self.map.inventory[self.location] and "rusty Crowbar" in self.inventory: #This line is to check whether the attack will happen.
                print("You have defeated the monster!")
                self.map.inventory[self.location].remove("monster") #This line is to remove the monster in the map so that it won't appear again.
            else: #otherwise, the player will die:
                print("You swing your sword wildly and....")
                self.alive = False

        #Checking for valid commands to 'get' an item
        if self.commandList[0] in ["get", "take", "obtain", "grab", "acquire"]:
            if self.commandList[1] in self.map.inventory[self.location]: #This line is to check whether the item is in the player's room.
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
            if self.commandList[1] == "health" and "health potion" in self.inventory: #This line is to check the valid command.
                print("You have used the health potion!")
                self.inventory.remove("health potion")
            else: #Or the player will not use the health potion.
                print("Stoping drinking the air. That will not help you!")

        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "shovel" and "obstacle" in self.map.inventory[self.location] and "shovel" in self.inventory: #This line is to check the valid command.
                print("You have removed the obstacle!")
                self.map.inventory[self.location].remove("obstacle")
                self.inventory.remove("shovel")
            else: #Or the player will not use the shovel.
                print("Don't do that. It will hurt yourself!")
          
        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy"]: #check for valid attack situation:
            if self.commandList[1] == "boss" and "boss" in self.map.inventory[self.location] and "master sword" in self.inventory and "Keepsake ring" in self.inventory: #This line is to check the valid command.
                print("You have defeated the boss!!")
                self.map.inventory[self.location].remove("boss")
            else: #Or the player will die.
                print("The Darkness has eaten you!")
                self.alive = False
                
        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "key" and "locked door" in self.map.inventory[self.location] and "key" in self.inventory: #This line is to check the valid command.
                print("You have opened the door to the 5th room!")
                self.map.inventory[self.location].remove("locked door")
                self.inventory.remove("key")
            else: #Or the player will not use the key.
                print("The door is important!")
                

