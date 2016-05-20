#!/usr/bin/env python

import socket

class Client:
    port = 8089

    @classmethod
    def sendMessage(self, message):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("opened socket")
        clientsocket.connect(('localhost', self.port))
        print("connected to socket")
        clientsocket.send(message.encode('UTF-8'))
        print("sent message")
        clientsocket.close()
        print("client socket closed")
