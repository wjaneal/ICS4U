#TIC TAC TO
order = input('give an order')
x = int(order[0])
y = int(order[1])
for yi in range (0,11):
    if yi != 3 and yi != 7:
        for xi in range (0,11):
            if xi == x*4 - 2 and yi == y*4 - 2:
                print ('x')
            else: 
                if xi != 3 and xi != 7:
                    print (' ',end='')
                else:
                    print ('|',end='')  
            
        print ('')
    else:
        for xi in range (0,11):
            print ('_',end='')
        print ('')


            
            
            
            
