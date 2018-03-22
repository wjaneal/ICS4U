# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:09:19 2018
movement
@author: Chris-Li
"""

def move(self, direction):
        if self.location == 3 and "nightmare" in self.map.inventory[self.location]:
            print("Nightmare drag you into the darkness...")
            self.alive = False
            return
        if self.location == 7 and "nightmare" in self.map.inventory[self.location]:
            print("Nightmare drag you into the darkness...")
            self.alive = False
            return
        if self.location == 10 and "bloody ape" in self.map.inventory[self.location]:
            print("Baron's whole body begin to bleed. After a few minutes, he fall into a pool of blood, and never wake up......")
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