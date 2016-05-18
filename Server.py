#!/usr/bin/env python

import socket

class Server:
    \
    queue

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 8089))
    serversocket.listen(5) # become a server socket, maximum 5 connections

    @classmethod
    def startServer():
        while True:
            connection, address = serversocket.accept()
            buf = connection.recv(64)
            if len(buf) > 0:
                print(buf)
                buf = ""
