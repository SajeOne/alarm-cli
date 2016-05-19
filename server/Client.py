#!/usr/bin/env python

import socket
from Server import Server

server = Server()
server.startServer()

message = input("Enter Message: ")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send(message.encode('UTF-8'))
