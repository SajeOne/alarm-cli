#!/usr/bin/env python

import socket
from threading import Thread

class Server:
    port = 8089
    queue = list()
    t = None

    @classmethod
    def handle(self, serversocket):
        while True:
            connection, address = serversocket.accept()
            buf = connection.recv(64)
            if len(buf) > 0:
                print(buf)
                self.queue.append(buf.decode("UTF-8"))
                buf = ""

    @classmethod
    def startServer(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', self.port))
        serversocket.listen(5) # become a server socket, maximum 5 connections     
        print("Listening")

        t = Thread(target=self.handle, args=(serversocket,))
        t.start()

    @classmethod
    def stopServer(self):
        t.stop()
