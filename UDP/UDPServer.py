from socket import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../OpenAI')))
from OpenAI import openai

serverPort = 12000

# create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind socket to local port number 12000
serverSocket.bind(("", serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    answer = openai.ask_openai(message.decode())
    serverSocket.sendto(answer.encode(), clientAddress)

serverSocket.close();
