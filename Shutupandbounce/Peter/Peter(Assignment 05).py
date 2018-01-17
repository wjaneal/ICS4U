#Name:Peter Zeng
#Date: January 16, 2018
#Program Title: Lists, Tuples, Dictionaries, Compound Data Types
#Program Function:
#(1) Make a short quiz program that uses a dictionary for its questions and answers.
#(1a) Create a dictionary with at least five key:value pairs to store the questions and answers.
#(1b) In a loop, ask questions based on the key values. 
#(1c) Allow the user to input the answers.
#(1d) Keep track of the score and, when all of the questions have been asked, tell print the final quiz score.

#Make two sets here
List1 = ["hamburger","pizza","fries","tuna"]
Tuple1 = ("beef","pork","salad","vegetables")

List1[0] = "noddles"
List1.append("fruit")
print(List1)
List1.pop(1)
print(List1)
List1.reverse()
print(List1)

print ('O-(///￣皿￣)☞ ─═≡☆゜★█▇▆▅▄...')

print("---------------------------------------------------------------------")
#Fun quiz/Dictionary
D = {"1+2+3+4+.......+100?":"5050",
    "what type of function the f(x)=cos(x)+10 is?":"trigonometric function",
    "1+1=2,is it correct?Yes or No?(probably not according to math\￣▽￣/)":"11",
    "987654321/123456789(remain the integer)?":"8"}
Dk = list(D.keys())
Dv = list(D.values())

for x in range(0, len(D.keys())):
    respond = input(Dk[x])
    if respond == Dv[x]:
        print('right,（。＾▽＾）')
    else:
        print ('wrong!Everything on top of this side are used to confuse you!(●ˇ?ˇ●)')

print("------------------------------------------------------------------------------------")
   
print ("The answer for the first one is'+(1+100)*100/2)=5050(you only need to write the answer)")
print ("The answer for the second one is trigonometric function")
print ("The answer for the third one is 11")
print ("The answer for the forth one is 8")







    
    

