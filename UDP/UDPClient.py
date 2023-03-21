from socket import *
import sys

serverName = 'localhost'
serverPort = 12000

# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

if len(sys.argv) > 1:
    message = sys.argv[1];
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
else:
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
