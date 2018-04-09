# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:15:51 2018

@author: 84999
"""
      
class Map:
    def __init__(self):
        self.directions = [{"n":1},{"s":0, "e":2},{"n":3,"w":1,"e":5},{"s":2,"e":4},{"w":3},{"w":2,"e":6},{"s":8,"e":7,"w":5},{"w":6},{"n":6,"w":9,"s":10},{"e":8},{"n":8,"s":11},{"s":12},{"w":13},{}]
        self.roomNames = ["MysteriousRoom","OldLibrary", "Courtyard", "Hallway","StarRoom","Hallway1","Courtyard2","WonderRoom","Hallway2","Ruins","BloodZone","Hallway3","Hallway4","Balcony"]
        self.inventory = [[],["rustycrowbar"],["healthpotion","lockeddoor"],["nightmare"],["key"],[],[],["shovel","goblin"],["healthpotion"],["mastersword","keepsakering"],["bloodyape"],[],[],[]]



class player:

    def __init__(self,name):
        self.name = name
        self.inventory = []
        self.location = 0
        self.alive = True
        self.map = Map()
        self.victory = False
        self.commandWords = []
        print("---------------------------------------------------------------------------------------------------------------")
        print(name,"a boy who is called Baron went to a place of interest with his classmates and teachers.")
        print("He sat beside Alley who was his best friend. Baron fell asleep on the bus because this journey did not reach his expected.")
        print("When he was wakened up, He suddenly realized that he was locked in the castle alone.\n\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("He saw a big rotten room around him with niff, he was looking outside that it had full of dark around the castle.")
        print("“This is not Earth!!” he shouted. It forced Baron to find the way out, in order to go back to the world he lived.\n")
        print ("""                    ┏┓   ┏┓
                   ┏┛┻━━━┛┻┓
                   ┃       ┃
                   ┃┳┛  ┗┳ ┃
                   ┃  ┻    ┃
                   ┗━┓   ┏━┛
                     ┃   ┗━━━┓
                     ┃神兽保佑┣┓
                     ┃永无BUG┏┛
                     ┗┓┓┏━┳┓┏┛
                      ┃┫┫ ┃┫┫
                      ┗┻┛ ┗┻┛""")
        print("------------------------------------------------------------------------------")
        print("type any words you want, and press the 'enter' bottom first to start the game!")
        print("------------------------------------------------------------------------------\n \n")



    def command(self):
        print('''              ◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾
              ◾Please enter a command:(up to 5 words)◾
              ◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾''')
        self.commandWords = input()
        self.commandList = self.commandWords.split(" ") #split the command by spaces
        if len(self.commandList) == 0 or len(self.commandList) >5:
            print("Please enter a valid action") #ensure correct length of command - 1 or 2 words
        if self.commandList[0] in ["n", "e", "w", "s"]:
            self.move()


        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy","hit"]: #check for valid attack situation:
            if self.commandList[1] == "nightmare" and "nightmare" in self.map.inventory[self.location] and "rustycrowbar" in self.inventory:
                self.map.inventory[self.location].remove("nightmare")
            elif "nightmare" in self.map.inventory[self.location]: #otherwise, the player will die:
                print("A nightmare drags you into the darkness......")
                self.alive = False
            else:
                print("You have defeated the nightmare!")
                self.alive = True
        
            if self.commandList[1] == "goblin" and "goblin" in self.map.inventory[self.location] and "rustycrowbar" in self.inventory:
                self.map.inventory[self.location].remove("goblin")
            elif "goblin" in self.map.inventory[self.location]: #otherwise, the player will die:
                print("A goblin has eaten your brain...")
                self.alive = False
            else:
                print("You have defeated the goblin!")
                self.alive = True

            if self.commandList[1] == "bloodyape" and "bloodyape" in self.map.inventory[self.location] and "master sword" in self.inventory and "keepsake ring" in self.inventory:
                self.map.inventory[self.location].remove("bloodyape")
            elif "bloodyape" in self.map.inventory[self.location]:
                print("Baron's whole body begin to bleed. After a few minutes, he fall into a pool of blood, and never wake up......")
                self.alive = False
            else:
                print("You have defeated the bloody ape!!")
                self.alive = True
                
                
        #Checking for valid commands to 'get' an item
        if self.commandList[0] in ["get", "take", "obtain", "grab", "acquire"]:
            if self.commandList[1] in self.map.inventory[self.location]:
                 print("You have taken the ", self.commandList[1])
                 self.inventory.append(self.commandList[1])
                 self.map.inventory[self.location].remove(self.commandList[1])
                 #If the player gets the monster, death results
                 if "nightmare" or "goblin" or "bloody ape" in self.inventory:
                     print("A bloody hand slowly close Baron's eyes.Everything is futile......")
                     self.alive = True
            else:
                 print("Are you hallucinating? There is no such item here.")


        if self.commandList[0] in ["use","drink"]:
            if self.commandList[1] == "health" and "healthpotion" in self.inventory:
                print("You have used the health potion!And nothing happen!HAAAAAAAA------HAAA")


        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "shovel" and "barrier" in self.map.inventory[self.location] and "shovel" in self.inventory:
                print("You have removed the barrier!")
                self.map.inventory[self.location].remove("barrier")
          
        
        
        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "key" and "lockeddoor" in self.map.inventory[self.location] and "key" in self.inventory:
                print("You need to find the key in the StarRoom, and opened the door to the Hallway1")
                self.map.inventory[self.location].remove("lockeddoor")


    
    def move(self):
        #print (self, self.map.inventory)
        if self.location == 3 and "nightmare" in self.map.inventory[self.location]:
            print("Nightmare drag you into the darkness...")
            self.alive = False
            return     
    
    
        if self.location == 7 and "goblin" in self.map.inventory[self.location]:
            print("Goblin has eaten your brain...")
            self.alive = False
            return
        
        
        if self.location == 10 and "bloody ape" in self.map.inventory[self.location]:
            print("Baron's whole body begin to bleed. After a few minutes, he fall into a pool of blood, and never wake up......")
            self.alive = False
            return
        
        
        if self.location == 13:
            print("Baron exhausted himself to find his unique best friend -- Allen. He was the only one, who is meaningful to him in his childhood.")
            print("He finally found his unconscious friend Allen and held tightly in his arms. Harsh light shined on their body,") 
            print("with a strong headache. After that, they woke up on the bus,  and they realized they escaped that castle, ")
            print("with a happy ending... A bloody hand grabbed their chair from the ground with a strange portal, is this really a good ending?")
            
            
    
                #Try to move to a new room; set the player's new location accordingly
        try:
            if self.map.directions[self.location][self.commandList[0]] != -1:
                print("\n")
                print("------------------------------")
                print("You have moved to "+self.map.roomNames[self.map.directions[self.location][self.commandList[0]]])
                self.location = self.map.directions[self.location][self.commandList[0]]
            else:
                print("Where are you going to? You cannot move in that direction.")
        #Indicate if the desired direction is not available
        except:
            print("You cannot move in that direction!")
            
        

    def checkVictory(self):
        if self.location == 1 and "rustycrowbar" in self.inventory:
            self.victory == True
        
        
        if self.location == 2 and "key" in self.inventory:
            self.victory == True
        
        
        if self.location == 8 and "shovel" in self.inventory:
            self.victory == True
            
            
        if self.location == 9 and "mastersword" in self.inventory:
            self.victory == True
        
        
        if self.location == 9 and "keepsakering" in self.inventory:
            self.victory == True
            
            
        if self.location == 10 and "bloody ape" in self.inventory:
            self.victory == True

            
        if self.victory == True:
            m = input("Baron defeated the bloody ape, but a mysterious sound told you, your friend Allen was here, do you want to save him? (YES or NO)")
            if m == 'YES':
                self.move.location[12] == True
            if m == 'NO':
                print("Baron felt so tired that he can’t even move his fingers, he unconsciously said “No!”.")
                print("After that, Baron woke up on the bus, he suddenly realized that Allen didn’t sit beside him,")
                print("he worryingly asks his classmates, but no one knows who is Allen......")




    def showstatus(self):
        #print the player's current status
        print("------------------------------")
        print("You are in the "+self.map.roomNames[self.location])
        print("------------------------------")
    
    
    
    def showitems(self):
        print("Baron's items: ")
        for i in self.inventory:
            print (i)

 
    
    def showRoomItems(self):
        print("------------------------------")
        print("Baron see the items here: ")
        for i in self.map.inventory[self.location]:
            print(i)
    
    
    
    def showDirections(self):
        print("--------------------------------------------")
        print("You may move in the following directions: ")
        item = self.map.directions[self.location]
        z = item.keys()
        for x in z:
            print(x)
    
            
            
#Run the game
P = player("Our main character, ")#set a player who called Baron, he is our main character , and intialize the game
while P.victory == False and P.alive == True: #check for whether the player is alive and whether the player has won.
    P.command() #Allow player to enter commands
    P.checkVictory() #Check for whether the player has won
    P.showstatus() #Show a description
    P.showitems() #Show player items
    P.showRoomItems() #Show the items in the room
    P.showDirections() #Show the available directions



#End of game
#Set the final message depending on whether the player is alive or die:
if P.alive == False:
    print("A bloody hand slowly close Baron's eyes.Everything is futile......")
else:
    print("Baron pay his effort and finally win his round! ")