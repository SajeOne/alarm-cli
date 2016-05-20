#!/usr/bin/env python

import socket
from Server import Server

print("Finished imports")
server = Server()
print("server declared")
server.startServer()
print("server started")

message = input("Enter Message: ")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send(message.encode('UTF-8'))
