# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 01:21:09 2018

@author: Chris-Li
"""

#Checking for valid commands to 'get' an item
        if self.commandList[0] in ["get", "take", "obtain", "grab", "acquire"]:
            if self.commandList[1] in self.map.inventory[self.location] and self.commandList[1] not in ["nightmare", "goblin", "bloodape"]:
                 print("You have taken the ", self.commandList[1])
                 self.inventory.append(self.commandList[1])
                 self.map.inventory[self.location].remove(self.commandList[1])
                 #If the player gets the monster, death results
                 if "nightmare" or "goblin" or "bloody ape" in self.inventory:
                     print("A bloody hand slowly close Baron's eyes.Everything is futile......")
                     self.alive = True
            else:
                 print("Are you hallucinating? There is no such item here.")