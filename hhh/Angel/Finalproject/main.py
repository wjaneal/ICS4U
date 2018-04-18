import sciencefact
import random

questions=list(sciencefact.SF.keys())
answers=list(sciencefact.SF.values())

class quiz:

    #basic and main part of creating multiple unrepeated answers
    def createa(numofque):
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
        num1=random.randrange(0,4)#the position to put the correct answer in the list choices
        #print(num1,"position")
        choices[num1]=allChoices[i]#put the correct answer in the list choices, replace num1 with a word
        #print(choices,"right answer")
        numbers=[]#order numbers of choices
        for element in choices:# 3 numbers and 1 word(the correct answer) -> 4 words
            #print(element,"start one by one")
            if element== 0 or element== 1 or element==2 or element==3:# if not a word
                quiz.rand(numbers,i,choices,allChoices,element)
        return choices

    #choose answers that have not been selected before.If they have, choose again
    def rand(numbers,i,choices,allChoices,element):
            num= random.randrange(0,7)# choose a wrong answer from all the possible answers
            #print(num,"pick one from answers")
            if num != i and num not in numbers:#if this answer has not been chosen before
                numbers.append(num)
                #print(numbers,"answers have been chosen")
                choices[choices.index(element)] = allChoices[num]#put the wrong answer in the list choices
                #print(num,i,choices)
            else:#if repeated,run again
                quiz.rand(numbers,i,choices,allChoices,element)


    #select a question from the dictionary
    def selectq(qs):
        numofque=random.randrange(0,len(questions))#choose a question
        if numofque not in qs:#if not repeated
            qs.append(numofque)
        else:# if repeated, run again
            quiz.selectq(qs)


    #show if the answer is correct
    def judge(numofque,item,choices):
        if choices[item-1]==answers[numofque]:
            print("correct!")
            quiz.ra+=1
        else:
            print("wrong!")
    '''THIS FUNCTION IS NOT USED IN CLIENT/SOCKET!!!'''        


    ra=0
    
    #run for n times
    def loop(n):
        qs=[]
        for i in range(n):
                print('current:',i+1,'/',n)
                print('correct:',quiz.ra,'/',n)
                quiz.selectq(qs)
                numofque=qs[-1]
                choices=quiz.createa(numofque)
                print(questions[numofque])
                print(choices)
                item=int(input("your answer:"))
                quiz.judge(numofque,item,choices)


        print('your correct percemtage:',quiz.ra/n*100,'%')
'''THIS FUNCTION IS NOT USED IN CLIENT/SOCKET!!!'''        
        
def start():
    print('the following questions all come from www.factslides.com')
    print('they do not support personal opinions')
    print('')
    print('input 1,2,3,or 4 when required')
    print('')





