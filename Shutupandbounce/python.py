# Asignment 1:
# File name: Halley's Asign.
# Informationat start of file
# date: 2018/1/10
# Halley Qiu
# asignment shut up and bounce
# Puepose: Write a short program that loops through 1000 numbers.
#          For each number that is divisible by 3, print "Divisible by 3"
#          For each number that is dividible by 19, print "Multiple of 19!!"
# Variable number : i

for i in range(0,1000):
    if i % 3 == 0:
        print('Divisible by 3')
    elif i % 19 == 0:
        print('Multiple pf 19!!')
    else:
        print(i)
