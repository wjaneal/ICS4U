import socket
import connection
import main

###############################
MY_SERVER_HOST = socket.gethostname()
MY_SERVER_PORT = 9999
OTHER_HOST = socket.gethostname()
OTHER_PORT = 9999
#############################

def data_transfer():
    me_data=main.quiz.loop
    connection.send(me_data,OTHER_HOST, OTHER_PORT)

    enemy_data = server.receive()

server = connection.Server(MY_SERVER_HOST, MY_SERVER_PORT) 

data_transfer()
    
