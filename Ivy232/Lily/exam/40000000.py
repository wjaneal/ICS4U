def function(x):
    if x == 0:
        return 2
    else:
        return 3*function(x-1) + 2



list1 = []
list2 = []
for i in range(1, 50):
    if function(i) < 40000000:
        
        list1.append(i)
        list2.append(function(i))

print(len(list1))

def checkIt():
    number = input("Please enter a number:")
    if number in list2:
        True
    else:
        False

checkIt()
    
    



    





