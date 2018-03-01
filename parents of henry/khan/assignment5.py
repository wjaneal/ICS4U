'''
Name:Khan
Date: January 15, 2018
Title:assignment5
propose:(1) Make a short quiz program that uses a dictionary for its questions and answers.
(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
(1b) In a loop, ask questions based on the key values. 
(1c) Allow the user to input the answers.
(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.
variables: Score,Dic1,i,answer
'''
Dic1={'When was the first U.S.consititution made out?':'1787' ,'When did Bismarck pass away':'1898','When was Napolean crowned':'1804','When did Kutuzov pass away':'1813','When did USSR fall apart':'1991'}
Score = 0
print('Each question worth 1 mark in the quiz.')
for i in range (0,5):
    print('Question number '+str(i + 1)+' :')
    print(list(Dic1.keys())[i])
    answer = input('Please write your answer here: ')
    if answer == list(Dic1.values())[i]:
        print('  correct')
        Score = Score + 1
    else:
        print('  wrong')
    print('Your current score is: '+str(Score))
print ('Your final score is: '+str(Score))

