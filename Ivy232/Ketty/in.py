"""
Ketty
2018/1/12
typecasting
to make a simple check between numbers and check whether the letter is in the word.

"""
a = int(input("Type the first number:"))
b = int(input("Type the second number:"))

if a == b:
    print("a is equal to b")

if a != b:
    print("a is not equal to b")
    
if a <= b:
    print("a is smaller or equal to b")
    
if a >= b:
    print("a is bigger or equal to b")

if a> b:
    print("a is bigger to b")

if a < b:
    print("a is smaller to b")

def checkletter(letter,word):
    if letter in word:
        return("This letter is in the word.")
    else:
        return("This letter isn't in the word.")

letter = input("Which letter do you want to check?")
word = input("Which word do you want to check?")
print(checkletter(letter,word))
    
        
