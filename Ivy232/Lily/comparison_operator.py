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





t = str(input("Please type in a string:"))
def func(letter,word):
    if letter in word:
        return letter + ' is in ' + word
    else:
        return letter + ' is not in ' + word

print(func('a',t))
print(func('b',t))
print(func('c',t))
print(func('d',t))    
print(func('e',t))




word = input("Please type in a string again:")

def check(letter,word):
    if letter in word:
        return (letter + ' is in the word')
    else:
        return (letter + ' is not in the word')

for i in range (65, 91):
    letter = chr(i)
    print(check(letter,word))
    
for i in range (97,123):
    letter=chr(i)
    print(check(letter,word))





