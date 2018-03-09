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
        self.inventory = [["rusty Crowbar"],["health potion"],["shovel"],["key"],["Keepsake ring"],["master sword"][]]
