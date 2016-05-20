#!/usr/bin/env python

import socket
from threading import Thread

class Server:
    queue = list()
    t = None

    @classmethod
    def handle(clientsocket):
        while True:
            connection, address = serversocket.accept()
            buf = connection.recv(64)
            if len(buf) > 0:
                print(buf)
                queue.append(buf.decode("UTF-8"))
                buf = ""

    @classmethod
    def startServer(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', 8089))
        serversocket.listen(5) # become a server socket, maximum 5 connections     
        print("Listening")

        (clientsocket, address) = serversocket.accept()

        t = Thread(target=self.handle, args=(clientsocket,))
        t.start()

    @classmethod
    def stopServer(self):
        t.stop()
