import sciencefact
import random

questions=list(sciencefact.SF.keys())
answers=list(sciencefact.SF.values())



#basic and main part of creating multiple unrepeated answers
def choosea(numofque):
        allChoices=['Indonesia','Asia','Israel','India','Russia','China',"Japan"]
        choices=[0,1,2,3]
        #set correct answer
        if numofque<3:
            i=0
        elif 3<=numofque<5:
            i=1
        elif 5<=numofque<7:
            i=2
        elif 7<=numofque<11:
            i=3
        elif 11<=numofque<13:
            i=4
        elif numofque==13:
            i=5
        elif numofque==14:
            i=6
        num1=random.randrange(0,4)#the position to put the correct answer
        #print(num1,"position")
        choices[num1]=allChoices[i]#put the correct answer
        #print(choices,"right answer")
        numbers=[]
        for element in choices:
            #print(element,"start one by one")
            if element== 0 or element== 1 or element==2 or element==3:
                rand(numbers,i,choices,allChoices,element)
        return choices

#choose answers that have not been selected before.If they have, choose again
def rand(numbers,i,choices,allChoices,element):
            num= random.randrange(0,7)# chhose a wrong answer from all the possible answers
            #print(num,"pick one from answers")
            if num != i and num not in numbers:#if not repeated
                numbers.append(num)
                #print(numbers,"answers have been chosen")
                choices[choices.index(element)] = allChoices[num]#put the wrong answer
                #print(num,i,choices)
            else:#if repeated,run again
                rand(numbers,i,choices,allChoices,element)


#select a question from the dictionary
def selectq(qs):
        numofque=random.randrange(0,len(questions))#choose a question
        if numofque not in qs:
            qs.append(numofque)
        else:# if repeated
            selectq(qs)

def action(qs):
        selectq(qs)
        numofque=qs[-1]
        choices=choosea(numofque)
        print(questions[numofque])
        print(choices)
        item=int(input("your answer:"))
        judge(numofque,item,choices)

#show if the answer is correct
def judge(numofque,item,choices):
        if choices[item]==answers[numofque]:
            print("correct!")
        else:
            print("wrong!")

#run for n times
def loop(n):
        qs=[]
        for i in range(n):
            action(qs)

loop(10)
    
