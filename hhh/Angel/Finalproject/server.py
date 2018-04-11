import socket
import main
import sciencefact

questions=list(sciencefact.SF.keys())
answers=list(sciencefact.SF.values())

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    print ("waiting for connection...")
    
    # establish a connection
    clientsocket,addr = serversocket.accept()      
    print("Got a connection from %s" % str(addr))

    qs=[]#order number of question selected in dictionary
    n = clientsocket.recv(1024).decode()
    if not n:
        break
    for i in range(int(n)):
        main.quiz.selectq(qs) #select questions
        numofque=qs[-1]#the last question of all the selected ones
        choices=main.quiz.createa(numofque)#create answers to the question
        qac=questions[numofque]+" 1."+choices[0]+" 2."+choices[1]+" 3."+choices[2]+" 4."+choices[3]
        clientsocket.send(qac.encode())#send question and choices to client

        item = clientsocket.recv(1024).decode()#receive the user choice
        if not item:
            break

        result="wrong!"
        if choices[int(item)-1]==answers[numofque]:#if correct
            result="correct!"
        clientsocket.send(result.encode())#send wrong if the answer is wrong, send correct if correct

    clientsocket.close()
serversocket.close()
