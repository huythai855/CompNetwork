from socket import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../OpenAI')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from OpenAI import openai

serverPort = 12000

# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

# server begins listening for incoming TCP requests
serverSocket.listen(3)

print('The server is ready to receive')

while True:
    # server waits on accept() for incoming requests
    # new socket created on return
    connectionSocket, addr = serverSocket.accept()
    # read bytes from socket
    question = connectionSocket.recv(1024).decode()
    answer = openai.ask_openai(question)
    connectionSocket.send(answer.encode())
    # close connection to this client (but not welcoming socket)
    connectionSocket.close()

