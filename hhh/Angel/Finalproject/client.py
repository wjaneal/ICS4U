import socket
import main

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
clientsocket.connect((host, port))                               

run = ""
while run !="Q":
    ra=0# number of correct answers
    main.start()#print notice
    n = str(input("how many questions?"))
    clientsocket.send(n.encode())#send number of questions to server
    for i in range(int(n)):
        print("current:"+str(i+1)+"/"+n)#current question of total question
        print("correct:"+str(ra)+"/"+n)# correct answers of total questions
        # Receive no more than 1024 bytes
        qac = clientsocket.recv(1024)#receive question and choices
        if not qac:
            break
        print(qac)

        item=str(input("your answer:"))#let user input answer
        clientsocket.send(item.encode())#send answer to server

        result= clientsocket.recv(1024)#receive result from server
        if not result:
            break
        print(result.decode())
        if result.decode()=="correct!":
            ra+=1#number of correct answers+1
    print("Your correct percentage:"+str(ra/int(n)*100)+'%')#print percentage
    run = input("Q to quit")#press Q to quit, other buttons to play again
clientsocket.close()


