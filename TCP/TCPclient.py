from socket import *

serverName = 'localhost'
serverPort = 12000

# create TCP socket for server, remote port 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    question = input('> ')
    clientSocket.send(question.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

clientSocket.close()
