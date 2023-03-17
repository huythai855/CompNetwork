from socket import *

serverPort = 12000

# create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind socket to local port number 12000
serverSocket.bind(("", serverPort))

print("The server is ready to receive")

while True:
    # read from UDP socket into message, getting client’s address (client IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print(modifiedMessage)
    # send upper case string back to this client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
