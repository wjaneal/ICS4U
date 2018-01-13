#this is another way to question 3 in assignment 3.


b=str(input("please enter a string"))
a = 0
def func(letter,word):
    for i in range (65,91):
        letter=chr(i)
        if letter in word:
            print (letter, " is in ",word)
        else:
            print (letter, " is not in ",word)
            
    for i in range (97,123):
        letter=chr(i)
        if letter in word:
            print (letter, " is in ",word)
        else:
            print (letter, " is not in ",word)

func(a,b)
    
