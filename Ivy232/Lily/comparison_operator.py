'''Lily Tao, Jan.12th 2018'''
   



a = input('Please type in a number:')
b = input('Please type in another number:')
if a == b:
    print('a is equal to b')
if a != b:
    print('a is not equal to b')
if a >= b:
    print('a is larger or equal to b')
if a <= b:
    print('a is smaller or equal to b')
if a > b:
    print('a is larger than b')
if a < b:
    print('a is larger than b')    





def func(letter,word):
    if letter in word:
        return letter + ' is in ' + word
    else:
        return letter + ' is not in ' + word

print(func('a',str(input("Please type in a string:"))))
print(func('b',str(input("Please type in a string:"))))
print(func('c',str(input("Please type in a string:"))))
print(func('d',str(input("Please type in a string:"))))    
print(func('e',str(input("Please type in a string:"))))




def check(letter,word):   
    if letter in word:
        return (letter + ' is in the word')
    else:
        return (letter + 'is not in the word')

for i in range (65, 91) and (97,123):
    a = str(chr(i))
    print(check(a,str(input("Please type in a string:"))))




