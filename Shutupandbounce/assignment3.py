#Aurora Hou 2018.01.12 
#Assignment3
#(a)
A = input("Please input a number:")
J = input("Now another one:")
#(b)
A = int(A)
J = int(J)
#(c)
if A == J:
    print("A equals to J")
if A < J:
    print("A is less than J")
if A <= J:
    print("A is less than or equals to J")
if A > J:
    print("A is greater than J")
if A >= J:
    print("A is greater than or equals to J")
if A != J:    
    print("A doesn't equal to J")

#(d)
wow = input("please input a word:")
def checkletter(letter,word):
    if letter in word:
        return("The "+letter+" is in the word!")
    else:
            return"The "+letter+" is not in the word!"
print(checkletter('a',wow))
print(checkletter('b',wow))
print(checkletter('c',wow))
print(checkletter('d',wow))
print(checkletter('e',wow))

lol = input("please input another word:")
def checkletter(letter,word):
    if letter in word:
        return("The "+letter+" is in the word!")
    else:
            return"The "+letter+" is not in the word!"
            
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for letters in range(len(alphabet)):
    print(checkletter(alphabet[letters],lol))
