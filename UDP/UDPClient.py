from socket import *

serverName = '127.0.0.1'
serverPort = 12000

# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get user keyboard input
message = input('Input lowercase sentence:')

# attach server name, port to message; send into socket
clientSocket.sendto(message.encode(), serverName, serverPort)

# read reply characters from socket into string
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print out received string
print(modifiedMessage.decode())

# close socket
clientSocket.close()
