#Final Prject:Adventure Game
#Team's Name:Peris
#Team members:Peter,Janue,Chris
#Date:2018.4.5
#Include in several factors of RPG
#Words Adventure Game

#define a map with several rooms, and also put some special items
class Map:
    def __init__(self):
        self.directions = [{"n":1},{"s":0, "e":2},{"n":4,"w":1,"e":3},{"w":2,"e":6},{"s":2,"e":5},{"w":4},{"w":3,"e":7},{"s":9,"e":8,"w":6},{"w":7},{"n":7,"s":10},{"n":9,"w":11,"s":12},{"e":10},{"s":13},{"s":14},{"w":15},{"w":16},{}]
        self.roomNames = ["MysteriousRoom","OldLibrary", "Courtyard","The room with lockeddoor","Hallway","StarRoom","Hallway1","Courtyard2","WonderRoom","The room with barrier","Hallway2","Ruins","BloodZone","Hallway3","Hallway4","Hallway5","Balcony"]
        self.inventory = [[],["rustycrowbar"],["healthpotion"],["lockeddoor"],["nightmare"],["key"],[],[],["shovel","goblin"],["barrier"],["healthpotion"],["mastersword","keepsakering"],["bloodyape"],["Yeslabel","Nolabel"], ["Statue of God"],["Allen"],[]]


