import tkinter as tk
import random
#dictionary Science Fact
SF={
"______is the world's largest island country":"Indonesia",
"______has the world's highest rate of deforestation":"Indonesia", 
"______banned kissing inpublic in 2004":"Indonesia",
"The five most practiced religions in the world have their origins in ____":"Asia",
"Wild tigers only exist in ______":"Asia",
"_____is the only country in the world to draft women into Military service":"Israel",
"______ have a net gain of trees in the last 100 years":"Israel",
"______has the world's lowest meat consumption per person":"India",
"70% of all the world's species come from ______":"India",
"The world's most polluted city is in ______":"India",
"People in _____ read the most in the world":"India",
"The most radioactive and polluted lake in the world is in _______":"Russia",
"_____ has the most nuclear weapons in the world":"Russia",
"Rock Paper Scissors was invented in ______":"China",
"_____has the highest life expectancy in the world":"Japan"}
allChoices=['Indonesia','Asia','Israel','India','Russia','China',"Japan"]
#all the answers in SF
question=list(SF.keys())
answers=list(SF.values())
a=[0]*15#correct answer for corresponding question：A-1，B-2，C-3，D-4
q=[]#questions that have been selected randomly
options=[]#options to be ctreated
for i in range(0,len(question)):
    options.append(["A. ","B. ","C. ","D. "])   
class TkinterQuiz():
    def __init__(self,master):
        self.opt_selected= tk.IntVar()# store user's answer：A-1，B-2，C-3，D-4
        self.qn=0#question number 0
        self.correct=0# number of user's correct answers
        self.prepare_q_and_o(self.qn)#prepare questions and options
        self.l=self.create_q_l(master,self.qn)#prepare question label
        self.rbs=self.create_op_rb(master,4,self.qn)#prepare option radio button
        self.display(self.qn)#show next question and corresponding options
        self.button=tk.Button(master,text="Pre",command=self.back_btn)
        self.button.pack(side="bottom")#button "Pre"
        self.button=tk.Button(master,text="Nex",command=self.next_btn)
        self.button.pack(side="bottom")#button "Nex"
    def prepare_q_and_o(self,qn):#include function generate questions and create options
        while self.qn<len(question):#loop for len（question）times，prepare all questions and options
            self.generate_q(self.qn)
            self.create_options(self.qn)
            self.qn+=1
        self.qn=0 #return question number to 0 for displaying   
    def generate_q(self,qn):# randomly select a question from all the questions
        self.qninSF=random.randrange(0,len(question))
        if question[self.qninSF] not in q:
            q.append(question[self.qninSF])#q list is for question selected
        else:# avoid same question
            self.generate_q(qn)       
    def create_options(self,qn):
        if self.qninSF<3:#These are sequence numbers of all correct answers in list allChoices
            i=0#questio 0-2 correct answer is Indonesia，order 0
        elif 3<=self.qninSF<5:
            i=1#questio 3-4 correct answer is Asia，order 1
        elif 5<=self.qninSF<7:
            i=2#sequence number 2
        elif 7<=self.qninSF<11:
            i=3#sequence num 3
        elif 11<=self.qninSF<13:
            i=4#sequence num 4
        elif self.qninSF==13:
            i=5#sequence num 5
        elif self.qninSF==14:
            i=6 #sequence num 6  
        correctanswposition=random.randrange(0,4)#randomly generate correct answer postion，let it be option A／B／C／D
        options[qn][correctanswposition]+=allChoices[i]#add answer content
        a[qn]=correctanswposition+1#correct answer sequence num：A-1，B-2，C-3，D-4
        wrongopset=[]#sn for option that are wrong answers selected for each question
        for element in options[qn]:
            if element== "A. " or element== "B. " or element=="C. " or element=="D. ":#if current option is not correct answer
                TkinterQuiz.rand(wrongopset,i,allChoices,element,qn)#add wrong answer content
        #return options[qn]
        
    def rand(wrongopset,i,allChoices,element,qn):
        wrongop = random.randrange(0,7)#generate options with wrong answers
        if wrongop !=i and wrongop not in wrongopset:#prevent correct answer／wrong answern option repeated
            options[qn][options[qn].index(element)]=element+allChoices[wrongop]#add wrong answer after A／B／C／D
            #to differentiate with 'element'，use 'options[qn][options[qn].index(element)]' here
            wrongopset.append(wrongop)
        else:
            TkinterQuiz.rand(wrongopset,i,allChoices,element,qn)#if repeated or correct answer
    
    def create_q_l(self,master,qn):
        w=tk.Label(master,text=q[qn])#label
        w.pack(side ="top")
        return w
    def create_op_rb(self,master,n,qn):#n is number of options in each question
        b_val=0
        b=[]#radiobuttons
        while b_val<n:
            btn=tk.Radiobutton(master,text="",variable=self.opt_selected,value=b_val+1)#value：to compare with lista
            b.append(btn)
            btn.pack(side="top",anchor="w")
            b_val+=1
        return b
    def display(self,qn):
        b_val=0
        self.opt_selected.set(0)#reset option selected as 0
        self.l['text']=q[qn]#update question
        for op in options[qn]:
            self.rbs[b_val]['text']=op#update options
            b_val+=1
    def check_q(self,qn):
        if self.opt_selected.get()==a[qn]:#correct／wrong
            return True
        return False
    def print_results(self):
        print("Score: ", self.correct,"/",len(q))#print score after all questions are answered
    def back_btn(self):
        print("go back")
    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct+=1
        else:
            print("Wrong")
        self.qn+=1
        if self.qn>=len(question):
            self.print_results()
        else:
            self.display(self.qn)#go to next question

root=tk.Tk()
TkinterQuiz(root)
root.mainloop()

