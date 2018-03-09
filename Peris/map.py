# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:55:00 2018

@author: CTL
"""
class map:

    def __init__(self):
        self.directions = [{"N":1},{"S":0, "E":2},{"N":3,"W":1,"E":5},{"S":2,"E":4},
                           {"W":3},{"W":2,"E":6},{"S":8,"E":7,"W":5},{"W":6},{"N":6,"W":9,"S":10},
                           {"E":8},{"N":8,"S":11},{"S":12},{"W":13},{}]
        self.roomNames = ["dungeon","hallway","courtyard", "countryside"]
        self.inventory = [["gem"], ["sword"], ["monster"],[]]
