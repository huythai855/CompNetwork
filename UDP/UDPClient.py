from socket import *

serverName = 'localhost'
serverPort = 12000

# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    # get user keyboard input
    message = input('> ')
    # attach server name, port to message; send into socket
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    # read reply characters from socket into string
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    # print out received string
    print(modifiedMessage.decode())

# close socket
clientSocket.close()
