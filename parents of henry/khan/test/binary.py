
import matplotlib.pyplot as draw
import random#This is to import modules
import time
class search():#This is to set up a class 

    def Binary():#This is to define a new function
        bt=[]
        for i in range (0,6):
            #N=random.randint(0,10^i)
            List=[]
            for j in range (0,10**i):
                N=random.randrange(0,10**i)
                
                List.append(float(N)/float(10**i))
            for fillslot in range(len(List)-1,0,-1):#This is to start the loop
            
                positionOfMax=0#This is to reset the position
                for location in range(1,fillslot+1):#This is to start a loop
                    if List[location]>List[positionOfMax]:#This is to judge whether the current value is larger than the current max value
                        positionOfMax = location#This is to push it as the max value

                temp = List[fillslot]#This is to switch value
                List[fillslot] = List[positionOfMax]
                List[positionOfMax] = temp
            
            Max=10**i
            Min=1
            start = time.clock()#This is to start the timer

            getit=False#This is to set a original judgement
            n=0
            while getit == False:#This is to start a loop
                Guess = int((Max+Min)/2)#This is to get the number right between the max and the min
                if Guess  >0.7:#This is to stop the loop
                    getit = True#This is to stop the judgement
                    '''
                    if Guess > self:#This is to judge
                        Max = Guess#This is to change the range
                    if Guess < self:#This is to judge
                        Min = Guess#This is to change the range
                    '''
                if Guess <= 0.7:
                    Min=Guess
                n=n+1
                if n == 10**i:
                    getit = True

            elapsed = (time.clock() - start)#This is to stop the timer
            bt.append(elapsed)
            print(elapsed)#This is to return the time value
               
        Nlist=[10,100,1000,10000,100000,1000000]#This is to set the N list


        draw.plot(Nlist,bt,color='red') #This is to draw the lines

        draw.title('Sorting') #This is to define the title
        draw.ylabel('t') #This is to name the axises
        draw.xlabel('n')
        draw.show()#This is to show the graph
        
    def act():#This is to define a new function to put all the functions all together
        search.Binary()


                    

search.act()#This is to start the managing function

            
            
            
        
        






 















