#define a class of player that organize the name,location or something about the game's basic function
class player:

    def __init__(self,name):
        self.name = name
        self.inventory = []
        self.location = 0
        self.alive = True
        self.map = Map()
        self.victory = False
        self.commandWords = []
        self.quit = True
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
                     ┃-------┣┓
                     ┃Welcome┏┛
                     ┗┓┓┏━┳┓┏┛
                      ┃┫┫ ┃┫┫
                      ┗┻┛ ┗┻┛""")
        print("------------------------------------------------------------------------------")
        print("type any words you want, and press the 'enter' bottom first to start the game!")
        print("------------------------------------------------------------------------------\n \n")



    #the important part of function to run the game about the command that player type
    def command(self):
        print('''              ◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾
              ◾Please enter a command:(up to 2 words)◾
              ◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾''')
        self.commandWords = input()
        self.commandList = self.commandWords.split(" ") #split the command by spaces
        if len(self.commandList) == 0 or len(self.commandList) > 2:
            print("Please enter a valid action") #ensure correct length of command - 1 or 2 words
        if self.commandList[0] in ["n", "e", "w", "s"]:
            self.move()


#Set three different monsters in map
        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy","hit"]: #check for valid attack situation:
            if self.commandList[1] == "nightmare" and "nightmare" in self.map.inventory[self.location] and "rustycrowbar" in self.inventory:
                print("--------------------------------")
                print("You have defeated the nightmare!")
                self.map.inventory[self.location].remove("nightmare")
            elif "nightmare" in self.map.inventory[self.location] and "rustycrowbar" not in self.inventory: #otherwise, the player will die:
                print("---------------------------------------------")
                print("A nightmare drags you into the darkness......")
                self.alive = False

        
        
        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy","hit"]: #check for valid attack situation:
            if self.commandList[1] == "goblin" and "goblin" in self.map.inventory[self.location] and "rustycrowbar" in self.inventory:
                print("-----------------------------")
                print("You have defeated the goblin!")
                self.map.inventory[self.location].remove("goblin")
            elif "goblin" in self.map.inventory[self.location]: #otherwise, the player will die:
                print("--------------------------------")
                print("A goblin has eaten your brain...")
                self.alive = False



        if self.commandList[0] in ["fight", "attack", "slice", "hack", "destroy","hit"]: #check for valid attack situation:
            if self.commandList[1] == "bloodyape" and "bloodyape" in self.map.inventory[self.location] and "mastersword" in self.inventory and "keepsakering" in self.inventory:
                print("----------------------------------")
                print("You have defeated the bloody ape!!")
                self.map.inventory[self.location].remove("bloodyape")
            elif "bloodyape" in self.map.inventory[self.location]:
                print("-------------------------------------------------------------------------------------------------------------")
                print("Baron's whole body begin to bleed. After a few minutes, he fall into a pool of blood, and never wake up......")
                self.alive = False

                
#set the function that how to get the items for typing the command
        if self.commandList[0] in ["get", "take", "obtain", "grab", "acquire"]:
            if self.commandList[1] in self.map.inventory[self.location] and self.commandList[1] not in ["nightmare", "goblin", "bloodape"]:
                 print("-----------------------------------------")
                 print("You have taken the ", self.commandList[1])
                 self.inventory.append(self.commandList[1])
                 self.map.inventory[self.location].remove(self.commandList[1])
                 #If the player gets the monster, death results
                 if "nightmare" or "goblin" or "bloody ape" in self.inventory:
                     self.alive = True
            else:
                 print("--------------------------------------------------")
                 print("Are you hallucinating? There is no such item here.")



        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "key" and "lockeddoor" in self.map.inventory[self.location] and "key" in self.inventory:
                print("---------------------------")
                print("You opened the locked door!")
                self.map.inventory[self.location].remove("lockeddoor")
            elif "lockeddoor" in self.map.inventory[self.location]:
                print("---------------------------------------------------------")
                print("Baron can't find the key, and waiting for his death......")
                self.alive = False



        if self.commandList[0] in ["use","drink"]:
            if self.commandList[1] == "healthpotion" in self.inventory:
                print("---------------------------------------------------------------------------")
                print("\nYou have used the health potion!And nothing happen!HAAAAAAAA------HAAAH\n")
                self.inventory.remove(self.commandList[1])

            
        
        if self.commandList[0] in ["use"]:
            if self.commandList[1] == "shovel" and "barrier" in self.map.inventory[self.location] and "shovel" in self.inventory:
                print("-----------------------------")
                print("You have removed the barrier!")
                self.map.inventory[self.location].remove("barrier")
            elif "barrier" in self.map.inventory[self.location]:
                print("------------------------------------------------------------------------------------------------")
                print("Baron was trying to hit the rock on his own.But he had a bad fall, and die.....HAAAAAAAHAAHAHAA!")
                self.alive = False
              
    
#special buttom for quiting game       
        if self.commandList[0] in ["quit","q"]:
            self.quit == True
            if self.quit == True:
                print("------------------")
                print("you quit the game!")
                self.alive = False
            
            
            
        if self.commandList[0] in ["give","use"]:
            if self.commandList[1] == "Nolabel" and "Statue of God" in self.map.inventory[self.location] and "Nolabel" in self.inventory:
                print("-----------------------------------------------------------END---------------------------------------")
                print("Baron felt so tired that he can’t even move his toes, so he gave the ‘No label’ to the Statue of God.")
                print("After that, Baron woke up on the bus, he suddenly realized that Allen didn’t sit beside him,")
                print("he worryingly asks his classmates, but no one knows who is Allen......")
                self.alive = False
            elif self.commandList[1] == "Yeslabel" and "Statue of God" in self.map.inventory[self.location] and "Yeslabel" in self.inventory:
                print("----------------------------------------------------------------------------------------------")
                print("go and help him!")
                print("A mysterious sound from Statue of God noticed Baron, make him more insistent on finding Allen.")
                print("And Statue of God disappered in front of him......")
                self.map.inventory[self.location].remove("Statue of God")
            
            
            
    def move(self):#kind of movement that if player go out of the room with crucial things, player will die
        #print (self, self.map.inventory)    #or maybe the tips of text which will show on the window
        if self.location == 1:
            print("--------------------------------------------")
            print("“Find the key, if you don't wanna die at next room.”A mysterious sound muttered")
            
            
        if self.location == 3 and "lockeddoor" in self.map.inventory[self.location]:
            print("---------------------------------------------------------")
            print("Baron can't find the key, and waiting for his death......")
            self.alive = False
            return     
    
    
        if self.location == 4 and "nightmare" in self.map.inventory[self.location]:
            print("---------------------------------------")
            print("A nightmare drag you into the darkness...")
            self.alive = False
            
            
        if self.location == 6:
            print("------------------------------------------------------------------------------------")
            print("“you would better not reach in the south direction until you get the shovel.”A mysterious sound said to Baron.")
        
        
        if self.location == 8:
            print("-------------------------------------------------------------------------------------------")
            print("Suddenly, a big stone was falling behind Baron, and Baron need the shovel to dig the stone!")
        
        
        if self.location == 8 and "goblin" in self.map.inventory[self.location]:
            print("------------------------------")
            print("A goblin has eaten your brain...")
            self.alive = False
            return
        
        
        if self.location == 9 and "barrier" in self.map.inventory[self.location]:
            print("------------------------------------------------------------------------------------------------")
            print("Baron was trying to hit the rock on his own.But he had a bad fall, and die.....HAAAAAAAHAAHAHAA!")
            self.alive = False
            return
        
        
        if self.location == 10:
            print("---------------------------------------------------------------------------------------------------------------")
            print("If you want safely enter to the BloodZone, you need to take the mastersword and keepsakering to win your fight.")
        
        
        if self.location == 11:
            print("----------------------------------------------------------------------------------")
            print("A bloody ape came out, and Baron must to defeat it, he had no choices to decide...")
        
        
        if self.location == 12 and "bloodyape" in self.map.inventory[self.location]:
            print("-------------------------------------------------------------------------------------------------------------")
            print("Baron's whole body begin to bleed. After a few minutes, he fall into a pool of blood, and never wake up......")
            self.alive = False
            return
        
        
        if self.location == 12:
            print("--------------------------------------------------------")
            print("Take Yeslabel or Nolabel, and give your answer to God!!!")
        
        
        if self.location == 14 and "Statue of God" in self.map.inventory[self.location]:
            print("--------------------------------------------------------------------------------------------------")
            print("Baron ignored the god, how dare he was! Of course, he got to taste the death as a reward from God!")
            self.alive = False
            return
        
        
        if self.location == 13:
            print("----------------------------------------------------------------------------------------------")
            print("A mysterious sound told Baron, his friend Allen was here, do you want to save him? (YES or NO)")
        
        
        if self.location == 15 and "Allen" in self.map.inventory[self.location]:
            print("-----------------------------------------------------------END------------------------------------------------------------------")
            print("Baron exhausted himself to find his unique best friend -- Allen. He was the only one, who is meaningful to him in his childhood.")
            print("He finally found his unconscious friend Allen and held tightly in his arms. Harsh light shined on their body,") 
            print("with a strong headache. After that, they woke up on the bus,  and they realized they escaped that castle, ")
            print("with a happy ending... A bloody hand grabbed their chair from the ground with a strange portal, is this really a good ending?")
            self.alive = False
            return
        #this is the one of the ending for this RPG game

        
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
            
        

    def checkVictory(self):#this is the key items for player to win the game
        #The key items for the player to win the game!
        if self.location == 10 and "mastersword" in self.inventory:
            self.victory == True
            
        if self.location == 10 and "keepsakering" in self.inventory:
            self.victory == True
            


    def showstatus(self):  
        #print the player's current status
        print("------------------------------")
        print("You are in the "+self.map.roomNames[self.location])
    
    
    
    def showitems(self):
        #show the items that player have
        print("---------------")
        print("Baron's items: ")
        for i in self.inventory:
            print (i)

 
    
    def showRoomItems(self):
        #show the key items in each specific rooms
        print("--------------------------")
        print("Baron see the items here: ")
        for i in self.map.inventory[self.location]:
            print(i)
    
    
    
    def showDirections(self):
        #show the directions of east, south, west, and north that player can move
        print("------------------------------------------")
        print("You may move in the following directions: ")
        print("------------------------------------------")
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
    print("------------------------------------------------------------------------------------------------------------------")
    print("A bloody hand slowly close Baron's eyes.Everything is futile......hah~ just joking, I'll see you in the next life!")

